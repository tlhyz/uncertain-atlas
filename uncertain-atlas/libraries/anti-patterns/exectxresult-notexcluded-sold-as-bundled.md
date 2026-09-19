# 反模式：把 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量）说成已经没进块 / 已经没进共识 / 已经和池门同一把尺

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[标成无效 not already excluded from block ≠ bundled（316）](../../tracks/implementation/worked-example-exectxresult-notexcluded-vs-bundled.md)。

## 卖法

把标成无效 / Code ≠ 0 / 标成无效交易 写成已经没进块 interchangeable / 已经 excluded from block interchangeable / 已经从块里删掉 interchangeable / 316 exectxresult bundled interchangeable / 33 four gates interchangeable / exectxresult-sold-as-consensus interchangeable；把没索引 / 无效交易不建索引 / 不建索引 写成已经没进共识 interchangeable / 已经 excluded from consensus interchangeable；把类比 CheckTx / 官方把它类比成没过 CheckTx 写成已经和池门同一把尺 interchangeable / 已经 same as CheckTx gate interchangeable，或已经和 316 exectxresult bundled / exectxresult-sold-as-consensus interchangeable / 708 exectxresult-notexcluded interchangeable。

## 为什么错

官方把标成无效单句、already excluded from block、already excluded from consensus、already same as CheckTx gate 写成三件独立的实现事。把它们卖成 already excluded from block interchangeable / already excluded from consensus interchangeable / already same as CheckTx gate interchangeable，会把 not already excluded from block、not already excluded from consensus、not already same as CheckTx gate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code 非零不是已经没进块 not already excluded from block / not already excluded from consensus / not already same as CheckTx gate 正式三事（316 余量），必须分开 not already excluded from block、not already excluded from consensus、not already same as CheckTx gate 三件事，不要和 316 / 33 / 707 / 709 / 315 糊成一句。

## 和相邻反模式

- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 ExecTxResult vs consensus bundled 全段，不是本页标成无效 item 2 单句边界。
- [exectxresult-notorder-sold-as-bundled](exectxresult-notorder-sold-as-bundled.md) 是回了列表 item 1，不是本页仍在块里边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx 另一门，不是本页类比 CheckTx 是否同一把尺边界。
