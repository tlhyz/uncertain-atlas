# 反模式：把 一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量） 写成已经 已经够用 / 已经是四门 / 已经交差

**层次**：实现 / 一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Client and Server](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_client_server.md) ABCI transport / four connections。  
**对应**：[`../tracks/implementation/worked-example-abci-conn-notgates-vs-bundled.md`](../tracks/implementation/worked-example-abci-conn-notgates-vs-bundled.md)。

把 一条连接 not already enough / not already four-gates / not already settled 正式三事（307 余量） 写成已经 已经够用 / 已经是四门 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一条连接 正式三事（307 余量），必须分开 not already enough、not already four-gates、not already settled 三件事，不要和 307 / 33 / 367 / 977 / 978 糊成一句。

也不是：

- [abci-conn-notfast-sold-as-bundled](abci-conn-notfast-sold-as-bundled.md) 是最容易仍未快单句边界（978 item 2），不是本页一条连接仍不是四门边界。
- CheckTx 已经进提案是不变量 33，不是本页四条连接仍不是四门方法边界。
