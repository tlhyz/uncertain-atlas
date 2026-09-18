# 反模式：把 BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量） 写成已经 已经有块 / 中间块已经在手里 / 重组已经处理完

**层次**：网络 / BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-hdr130-nothave-vs-bundled.md`](../tracks/network/worked-example-hdr130-nothave-vs-bundled.md)。

把 BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量） 写成已经 已经有块 / 中间块已经在手里 / 重组已经处理完，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头通告偏好 正式三事（247 余量），必须分开 not already switched、not already must、not already have-block 三件事，不要和 247 / 36 / 246 / 1235 / 1236 糊成一句。

也不是：

- [hdr130-notswitch-sold-as-bundled](hdr130-notswitch-sold-as-bundled.md) 是 notswitch 单句边界（1235），不是本页边界。
- [hdr130-notmust-sold-as-bundled](hdr130-notmust-sold-as-bundled.md) 是 notmust 单句边界（1236），不是本页边界。
- [addr155-notreach-sold-as-bundled](addr155-notreach-sold-as-bundled.md) 是 BIP-155 流言仍未连得上边界（246/1232），不是本页头通告偏好边界。
