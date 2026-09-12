# 反模式：看见 Finalize 算出的状态必须只依赖上一份状态和决定块就当成已经可以像 Prepare 那样依赖其它值 / 看见 Finalize 算出的结果必须只依赖上一份状态和决定块就当成已经是 Code/Data 印进本头 / 看见两边状态机复制就当成已经是 Process 对任意块同一裁决

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**例**：[Finalize 算出的状态必须只依赖上一份状态和决定块 ≠ 已经可以像 Prepare 那样依赖其它值](../../tracks/implementation/worked-example-finalize-det-vs-prepare.md)。

## 塌法

1. 看见 `FinalizeBlock` 算出的状态必须只依赖上一份状态和决定块 / 看见必须确定，就当成已经可以像 Prepare 那样依赖其它值，或当成已经和 Prepare / ExtendVote 同一把尺。
2. 看见 Finalize 算出的结果必须只依赖上一份状态和决定块 / 看见 *T_h* 必须确定，就当成已经是 Code/Data 印进本头，或当成已经是列表同一顺序。
3. 看见两边状态机复制 / 看见应用状态一起演化，就当成已经是 Process 对任意块同一裁决，或当成已经有协议层补丁。

## 为什么会出事

官方写：Finalize 造出 *s_h*，只依赖上一份已提交状态和决定块。同一次还造出结果集合 *T_h*，也只依赖这两份。Requirement 11 和 12 再加上共识的 Agreement，才保证各正确进程上的应用状态一起演化。

## 和相邻反模式

- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求 ≠ 已经必须确定，不是本页这种 Finalize 必须确定 ≠ 已经可以像 Prepare 那样。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表已经同一顺序 / Code 非零已经没进块，不是本页这种结果必须只依赖上一份状态和决定块 ≠ 已经印进本头。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 Process 必须只依赖请求和上一份状态 ≠ 已经可以像 Prepare 那样，不是本页这种状态机复制 ≠ 已经是 Process 同判。
