# 反模式：把 gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量） 写成已经 已经快 / 已经没有开销 / 已经交差

**层次**：实现 / gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应**：[`../tracks/implementation/worked-example-abci-conn-notfast-vs-bundled.md`](../tracks/implementation/worked-example-abci-conn-notfast-vs-bundled.md)。

把 gRPC 最容易 not already fast / not already no-overhead / not already settled 正式三事（307 余量） 写成已经 已经快 / 已经没有开销 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 gRPC 最容易 正式三事（307 余量），必须分开 not already fast、not already no-overhead、not already settled 三件事，不要和 307 / 52 / 334 / 977 / 979 糊成一句。

也不是：

- [abci-conn-notsock-sold-as-bundled](abci-conn-notsock-sold-as-bundled.md) 是同进程仍无套接字隔离单句边界（977 item 1），不是本页最容易仍未快边界。
- post-commit 等待已经是槽位是不变量 52，不是本页能回话仍有开销边界。
