# 模式：点名 genesis-notset 杠

**层次**：实现 / 空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应**：[`../tracks/implementation/worked-example-genesis-notset-vs-bundled.md`](../tracks/implementation/worked-example-genesis-notset-vs-bundled.md)。

- **空名单 不是已经没有集合：** 看见名单空，不是已经没有验证者 interchangeable / 988 genesis-notset interchangeable。
- **看见根空 不是已经没有状态根：** 看见根空，不是已经没有状态根 interchangeable。
- **看见 InitChain 被叫了 不是已经交差：** 看见 InitChain 被叫了，不是已经过了四门 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空名单 / 空根 正式三事（303 余量），先数清问的是是不是已经没有集合、是不是已经没有状态根、还是看见 InitChain 被叫了是不是已经交差，再决定要不要同一次发布。303 genesis vs app bundled unbundling 在本页 item 3 完成。
