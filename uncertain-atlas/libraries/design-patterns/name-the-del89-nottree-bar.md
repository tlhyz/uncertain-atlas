# 模式：点名 del89-nottree 杠

**层次**：应用 / BIP-89 delegator-plain-key not already xpub / not already whole-wallet / not already settled 正式三事（289 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)（Deployed, Applications, Specification）。  
**对应**：[`../tracks/implementation/worked-example-del89-nottree-vs-bundled.md`](../tracks/implementation/worked-example-del89-nottree-vs-bundled.md)。

- **委托方那把非扩展钥对 不是已经是扩展公钥：** 看见一把普通公钥，不是已经带了链码 interchangeable / 1140 del89-nottree interchangeable。
- **看见受托方有扩展公钥 不是已经能推出整棵钱包：** 看见受托方有扩展公钥，不是委托方已经看见整棵树 interchangeable。
- **看见从这份扩展钥往下长只能走未硬化派生 不是已经交差：** 看见从这份扩展钥往下长只能走未硬化派生，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看委托方那把非扩展钥对 正式三事（289 余量），先数清问的是是不是已经是扩展公钥、是不是已经能推出整棵钱包、还是看见从这份扩展钥往下长只能走未硬化派生是不是已经交差，再决定要不要同一次发布。289 delegation vs xpub bundled unbundling 在本页 item 2 续。
