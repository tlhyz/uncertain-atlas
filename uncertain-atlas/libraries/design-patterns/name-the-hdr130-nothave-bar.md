# 模式：点名 hdr130-nothave 杠

**层次**：网络 / BIP-130 tip-headers not already have-block / not already have-middle / not already reorg-done 正式三事（247 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)（Deployed, Peer Services）。  
**对应**：[`../tracks/network/worked-example-hdr130-nothave-vs-bundled.md`](../tracks/network/worked-example-hdr130-nothave-vs-bundled.md)。

- **用头通告新尖 不是已经有块：看见用头通告新尖，不是已经有块 interchangeable / 1237 hdr130-nothave interchangeable。**
- **重组时先发了头 不是中间块已经在手里：看见重组时先发了头，不是中间块已经在手里 interchangeable / 1237 hdr130-nothave interchangeable。**
- **先发头 不是重组已经处理完：看见先发头，不是重组已经处理完 interchangeable / 1237 hdr130-nothave interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头通告偏好 正式三事（247 余量），必须分开 not already switched、not already must、not already have-block 三件事。
