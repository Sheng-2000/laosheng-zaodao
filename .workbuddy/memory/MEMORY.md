# 项目长期约定 · 大福・老盛早知道

## 1. 生成铁律
- 唯一起点 = `规则/template.html`（v2.17），每期**全量联网重生成**；严禁 `cp` 上期成品改数字（8/18 曾照抄 81%）。
- 数据源优先级：neodata-financial-search > westock-data > WebSearch；**禁编造数据**。
- 机制：定时任务 agent 走 5 步（搜 → 重写 g_data1/g_data2 → build → 高亮 → 质检 → 推送）；`build.py` 只是渲染器，**严禁跳过重写直接 build 旧 g_data**。
- 数据时点：晨间生成 A股/港股/亚太/欧股取 **T-1** 收盘，美股取 T-1 当日收盘。上期若是晚间二轮（含 T-1 A股），本期 A股口径相同属正常，差异靠美股欧股推进一日 + 叙事全换。

## 2. 配色 / 字号
- 涨/利好 → 红 `#f85149`（class `up`）；跌/利空 → 绿 `#3fb950`（`down`）；中性灰；数据青 `#00d4ff`；预警黄 `#f0b429`；动作建议橙 `#ffa657`。
- **高亮不改字号**（正文 13px、模板强调 span 15px）。债券行不写 +/-，写"上行Xbp"防误染红。
- 页眉 ticker 无涨跌占位符 → build 后按符号后处理 `up/down/neutral` + ▲▼，内层再包语义色 span。

## 3. 内容结构
- 社区话题固定 **5 个**：问句标题 + `@机构分析师`(橙)/`@价值投资者`(红)/`@谨慎派`(绿) + 老盛观点；模板已渲染"老盛观点："前缀，填充值禁带该前缀。老盛观点亦需 ≥120 字 + 2-4 处高亮。
- 关注标的 **16 个**，顺序固定：工1 建2 农3 中4 招5 宁波6 江苏7 杭州8 重庆9 长江10 大秦11 移动12 核电13 平安14 神华15 邮储16（国有大行含邮储 5 家）。**模板 Tab5 的 `标的N` 引用必须与列表顺序一致**，改顺序/增删后必须同步重排模板卡片（含 tag、sub-title 分组），并用脚本比对"渲染名 vs 数据源名"复核。
- 近期日历 6 条；页眉 `{{每日重点事件}}` ≤20 字。四区（机构/高股息/社区/操作）各 ≥120 字。

## 4. 生成器工程
- 占位符 794 处 / 779 唯一，键名须带 `{{}}` 再 `re.sub`（否则静默失败）。
- 中文引号：正文用 “”，Python 定界用 ASCII `"`。
- 架构：`g_data1.py`(市场/指数/情绪/速查/估值/综评) + `g_data2.py`(叙事/新闻/机构/社区/标的/高股息) → `build.py` 合并 → `hl_boost.apply(D)` → 填充模板 → 输出 `老盛早知道_YYYYMMDD.html`。
- 运行：`python 脚本/build.py`、`python 脚本/qc_check.py 老盛早知道_YYYYMMDD.html`。`build.py` 用 `HERE`+`ROOT` 回指根目录。

## 5. 高亮增强（hl_boost.py）
- 手工 H() 覆盖不足，必须自动兜底；`apply(D)` **必须在 build 合并 d1+d2 之后调用**（`宏观_*`/`要点*`/`综评_*`/`资金_*` 在 g_data1）。
- 规则优先级：带符号百分比 → 涨跌+数值 → 涨跌语义词 → 数字单位 → 主题词 → 实体词 → 机构产品名 → 产业技术词(青) → 动作词(橙)。已有 `<span style="color:...">` 用 `\x00N\x00` 占位保护，达标即 break。
- 词表分层 `_UPW/_DNW/_YEW/_ENT/_ORG/_TEC/_ORW`；缺词优先补 `_TEC`/`_ORG`。
- 密度目标：新闻/AI 卡 ≥5，其余卡 ≥2；**数据展示卡（深度解读/关键数字速查/股息率对比/指数速览）豁免**。

## 6. 质检三脚本（三者均 PASS 才算通过）
- `qc_check.py`（统一入口）：数据及时性 / 结构与样式 / 涨跌 class↔符号 / 高亮字号 / switchTab / 四区≥120字 / 社区格式 / 8 市场块日期。
- `deep_qc.py`：语义色强矛盾、逐卡高亮密度、Tab5 十六卡同名同码、页头指数速览、8 市场块着色。
- `cover_qc.py`：Tab0-7 逐 Tab 高亮密度、标签语义（利好红·利空绿）、数据标注日期。
- **基线判定原则**：Tailwind 污染正则会命中自有类名 `grid-2/3/4`；「高亮 span 含 font-size」会命中模板自带 15px span。二者必须与 `规则/template.html` 对比计数，模板里也有的记为继承项，不算缺陷。
- **结论判定铁律**：初始 FAIL 先甄别「报告真缺陷」vs「脚本误报」，禁止一见 FAIL 就改报告。
- 已知脚本坑：①语义色正则会误判「美债收益率上行→绿」，须字符串豁免（`突破5.27%`/`收益率突破`）或上下文查"收益率/利率/债"；②查 `class="hm-mq"` 而非 `hm-mq`（会命中 CSS）；③切卡须对 `finditer('<div class="card-body')` 起点切片，勿用 `re.split`；④Tab0/3/5 不用 `card-body`，须按组件/真实标题定位；⑤`importlib.util as _iu` → `_iu.spec_from_file_location`；⑥查真实失败用 `grep "  FAIL "`（末尾提示句含 FAIL 会误计 1）。

## 7. 防照抄门禁
- `freshness_gate.py`：句子级比对新报告 vs 上一期，剥离 script/style/代码句；区分「市场数据句(T-1 共享，可接受)」与「叙事句（逐字复制 = 硬 FAIL）」。build 第7步调用，仅告警不 exit。
- 核查标准：核心叙事区块完全相同句占比 **0%~4%** 合格；全局 ~4% 属正常（共享 T-1 收盘数据 + 通用框架表述）。

## 8. 实时取数
- `fetch_market.py`：akshare 隔离 venv（`/Users/sheng/.workbuddy/binaries/python/envs/default/bin/python3` 已装 akshare）。覆盖键：A股5指数 / 美股3指数 / 中美国债收益率(+bp) / 16 标的。可用端点：指数 `stock_zh_index_daily`、美股 `stock_us_daily`、债券 `bond_zh_us_rate`；个股/港股/商品/外汇受限 → 硬编码兜底。
- **交叉校验铁律**：实时值若与搜索核实值冲突，**以搜索核实值为准**。可用 `LAOSHENG_STATIC=1` 跳过数值覆盖、锁定搜索核实的硬编码值（当前默认此模式）。
- `fetch_news.py`：akshare `stock_info_global_em`(200条真实头条) + `stock_news_em` + `stock_hot_keyword_em`；覆盖新闻卡 `标签和标题`，正文仍由 agent 维护。
- **致命坑**：网络取数绝不可用 `with ThreadPoolExecutor` + `fut.result(timeout)`（挂死时 `__exit__` 的 `shutdown(wait=True)` 无限阻塞，build 卡 7-11 分钟）。一律用 `threading.Thread(daemon=True)` + `join(timeout)`。另 `importlib.load()` 每次建独立模块实例、`_CACHE` 不共享，改用**当日磁盘缓存**（temp json, TTL 600s）。

## 9. 理财利率真实口径（2026-09 核实）
- 六大行挂牌：活期 0.05%、3M 0.65%、半年 0.85%、**1年 0.95%**、2年 1.05%、**3年 1.25%**、**5年 1.30%**；邮储一年 0.98%。
- 大额存单 3年 ≈1.55%、5年最高 1.60%（20万起）；储蓄国债 3年 1.63%、5年 1.70%；货基 7日年化 0.97%-1.3%；R2 固收年化 2%-3%。

## 10. 文件 / 目录
- `规则/`：template.html、报告生成规范.md、报告质量检查.md。`脚本/`：build/g_data1/g_data2/hl_boost/qc_check/deep_qc/cover_qc/fetch_market/fetch_news/freshness_gate。
- 移动文件须用 `git mv`（普通 mv 会失联 rename）；中文文件名在 git 输出被转义成八进制，核对用 `git status --short` / `git diff --cached --stat`。

## 11. 预览污染 / 推送
- `present_files` 会回注 `data-page-node-id` → 提交前 regex 清除（`git diff` 应为 0），或先 commit 再 present。
- GitHub 超时兜底：github.com 不可达但 api.github.com 可达 → 用 Git Data API（`/tmp/gh_push.py`：blobs→trees→commits→PATCH ref）；远端 HEAD 为父，内容一致后 `git reset --soft origin/main` 对齐；推送后校验 size/SHA256 一致。

## 12. index.html 维护
- 密码锁 `12345678`（base64 混淆）；`reports` 数组只留一个 `];`，提交前 `node --check` 两段 `<script>`。
- logo 维持暗色原版（青闪 `#00d4ff`）。**主题跟随系统（系统优先·手动临时）**：init 用 `matchMedia('(prefers-color-scheme: dark)')` 设置并实时监听；**不读不写 localStorage**；手动 ☀️/🌙 仅临时 flip `light-theme` 类。三处 init 统一 `classList.toggle('light-theme', !isDark)`，toggleTheme 仅做 class 翻转。三文件 head 已加 `<meta name="color-scheme" content="light dark">`。改 logo 前先问清风格。
