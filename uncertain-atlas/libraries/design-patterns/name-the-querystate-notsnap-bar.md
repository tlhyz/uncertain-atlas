# 模式：点名 querystate-notsnap 杠

**层次**：实现 / 启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应**：[`../tracks/implementation/worked-example-querystate-notsnap-vs-bundled.md`](../tracks/implementation/worked-example-querystate-notsnap-vs-bundled.md)。

- **启动对齐 不是已经是快照重放：** 看见对齐，不是已经装了快照 interchangeable / 964 querystate-notsnap interchangeable。
- **看见启动握手 不是已经从创世重放：** 看见启动握手，不是已经从创世重放 interchangeable。
- **看见 Query 门 不是已经交差：** 看见 Query 门，不是已经是 Snapshot 连接 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动对齐 正式三事（314 余量），先数清问的是是不是已经是快照重放、是不是已经从创世重放、还是看见 Query 门是不是已经交差，再决定要不要同一次发布。314 querystate vs execute bundled unbundling 在本页 item 3 完成。
