# 模式：点名 snapshot-take-notall 杠

**层次**：实现 / 只留最近两份 not already all-history / not already five-fields / not already settled 正式三事（324 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应**：[`../tracks/implementation/worked-example-snapshot-take-notall-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-take-notall-vs-bundled.md)。

- **只留最近两份 不是已经有了全部历史快照：** 看见只留两份，不是已经有了全部历史 interchangeable / 952 snapshot-take-notall interchangeable。
- **看见 Hash 对上 不是已经五个字段都相同：** 看见 Hash 对上，不是五个字段都对上 interchangeable。
- **看见 Hash 不是已经交差：** 看见 Hash，不是已经是轻验 AppHash interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只留最近两份 正式三事（324 余量），先数清问的是是不是已经有了全部历史、是不是已经五个字段都相同、还是看见 Hash 是不是已经交差，再决定要不要同一次发布。324 snapshot-take vs commit bundled unbundling 在本页 item 3 完成。
