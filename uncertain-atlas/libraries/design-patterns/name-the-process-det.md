# 模式：把 ProcessProposal 确定性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**例**：[Process 必须只依赖请求和上一份状态 ≠ 已经可以像 Prepare 那样依赖其它值](../../tracks/implementation/worked-example-process-det-vs-prepare.md)。

## 三个名字

1. **Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值：** 看见必须确定不是已经和 Prepare / ExtendVote 同一把尺。
2. **两边对任意块同一裁决不是已经只对诚实提案同一裁决：** 看见提议者是拜占庭不是已经可以各判各的。
3. **Process 非确定 bug 没有现成解法不是已经丢了安全性：** 看见活性不能保证不是已经有协议层补丁。

## 为什么要分开叫

官方把 Process 必须确定、对拜占庭提案也要同一裁决、没有清楚解法写成三件事。把它们叫成一个「看见必须确定就已经可以像 Prepare 那样」，会把 Prepare 可以不确定、四门和提议超时一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须确定就已经可以像 Prepare 那样」，先数清问的是 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值、两边对任意块同一裁决不是已经只对诚实提案同一裁决，还是 Process 非确定 bug 没有现成解法不是已经丢了安全性，再决定要不要同一次发布。
