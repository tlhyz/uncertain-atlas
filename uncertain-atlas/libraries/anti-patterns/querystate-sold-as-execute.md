# 反模式：看见 Query 连接就当成已经是 ExecuteTxState / 看见上次 Commit 就当成已经跟上正在跑的块 / 看见启动对齐就当成已经是快照重放

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**例**：[QueryState ≠ 已经是 ExecuteTxState](../../tracks/implementation/worked-example-querystate-vs-execute.md)。

## 塌法

1. 看见 Query 连接 / 看见在答用户查询，就当成已经是 ExecuteTxState，或当成已经能改工作状态。
2. 看见 QueryState / 看见上次 Commit，就当成已经跟上正在跑的块，或当成已经是 CheckTxState。
3. 看见启动时对齐 / 看见 state sync 之后对齐，就当成已经是快照重放，或当成已经从创世重放。

## 为什么会出事

官方写：QueryState 是 ExecuteTxState 在上次 Commit 之后的只读副本，而且是整块处理完、已经提交到盘之后的那一份。这条连接用来答用户查询，也用来在启动或 state sync 之后对齐，不是 Snapshot 连接。

## 和相邻反模式

- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState，不是本页这种 QueryState。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是默认锁 ≠ 已经 RPC 安全，不是本页。
