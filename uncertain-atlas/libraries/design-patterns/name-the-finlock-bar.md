# 模式：把 FinalizeBlock When locks mempool 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**例**：[CometBFT locks mempool ≠ 已经交差](../../tracks/implementation/worked-example-finlock-vs-commitlock.md)。

## 三个名字

1. **CometBFT locks the mempool 不是已经交差：** 看见 When 第 7 步锁内存池，不是已经 Finalize + Commit 交差。
2. **no calls to CheckTx on new transactions 不是已经 CheckTx 技术上可选 / 已经进池：** 看见新交易不进 CheckTx，不是已经 optional / 已经池门过了。
3. **locks mempool after persist 不是已经是 Commit 锁 / 已经解锁 / 已经是 Recheck：** 看见 persist 之后才锁，不是已经 Commit RPC 锁 / unlock / Recheck interchangeable。

## 为什么要分开叫

官方把 When 第 7 步 locks the mempool — no calls to `CheckTx` on new transactions 写成两个子句、三个名字。把它们叫成一个「看见锁了内存池就已经交差、已经不能再收新交易」，会把交差、CheckTx optional、Commit 锁、Recheck 四条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见锁了内存池就已经交差」，先数清问的是 CometBFT locks the mempool 是不是已经交差、no calls to CheckTx on new transactions 是不是已经 CheckTx 技术上可选 / 已经进池，还是 locks mempool after persist 是不是已经是 Commit 锁 / 已经解锁 / 已经是 Recheck，再决定要不要同一次发布。
