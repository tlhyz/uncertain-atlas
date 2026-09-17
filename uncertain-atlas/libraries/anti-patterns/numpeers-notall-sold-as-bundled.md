# 反模式：把 NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量） 写成已经 已经数完 / 无条件名单已经算进去 / 正在拨就已经连上

**层次**：网络 / NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / NumPeers vs all。  
**对应**：[`../tracks/network/worked-example-numpeers-notall-vs-bundled.md`](../tracks/network/worked-example-numpeers-notall-vs-bundled.md)。

把 NumPeers not already all-neighbors / not already unconditional / not already dialing-ok 正式三事（308 余量） 写成已经 已经数完 / 无条件名单已经算进去 / 正在拨就已经连上，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 NumPeers 正式三事（308 余量），必须分开 not already all-neighbors、not already unconditional、not already dialing-ok 三件事，不要和 308 / 306 / 305 / 1008 / 1009 糊成一句。

也不是：

- [peerhand-notgone-sold-as-bundled](peerhand-notgone-sold-as-bundled.md) 是踢持久邻居仍未断干净边界（306/1006），不是本页 NumPeers 仍未数完边界。
- 句柄已经是那个人是不变量 306/1004，不是本页出站加进站仍未算无条件名单边界。
