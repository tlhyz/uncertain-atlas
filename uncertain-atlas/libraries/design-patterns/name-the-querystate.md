# 模式：把 QueryState 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**例**：[QueryState ≠ 已经是 ExecuteTxState](../../tracks/implementation/worked-example-querystate-vs-execute.md)。

## 三个名字

1. **QueryState 不是已经是 ExecuteTxState：** 看见能查不是已经能改工作状态。
2. **上次 Commit 不是已经跟上正在跑的块：** 看见只读副本不是已经含本轮还没交差的执行。
3. **启动对齐不是已经是快照重放：** 看见 Query 门对齐不是已经装了快照。

## 为什么要分开叫

官方把只读副本、已提交到盘、启动/state sync 对齐写成三件事。把它们叫成一个「看见能查就已经是工作状态」，会把 CheckTxState、RPC 锁和快照重放一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Query 已经能查」，先数清问的是 QueryState 不是已经是 ExecuteTxState、上次 Commit 不是已经跟上正在跑的块，还是启动对齐不是已经是快照重放，再决定要不要同一次发布。
