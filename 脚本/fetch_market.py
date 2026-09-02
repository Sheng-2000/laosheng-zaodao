# -*- coding: utf-8 -*-
# fetch_market.py — 实时行情取数（B 方案核心）
# 生成时由 g_data1 / g_data2 调用，拉取最新交易日收盘数据。
# 设计原则：
#   1) 每个取数在独立线程中执行，硬超时（默认 8s）；接口不可达即快速失败返回 None。
#   2) 16 只标的并行抓取，避免串行挂死。
#   3) 失败项置 None，调用方用硬编码兜底值；FALLBACK 列表记录非实时项供告警。
import os, sys, time, datetime, json, tempfile, concurrent.futures, threading as _th

try:
    import akshare as ak
except Exception:
    ak = None

FALLBACK = []        # 记录用兜底值的键名
_DATA_DATE = None    # 实际取到的数据日期（最新交易日）
_TIMEOUT = 8         # 单接口超时（秒）
_OVERALL = 90        # 整体取数硬上限（秒），防止极端挂死
_CACHE = None         # 同进程缓存
_TTL = 600           # 磁盘缓存有效期（秒），同日内重复 build / 多模块实例复用


def _cache_path():
    return os.path.join(tempfile.gettempdir(),
                        "laosheng_market_%s.json" % datetime.date.today().strftime("%Y%m%d"))


def _load_disk():
    try:
        p = _cache_path()
        if os.path.exists(p) and (time.time() - os.path.getmtime(p)) < _TTL:
            with open(p, encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        return None
    return None


def _save_disk(M):
    try:
        with open(_cache_path(), "w", encoding="utf-8") as f:
            json.dump(M, f)
    except Exception:
        pass

def _run(fn):
    """在独立守护线程执行 fn，超时（_TIMEOUT）即返回 None。
    注意：不使用 ThreadPoolExecutor 的 with 写法——其 __exit__ 会 shutdown(wait=True)，
    在底层网络调用挂死时导致主线程无限阻塞。改用 daemon 线程 + join(timeout)，
    超时后主线程立即返回，残留网络线程随进程退出回收，绝不阻塞流水线。"""
    if ak is None:
        return None
    res = [None]
    err = [None]

    def _go():
        try:
            res[0] = fn()
        except Exception:  # noqa: BLE001
            err[0] = True

    t = _th.Thread(target=_go, daemon=True)
    t.start()
    t.join(_TIMEOUT)
    if t.is_alive() or err[0]:
        return None
    r = res[0]
    if r is None or (hasattr(r, "empty") and r.empty) or (hasattr(r, "__len__") and len(r) == 0):
        return None
    return r

def _last(row):
    return row.iloc[-1], (row.iloc[-2] if len(row) >= 2 else None)

def _idx(sym):
    r = _run(lambda: ak.stock_zh_index_daily(symbol=sym))
    if r is None:
        return None
    cur, prev = _last(r)
    close = float(cur["close"])
    pct = (close - float(prev["close"])) / float(prev["close"]) * 100 if prev is not None else 0.0
    return close, pct, str(cur["date"])

def _astock(sym):
    r = _run(lambda: ak.stock_zh_a_daily(symbol="sh" + sym, adjust=""))
    if r is None:
        return None
    cur, prev = _last(r)
    close = float(cur["close"])
    pct = (close - float(prev["close"])) / float(prev["close"]) * 100 if prev is not None else 0.0
    return close, pct, str(cur["date"])

def _us(sym):
    r = _run(lambda: ak.stock_us_daily(symbol=sym, adjust=""))
    if r is None:
        return None
    cur, prev = _last(r)
    close = float(cur["close"])
    pct = (close - float(prev["close"])) / float(prev["close"]) * 100 if prev is not None else 0.0
    return close, pct, str(cur["date"])

def _get_market():
    """返回统一原始值字典 M（内部实现，不带整体超时）。"""
    global _CACHE, _DATA_DATE
    M = {}

    # ---- A股 5 指数（sina 日线）----
    for sym in ["sh000001", "sz399001", "sz399006", "sh000300", "sh000688"]:
        v = _idx(sym)
        M[sym] = v
        if v is None:
            FALLBACK.append("A股指数_" + sym)
        else:
            _DATA_DATE = v[2]

    # ---- 美股 3 指数（akshare us_daily）----
    for key, sym in [("dji", ".DJI"), ("ixic", ".IXIC"), ("inx", ".INX")]:
        v = _us(sym)
        M[key] = v
        if v is None:
            FALLBACK.append("美股指数_" + key)

    # ---- 中/美国债收益率（bond_zh_us_rate）----
    M["us10y"] = M["us30y"] = M["cn10y"] = M["cn30y"] = None
    M["us10y_chg"] = M["us30y_chg"] = M["cn10y_chg"] = M["cn30y_chg"] = None
    br = _run(lambda: ak.bond_zh_us_rate())
    if br is not None and len(br) >= 2:
        last = br.iloc[-1]; prev = br.iloc[-2]
        cmap = {"美国国债收益率10年": "us10y", "美国国债收益率30年": "us30y",
                "中国国债收益率10年": "cn10y", "中国国债收益率30年": "cn30y"}
        for col, key in cmap.items():
            if col in br.columns:
                try:
                    cur_v = float(last[col]); pre_v = float(prev[col])
                    M[key] = cur_v
                    M[key + "_chg"] = round((cur_v - pre_v) * 100, 1)
                except Exception:
                    pass
    for k in ["us10y", "us30y", "cn10y", "cn30y"]:
        if M[k] is None:
            FALLBACK.append("债券_" + k)

    # ---- 16 关注标的（并行抓取，sina 日线；受限时兜底）----
    codes = ["601398", "601939", "601288", "601988", "600036", "002142", "600919",
             "600926", "601963", "600900", "601006", "600941", "601985", "601318",
             "601088", "601658"]
    stocks = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(_astock, c): c for c in codes}
        for f in concurrent.futures.as_completed(futs):
            c = futs[f]
            try:
                stocks[c] = f.result(timeout=_TIMEOUT)
            except Exception:
                stocks[c] = None
            if stocks[c] is None:
                FALLBACK.append("A股标的_" + c)
    M["stocks"] = stocks

    # ---- 以下类别沙箱网络受限，统一兜底（生产环境若可达则启用）----
    for k in ["hsi", "hscei", "hstech", "hk0941", "wti", "brent", "shgold",
             "intgold", "silver", "btc", "eth", "usdcny_mid", "usdcny_onshore", "dxy"]:
        M[k] = None
        FALLBACK.append("未启用_" + k)

    return M


def get_market():
    """返回统一原始值字典 M；整体硬上限 _OVERALL 秒，超时即返回已取/空结果，绝不挂死。
    同时复用当日磁盘缓存：importlib 为 g_data1/g_data2 各建独立模块实例，磁盘缓存避免重复抓网。"""
    global _CACHE, _DATA_DATE
    if _CACHE is not None:
        return _CACHE
    cached = _load_disk()
    if cached:
        _CACHE = cached
        return _CACHE
    res = [None]
    err = [None]

    def _go():
        try:
            res[0] = _get_market()
        except Exception:  # noqa: BLE001
            err[0] = True

    t = _th.Thread(target=_go, daemon=True)
    t.start()
    t.join(_OVERALL)
    if t.is_alive():
        FALLBACK.append("行情_整体超时(%ds)" % _OVERALL)
        return {}
    if err[0] or res[0] is None:
        return {}
    _CACHE = res[0]
    _save_disk(_CACHE)
    return _CACHE

def pct_str(pct):
    return ("+%.2f%%" if pct >= 0 else "%.2f%%") % pct

def cls_of(pct):
    return "up" if pct >= 0 else "down"

if __name__ == "__main__":
    t0 = time.time()
    M = get_market()
    print("耗时 %.1fs  DATA_DATE:%s" % (time.time() - t0, _DATA_DATE))
    print("FALLBACK 项数:", len(FALLBACK))
    for k in FALLBACK:
        print("  兜底:", k)
    for k, v in M.items():
        if k == "stocks":
            print("  标的样本:", {c: M["stocks"].get(c) for c in ["601398", "600036", "601658"]})
            continue
        print("  %s = %s" % (k, v))
