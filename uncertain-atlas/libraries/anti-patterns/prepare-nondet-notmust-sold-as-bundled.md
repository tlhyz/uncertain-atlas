# 反模式：把 Prepare 没有确定性要求 not already must be deterministic / not already same ruler as Process / not already settled 正式三事（338 余量） 卖成 已经必须确定 / 已经和 Process 同一把尺 / 已经交差

**层次**：实现 / PrepareProposal 与 ExtendVote 的确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-nondet-notmust-vs-bundled.md](../../tracks/implementation/worked-example-prepare-nondet-notmust-vs-bundled.md)。

官方把 Prepare 没有确定性要求 / 两边 raw 一样 / ExtendVote 没有确定性要求 三条核心句写成三件独立的实现事。把它们卖成已经必须确定 / 已经和 Process 同一把尺 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有确定性要求 正式三事（338 余量），必须分开 not already must be deterministic、not already same ruler as Process、not already settled 三件事，不要和 338 / 340 / 33 / 897 / 898 糊成一句。

## 和相邻反模式

- [process-det-notprep-sold-as-bundled](process-det-notprep-sold-as-bundled.md) 是 Process 必须确定（340/893），不是本页 Prepare 可以不确定边界。
- Process 必须只依赖请求和上一份状态是不变量 340 / 893，不是本页 Prepare 可以不确定边界。
