# -*- coding: utf-8 -*-
# fetch_market.py — 实时行情取数（B 方案核心）
# 生成时由 g_data1 / g_data2 调用，拉取最新交易日收盘数据。
# 设计原则：
#   1) 每个取数在独立线程中执行，硬超时（默认 8s）；接口不可达即快速失败返回 None。
#   2) 16 只标的并行抓取，避免串行挂死。
#   3) 失败项置 None，调用方用硬编码兜底值；FALLBACK 列表记录非实时项供告警。
import os, sys, time, datetime, concurrent.futures

try:
    import akshare as ak
except Exception:
    ak = None

FALLBACK = []        # 记录用兜底值的键名
_DATA_DATE = None    # 实际取到的数据日期（最新交易日）
_TIMEOUT = 8         # 单接口超时（秒）
_CACHE = None         # 同进程缓存

def _run(fn):
    """在独立线程执行 fn，超时返回 None。"""
    if ak is None:
        return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
        fut = ex.submit(fn)
        try:
            r = fut.result(timeout=_TIMEOUT)
        except Exception:
            return None
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

def get_market():
    """返回统一原始值字典 M；结果进程内缓存，避免 g_data1/g_data2 重复抓取。"""
    global _CACHE, _DATA_DATE
    if _CACHE is not None:
        return _CACHE
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
                stocks[c] = f.result()
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

    _CACHE = M
    return M

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
