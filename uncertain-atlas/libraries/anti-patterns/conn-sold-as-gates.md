# 反模式：看见同进程就当成已经有套接字隔离 / 看见 gRPC 最容易就当成已经高性能 / 看见一条连接就当成已经够用或已经是四门

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md)。  
**例**：[一条连接 ≠ 已经是四门](../../tracks/implementation/worked-example-abci-conn-vs-gates.md)。

## 塌法

1. 看见同进程 / 看见编进同一个二进制，就当成已经有套接字隔离。
2. 看见语言里有 gRPC / 看见这是最容易的做法，就当成已经是高性能路径。
3. 看见一条 ABCI 连接 / 看见已经能回话，就当成已经够用，或当成已经是四门。
4. 看见套接字那套长度前缀，就当成已经套在 gRPC 上。
5. 看见 ABCI 客户端，就当成已经只是共识引擎。

## 为什么会出事

官方写：同进程是函数调用。gRPC 最容易，但有显著开销，长度前缀不适用于 gRPC。服务器必须能处理多条连接，因为 CometBFT 用四条。四条连接不是四门。

## 和相邻反模式

- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页这种一条连接不是四门。
- [appstate-sold-as-validated](appstate-sold-as-validated.md) 是创世应用段 ≠ 已经验过，不是本页。
