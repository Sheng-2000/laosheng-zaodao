# 老盛早知道 · 项目长期记忆

## 项目信息
- 仓库：https://github.com/Sheng-2000/laosheng-zaodao.git
- 分支：main
- 部署方式：GitHub Pages（push 后自动部署）
- 本地路径：/Users/sheng/Sheng/MyData/老盛的每日快讯/WorkBuddy版/

## 每日快讯生成规范（必须严格遵守）
1. 读取 template.html 了解结构和样式
2. 搜索当日新闻、AI动态、市场行情、投资观点、关注标的
3. 生成 `老盛早知道_YYYYMMDD.html` 并写入本地
4. 更新 index.html 的 reports 数组（首位插入）和 header-meta 日期
5. **【关键步骤，每次必须执行】** git add + git commit + git push origin main 部署到 GitHub Pages
   - 不能遗漏推送步骤，用户明确要求每次生成后都要推送

## 关注标的
银行：工商银行(601398)、招商银行(600036)、宁波银行(002142)、江苏银行(600919)、杭州银行(600926)、农业银行(601288)、重庆银行(601963)
公用事业/能源/通信：中国移动(600941)、长江电力(600900)、中国核电(601985)、大秦铁路(601006)、中国海油(600938)、中国平安(601318)

## Tab切换JS规范
switchTab 函数必须使用 classList.toggle 方式，严禁使用 inline style。

## 移动端适配规范
@media(max-width:768px) 中的 header-top 必须用 grid 语法，不能用 flex。
- **闪电图标（brand-icon）和标题（brand-title）必须在同一行**：header-top 用 `grid-template-columns: 48px 1fr`，绝不能用 `1fr`（单列）。
- header-meta 独占下一行：设置 `grid-column: 1 / -1`，同时保留 `border-left:none; padding-left:0; flex-direction:row; flex-wrap:wrap`。
