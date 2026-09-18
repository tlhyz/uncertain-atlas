# 例：看见合成扩展公钥不是已经能做硬化派生；看见少存了几份扩展公钥不是已经是脚本多签那种各自派生再拼；看见没有聚合私钥不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-328](https://github.com/bitcoin/bips/blob/master/bip-0328.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-328 synthetic-xpub not already hardened / not already many-xpubs-then-aggregate / not already settled 正式三事（283 余量）/ not 1170 musig328-nothard interchangeable / not 283 musig-xpub-vs-aggregate bundled interchangeable」，不是聚合钥派生 bundled（283），也不是 multi 就已经是 sortedmulti（1142），也不是看见描述符就已经是地址（184）。不要另写怎样算派生微调。

## 官方三件事

1. **看见合成扩展公钥 / 看见没有聚合私钥 这份栏 is not already 已经能做硬化派生 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1170 musig328-nothard interchangeable / 1169 musig328-notxpub interchangeable / 283 musig item 1 agg-not-xpub interchangeable，也不是已经 BIP-328 synthetic-xpub not already hardened / not already many-xpubs-then-aggregate / not already settled 正式三事 bundled（283 item 2 余量） interchangeable / 283 musig item 2 interchangeable。**  
   官方写：没有聚合私钥，所以只能从聚合公钥做未硬化派生。看见合成扩展公钥，不是已经能硬化。

2. **看见少存了几份扩展公钥 / 看见合成扩展公钥 / 这份栏 is not already 已经是脚本多签那种各自派生再拼 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1170 musig328-nothard interchangeable / 283 musig item 3 child-not-tweak interchangeable / 1171 musig328-nottweak interchangeable，也不是已经 multi 就已经是 sortedmulti interchangeable / 1142 desc383-notsort interchangeable。**  
   官方另写：更省事的做法是从一份扩展公钥派生，而不是每次先从许多扩展公钥派生再聚合。看见少存了几份扩展公钥，不是已经是脚本多签那种各自派生再拼。

3. **看见没有聚合私钥 / 看见合成扩展公钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经聚合钥派生 bundled（283） interchangeable / 1170 musig328-nothard interchangeable / 1169 musig328-notxpub interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把「没有聚合私钥」写成只能未硬化。看见没有聚合私钥，不是已经交差。

固定链码取值、测试向量、例钥、派生公式是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **合成扩展公钥 不是已经能硬化：** 官方把没有聚合私钥写成只能未硬化。
- **少存了几份扩展公钥 不是已经是各自派生再拼：** 官方把从一份扩展公钥派生写成更省事。
- **没有聚合私钥 不是已经交差：** 官方把只能未硬化写成独立一句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 硬化 | 不是已经能硬化 | 不是已经是 383 那种 multi（1142） |
| 各自派生再拼 | 不是已经是脚本多签那种 | 不是已经是扩展公钥（1169） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-328 synthetic-xpub not already hardened / not already many-xpubs-then-aggregate / not already settled 正式三事（283 余量），必须分开是不是已经能硬化、是不是已经是各自派生再拼、是不是已经交差。可以跳过「看见聚合钥就已经能当普通扩展公钥用」。不要另写怎样算派生微调。283 musig xpub vs aggregate bundled unbundling 在本页 item 2 续；续 [`worked-example-musig328-nottweak-vs-bundled.md`](worked-example-musig328-nottweak-vs-bundled.md)（不变量 1171 item 3）。

## 本页不抄

- 固定链码取值、测试向量、例钥、派生公式。
- 怎样造合成扩展公钥、怎样算每一步微调、怎样放进签名会话。
