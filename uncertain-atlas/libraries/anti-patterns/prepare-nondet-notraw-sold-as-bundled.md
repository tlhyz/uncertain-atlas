# 反模式：把 两边 raw 一样 not already same prepared / not already must be same / not already settled 正式三事（338 余量） 卖成 已经是同一份提案 / 已经必须同一份 / 已经交差

**层次**：实现 / PrepareProposal 与 ExtendVote 的确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-nondet-notraw-vs-bundled.md](../../tracks/implementation/worked-example-prepare-nondet-notraw-vs-bundled.md)。

官方把 Prepare 没有确定性要求 / 两边 raw 一样 / ExtendVote 没有确定性要求 三条核心句写成三件独立的实现事。把它们卖成已经是同一份提案 / 已经必须同一份 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边 raw 一样 正式三事（338 余量），必须分开 not already same prepared、not already must be same、not already settled 三件事，不要和 338 / 327 / 347 / 896 / 898 糊成一句。

## 和相邻反模式

- [prepare-nondet-notmust-sold-as-bundled](prepare-nondet-notmust-sold-as-bundled.md) 是 Prepare 没有确定性要求单句边界（896 item 1），不是本页 raw 边界。
- Req 3 必须 Accept 是不变量 347 / 872，不是本页 raw 边界。
