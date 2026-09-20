# 反模式：把 BIP-125 opt-in-signal not already replaced / not already 144 / not already 166-bundled 正式三事（166 余量） 写成已经 已经换掉 / 已经是不变量 144 / 已经 166 bundled

**层次**：实现 / BIP-125 opt-in-signal not already replaced / not already 144 / not already 166-bundled 正式三事（166 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)（Opt-in Full Replace-by-Fee Signaling）。  
**对应**：[`../tracks/mempool/worked-example-rbfs-notrep-vs-bundled.md`](../tracks/mempool/worked-example-rbfs-notrep-vs-bundled.md)。

把 BIP-125 opt-in-signal not already replaced / not already 144 / not already 166-bundled 正式三事（166 余量） 写成已经 已经换掉 / 已经是不变量 144 / 已经 166 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-125 RBF 正式三事（166 余量），必须分开 not already replaced、not already relative-lock、not already explicit-join 三件事，不要和 166 / 144 / 165 / 1525 / 1526 糊成一句。

也不是：

- [rbfs-notlock-sold-as-bundled](rbfs-notlock-sold-as-bundled.md) 是 notlock 单句边界（1525），不是本页边界。
- [rbfs-notjoin-sold-as-bundled](rbfs-notjoin-sold-as-bundled.md) 是 notjoin 单句边界（1526），不是本页边界。
- [polc-notill-sold-as-bundled](polc-notill-sold-as-bundled.md) 是 policy 边界（144/1521），不是本页 RBF 信号边界。
