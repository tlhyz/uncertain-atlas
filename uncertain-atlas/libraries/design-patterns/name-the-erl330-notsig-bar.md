# 模式：点名 erl330-notsig 杠

**层次**：网络 / BIP-330 sendtxrcncl not already reconciling / not already opened / not already aligned 正式三事（249 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-330](https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki)（Draft, Peer Services）。  
**对应**：[`../tracks/network/worked-example-erl330-notsig-vs-bundled.md`](../tracks/network/worked-example-erl330-notsig-vs-bundled.md)。

- **发了 sendtxrcncl 不是已经在对账：看见发了 sendtxrcncl，不是已经在对账 interchangeable / 1251 erl330-notsig interchangeable。**
- **发了 wtxidrelay 不是对账已经打开：看见发了 wtxidrelay，不是对账已经打开 interchangeable / 1251 erl330-notsig interchangeable。**
- **协议两边都写了支持 不是已经对齐过一轮：看见协议两边都写了支持，不是已经对齐过一轮 interchangeable / 1251 erl330-notsig interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通告集合对账 正式三事（249 余量），必须分开 not already have、not already reconciling、not already flood-retired 三件事。
