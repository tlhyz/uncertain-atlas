# 例：看见 delegator-plain-key is not already xpub interchangeable / not already whole-wallet interchangeable / not already settled interchangeable

**层次**：应用 / BIP-89 delegator-plain-key not already xpub / not already whole-wallet / not already settled 正式三事（289 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-89 delegator-plain-key not already xpub / not already whole-wallet / not already settled 正式三事（289 余量）/ not 1140 del89-nottree interchangeable / not 289 delegation-vs-xpub bundled interchangeable」，不是链码委托 bundled（289），也不是聚合钥就已经是扩展公钥（283），也不是种子备份就已经能找回单钥 P2TR（1138）。不要另写怎样做委托微调或盲签。

## 官方三件事

1. **看见委托方那把非扩展钥对 这份栏 is not already 已经是扩展公钥 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1140 del89-nottree interchangeable / 1139 del89-notshare interchangeable / 289 delegation item 1 share-not-this interchangeable，也不是已经 BIP-89 delegator-plain-key not already xpub / not already whole-wallet / not already settled 正式三事 bundled（289 item 2 余量） interchangeable / 289 delegation item 2 interchangeable。**  
   官方写：委托方必须自己造一把普通钥对，把公钥交给对方。委托方不得留下、也不得被发给这把钥的链码。看见一把普通公钥，不是已经带了链码 interchangeable——本页从 289 item 2 侧钉 not already xpub 单句。289 delegation vs xpub bundled unbundling 在本页 item 2 续。

2. **看见受托方有扩展公钥 / 看见委托方那把非扩展钥对 / 这份栏 is not already 已经能推出整棵钱包 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1140 del89-nottree interchangeable / 289 delegation item 3 tweak-not-blind interchangeable / 1141 del89-notblind interchangeable，也不是已经聚合钥就已经是扩展公钥 interchangeable / 283 musig interchangeable。**  
   官方把受托方算出并留下绑在这把公钥上的链码、而且这份扩展公钥不得再透露给委托方写成两道门。看见受托方有扩展公钥，不是委托方已经看见整棵树 interchangeable。本页钉 not already whole-wallet 单句。

3. **看见从这份扩展钥往下长只能走未硬化派生 / 看见委托方那把非扩展钥对 / 这份栏 is not already 已经交差 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1140 del89-nottree interchangeable / 1139 del89-notshare interchangeable，也不是已经种子备份就已经能找回单钥 P2TR interchangeable / 1138 tap86-notseed interchangeable。**  
   官方把委托方拿到微调后只能为这一路径验和签、认不出别的路径上的钥写成独立限制。看见从这份扩展钥往下长只能走未硬化派生，不是已经交差 interchangeable。289 delegation vs xpub bundled unbundling 在本页 item 2 续。

微调算法、验输入/找零步骤、盲 nonce 配方、曲线常数、测试向量是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-89 delegator-plain-key not already xpub ≠ 已经是扩展公钥 interchangeable：** 官方把委托方不得持有链码写成一道门。
- **看见受托方有扩展公钥 not already whole-wallet ≠ 已经能推出整棵钱包 interchangeable：** 官方把受托方的扩展公钥不得回传写成第二道门。
- **看见从这份扩展钥往下长只能走未硬化派生 not already settled ≠ 已经交差 interchangeable：** 官方把只能为这一路径验和签写成独立限制；289 delegation vs xpub bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 委托方那把非扩展钥对 | 不是已经是扩展公钥 | 不是聚合钥就已经是扩展公钥（283） |
| 看见受托方有扩展公钥 | 不是已经能推出整棵钱包 | 不是种子备份就已经能找回单钥 P2TR（1138） |
| 看见从这份扩展钥往下长只能走未硬化派生 | 不是已经交差 | 不是这一输入的微调就已经是盲签（1141） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-89 delegator-plain-key not already xpub / not already whole-wallet / not already settled 正式三事（289 余量），必须分开是不是已经是扩展公钥、是不是已经能推出整棵钱包、是不是已经交差。可以跳过「看见共享了扩展公钥就已经对托管方藏住余额」。不要另写怎样做委托微调或盲签。289 delegation vs xpub bundled unbundling 在本页 item 2 续；续 [`worked-example-del89-notblind-vs-bundled.md`](worked-example-del89-notblind-vs-bundled.md)（不变量 1141 item 3）。

## 本页不抄

- 微调算法、验输入/找零步骤、盲 nonce 配方、曲线常数、测试向量。
- 怎样算派生微调、怎样做盲挑战、怎样解盲、怎样并行开盲签会话。
- 链码委托 bundled。那是不变量 289。
- 聚合钥就已经是扩展公钥。那是不变量 283。
