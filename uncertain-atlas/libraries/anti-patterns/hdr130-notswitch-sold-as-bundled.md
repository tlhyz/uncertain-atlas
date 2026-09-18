# 反模式：把 BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量） 写成已经 已经改用头通告 / 已经有那块 / 头先同步已经做完

**层次**：网络 / BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-hdr130-notswitch-vs-bundled.md`](../tracks/network/worked-example-hdr130-notswitch-vs-bundled.md)。

把 BIP-130 sendheaders not already switched / not already have-block / not already headers-first 正式三事（247 余量） 写成已经 已经改用头通告 / 已经有那块 / 头先同步已经做完，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头通告偏好 正式三事（247 余量），必须分开 not already switched、not already must、not already have-block 三件事，不要和 247 / 36 / 246 / 1236 / 1237 糊成一句。

也不是：

- [hdr130-notmust-sold-as-bundled](hdr130-notmust-sold-as-bundled.md) 是 notmust 单句边界（1236），不是本页边界。
- [hdr130-nothave-sold-as-bundled](hdr130-nothave-sold-as-bundled.md) 是 nothave 单句边界（1237），不是本页边界。
- [addr155-notreach-sold-as-bundled](addr155-notreach-sold-as-bundled.md) 是 BIP-155 流言仍未连得上边界（246/1232），不是本页头通告偏好边界。
