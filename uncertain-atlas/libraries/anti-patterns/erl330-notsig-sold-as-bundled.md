# 反模式：把 BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量） 写成已经 已经在对账 / 对账已经打开 / 已经对齐过一轮

**层次**：网络 / BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki)（Draft, Peer Services）。  
**对应**：[`../tracks/network/worked-example-erl330-notsig-vs-bundled.md`](../tracks/network/worked-example-erl330-notsig-vs-bundled.md)。

把 BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量） 写成已经 已经在对账 / 对账已经打开 / 已经对齐过一轮，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通告集合对账 正式三事（249 余量），必须分开 not already have、not already reconciling、not already flood-retired 三件事，不要和 249 / 248 / 259 / 1250 / 1252 糊成一句。

也不是：

- [erl330-nothave-sold-as-bundled](erl330-nothave-sold-as-bundled.md) 是 nothave 单句边界（1250），不是本页边界。
- [erl330-notflood-sold-as-bundled](erl330-notflood-sold-as-bundled.md) 是 notflood 单句边界（1252），不是本页边界。
- [wtx339-nothave-sold-as-bundled](wtx339-nothave-sold-as-bundled.md) 是 BIP-339 按 wtxid 通告仍未有交易边界（248/1247），不是本页通告集合对账边界。
