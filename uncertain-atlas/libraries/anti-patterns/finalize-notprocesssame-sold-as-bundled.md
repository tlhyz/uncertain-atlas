# 反模式：把两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量）说成已经是 Process 同判 / 已经是 Prepare 可以不确定 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[状态机复制 not already process-same ≠ bundled（342）](../../tracks/implementation/worked-example-finalize-notprocesssame-vs-bundled.md)。

## 卖法

把两边状态机复制 / 应用状态一起演化 / 各正确进程上的应用状态一起演化 写成已经是 Process 对任意块同一 Accept/Reject interchangeable / 已经 process-same interchangeable / 已经 Process 同判交差 interchangeable / 342 finalizedet bundled interchangeable / 340 processdet interchangeable / finalizedet-sold-as-prepare interchangeable；把两边状态一起走 / 状态一起演化 / 不是只靠 Process 同判 写成已经是 Prepare 可以不确定 interchangeable / 已经 prepare-nondet interchangeable；把 Agreement / 共识 Agreement / 已经造出 *s_h* 和 *T_h* 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 342 finalizedet bundled / finalizedet-sold-as-prepare interchangeable / 781 finalize-notprocesssame interchangeable。

## 为什么错

官方把状态机复制单句、already process-same、already prepare-nondet、already settled 写成三件独立的实现事。把它们卖成 already process-same interchangeable / already prepare-nondet interchangeable / already settled interchangeable，会把 not already process-same、not already prepare-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边状态机复制不是已经是 Process 对任意块同一裁决 not already process-same / not already prepare-nondet / not already settled 正式三事（342 余量），必须分开 not already process-same、not already prepare-nondet、not already settled 三件事，不要和 342 / 338 / 340 / 335 / 779 / 780 糊成一句。

## 和相邻反模式

- [finalizedet-sold-as-prepare](finalizedet-sold-as-prepare.md) 是 FinalizeBlock 确定性 bundled 全段，不是本页状态机复制 item 3 单句边界。
- [finalize-notlikeprepare-sold-as-bundled](finalize-notlikeprepare-sold-as-bundled.md) 是必须确定 ≠ 已经可以像 Prepare 那样（342 item 1），不是本页状态机复制 ≠ 已经是 Process 同判 边界。
- [finalize-notprinted-sold-as-bundled](finalize-notprinted-sold-as-bundled.md) 是结果必须确定 ≠ 已经印进本头（342 item 2），不是本页 Agreement ≠ 已经交差 边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 ProcessProposal 确定性（340），不是本页状态机复制边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求（338），不是本页状态一起演化 ≠ 已经是 Prepare nondet 边界。
