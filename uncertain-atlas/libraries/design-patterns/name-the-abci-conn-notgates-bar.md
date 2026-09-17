# 模式：点名 abci-conn-notgates 杠

**层次**：实现 / 一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应**：[`../tracks/implementation/worked-example-abci-conn-notgates-vs-bundled.md`](../tracks/implementation/worked-example-abci-conn-notgates-vs-bundled.md)。

- **一条连接 不是已经够用：** 看见回了一句，不是已经齐了连接 interchangeable / 979 abci-conn-notgates interchangeable。
- **看见四条连接 不是已经是四门：** 看见四条连接，不是已经是 Prepare / Process / Finalize / Extend interchangeable。
- **看见客户端 不是已经交差：** 看见客户端，不是已经只是共识引擎 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一条连接 正式三事（307 余量），先数清问的是是不是已经够用、是不是已经是四门、还是看见客户端是不是已经交差，再决定要不要同一次发布。307 abci-conn vs gates bundled unbundling 在本页 item 3 完成。
