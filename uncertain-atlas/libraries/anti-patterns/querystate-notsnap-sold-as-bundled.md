# 反模式：把 启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量） 写成已经 已经是快照重放 / 已经从创世重放 / 已经交差

**层次**：实现 / 启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应**：[`../tracks/implementation/worked-example-querystate-notsnap-vs-bundled.md`](../tracks/implementation/worked-example-querystate-notsnap-vs-bundled.md)。

把 启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量） 写成已经 已经是快照重放 / 已经从创世重放 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动对齐 正式三事（314 余量），必须分开 not already snapshot-replay、not already genesis-replay、not already settled 三件事，不要和 314 / 38 / 334 / 962 / 963 糊成一句。

也不是：

- [querystate-notlive-sold-as-bundled](querystate-notlive-sold-as-bundled.md) 是上次 Commit 仍未跟上正在跑的块单句边界（963 item 2），不是本页启动对齐仍不是快照重放边界。
- 应用快照已经从创世重放是不变量 38，不是本页 Query 门仍不是 Snapshot 连接边界。
