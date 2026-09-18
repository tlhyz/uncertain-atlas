# 反模式：把 Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量） 写成已经 已经是握手对齐 / 已经是快照重放 / 已经交差

**层次**：实现 / Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应**：[`../tracks/implementation/worked-example-ffields-notinfo-vs-bundled.md`](../tracks/implementation/worked-example-ffields-notinfo-vs-bundled.md)。

把 Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量） 写成已经 已经是握手对齐 / 已经是快照重放 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 回应用状态 正式三事（407 余量），必须分开 not already handshake-aligned、not already snapshot-replay、not already settled 三件事，不要和 407 / 370 / 367 / 1109 / 1110 糊成一句。

也不是：

- [ffields-notprep-sold-as-bundled](ffields-notprep-sold-as-bundled.md) 是必须确定仍未可以像 Prepare 那样单句边界（1110 item 2），不是本页 Info 回应用状态仍未是握手对齐边界。
- Info 用来握手对齐就已经是快照重放是不变量 370，不是本页写了应用状态仍未是快照重放边界。
