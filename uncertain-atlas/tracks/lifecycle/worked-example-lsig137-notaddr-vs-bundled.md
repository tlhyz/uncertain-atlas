# 例：看见头字节标了地址种类不是已经有那条地址；看见能分开种类不是已经能花；看见格式能区分不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-137](https://github.com/bitcoin/bips/blob/master/bip-0137.mediawiki)（Deployed, Applications, Specification）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L1.2](../../courses/level-01-crypto/L01-M02-signatures.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事（294 余量）/ not 1200 lsig137-notaddr interchangeable / not 294 legacy-sign-vs-322 bundled interchangeable」，不是旧式签消息 bundled（294），也不是地址串就已经有输出（174），也不是部分签名包就已经能广播（179）。不要另写怎样从头字节还原公钥。

## 官方三件事

1. **看见头字节标了地址种类 / 看见能分开种类 这份签 is not already 已经有那条地址 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1200 lsig137-notaddr interchangeable / 1199 lsig137-not322 interchangeable / 294 lsig item 1 sign-not-322 interchangeable，也不是已经 BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事 bundled（294 item 2 余量） interchangeable / 294 lsig item 2 interchangeable。**  
   官方写：当时已经有好几种比特币地址；若不另定标准，就分不清面前这份签对应哪一种。本页要定一套清楚格式，让客户端能分开普通付给公钥哈希、付给脚本哈希、以及原生隔离见证那种地址。看见头字节说了种类，不是链上已经有那条地址。

2. **看见能分开种类 / 看见头字节标了地址种类 / 这份签 is not already 已经能花 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1200 lsig137-notaddr interchangeable / 294 lsig item 3 habit-not-interop interchangeable / 1201 lsig137-nothabit interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见能分开种类，不是已经能花。看见格式能区分，不是已经知道未花输出在哪。

3. **看见格式能区分 / 看见头字节标了地址种类 / 这份签 is not already 已经交差 interchangeable，也不是已经旧式签消息 bundled（294） interchangeable / 1200 lsig137-notaddr interchangeable / 1199 lsig137-not322 interchangeable，也不是已经部分签名包就已经能广播 interchangeable / 179 psbt interchangeable。**  
   官方把「能区分地址种类」和「链上已经有那条地址」写成两件事。看见格式能区分，不是已经交差。

头字节取值、椭圆曲线背景、示例代码、怎样还原公钥是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **头字节标了地址种类 不是已经有那条地址：** 官方把分清种类写成不是链上已经有地址。
- **能分开种类 不是已经能花：** 官方把能分开种类写成不是已经能花。
- **格式能区分 不是已经交差：** 官方把格式能区分写成不是已经知道未花输出在哪。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 地址 | 不是已经有那条地址 | 不是已经有输出（174） |
| 能花 | 不是已经能花 | 不是已经能广播（179） |
| 交差 | 不是已经交差 | 不是已经是 322（1199） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-137 header-byte not already have-address / not already spendable-output / not already settled 正式三事（294 余量），必须分开是不是已经有那条地址、是不是已经能花、是不是已经交差。可以跳过「看见用私钥签过就已经是 322」。不要另写怎样从头字节还原公钥。294 legacy sign vs 322 bundled unbundling 在本页 item 2 续；续 [`worked-example-lsig137-nothabit-vs-bundled.md`](worked-example-lsig137-nothabit-vs-bundled.md)（不变量 1201 item 3）。

## 本页不抄

- 头字节取值、椭圆曲线背景、示例代码、怎样还原公钥。
- 怎样签、怎样验、怎样从 recId 还原。
