# 反模式：把 BIP-159 served-recent not already leaked / not already ibd-done / not already light-checked 正式三事（250 余量） 写成已经 已经暴露了剪到哪 / 初始同步已经能靠它从创世拉完 / 轻客户端已经核过服务位

**层次**：网络 / BIP-159 served-recent not already leaked / not already ibd-done / not already light-checked 正式三事（250 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-159](https://github.com/bitcoin/bips/blob/master/bip-0159.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-lim159-notcut-vs-bundled.md`](../tracks/network/worked-example-lim159-notcut-vs-bundled.md)。

把 BIP-159 served-recent not already leaked / not already ibd-done / not already light-checked 正式三事（250 余量） 写成已经 已经暴露了剪到哪 / 初始同步已经能靠它从创世拉完 / 轻客户端已经核过服务位，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看有限历史服务 正式三事（250 余量），必须分开 not already archive、not already pruned、not already leaked 三件事，不要和 250 / 243 / 25 / 1253 / 1254 糊成一句。

也不是：

- [lim159-notarch-sold-as-bundled](lim159-notarch-sold-as-bundled.md) 是 notarch 单句边界（1253），不是本页边界。
- [lim159-notprune-sold-as-bundled](lim159-notprune-sold-as-bundled.md) 是 notprune 单句边界（1254），不是本页边界。
- [erl330-nothave-sold-as-bundled](erl330-nothave-sold-as-bundled.md) 是 BIP-330 对账仍未有交易边界（249/1250），不是本页有限历史服务边界。
