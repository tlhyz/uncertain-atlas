# 例：看见熟悉的标准脚本不是已经能互操作；看见旧钱包认得输出不是已经不必再写本页；看见全新描述符不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-381](https://github.com/bitcoin/bips/blob/master/bip-0381.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-381 familiar-scripts not already interoperable / not already skip-page / not already settled 正式三事（276 余量）/ not 1150 pk381-notcompat interchangeable / not 276 pk-vs-toplevel bundled interchangeable」，不是非隔离见证描述符 bundled（276），也不是已经 BIP32 compatible（1118），也不是看见描述符就已经是地址（184）。不要另写怎样拼 P2PK。

## 官方三件事

1. **看见熟悉的标准脚本 / 看见旧节点认得输出 这份栏 is not already 已经能互操作 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1150 pk381-notcompat interchangeable / 1148 pk381-notplace interchangeable / 276 pk item 1 pk-not-place interchangeable，也不是已经 BIP-381 familiar-scripts not already interoperable / not already skip-page / not already settled 正式三事 bundled（276 item 3 余量） interchangeable / 276 pk item 3 interchangeable。**  
   官方写：这些是全新的描述符，和任何实现都不兼容。不过产出的脚本是标准脚本，现有软件多半认得。看见脚本眼熟，不是已经能读这份描述符。

2. **看见旧钱包认得输出 / 看见熟悉的标准脚本 / 这份栏 is not already 已经不必再写本页 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1150 pk381-notcompat interchangeable / 276 pk item 2 sh-not-redeem interchangeable / 1149 pk381-notredeem interchangeable，也不是已经 BIP32 compatible interchangeable / 1118 purp43 interchangeable。**  
   官方把「全新描述符」和「标准脚本眼熟」写成两句。看见旧钱包认得输出，不是已经能导入这段字，也不是已经不必再写本页。

3. **看见全新描述符 / 看见熟悉的标准脚本 / 这份栏 is not already 已经交差 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1150 pk381-notcompat interchangeable / 1148 pk381-notplace interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把眼熟和兼容写成两句。看见全新描述符，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **熟悉的标准脚本 不是已经能互操作：** 官方把全新描述符和标准脚本眼熟写成两句。
- **旧钱包认得输出 不是已经不必再写本页：** 官方把认得输出和能导入描述符写成两句。
- **全新描述符 不是已经交差：** 官方把眼熟和兼容写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 眼熟 | 不是已经能互操作 | 不是已经 BIP32 compatible（1118） |
| 旧钱包 | 不是已经不必再写本页 | 不是已经有赎回脚本（1149） |
| 交差 | 不是已经交差 | 不是已经是地址（184） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-381 familiar-scripts not already interoperable / not already skip-page / not already settled 正式三事（276 余量），必须分开是不是已经能互操作、是不是已经不必再写本页、是不是已经交差。可以跳过「看见熟悉脚本就已经能互操作」。不要另写怎样拼 P2PK。276 pk vs toplevel bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样算 HASH160、怎样拼赎回、怎样嵌套。
