# 反模式：把 同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量） 写成已经 已经隔离 / 已经是另一条传输 / 已经交差

**层次**：实现 / 同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应**：[`../tracks/implementation/worked-example-abci-conn-notsock-vs-bundled.md`](../tracks/implementation/worked-example-abci-conn-notsock-vs-bundled.md)。

把 同进程 not already socket-isolated / not already other-transport / not already settled 正式三事（307 余量） 写成已经 已经隔离 / 已经是另一条传输 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同进程 正式三事（307 余量），必须分开 not already socket-isolated、not already other-transport、not already settled 三件事，不要和 307 / 5 / 310 / 978 / 979 糊成一句。

也不是：

- [commit-lock-notbcast-sold-as-bundled](commit-lock-notbcast-sold-as-bundled.md) 是等广播仍不能往下走边界（310/976），不是本页同进程仍无套接字隔离边界。
- 半写已经原子是不变量 5，不是本页一个进程仍不是另一条传输边界。
