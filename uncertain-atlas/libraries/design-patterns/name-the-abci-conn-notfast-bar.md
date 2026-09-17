# 模式：点名 abci-conn-notfast 杠

**层次**：实现 / gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应**：[`../tracks/implementation/worked-example-abci-conn-notfast-vs-bundled.md`](../tracks/implementation/worked-example-abci-conn-notfast-vs-bundled.md)。

- **gRPC 最容易 不是已经高性能：** 看见最容易，不是已经快 interchangeable / 978 abci-conn-notfast interchangeable。
- **看见能回话 不是已经没有开销：** 看见能回话，不是已经没有开销 interchangeable。
- **看见套接字那套前缀 不是已经交差：** 看见套接字那套前缀，不是已经套在 gRPC 上 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 gRPC 最容易 正式三事（307 余量），先数清问的是是不是已经快、是不是已经没有开销、还是看见套接字那套前缀是不是已经交差，再决定要不要同一次发布。307 abci-conn vs gates bundled unbundling 在本页 item 2 续。
