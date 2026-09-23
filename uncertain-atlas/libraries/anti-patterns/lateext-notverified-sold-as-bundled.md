# 反模式：把 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量）说成已经 Verify 过 / 已经 Accept / 已经后来的也验过

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[+2/3 之后才进来的扩展写进了 commit info not already verified ≠ bundled（352）](../../tracks/implementation/worked-example-lateext-notverified-vs-bundled.md)。

## 卖法

把 +2/3 之后才进来的扩展写进了 commit info / 写进了 last_commit / last_commit 里有扩展 写成已经 Verify 过 interchangeable / 已经 verified interchangeable / 已经 Verify 交差 interchangeable / 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable；把有扩展 / 票上带了扩展 写成已经 Accept interchangeable / 已经 accept interchangeable / 已经 Accept 交差 interchangeable；把凑齐了 +2/3 / 过了最低 +2/3 写成已经后来的也验过 interchangeable / 已经 later-verified interchangeable / 已经后来验过交差 interchangeable，或已经和 352 lateext bundled / lateext-sold-as-verified interchangeable / 809 lateext-notverified interchangeable。

## 为什么错

官方把写进了 last_commit、不是已经 Accept、不是后来的也已经验过写成三件独立的实现事。把它们卖成 already verified interchangeable / already accept interchangeable / already later-verified interchangeable，会把 not already verified、not already accept、not already later-verified 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量），必须分开 not already verified、not already accept、not already later-verified 三件事，不要和 352 / 34 / 348 / 810 / 811 糊成一句。

## 和相邻反模式

- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是迟到扩展 bundled 全段，不是本页写进了 last_commit item 1 单句边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交就已经是块非法（34），不是本页 not already verified 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept（348），不是本页 not already accept 边界。
