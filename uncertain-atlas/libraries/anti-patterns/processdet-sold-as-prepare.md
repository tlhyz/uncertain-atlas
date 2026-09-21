# 反模式：看见 Process 必须只依赖请求和上一份状态就当成已经可以像 Prepare 那样依赖其它值 / 看见两边对任意块同一裁决就当成已经只对诚实提案同一裁决 / 看见 Process 非确定 bug 没有现成解法就当成已经丢了安全性

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**例**：[Process 必须只依赖请求和上一份状态 ≠ 已经可以像 Prepare 那样依赖其它值](../../tracks/implementation/worked-example-process-det-vs-prepare.md)。

## 塌法

1. 看见 `ProcessProposal` 必须只依赖本次请求和 `s_{h-1}` / 看见必须确定，就当成已经可以像 Prepare 那样依赖其它值，或当成已经和 Prepare / ExtendVote 同一把尺。
2. 看见两边对任意块同一裁决 / 看见提议者是拜占庭，就当成已经只对诚实提案同一裁决，或当成已经是诚实 Prepare 必须被诚实 Process Accept。
3. 看见 Process 里有非确定 bug / 看见没有现成解法，就当成已经丢了安全性，或当成已经有协议层补丁。

## 为什么会出事

官方写：Process 是确定函数，Accept/Reject 只依赖这块和上一份已提交状态。所有正确进程对任意块同判，即使提议者是拜占庭。Process 若不再确定，打中的进程严格说已经是 Byzantine，活性不能保证，目前没有清楚的解法。

## 和相邻反模式

- [process-nothonestonly-sold-as-bundled](process-nothonestonly-sold-as-bundled.md) 是两边对任意块同一裁决不是已经只对诚实提案同一裁决 item 2 单句边界，不是本页 ProcessProposal 确定性 bundled 全段。
- [process-notlikeprepare-sold-as-bundled](process-notlikeprepare-sold-as-bundled.md) 是 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 item 1 单句边界，不是本页 ProcessProposal 确定性 bundled 全段。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求 ≠ 已经必须确定，不是本页这种 Process 必须确定 ≠ 已经可以像 Prepare 那样。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种对任意块同判 ≠ 已经只对诚实提案。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径，不是本页这种没有现成解法 ≠ 已经丢了安全性。
