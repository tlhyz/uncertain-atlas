# 模式：点名 genesis-notapp 杠

**层次**：实现 / 创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应**：[`../tracks/implementation/worked-example-genesis-notapp-vs-bundled.md`](../tracks/implementation/worked-example-genesis-notapp-vs-bundled.md)。

- **创世 app_state 不是已经验过：** 看见创世文件齐了，不是应用段已经验过 interchangeable / 986 genesis-notapp interchangeable。
- **看见引擎收下了 不是已经懂余额：** 看见引擎收下了，不是已经懂余额 interchangeable。
- **看见有 app_state 不是已经交差：** 看见有 app_state，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看创世 app_state 正式三事（303 余量），先数清问的是是不是已经验过、是不是已经懂余额、还是看见有 app_state 是不是已经交差，再决定要不要同一次发布。303 genesis vs app bundled unbundling 在本页 item 1 启动。
