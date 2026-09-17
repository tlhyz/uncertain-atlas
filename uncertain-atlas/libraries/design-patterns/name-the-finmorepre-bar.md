# 模式：把 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**例**：[includes processing time ≠ 已经是 timeout_commit](../../tracks/implementation/worked-example-finmorepre-vs-timeout.md)。

## 三个名字

1. **includes processing time 不是已经是 timeout_commit：** 看见包含应用和 CometBFT 处理已提交块的时间不是已经 Previously timeout_commit interchangeable。
2. **more precommits despite 2/3+ 不是已经决定 / 已经最终：** 看见给提议者多收 precommit 的机会不是已经 has required 2/3+ 就已经决定 interchangeable。
3. **after committing before next height 不是已经是槽位 / 1s 常量：** 看见 Commit 后再开下一高 / set to 0 不是已经槽位 / 已经最终 / 已经把 1s 抄进不确定 interchangeable。

## 为什么要分开叫

官方把 includes processing time、more precommits despite 2/3+、after committing before next height 和 timeout_commit、已经决定、槽位 / 最终性 写成三个名字。把它们叫成一个「已经有 2/3+ 就不需要 delay、已经是 timeout_commit」，会把 processing time、more precommits、Commit 后再等 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.next_block_delay Usage，先数清问的是 includes processing time 是不是已经是 timeout_commit、more precommits despite 2/3+ 是不是已经决定 / 已经最终，还是 after committing before next height 是不是已经是槽位 / 1s 常量，再决定要不要同一次发布。
