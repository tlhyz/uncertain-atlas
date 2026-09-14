# 反模式：把 FinalizeBlock decided_last_commit from decided block not proposed_last_commit 正式三事卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled / 已经 proposed_last_commit / 已经 local_last_commit

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock decided_last_commit from decided block not proposed_last_commit ≠ bundled](../../tracks/implementation/worked-example-findecided-notproposed-vs-bundled.md)。

## 卖法

- 「看见 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 / 看见 decided_last_commit 从刚决定那块拿到 就已经 ProcessProposalRequest.proposed_last_commit interchangeable / 已经 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled interchangeable。」
- 「看见 decided_last_commit 从刚决定那块拿到 就已经 PrepareProposalRequest.local_last_commit interchangeable / 已经交差 local_last_commit interchangeable。」
- 「看见 decided_last_commit 从刚决定那块拿到 就已经可以用这两列定奖惩 / 已经 slashed interchangeable / 已经 determine rewards and punishments interchangeable。」

## 为什么错

官方把 Finalize 请求表上 decided_last_commit 从刚决定那块拿到、Process 请求表上 proposed_last_commit 从拟议块拿到、Prepare 请求表上 local_last_commit 从本进程数据结构拿到，以及 Usage 里 can use decided_last_commit and misbehavior to determine rewards and punishments 写成三件独立的实现事。把它们卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled、已经 proposed_last_commit、已经 local_last_commit，会把 decided vs proposed commit、decided vs local commit、decided vs can use slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock decided_last_commit from decided block not proposed_last_commit 正式三事，必须分开 decided vs proposed commit、decided vs local commit、decided vs can use slashed 三个名字，不要把它们卖成 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled / 已经 proposed_last_commit / 已经 local_last_commit。

## 和相邻反模式

- [finreward-sold-as-slashed](finreward-sold-as-slashed.md) 是 463 bundled 三事专用，不是本页 decided vs proposed commit 单句边界。
- [finreward-notslashed-sold-as-bundled](finreward-notslashed-sold-as-bundled.md) 是 558 can use not slashed，不是本页 decided vs can use slashed 边界。
- [finreq-sold-as-procreq](finreq-sold-as-procreq.md) 是 422 Finalize 请求栏 decided vs proposed 单栏，不是本页 decided block commit vs proposed block commit 边界。
