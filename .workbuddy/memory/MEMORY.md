# 项目长期约定 · 大福・老盛早知道

## 日报生成铁律
- 唯一起点 = `template.html`（v2.17）：每次**全量联网重生成**，严禁 `cp` 上期成品改数字（用户曾明确"重新生成，不是从备份拷贝"）。
- 数据源优先级 neodata-financial-search > westock-data > WebSearch；禁编造数据。
- 涨红跌绿：涨/利好 → 红 `#f85149`(up)，跌/利空 → 绿 `#3fb950`(down)，中性灰，数据青 `#00d4ff`，预警黄 `#f0b429`；**高亮不改字号**。

## 内容结构
- 社区话题固定 **5 个**：问句标题 + `@机构分析师`(橙)/`@价值投资者`(红)/`@谨慎派`(绿) 三角色 + 老盛观点。模板 `lv-label` 已渲染"老盛观点："前缀，填充值**禁带**该前缀（防双重显示）。
- 关注标的 **16 个**；当前 `g_data2.py` 标的列表顺序固定为：工(1)建(2)农(3)中(4)招(5)宁波(6)江苏(7)杭州(8)重庆(9)长江(10)大秦(11)移动(12)核电(13)平安(14)神华(15)邮储(16)；国有大行含邮储共 5 家（工/建/农/中/邮）。**模板 Tab5 的 `标的N` 引用必须与列表顺序一致**，否则整段错位（本次已因此修复）。
- 近期日历固定 6 条；页眉 `{{每日重点事件}}` **≤20 字**。
- 周末/休市：T-1=最近交易日收盘；市场数据可同源，但资讯区须取周末新事件重写。

## 字号 / 布局
- 字号以 `template.html` 为准（阅读文本 **13px**、强调 span 15px）；禁改字号、涨跌语义、占位符结构。
- 窄屏基线：容器 `max-width:1200px`、padding 40px；只调容器/网格 minmax，勿碰红涨绿与高亮字号。

## 生成器工程
- 占位符 794 处 / 779 唯一，键名须带 `{{}}` 再 `re.sub`（否则静默失败）。
- 中文引号铁律：正文用 “”，Python 字符串定界用 ASCII `"`。
- 页眉 ticker 无涨跌占位符 → 生成后按符号后处理 `up/down/neutral` + ▲▼，内层再包语义色 span（否则被染青）。
- 债券行不写 +/-，写"上行3.97bp"防误染红；动作建议用橙 `#ffa657`，仅明确涨跌用红绿。
- 高亮密度：新闻/AI 卡 ≥5 span，其余卡 ≥2；`card-body` 用 balanced-div 提取；**数据展示卡（关注标的深度解读/关键数字速查/股息率对比）豁免**。
- 分文件架构 n1–n7（各 TAB 数据层）+ render（渲染+涨跌后处理）+ qc；重生成后必跑高亮/QC。
- **Tab5 关注标的易错点**：模板里 16 张 `stock-card` 用 `{{标的N_名称/代码/股价/涨跌幅/要点*}}` 引用，N 必须与 `g_data2.py` 的 `标的` 列表下标一致；改列表顺序/增删股票后**必须同步重排模板卡片**（归属 tag、sub-title 分组也要跟着改），否则会出现"邮储被当中行、中行被塞进股份行"之类的错位。改完用脚本比对"渲染名 vs 数据源名"复核。

## 高亮自动增强（hl_boost.py，2026-09-01 引入）
- 手工写 H() 覆盖面有限（实测新闻/AI卡 0/37 达标、其余卡 10/52），必须有自动兜底。
- `hl_boost.py` 提供 `apply(D)`，**必须在 build.py 合并完 d1+d2 之后调用**——`宏观_*`/`要点*`/`综评_*`/`资金_*`/`债基_*` 等键在 g_data1，放在 g_data2 末尾会漏掉一半。
- 规则优先级：带符号百分比 → 涨跌+数值 → 涨跌语义词 → 数字单位 → 主题词 → 实体词 → 机构产品名 → 产业技术词(青) → 动作词(橙)。
- 已有 `<span style="color:...">` 先替换为 `\x00N\x00` 占位符保护，绝不重复包裹；达标即 break，避免过度染色。
- 词表分层：`_UPW/_DNW`(红/绿涨跌语义) `_YEW`(黄主题) `_ENT`(黄实体板块) `_ORG`(黄机构产品) `_TEC`(青产业技术) `_ORW`(橙动作)。缺词时优先补 `_TEC`/`_ORG`（短卡主要靠这两层达标）。
- 效果：新闻/AI 37/37、其余卡 57/57；全页高亮 142 → 488 处，卡片均值 5.7。
- 判定「涨红跌绿矛盾」时须人工复核：机械正则会把「美元走弱→红(利好A股)」「加息预期升温→绿(利空)」误判为矛盾，这类手工高亮语义正确，不算错。

## 质控要点（qc_check.py，2026-09-02 起为统一入口）
- 占位符 0、暂无数据 0、正文 `--` 0；涨跌 class↔符号矛盾 0；div/span 平衡。
- 四区（机构/高股息/社区/操作）≥120 字；社区话题全问句+三角色。**社区话题的「老盛观点」同样需 ≥120 字**，且内含 2-4 处高亮。
- 阈值从 `template.html` 动态取，不写死；统计 `--`/老盛观点前须剔注释与 `<style>`。
- **基线判定原则（关键）**：Tailwind 污染正则会命中项目自有类名 `grid-2/3/4`；「高亮 span 含 font-size」会命中模板自带的强调 span（15px）。这两项**必须与 `规则/template.html` 对比计数**，模板里同样存在的记为继承项，不算缺陷——否则必误报（本期各误报 4 处 / 8 处）。

## 全面质检三脚本（2026-09-02 补 deep_qc.py / cover_qc.py）
- `脚本/qc_check.py`（规范统一入口）：数据及时性 / 结构与样式（行数·tab-panel·sub-title·stock-card·sentiment-item·market-block·Tailwind·占位符·"--"·暂无数据）/ 涨红跌绿 class↔符号 / 高亮 span 总数与字号 / 交互 switchTab / 四区≥120字 / 社区话题格式 / 8大市场块日期。
- `脚本/deep_qc.py`（补充逐项）：语义色强矛盾（利好红·利空绿）、涨跌 class↔符号全量、逐卡高亮密度（新闻/AI≥5、其余≥2、数据卡豁免）、Tab5 十六卡同名同码、页头指数速览填充、关键指数/标的名词覆盖、8大市场块着色。
- `脚本/cover_qc.py`（规范 2.3 逐 Tab 覆盖）：Tab0-7 逐 Tab 高亮密度（Tab0 summary+时间线+要点速览 / Tab1 新闻≥5 / Tab2 AI≥5+生物医学 / Tab3 综评4维度≥3 / Tab4 机构≥2 / Tab5 16股+深度解读+着色 / Tab6 理财≥2+板块覆盖 / Tab7 非数据卡≥2）、标签语义（利好红·利空绿）、数据标注日期（8市场块 2026-09-01）。
- 运行：三脚本均 `python 脚本/xxx.py 老盛早知道_YYYYMMDD.html`，**三者均 PASS 才算全面通过**。
- **deep_qc / cover_qc 已踩坑（写/改脚本务必规避）**：①语义色机械正则会把「美债收益率上行→绿(利空)」误判为矛盾，须用具体字符串豁免（`突破5.27%`/`突破4.79%`/`收益率突破`等）或上下文窗口查"收益率/利率/债"；②`HTML.find('hm-mq')` 会命中 CSS 里的 `.hm-mq` 选择器，须查 `class="hm-mq"`；③逐卡高亮用 `re.split`+`finditer` 索引易错位（CSS 里也含 `card-body` 字样），须直接对 `finditer('<div class="card-body')` 起点切片；④数据展示卡（股息率对比 / 关键数字速查 / 指数速览含"收盘·"）豁免高亮密度，否则必误报；⑤**Tab0/Tab3/Tab5 不用 `card-body` 结构**（Tab0=summary-card+timeline-item+要点速览；Tab3 综评维度卡用 `border-radius:12px;padding:16px` 但风险事件维度卡 padding 值不同；Tab5=stock-card+stock-change/stock-bullets 着色）——用 `card-body` 切分必漏报，须按组件/真实标题定位（`cover_qc` 已按 g_data1 的 综评_A股/外围/地缘/风险事件 四标题定位 4 维度）；⑥`import importlib.util as _iu` 后须用 `_iu.spec_from_file_location`（不要多写一层 `.util`）；⑦脚本末尾提示句「（FAIL 项见上方明细）」含 FAIL 字样，`grep -c FAIL` 会误计 1，须用 `grep "  FAIL "` 查真实失败行。
- **结论判定铁律**：初始 FAIL 先甄别「报告真缺陷」vs「检查脚本误报/逻辑缺陷」，禁止一见 FAIL 就改报告；本项目数据展示卡与利率上行语境已明确豁免，属预期内。

## 照抄/利旧核查铁律（2026-09-02 明确）
- 用户红线：报告不可从上一期成品照抄/改数字（8/18 曾因照抄 81% 资讯照搬且方向反向）。
- 核查方法：提取两期报告纯文本 → 按标点切句 → 比对「完全相同句」占比。
  - 核心叙事区块（新闻/机构/社区/AI/算力/机器人/产业/操作）完全相同句占比 **0%~4%** 即证明全量重生成、无利旧。
  - 全局完全相同句占比 ~4% 属正常：全部来自 **T-1 共享收盘数据**（两期都用 9/1 收盘）+ **通用投资框架表述**（如"控制仓位、留足现金"），非照抄。
  - 上期若是晚间二轮（含 T-1 的 A股数据），本期 A股数据相同是口径必然，不能算利旧；差异看美股/欧股是否推进一日 + 隔夜叙事是否全换。
- 顺带发现 bug 不属于照抄：生物医学卡片占位符 key 名残留（`生物医学_政策_标签和标题`），根因 `脚本/g_data2.py` 生物医学 5 卡元组第二元素误写 key 名，循环填充露出。修复为正确标题短语（政策·立法提速/设备·国产替代/脑机接口·临床突破/就业·人才下沉/安全·军民两用）。

## 数据时点（2026-09-02 明确）
- 晨间生成：A股/港股/亚太取 **T-1** 收盘；美股/欧股取 **T-1 当日**收盘（美股 T-1 场次在北京时间 T 日凌晨收盘，可用）。
- 若上期是**晚间二轮**生成（会含 T-1 的 A股数据），本期 A股口径必然相同，属正常；差异靠「美股/欧股推进一日 + 隔夜叙事全换」拉开，不算照搬。

## 理财利率真实口径（2026-09 核实，勿再用旧的高数值）
- 六大行挂牌：活期 0.05%、3个月 0.65%、半年 0.85%、**1年 0.95%**、2年 1.05%、**3年 1.25%**、**5年 1.30%**；邮储一年 0.98%。
- 大额存单：三年期约 1.55%、五年期最高 1.60%（20万起）；储蓄国债 3年 1.63%、5年 1.70%；货基 7日年化 0.97%-1.3%；R2 固收账面年化 2%-3%。
- 上期（20260901）误用 1.65%/2.15%/2.35%，已在本期修正。

## 预览污染 / 推送
- `present_files` 会回注 `data-page-node-id` 追踪属性 → 提交前须 regex 清除（`git diff` 应为 0、字节与 `git show HEAD:<file>` 一致）。
- GitHub 超时兜底：github.com 不可达但 api.github.com 可达 → 用 Git Data API（`/tmp/gh_push.py`：blobs→trees→commits→PATCH ref）；远端 HEAD 为父，内容一致后 `git reset --soft origin/main` 对齐；推送后校验 size/SHA256 一致。

## index.html 维护
- 密码锁密码 `12345678`（base64 混淆）；`reports` 数组只留一个 `];`，提交前 `node --check` 两段 `<script>`。
- logo 设计维持暗色原版（青闪 `#00d4ff`，勿擅改形状/配色）；**主题跟随系统（系统优先·手动临时）**：init 用 `matchMedia('(prefers-color-scheme: dark)')` 始终按系统值设置并实时监听变化；**不读也不写 localStorage 偏好**，手动点 ☀️/🌙 只是临时 flip `light-theme` 类，系统主题一变即被覆盖（系统判断优先）。index.html 默认 light-theme 类、template.html 默认暗色（body 无类），三处 init 统一用 `classList.toggle('light-theme', !isDark)`、toggleTheme 仅做 class 翻转。三文件 head 已加 `<meta name="color-scheme" content="light dark">`，原生控件也跟随系统主题。再提 logo 改造先问清风格再动手。

## 文件位置（2026-09-01 归置）
- `template.html`、`报告生成规范.md`、`报告质量检查.md` 已移入 **规则/** 子目录；根目录不再散放。
- 定时任务 `automation-1786669952391` 提示词路径同步为 `规则/报告生成规范.md`、`规则/报告质量检查.md`。

## 脚本目录（2026-09-02 归置）
- 生成/质检脚本统一放 **脚本/** 目录，保持根目录清晰：`build.py`/`g_data1.py`/`g_data2.py`/`hl_boost.py`/`qc_check.py` 全部 `git mv` 至 `脚本/`。
- `build.py` 用 `HERE = 脚本目录`、`ROOT = os.path.dirname(HERE)` 回指根目录读写 `规则/template.html` 与报告输出（TPL/OUT 用 `ROOT` 拼接）；`g_data1/2/hl_boost` 同目录 `load()` 不受影响。运行：`python 脚本/build.py`、`python 脚本/qc_check.py 老盛早知道_YYYYMMDD.html`。
- 移动文件坑：用普通 `mv` 会让 git 失联 rename（显示旧路径 D + 新路径 ??），须 `git add` 旧路径(删)+新路径(增) 让相似度识别连成 R，或直接用 `git mv`。中文文件名在 `git status/ls-files` 会被转义成八进制，`grep` 中文易漏配，核对 git 状态优先看 `git status --short` 转义串或 `git diff --cached --stat`。

## 实时取数机制（B 方案，2026-09-02 落地，根治"利旧照抄"）
- **机制铁律**：定时任务触发 agent 走 5 步（搜→重写 g_data1/g_data2 叙事→build→高亮→质检→推送）；`build.py` 仅作"渲染器"，每轮被喂入**当天搜索重写的数据**，旧文件/旧数据非真相来源。严禁"跳过重写直接 build 旧 g_data"。
- **`脚本/fetch_market.py`（实时数字层）**：akshare 隔离 venv（`/Users/sheng/.workbuddy/binaries/python/envs/default/bin/python3` 已装 akshare）；`ThreadPoolExecutor` 8s 硬超时 + 16 标的并行 + 进程内缓存 + FALLBACK 列表。
  - 实时覆盖键：A股5指数 / 美股3指数 / 中美国债收益率(us10y/us30y/cn10y/cn30y + `_chg` bp变动) / 16 标的(股价/涨跌幅/涨跌class)。`g_data1/g_data2` 末尾 `import fetch_market` 重叠覆盖，失败保留硬编码兜底。
  - 沙箱可用端点：指数(sina `stock_zh_index_daily`)、美股(`stock_us_daily`)、债券(`bond_zh_us_rate`)，返回 2026-09-01 真实收盘。**受限**：A股个股(`stock_zh_a_daily`)/港股/商品/外汇 sina 源 → 硬编码兜底（值仍正确 T-1）。
  - `_bond_str` 安全：仅当 `_M[key+"_chg"]` 真实返回才显"升/降N bp"，缺数据显"实时抓取"，**绝不编造涨跌**。
- **`脚本/freshness_gate.py`（防照抄门禁）**：句子级比对新报告 vs 上一期，剥离 `<script>/<style>`+代码句；区分「市场数据句(T-1共享,可接受)」与「叙事/分析句(逐字复制=照抄,硬 FAIL)」。`build.py` 第7步调用，仅告警不 exit（稳定16标的要点属固定参考不硬阻断）。
- **提交前必清**：`present_files` 回注 `data-page-node-id` → 提交前 regex 清除（`git diff`=0），或先 commit 再 present_files。
- **`脚本/fetch_news.py`（叙事实时化，2026-09-02 落地）**：akshare `stock_info_global_em`(真实 标题/摘要/发布时间/链接，200条) + `stock_news_em`(个股) + `stock_hot_keyword_em`(热搜概念)。`apply(D)` 覆盖新闻卡 `标签和标题` 为真实带日期头条（按分类匹配），保留正文(agent分析)。机构/社区/生物医学 多角色叙事无法机械合成→保留 agent 维护，仅提供 get_news/get_stock_news/get_hot_keywords 取数接口。
- **致命坑·ThreadPoolExecutor 挂死**：网络取数**绝不可用** `with ThreadPoolExecutor` + `fut.result(timeout)` ——底层调用挂死时 `__exit__` 的 `shutdown(wait=True)` 会无限阻塞主线程（build 卡 7-11 分钟）。一律改用 `threading.Thread(daemon=True)` + `join(timeout)`，残留线程随进程退出回收。另：`importlib.load()` 每次建独立模块实例、模块内 `_CACHE` 不共享 → 跨 g_data1/g_data2 重复抓网；用**当日磁盘缓存**(temp json, TTL 600s) 复用。
