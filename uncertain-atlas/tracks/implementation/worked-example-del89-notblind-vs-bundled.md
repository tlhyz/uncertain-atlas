# 例：看见 this-input-tweak is not already whole-tree interchangeable / not already blind-sign interchangeable / not already settled interchangeable

**层次**：应用 / BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量）/ not 1141 del89-notblind interchangeable / not 289 delegation-vs-xpub bundled interchangeable」，不是链码委托 bundled（289），也不是登记过就已经批准这笔花（280），也不是部分签名包就已经是跨厂开户（287）。不要另写怎样做委托微调或盲签。

## 官方三件事

1. **看见这一输入的微调 / 看见一次签名会话 这份栏 is not already 已经能扫整棵钱包 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1141 del89-notblind interchangeable / 1139 del89-notshare interchangeable / 289 delegation item 1 share-not-this interchangeable，也不是已经 BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事 bundled（289 item 3 余量） interchangeable / 289 delegation item 3 interchangeable。**  
   官方写：受托方在签名时按输入给出标量微调。非盲模式里，委托方只看见自己要签的那些子钥和交易，看不见更宽的地址空间。看见这一输入的微调，不是已经能扫整棵钱包 interchangeable——本页从 289 item 3 侧钉 not already whole-tree 单句。289 delegation vs xpub bundled unbundling 在本页 item 3 完成。

2. **看见能签 / 看见这一输入的微调 / 这份栏 is not already 已经是盲签 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1141 del89-notblind interchangeable / 289 delegation item 2 key-not-tree interchangeable / 1140 del89-nottree interchangeable，也不是已经登记过就已经批准这笔花 interchangeable / 280 policy interchangeable。**  
   官方把盲模式里委托方连消息和子钥都看不见、只看见一个被盲过的挑战写成另一档。看见能签，不是已经是盲签 interchangeable。本页钉 not already blind-sign 单句。

3. **看见签过了 / 看见这一输入的微调 / 这份栏 is not already 已经交差 interchangeable，也不是已经链码委托 bundled（289） interchangeable / 1141 del89-notblind interchangeable / 1139 del89-notshare interchangeable，也不是已经部分签名包就已经是跨厂开户 interchangeable / 287 setup interchangeable。**  
   官方把找零输出的微调只有委托方想算出自己花了多少时才需要、看见签过了不是已经核过找零写成独立限制。看见签过了，不是已经核过找零 interchangeable。289 delegation vs xpub bundled unbundling 在本页 item 3 完成。

微调算法、验输入/找零步骤、盲 nonce 配方、曲线常数、测试向量是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-89 this-input-tweak not already whole-tree ≠ 已经能扫整棵钱包 interchangeable：** 官方把非盲只看见本笔写成看不见更宽的地址空间。
- **看见能签 not already blind-sign ≠ 已经是盲签 interchangeable：** 官方把非盲只看见本笔、盲签看不见消息写成两档。
- **看见签过了 not already settled ≠ 已经交差 interchangeable：** 官方把签过了不是已经核过找零写成独立限制；289 delegation vs xpub bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 这一输入的微调 / 一次签名会话 | 不是已经能扫整棵钱包 | 不是登记过就已经批准这笔花（280） |
| 看见能签 | 不是已经是盲签 | 不是部分签名包就已经是跨厂开户（287） |
| 看见签过了 | 不是已经交差 | 不是共享了扩展公钥就已经是链码委托（1139） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-89 this-input-tweak not already whole-tree / not already blind-sign / not already settled 正式三事（289 余量），必须分开是不是已经能扫整棵钱包、是不是已经是盲签、是不是已经交差。可以跳过「看见共享了扩展公钥就已经对托管方藏住余额」。不要另写怎样做委托微调或盲签。289 delegation vs xpub bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 微调算法、验输入/找零步骤、盲 nonce 配方、曲线常数、测试向量。
- 怎样算派生微调、怎样做盲挑战、怎样解盲、怎样并行开盲签会话。
- 链码委托 bundled。那是不变量 289。
- 登记过就已经批准这笔花。那是不变量 280。
