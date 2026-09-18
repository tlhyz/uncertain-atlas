# 例：看见 sh 产出不是已经有赎回脚本；看见套进了脚本表达式不是已经能花；看见另造一份赎回脚本不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-381](https://github.com/bitcoin/bips/blob/master/bip-0381.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事（276 余量）/ not 1149 pk381-notredeem interchangeable / not 276 pk-vs-toplevel bundled interchangeable」，不是非隔离见证描述符 bundled（276），也不是付给脚本哈希就已经揭开赎回（170），也不是 multi 就已经是 sortedmulti（1142）。不要另写怎样拼 P2PK。

## 官方三件事

1. **看见 sh 产出 / 看见 P2SH 输出脚本 这份栏 is not already 已经有赎回脚本 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1149 pk381-notredeem interchangeable / 1148 pk381-notplace interchangeable / 276 pk item 1 pk-not-place interchangeable，也不是已经 BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事 bundled（276 item 2 余量） interchangeable / 276 pk item 2 interchangeable。**  
   官方写：`sh` 还会另造一份赎回脚本，花费时要用。看见 `sh` 产出了 P2SH 输出脚本，不是已经把赎回脚本交出来。

2. **看见套进了脚本表达式 / 看见 sh 产出 / 这份栏 is not already 已经能花 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1149 pk381-notredeem interchangeable / 276 pk item 3 familiar-not-compat interchangeable / 1150 pk381-notcompat interchangeable，也不是已经付给脚本哈希就已经揭开赎回 interchangeable / 170 hash interchangeable。**  
   官方把这份赎回脚本写成参数那条脚本表达式产出的输出脚本。看见套进了脚本表达式，不是已经揭开赎回，也不是已经能花。

3. **看见另造一份赎回脚本 / 看见 sh 产出 / 这份栏 is not already 已经交差 interchangeable，也不是已经非隔离见证描述符 bundled（276） interchangeable / 1149 pk381-notredeem interchangeable / 1148 pk381-notplace interchangeable，也不是已经 multi 就已经是 sortedmulti interchangeable / 1142 desc383-notsort interchangeable。**  
   官方把输出脚本和另造的赎回脚本写成两份对象。看见另造了一份赎回脚本，不是已经交差。

脚本模板、测试向量、例钥、十六进制脚本是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **sh 产出 不是已经有赎回脚本：** 官方把输出脚本和赎回脚本写成两份。
- **套进了脚本表达式 不是已经能花：** 官方把赎回脚本写成花费时要用。
- **另造一份赎回脚本 不是已经交差：** 官方把两份对象写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 赎回脚本 | 不是已经有赎回脚本 | 不是已经揭开赎回（170） |
| 能花 | 不是已经能花 | 不是已经同一套放置（1148） |
| 交差 | 不是已经交差 | 不是 multi 就已经是 sortedmulti（1142） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-381 sh-output not already have-redeem / not already spendable / not already settled 正式三事（276 余量），必须分开是不是已经有赎回脚本、是不是已经能花、是不是已经交差。可以跳过「看见熟悉脚本就已经能互操作」。不要另写怎样拼 P2PK。276 pk vs toplevel bundled unbundling 在本页 item 2 续；续 [`worked-example-pk381-notcompat-vs-bundled.md`](worked-example-pk381-notcompat-vs-bundled.md)（不变量 1150 item 3）。

## 本页不抄

- 脚本模板、测试向量、例钥、十六进制脚本。
- 怎样算 HASH160、怎样拼赎回、怎样嵌套。
