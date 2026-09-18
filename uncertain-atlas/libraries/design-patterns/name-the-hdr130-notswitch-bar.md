# 模式：点名 hdr130-notswitch 杠

**层次**：网络 / BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-hdr130-notswitch-vs-bundled.md`](../tracks/network/worked-example-hdr130-notswitch-vs-bundled.md)。

- **发了 sendheaders 不是已经改用头通告：看见发了 sendheaders，不是已经改用头通告 interchangeable / 1235 hdr130-notswitch interchangeable。**
- **发了偏好 不是已经有那块：看见发了偏好，不是已经有那块 interchangeable / 1235 hdr130-notswitch interchangeable。**
- **发了 sendheaders 不是头先同步已经做完：看见发了 sendheaders，不是头先同步已经做完 interchangeable / 1235 hdr130-notswitch interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头通告偏好 正式三事（247 余量），必须分开 not already switched、not already must、not already have-block 三件事。
