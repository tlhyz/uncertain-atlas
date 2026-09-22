# 反模式：把会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量）说成已经丢了安全性 / 已经是提案一致性 / 已经是提案那条

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[会面对和 Req 5 同一类活性问题 not already lost-safety ≠ bundled（348）](../../tracks/implementation/worked-example-req6-notsafety-vs-bundled.md)。

## 卖法

把会面对和 Requirement 5 同一类活性问题 / 会伤活性 / 和 Process 确定性那条同一路 写成已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable / 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable；把和 Req 5 同一路 / 和 Process 确定性那条同一路 写成已经是 347 那种提案一致性 interchangeable / 已经 req3-same interchangeable / 已经提案一致性交差 interchangeable；把扩展这条 / Extend–Verify 这条活性 写成已经是提案那条 interchangeable / 已经 proposal-path interchangeable / 已经提案路径交差 interchangeable，或已经和 348 req6coherence bundled / req6coherence-sold-as-accept interchangeable / 799 req6-notsafety interchangeable。

## 为什么错

官方把会面对和 Req 5 同一类活性问题、不是已经是提案一致性、不是已经是提案那条写成三件独立的实现事。把它们卖成 already lost-safety interchangeable / already req3-same interchangeable / already proposal-path interchangeable，会把 not already lost-safety、not already req3-same、not already proposal-path 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量），必须分开 not already lost-safety、not already req3-same、not already proposal-path 三件事，不要和 348 / 340 / 347 / 797 / 798 糊成一句。

## 和相邻反模式

- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是 Extend–Verify 一致性 bundled 全段，不是本页会面对和 Req 5 同一类活性问题 item 3 单句边界。
- [req6-notany-sold-as-bundled](req6-notany-sold-as-bundled.md) 是正确进程交出的扩展必须 Verify Accept not already any-extension（348 item 1），不是本页 not already lost-safety 边界。
- [req6-notliveness-sold-as-bundled](req6-notliveness-sold-as-bundled.md) 是确定 bug 丢掉 Precommit not already only-liveness（348 item 2），不是本页 not already lost-safety 边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) / [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是 Process / 提案侧，不是本页扩展这条活性边界。
