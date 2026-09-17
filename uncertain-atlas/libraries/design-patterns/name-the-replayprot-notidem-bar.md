# 模式：点名 replayprot-notidem 杠

**层次**：实现 / 通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应**：[`../tracks/implementation/worked-example-replayprot-notidem-vs-bundled.md`](../tracks/implementation/worked-example-replayprot-notidem-vs-bundled.md)。

- **通常不受欢迎 不是已经没有幂等例外：** 看见通常不受欢迎，不是已经没有例外 interchangeable / 967 replayprot-notidem interchangeable。
- **看见幂等 不是已经由内存池保证：** 看见幂等，不是已经由内存池保证 interchangeable。
- **看见官方点名 undesirable 不是已经交差：** 看见官方点名 undesirable，不是已经规定不确定必须怎样写幂等 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常不受欢迎 正式三事（313 余量），先数清问的是是不是已经没有例外、是不是已经由内存池保证、还是看见官方点名 undesirable 是不是已经交差，再决定要不要同一次发布。313 replayprot vs replay bundled unbundling 在本页 item 3 完成。
