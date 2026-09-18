# 例：看见 shared-xpub is not already chaincode-delegation interchangeable / not already hide-balance interchangeable / not already settled interchangeable

**层次**：应用 / BIP-89 shared-xpub not already chaincode-delegation / not already hide-balance / not already settled 正式三事（289 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-89 shared-xpub not already chaincode-delegation / not already hide-balance / not already settled 正式三事（289 余量）/ not 1139 del89-notshare interchangeable / not 289 delegation-vs-xpub bundled interchangeable」，不是链码委托 bundled（289），也不是扩展公钥就已经能花（182），也不是聚合钥就已经是扩展公钥（283）。不要另写怎样做委托微调或盲签。

## 官方三件事

1. **看见共享了扩展公钥 / 看见共享了描述符 这份栏 is not already 已经是本页 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1139 del89-notshare interchangeable / 1140 del89-nottree interchangeable / 289 delegation item 2 key-not-tree interchangeable，也不是已经 BIP-89 shared-xpub not already chaincode-delegation / not already hide-balance / not already settled 正式三事 bundled（289 item 1 余量） interchangeable / 289 delegation item 1 interchangeable。**  
   官方写：多签里把扩展公钥或描述符分给各方，所有人都能扫链、推断对方在干什么。本页让没有特权的一方只拿一把非扩展钥对。看见共享了扩展公钥，不是已经是本页 interchangeable——本页从 289 item 1 侧钉 not already chaincode-delegation 单句。289 delegation vs xpub bundled unbundling 在本页 item 1 启动。

2. **看见共享了扩展公钥 / 看见能共签 / 这份栏 is not already 已经对共同签名人藏住余额 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1139 del89-notshare interchangeable / 289 delegation item 3 tweak-not-blind interchangeable / 1141 del89-notblind interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把分扩展公钥就能扫链和只委托链码、不交签名权写成两件相反的事。看见共享了扩展公钥，不是已经藏住余额 interchangeable。本页钉 not already hide-balance 单句。

3. **看见能共签 / 看见共享了扩展公钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1139 del89-notshare interchangeable / 1140 del89-nottree interchangeable，也不是已经聚合钥就已经是扩展公钥 interchangeable / 283 musig interchangeable。**  
   官方把交出链码的人仍能共签、只是看不见整棵派生写成独立限制。看见能共签，不是已经交出了签名权 interchangeable。289 delegation vs xpub bundled unbundling 在本页 item 1 启动。

微调算法、验输入/找零步骤、盲 nonce 配方、曲线常数、测试向量是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-89 shared-xpub not already chaincode-delegation ≠ 已经是本页 interchangeable：** 官方把分扩展公钥就能扫链和只委托链码写成两件相反的事。
- **看见共享了扩展公钥 not already hide-balance ≠ 已经藏住余额 interchangeable：** 官方把所有人都能扫链写成共享扩展公钥的后果。
- **看见能共签 not already settled ≠ 已经交差 interchangeable：** 官方把能共签不是已经交出签名权写成独立限制；289 delegation vs xpub bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 共享了扩展公钥 / 共享了描述符 | 不是已经是本页 | 不是扩展公钥就已经能花（182） |
| 看见共享了扩展公钥 | 不是已经藏住余额 | 不是聚合钥就已经是扩展公钥（283） |
| 看见能共签 | 不是已经交差 | 不是委托方那把非扩展钥就已经能推出整棵钱包（1140） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-89 shared-xpub not already chaincode-delegation / not already hide-balance / not already settled 正式三事（289 余量），必须分开是不是已经是本页、是不是已经藏住余额、是不是已经交差。可以跳过「看见共享了扩展公钥就已经对托管方藏住余额」。不要另写怎样做委托微调或盲签。289 delegation vs xpub bundled unbundling 在本页 item 1 启动；续 [`worked-example-del89-nottree-vs-bundled.md`](worked-example-del89-nottree-vs-bundled.md)（不变量 1140 item 2）。

## 本页不抄

- 微调算法、验输入/找零步骤、盲 nonce 配方、曲线常数、测试向量。
- 怎样算派生微调、怎样做盲挑战、怎样解盲、怎样并行开盲签会话。
- 链码委托 bundled。那是不变量 289。
- 扩展公钥就已经能花。那是不变量 182。
