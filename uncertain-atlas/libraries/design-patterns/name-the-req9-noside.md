# 模式：把四门无副作用三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**例**：[Prepare 不得改已提交状态 ≠ 已经立刻执行就已经交差](../../tracks/implementation/worked-example-req9-noside-vs-commit.md)。

## 三个名字

1. **Prepare 不得改已提交状态不是已经立刻执行就已经交差：** 看见立刻执行了不是已经换了已提交状态。
2. **Process 不得改已提交状态不是已经 Accept 就已经改了：** 看见 Accept 了不是已经进工作状态。
3. **Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态：** 看见签了扩展不是已经写进已提交状态。

## 为什么要分开叫

官方把 Prepare、Process、Extend/Verify 三处不得改 *s<sub>h-1</sub>* 写成三件事。把它们叫成一个「看见立刻执行了就已经交差」，会把四门、候选状态和扩展不进本高状态一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见立刻执行了就已经交差」，先数清问的是 Prepare 不得改已提交状态不是已经立刻执行就已经交差、Process 不得改已提交状态不是已经 Accept 就已经改了，还是 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态，再决定要不要同一次发布。
