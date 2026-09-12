# 模式：把 CheckTx 最终不再振荡三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**例**：[同一高度回了不同码 ≠ 已经有了 CheckTxCode](../../tracks/implementation/worked-example-checktx-oscillate-vs-stable.md)。

## 三个名字

1. **同一高度回了不同码不是已经有了 CheckTxCode：** 看见集合在不是已经能说 OK。
2. **还在振荡不是已经过了 h_stable：** 看见还在池里不是已经离池。
3. **本地不再振荡不是已经各节点同一份 b：** 看见本地稳定高度不是已经是全局同一高度。

## 为什么要分开叫

官方把同一高度上的码集合、最终存在的稳定高度、必须全网同一份 *b* 写成三件事。把它们叫成一个「看见过了就已经稳定」，会把 CheckTxState、池交接和重放保护一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「CheckTx 过了就已经稳定」，先数清问的是同一高度回了不同码不是已经有了 CheckTxCode、还在振荡不是已经过了 h_stable，还是本地不再振荡不是已经各节点同一份 b，再决定要不要同一次发布。
