# 反模式：把引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量）说成已经验过重复 / 已经有应用级重放保护 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[引擎没有再验重复交易 not already dedup-checked ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notdedup-vs-bundled.md)。

## 卖法

把引擎没有再验重复交易 / 回了提案 / 没有再做额外有效性检查 写成已经验过重复 interchangeable / 已经 dedup-checked interchangeable / 已经验过重复交差 interchangeable / 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable；把能提 / 回了提案 写成已经有应用级重放保护 interchangeable / 已经 app-replay interchangeable / 已经有应用级重放保护交差 interchangeable；把没有再验 / 引擎没有再验 / 没有再做额外检查 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 357 preparevalid bundled / preparevalid-sold-as-checked interchangeable / 824 prepvalid-notdedup interchangeable。

## 为什么错

官方把回了提案、不是已经有应用级重放保护、不是已经交差写成三件独立的实现事。把它们卖成 already dedup-checked interchangeable / already app-replay interchangeable / already settled interchangeable，会把 not already dedup-checked、not already app-replay、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎没有再验重复交易不是已经验过重复 not already dedup-checked / not already app-replay / not already settled 正式三事（357 余量），必须分开 not already dedup-checked、not already app-replay、not already settled 三件事，不要和 357 / 313 / 347 / 825 / 826 糊成一句。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled 全段，不是本页回了提案 item 1 单句边界。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是内存池去重就已经保证不重放（313），不是本页 not already dedup-checked 边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
