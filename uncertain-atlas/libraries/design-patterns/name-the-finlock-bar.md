# 模式：把 FinalizeBlock When lock mempool Commit recheck 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 7–11。  
**例**：[locks mempool ≠ 已经是 Commit 锁](../../tracks/implementation/worked-example-finlock-vs-commit.md)。

## 三个名字

1. **locks mempool / no CheckTx on new tx 不是已经是 Commit 锁：** 看见 When 第 7 步不是已经 RPC 安全默认锁。
2. **calls Commit to persist application state 不是已经引擎 persist 这三份：** 看见 Commit 不是已经 Finalize 改了就已经落盘。
3. **optionally recheck / unlock / start h+1 round 0 不是已经是 Recheck：** 看见再验不是已经 RECHECK 类型 interchangeable。

## 为什么要分开叫

官方把 When 第 7 步 locks mempool、第 8 步 calls Commit、第 9–11 步 optionally recheck / unlock / start h+1 round 0 写成三个名字。把它们叫成一个「看见 Finalize 之后就已经锁池、已经 Commit 落盘、已经 Recheck」，会把锁池、应用 Commit 落盘和可选再验三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 之后就已经交差」，先数清问的是 locks mempool 是不是已经是 Commit 锁、calls Commit 是不是已经引擎 persist 这三份，还是 optionally recheck / unlock / start h+1 是不是已经是 Recheck，再决定要不要同一次发布。
