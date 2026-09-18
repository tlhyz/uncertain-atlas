# 例：看见加密私钥记录不是已经是私钥；看见还缺一样才能用不是已经能签；看见能打印不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki)（Deployed, Applications, Specification）。评论摘要：一致不鼓励实现。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-38 encrypted-record not already private-key / not already usable / not already settled 正式三事（296 余量）/ not 1205 enc38-notuse interchangeable / not 296 encrypted-key-vs-usable bundled interchangeable」，不是加密私钥 bundled（296），也不是助记词就已经是种子（183），也不是扩展公钥就已经能花（182）。不要另写怎样用口令解开或怎样做椭圆曲线倍点。

## 官方三件事

1. **看见加密私钥记录 / 看见还缺一样才能用 这份记录 is not already 已经是私钥 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1205 enc38-notuse interchangeable / 1206 enc38-notmint interchangeable / 296 enc item 2 factory-not-redeem interchangeable，也不是已经 BIP-38 encrypted-record not already private-key / not already usable / not already settled 正式三事 bundled（296 item 1 余量） interchangeable / 296 enc item 1 interchangeable。**  
   官方写：本页给纸钱包和实物币用，把口令保护的私钥记录编成一串可打印字符。每条记录里有凑回私钥所需的信息，就缺口令。看见加密记录，不是已经是私钥。

2. **看见还缺一样才能用 / 看见加密私钥记录 / 这份记录 is not already 已经能用 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1205 enc38-notuse interchangeable / 296 enc item 3 frag-not-addr interchangeable / 1207 enc38-notfrag interchangeable，也不是已经助记词就已经是种子 interchangeable / 183 mnemonic interchangeable。**  
   官方另写：用户眼里，开头那种标记代表「一把还缺一样才能用的私钥」。看见加密记录，不是已经能签。看见有了记录，不是已经有口令。

3. **看见能打印 / 看见加密私钥记录 / 这份记录 is not already 已经交差 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1205 enc38-notuse interchangeable / 1206 enc38-notmint interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把可打印记录和已经能花写成两件。看见能打印，不是已经能花，也不是已经交差。

加密步骤、口令派生参数、前缀取值、例串、标志位是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **加密私钥记录 不是已经是私钥：** 官方把记录写成还缺口令。
- **还缺一样才能用 不是已经能用：** 官方把开头标记写成还缺一样。
- **能打印 不是已经交差：** 官方把能打印写成不是已经能花。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 私钥 | 不是已经是私钥 | 不是已经是种子（183） |
| 能用 | 不是已经能用 | 不是已经能花（182） |
| 交差 | 不是已经交差 | 不是已经能兑（1206） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-38 encrypted-record not already private-key / not already usable / not already settled 正式三事（296 余量），必须分开是不是已经是私钥、是不是已经能用、是不是已经交差。可以跳过「看见加密串就已经能花」。官方评论已写一致不鼓励实现；第一版不要抄本页当默认备份。不要另写怎样用口令解开或怎样做椭圆曲线倍点。296 encrypted key vs usable bundled unbundling 在本页 item 1 启动；续 [`worked-example-enc38-notmint-vs-bundled.md`](worked-example-enc38-notmint-vs-bundled.md)（不变量 1206 item 2）。

## 本页不抄

- 加密步骤、口令派生参数、前缀取值、例串、标志位。
- 怎样用口令解开、怎样做椭圆曲线倍点、怎样造确认码。
