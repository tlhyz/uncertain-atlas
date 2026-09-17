# 模式：把 FinalizeBlock 确定性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**例**：[Finalize 算出的状态必须只依赖上一份状态和决定块 ≠ 已经可以像 Prepare 那样依赖其它值](../../tracks/implementation/worked-example-finalize-det-vs-prepare.md)。

## 三个名字

1. **Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值：** 看见必须确定不是已经和 Prepare / ExtendVote 同一把尺。
2. **Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头：** 看见造出了 *T* 不是已经是回执顺序对上。
3. **两边状态机复制不是已经是 Process 对任意块同一裁决：** 看见应用状态一起演化不是已经是提案同判。

## 为什么要分开叫

官方把 Finalize 造出的状态必须确定、造出的结果必须确定、再加上 Agreement 才是状态机复制写成三件事。把它们叫成一个「看见必须确定就已经可以像 Prepare 那样」，会把 Prepare 可以不确定、回执字段和 Process 裁决一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须确定就已经可以像 Prepare 那样」，先数清问的是 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值、Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头，还是两边状态机复制不是已经是 Process 对任意块同一裁决，再决定要不要同一次发布。
