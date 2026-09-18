# 模式：点名 sort67-notaddr 杠

**层次**：应用 / BIP-67 same-keys-threshold not already same-redeem / not already same-p2sh / not already settled 正式三事（270 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-67](https://github.com/bitcoin/bips/blob/master/bip-0067.mediawiki)（Complete, Applications）。  
**对应**：[`../tracks/implementation/worked-example-sort67-notaddr-vs-bundled.md`](../tracks/implementation/worked-example-sort67-notaddr-vs-bundled.md)。

- **同一套钥 不是已经是同一条赎回脚本：** 看见钥集合对齐了，不是已经对齐了赎回脚本 interchangeable / 1133 sort67-notaddr interchangeable。
- **看见门限一样 不是已经是同一条 P2SH 地址：** 看见门限一样，不是已经是同一条地址 interchangeable。
- **看见遵守顺序和编码 不是已经交差：** 看见遵守顺序和编码，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一套钥 正式三事（270 余量），先数清问的是是不是已经是同一条赎回脚本、是不是已经是同一条 P2SH 地址、还是看见遵守顺序和编码是不是已经交差，再决定要不要同一次发布。270 sorted vs one-address bundled unbundling 在本页 item 1 启动。
