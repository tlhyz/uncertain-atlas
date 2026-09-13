# 模式：把 FinalizeBlock must provide values as a result of executing the block 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[must provide 四列 ≠ 已经改了集合](../../tracks/implementation/worked-example-finasresult-vs-candidate.md)。

## 三个名字

1. **must provide 四列不是已经改了集合：** 看见必须回 app_hash / tx_results / validator_updates / consensus_param_updates 不是已经交差 interchangeable。
2. **as a result of executing the block 不是已经 candidate 就不需要执行：** 看见是执行这块的结果不是已经 Process / Prepare candidate interchangeable。
3. **提供了值不是已经空更新就没有义务：** 看见 tx_results 等来自执行结果不是已经 CheckTx 过了 interchangeable。

## 为什么要分开叫

官方把 must provide values、as a result of executing the block、provided values 和 empty keep current 写成三个名字。把它们叫成一个「看见 must provide 就已经改了集合、已经 Process 跑过就不用再执行」，会把 must provide 义务、执行来源和空更新 keep current 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「The Application must provide values … as a result of executing the block」，先数清问的是 must provide 四列是不是已经改了集合、as a result of executing the block 是不是已经 candidate 就不需要执行，还是提供了值是不是已经空更新就没有义务，再决定要不要同一次发布。
