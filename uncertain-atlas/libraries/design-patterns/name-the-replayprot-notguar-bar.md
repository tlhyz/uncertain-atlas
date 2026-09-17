# 模式：点名 replayprot-notguar 杠

**层次**：实现 / 内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应**：[`../tracks/implementation/worked-example-replayprot-notguar-vs-bundled.md`](../tracks/implementation/worked-example-replayprot-notguar-vs-bundled.md)。

- **内存池去重 不是已经保证不重复：** 看见池子挡过一次，不是已经保证 interchangeable / 965 replayprot-notguar interchangeable。
- **看见索引器在 不是已经有强保证：** 看见索引器在，不是已经有强保证 interchangeable。
- **看见没报重复 不是已经交差：** 看见没报重复，不是已经不会再来 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看内存池去重 正式三事（313 余量），先数清问的是是不是已经保证、是不是已经有强保证、还是看见没报重复是不是已经交差，再决定要不要同一次发布。313 replayprot vs replay bundled unbundling 在本页 item 1 启动。
