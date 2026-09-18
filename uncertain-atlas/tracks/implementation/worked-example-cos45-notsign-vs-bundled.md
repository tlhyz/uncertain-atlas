# 例：看见 independent-address is not already independent-sign interchangeable / not already same-person-key interchangeable / not already settled interchangeable

**层次**：应用 / BIP-45 independent-address not already independent-sign / not already same-person-key / not already settled 正式三事（271 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-45](https://github.com/bitcoin/bips/blob/master/bip-0045.mediawiki)（Complete, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-45 independent-address not already independent-sign / not already same-person-key / not already settled 正式三事（271 余量）/ not 1131 cos45-notsign interchangeable / not 271 cosigner-vs-discovered bundled interchangeable」，不是分层确定性多签结构 bundled（271），也不是同一套钥就已经是同一条 P2SH 地址（270），也不是本页多签就已经不排序（1129）。不要另写怎样按用途公钥排下标，也不要另写 BIP-11 / BIP-67。

## 官方三件事

1. **看见能独立长地址 / 看见不必通信就能长地址 这份栏 is not already 已经能独立花 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1131 cos45-notsign interchangeable / 1130 cos45-notmaster interchangeable / 271 cosigner item 1 master-not-this interchangeable，也不是已经 BIP-45 independent-address not already independent-sign / not already same-person-key / not already settled 正式三事 bundled（271 item 2 余量） interchangeable / 271 cosigner item 2 interchangeable。**  
   官方写：长地址不应当要求各方通信，所以每一方都必须能长出所有公钥。造交易和签名要求各方通信。看见能独立长地址，不是已经能独立花 interchangeable——本页从 271 item 2 侧钉 not already independent-sign 单句。271 cosigner vs discovered bundled unbundling 在本页 item 2 续。

2. **看见同一条路径 / 看见能独立长地址 / 这份栏 is not already 已经是同一个人的钥 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1131 cos45-notsign interchangeable / 271 cosigner item 3 branch-not-done interchangeable / 1132 cos45-notdone interchangeable，也不是已经同一套钥就已经是同一条 P2SH 地址 interchangeable / 270 sorted interchangeable。**  
   官方把同一条路径和已经是同一个人的钥分开。看见同一条路径，不是已经是同一个人的钥 interchangeable。本页钉 not already same-person-key 单句。

3. **看见造交易和签名要求各方通信 / 看见能独立长地址 / 这份栏 is not already 已经交差 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1131 cos45-notsign interchangeable / 1130 cos45-notmaster interchangeable，也不是已经本页多签就已经不排序 interchangeable / 1129 msig48-notsort interchangeable。**  
   官方把长地址写成不必通信，把造交易和签名写成必须通信。看见造交易和签名要求各方通信，不是已经交差 interchangeable。271 cosigner vs discovered bundled unbundling 在本页 item 2 续。

用途号、间隙条数、例路径、怎样按用途公钥排联合签名人下标是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-45 independent-address not already independent-sign ≠ 已经能独立花 interchangeable：** 官方把长地址写成不必通信，把造交易和签名写成必须通信。
- **看见同一条路径 not already same-person-key ≠ 已经是同一个人的钥 interchangeable：** 官方把同一条路径和已经是同一个人的钥分开。
- **看见造交易和签名要求各方通信 not already settled ≠ 已经交差 interchangeable：** 官方把必须通信和已经交差分开；271 cosigner vs discovered bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能独立长地址 / 不必通信就能长地址 | 不是已经能独立花 | 不是同一套钥就已经是同一条 P2SH 地址（270） |
| 看见同一条路径 | 不是已经是同一个人的钥 | 不是本页多签就已经不排序（1129） |
| 看见造交易和签名要求各方通信 | 不是已经交差 | 不是前面分支没有交易就已经发现完（1132） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-45 independent-address not already independent-sign / not already same-person-key / not already settled 正式三事（271 余量），必须分开是不是已经能独立花、是不是已经是同一个人的钥、是不是已经交差。可以跳过「看见多签路径就已经能扫完」。不要另写怎样按用途公钥排下标，也不要另写 BIP-11 / BIP-67。271 cosigner vs discovered bundled unbundling 在本页 item 2 续；续 [`worked-example-cos45-notdone-vs-bundled.md`](worked-example-cos45-notdone-vs-bundled.md)（不变量 1132 item 3）。

## 本页不抄

- 用途号、间隙条数、例路径、例压缩钥。
- 怎样按用途公钥排联合签名人下标、怎样从种子扫每一支。
- 分层确定性多签结构 bundled。那是不变量 271。
- 同一套钥就已经是同一条 P2SH 地址。那是不变量 270。
