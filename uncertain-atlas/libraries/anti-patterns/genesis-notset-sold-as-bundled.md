# 反模式：把 空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量） 写成已经 已经没有集合 / 已经没有状态根 / 已经交差

**层次**：实现 / 空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应**：[`../tracks/implementation/worked-example-genesis-notset-vs-bundled.md`](../tracks/implementation/worked-example-genesis-notset-vs-bundled.md)。

把 空名单 / 空根 not already no-set / not already no-root / not already settled 正式三事（303 余量） 写成已经 已经没有集合 / 已经没有状态根 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空名单 / 空根 正式三事（303 余量），必须分开 not already no-set、not already no-root、not already settled 三件事，不要和 303 / 318 / 300 / 986 / 987 糊成一句。

也不是：

- [genesis-nottime-sold-as-bundled](genesis-nottime-sold-as-bundled.md) 是进程起来仍未开出块单句边界（987 item 2），不是本页空名单仍未没有集合边界。
- InitChain 空名单就已经没有集合是不变量 318，不是本页根空仍未没有状态根边界。
