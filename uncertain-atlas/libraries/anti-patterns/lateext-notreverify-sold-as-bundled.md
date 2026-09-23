# 反模式：把建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量）说成已经是引擎会再 Verify / 已经过了 Req 6 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[建议按 Verify 同款逻辑再看一遍 not already engine-reverify ≠ bundled（352）](../../tracks/implementation/worked-example-lateext-notreverify-vs-bundled.md)。

## 卖法

把建议按 `VerifyVoteExtension` 同款逻辑再看一遍 / 建议再看 / 同款逻辑再看 写成已经是引擎会再 Verify interchangeable / 已经 engine-reverify interchangeable / 已经引擎再 Verify 交差 interchangeable / 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable；把 Prepare 在用扩展 / Prepare 要用这些扩展改提案 写成已经过了 Req 6 interchangeable / 已经 req6-done interchangeable / 已经 Req 6 交差 interchangeable；把能改提案 / MAY 用扩展改提案 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 352 lateext bundled / lateext-sold-as-verified interchangeable / 810 lateext-notreverify interchangeable。

## 为什么错

官方把建议再看、不是已经过了 Req 6、不是已经交差写成三件独立的实现事。把它们卖成 already engine-reverify interchangeable / already req6-done interchangeable / already settled interchangeable，会把 not already engine-reverify、not already req6-done、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量），必须分开 not already engine-reverify、not already req6-done、not already settled 三件事，不要和 352 / 34 / 348 / 809 / 811 糊成一句。

## 和相邻反模式

- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是迟到扩展 bundled 全段，不是本页建议再看 item 2 单句边界。
- [lateext-notverified-sold-as-bundled](lateext-notverified-sold-as-bundled.md) 是 +2/3 之后才进来的扩展写进了 commit info not already verified（352 item 1），不是本页 not already engine-reverify 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept（348），不是本页 not already req6-done 边界。
