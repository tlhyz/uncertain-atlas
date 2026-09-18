# 例：看见 shared-master-xpub is not already this-page interchangeable / not already enough interchangeable / not already settled interchangeable

**层次**：应用 / BIP-45 shared-master-xpub not already this-page / not already enough / not already settled 正式三事（271 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-45](https://github.com/bitcoin/bips/blob/master/bip-0045.mediawiki)（Complete, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-45 shared-master-xpub not already this-page / not already enough / not already settled 正式三事（271 余量）/ not 1130 cos45-notmaster interchangeable / not 271 cosigner-vs-discovered bundled interchangeable」，不是分层确定性多签结构 bundled（271），也不是扩展公钥就已经能花（182），也不是 BIP32 compatible 就已经能互操作（1118）。不要另写怎样按用途公钥排下标，也不要另写 BIP-11 / BIP-67。

## 官方三件事

1. **看见共享主公钥 / 看见扩展公钥 这份栏 is not already 已经是本页 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1130 cos45-notmaster interchangeable / 1131 cos45-notsign interchangeable / 271 cosigner item 2 addr-not-sign interchangeable，也不是已经 BIP-45 shared-master-xpub not already this-page / not already enough / not already settled 正式三事 bundled（271 item 1 余量） interchangeable / 271 cosigner item 1 interchangeable。**  
   官方写：各方各自独立生成自己的主私钥。各参与方之间不共享主公钥，只共享硬化用途层扩展公钥。看见共享了主公钥，不是已经是本页 interchangeable——本页从 271 item 1 侧钉 not already this-page 单句。271 cosigner vs discovered bundled unbundling 在本页 item 1 启动。

2. **看见扩展公钥 / 看见共享主公钥 / 这份栏 is not already 已经共享了本页要的那一层 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1130 cos45-notmaster interchangeable / 271 cosigner item 3 branch-not-done interchangeable / 1132 cos45-notdone interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把只共享硬化用途层扩展公钥和已经共享了本页要的那一层分开。看见扩展公钥，不是已经共享了本页要的那一层 interchangeable。本页钉 not already enough 单句。

3. **看见各方各自独立生成自己的主私钥 / 看见共享主公钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1130 cos45-notmaster interchangeable / 1131 cos45-notsign interchangeable，也不是已经 BIP32 compatible 就已经能互操作 interchangeable / 1118 purp43-notinterop interchangeable。**  
   官方把各方各自独立生成自己的主私钥写成独立限制。看见各方各自独立生成自己的主私钥，不是已经交差 interchangeable。271 cosigner vs discovered bundled unbundling 在本页 item 1 启动。

用途号、间隙条数、例路径、怎样按用途公钥排联合签名人下标是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-45 shared-master-xpub not already this-page ≠ 已经是本页 interchangeable：** 官方把只共享硬化用途层扩展公钥写成和主公钥不是同一把。
- **看见扩展公钥 not already enough ≠ 已经共享了本页要的那一层 interchangeable：** 官方把看见扩展公钥和已经共享了本页要的那一层分开。
- **看见各方各自独立生成自己的主私钥 not already settled ≠ 已经交差 interchangeable：** 官方把各自独立生成主私钥写成独立限制；271 cosigner vs discovered bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 共享主公钥 / 扩展公钥 | 不是已经是本页 | 不是扩展公钥就已经能花（182） |
| 看见扩展公钥 | 不是已经共享了本页要的那一层 | 不是 BIP32 compatible 就已经能互操作（1118） |
| 看见各方各自独立生成自己的主私钥 | 不是已经交差 | 不是能独立长地址就已经能独立签（1131） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-45 shared-master-xpub not already this-page / not already enough / not already settled 正式三事（271 余量），必须分开是不是已经是本页、是不是已经共享了本页要的那一层、是不是已经交差。可以跳过「看见多签路径就已经能扫完」。不要另写怎样按用途公钥排下标，也不要另写 BIP-11 / BIP-67。271 cosigner vs discovered bundled unbundling 在本页 item 1 启动；续 [`worked-example-cos45-notsign-vs-bundled.md`](worked-example-cos45-notsign-vs-bundled.md)（不变量 1131 item 2）。

## 本页不抄

- 用途号、间隙条数、例路径、例压缩钥。
- 怎样按用途公钥排联合签名人下标、怎样从种子扫每一支。
- 分层确定性多签结构 bundled。那是不变量 271。
- 扩展公钥就已经能花。那是不变量 182。
