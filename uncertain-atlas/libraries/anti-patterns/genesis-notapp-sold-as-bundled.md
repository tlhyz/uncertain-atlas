# 反模式：把 创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量） 写成已经 已经验过 / 已经懂余额 / 已经交差

**层次**：实现 / 创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应**：[`../tracks/implementation/worked-example-genesis-notapp-vs-bundled.md`](../tracks/implementation/worked-example-genesis-notapp-vs-bundled.md)。

把 创世 app_state not already app-verified / not already understood / not already settled 正式三事（303 余量） 写成已经 已经验过 / 已经懂余额 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看创世 app_state 正式三事（303 余量），必须分开 not already app-verified、not already understood、not already settled 三件事，不要和 303 / 38 / 300 / 987 / 988 糊成一句。

也不是：

- [stategossip-notspec-sold-as-bundled](stategossip-notspec-sold-as-bundled.md) 是落盘接口仍未进规范边界（300/985），不是本页创世段仍未验过边界。
- 快照已经从创世重放是不变量 38，不是本页引擎收下了仍不懂余额边界。
