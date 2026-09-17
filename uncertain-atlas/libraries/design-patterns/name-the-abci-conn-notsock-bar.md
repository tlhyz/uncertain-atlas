# 模式：点名 abci-conn-notsock 杠

**层次**：实现 / 同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应**：[`../tracks/implementation/worked-example-abci-conn-notsock-vs-bundled.md`](../tracks/implementation/worked-example-abci-conn-notsock-vs-bundled.md)。

- **同进程 不是已经有套接字隔离：** 看见同进程，不是已经有套接字边界 interchangeable / 977 abci-conn-notsock interchangeable。
- **看见一个进程 不是已经是另一条传输：** 看见一个进程，不是已经是另一条传输 interchangeable。
- **看见链在一起 不是已经交差：** 看见链在一起，不是已经换了信任对象 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同进程 正式三事（307 余量），先数清问的是是不是已经隔离、是不是已经是另一条传输、还是看见链在一起是不是已经交差，再决定要不要同一次发布。307 abci-conn vs gates bundled unbundling 在本页 item 1 启动。
