# 反模式：把 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量）说成已经印进本头 / 已经是回执顺序对上 / 已经落盘

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[结果必须确定 not already printed ≠ bundled（342）](../../tracks/implementation/worked-example-finalize-notprinted-vs-bundled.md)。

## 卖法

把 Finalize 算出的结果必须只依赖上一份状态和决定块 / *T_h* 必须确定 / 造出交易结果集合 写成已经是 Code/Data 印进本头 interchangeable / 已经 printed interchangeable / 已经印进本头交差 interchangeable / 342 finalizedet bundled interchangeable / 316 exectxresult interchangeable / finalizedet-sold-as-prepare interchangeable；把只依赖这两份 / 只依赖 *s_{h-1}* 和 *v* / 结果内容只依赖这两份 写成已经是回执顺序对上 interchangeable / 已经 same-order interchangeable；把造出了 *T* / 造出了交易结果集合 / *T_{p,h}* 回来了 写成已经落盘 interchangeable / 已经 persisted interchangeable，或已经和 342 finalizedet bundled / finalizedet-sold-as-prepare interchangeable / 780 finalize-notprinted interchangeable。

## 为什么错

官方把结果必须确定单句、already printed、already same-order、already persisted 写成三件独立的实现事。把它们卖成 already printed interchangeable / already same-order interchangeable / already persisted interchangeable，会把 not already printed、not already same-order、not already persisted 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头 not already printed / not already same-order / not already persisted 正式三事（342 余量），必须分开 not already printed、not already same-order、not already persisted 三件事，不要和 342 / 338 / 316 / 335 / 779 / 781 糊成一句。

## 和相邻反模式

- [finalize-notprocesssame-sold-as-bundled](finalize-notprocesssame-sold-as-bundled.md) 是状态机复制 ≠ 已经是 Process 同判（342 item 3），不是本页结果必须确定 item 2 单句边界。
- [finalizedet-sold-as-prepare](finalizedet-sold-as-prepare.md) 是 FinalizeBlock 确定性 bundled 全段，不是本页结果必须确定 item 2 单句边界。
- [finalize-notlikeprepare-sold-as-bundled](finalize-notlikeprepare-sold-as-bundled.md) 是必须确定 ≠ 已经可以像 Prepare 那样（342 item 1），不是本页结果必须确定 ≠ 已经印进本头 边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表已经同一顺序（316），不是本页只依赖这两份 ≠ 已经是回执顺序对上 边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 改了状态不是已经落盘（335），不是本页造出了 *T* ≠ 已经落盘 边界。
