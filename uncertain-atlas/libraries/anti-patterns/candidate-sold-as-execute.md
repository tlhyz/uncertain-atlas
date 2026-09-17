# 反模式：看见 Prepare 没有头哈希就当成已经知道本头 / 看见立刻执行出候选就当成已经是 ExecuteTxState / 看见丢掉候选就当成已经永远不用再执行

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[候选 ≠ 已经是 ExecuteTxState](../../tracks/implementation/worked-example-candidate-vs-execute.md)。

## 塌法

1. 看见 PrepareProposal 披露了提案 / 看见两门给的字段差不多，就当成已经知道本头哈希。
2. 看见立刻执行出一份候选 / 看见内存里有状态，就当成已经是 ExecuteTxState，或当成已经能预测本高度 Finalize 会交哪一块。
3. 看见候选很多 / 看见还没 Finalize，就当成已经能无界攒着，或当成丢掉就永远不用再执行。

## 为什么会出事

官方写：Prepare 里还不知道块头哈希。立刻执行不得改 ExecuteTxState，也无法准确预测哪一块会被决定。某一高度收到的提案数没有上界，丢掉之后仍可能在 Finalize 再执行。

## 和相邻反模式

- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页这种候选不是已经是工作状态。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是默认锁 ≠ 已经 RPC 安全，不是本页。
