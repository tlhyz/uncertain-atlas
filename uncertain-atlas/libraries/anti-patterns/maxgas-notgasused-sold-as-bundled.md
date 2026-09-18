# 反模式：把 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量）说成已经算进共识 / 已经按实用气验过 / 已经由引擎强制不等式

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有 GasUsed not already in consensus ≠ bundled（315）](../../tracks/implementation/worked-example-maxgas-notgasused-vs-bundled.md)。

## 卖法

把有 GasUsed / 回包 GasUsed / GasUsed 字段在 写成已经算进共识 interchangeable / 已经 in consensus interchangeable / 已经被 CometBFT 用进共识 interchangeable / 315 maxgas bundled interchangeable / 704 maxgas-notenforced interchangeable / maxgas-sold-as-enforced interchangeable；把 GasWanted 过了池门 / 每笔 GasWanted <= MaxGas / 提议一块 GasWanted 之和 <= MaxGas 写成已经按实用气验过 interchangeable / 已经 practical-gas checked interchangeable；把应用应强制 GasUsed <= GasWanted / 官方写应用应强制 写成已经由引擎强制该不等式 interchangeable / 已经 engine-enforced inequality interchangeable，或已经和 315 maxgas bundled / maxgas-sold-as-enforced interchangeable / 705 maxgas-notgasused interchangeable。

## 为什么错

官方把有 GasUsed 单句、already in consensus、already practical-gas checked、already engine-enforced inequality 写成三件独立的实现事。把它们卖成 already in consensus interchangeable / already practical-gas checked interchangeable / already engine-enforced inequality interchangeable，会把 not already in consensus、not already practical-gas checked、not already engine-enforced inequality 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 GasUsed 不是已经算进共识 not already in consensus / not already practical-gas checked / not already engine-enforced inequality 正式三事（315 余量），必须分开 not already in consensus、not already practical-gas checked、not already engine-enforced inequality 三件事，不要和 315 / 704 / 706 / 299 / 33 糊成一句。

## 和相邻反模式

- [maxgas-sold-as-enforced](maxgas-sold-as-enforced.md) 是 MaxGas vs enforced bundled 全段，不是本页有 GasUsed item 2 单句边界。
- [maxgas-notenforced-sold-as-bundled](maxgas-notenforced-sold-as-bundled.md) 是字段在 item 1，不是本页 GasUsed 算进共识边界。
- [exectxgas-sold-as-checktx](exectxgas-sold-as-checktx.md) 是另一气路径卖法，不是本页引擎是否强制 GasUsed <= GasWanted 边界。
