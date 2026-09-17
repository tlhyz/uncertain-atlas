# 反模式：把 进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量） 写成已经 已经开出块 / 已经过了创世时间 / 已经交差

**层次**：实现 / 进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应**：[`../tracks/implementation/worked-example-genesis-nottime-vs-bundled.md`](../tracks/implementation/worked-example-genesis-nottime-vs-bundled.md)。

把 进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量） 写成已经 已经开出块 / 已经过了创世时间 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看进程起来 正式三事（303 余量），必须分开 not already past-genesis-time、not already handshake-ready、not already settled 三件事，不要和 303 / 147 / 300 / 986 / 988 糊成一句。

也不是：

- [genesis-notapp-sold-as-bundled](genesis-notapp-sold-as-bundled.md) 是创世段仍未验过单句边界（986 item 1），不是本页进程起来仍未开出块边界。
- 本头 AppHash 已经交差是不变量 147，不是本页握手过了仍未过创世时间边界。
