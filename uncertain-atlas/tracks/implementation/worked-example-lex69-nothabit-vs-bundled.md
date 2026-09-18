# 例：看见自家习惯的输入输出顺序不是已经是字典序标准；看见先花后找零不是已经没有指纹；看见一种排法不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-69 habit-order not already lex-standard / not already no-fingerprint / not already settled 正式三事（291 余量）/ not 1187 lex69-nothabit interchangeable / not 291 order-vs-lex bundled interchangeable」，不是输入输出字典序 bundled（291），也不是 payjoin 提案就已经不得打乱（1185），也不是策略就已经是共识（144）。不要另写怎样按前交易哈希排输入。

## 官方三件事

1. **看见自家习惯的输入输出顺序 / 看见先花后找零 这份顺序 is not already 已经是字典序标准 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1187 lex69-nothabit interchangeable / 1188 lex69-notcons interchangeable / 291 lex item 2 lex-not-cons interchangeable，也不是已经 BIP-69 habit-order not already lex-standard / not already no-fingerprint / not already settled 正式三事 bundled（291 item 1 余量） interchangeable / 291 lex item 1 interchangeable。**  
   官方写：钱包客户端怎么排输入输出，当时没有标准。各家自己排，往往会在链上留下能辨认的指纹，把用户的财务信息漏出去。看见一种排法，不是已经是本页。

2. **看见先花后找零 / 看见自家习惯的输入输出顺序 / 这份顺序 is not already 已经没有指纹 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1187 lex69-nothabit interchangeable / 291 lex item 3 lex-not-priv interchangeable / 1189 lex69-notpriv interchangeable，也不是已经 payjoin 提案就已经不得打乱 interchangeable / 1185 pj78-notorig interchangeable。**  
   官方另写：例如按地址何时导入来排输入，或把花费输出放前面、找零放后面。看见先花后找零，不是已经藏住了谁收谁找。

3. **看见一种排法 / 看见自家习惯的输入输出顺序 / 这份顺序 is not already 已经交差 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1187 lex69-nothabit interchangeable / 1188 lex69-notcons interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方把没有标准就会漏指纹写成动机，不是已经有本页。看见一种排法，不是已经交差。

比较算法、反字节序哈希、金额优先、例交易、脚本十六进制是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **自家习惯的输入输出顺序 不是已经是字典序标准：** 官方把当时没有标准写成还不是本页。
- **先花后找零 不是已经没有指纹：** 官方把先花后找零写成会漏谁收谁找。
- **一种排法 不是已经交差：** 官方把标准和指纹写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 标准 | 不是已经是字典序标准 | 不是已经不得打乱（1185） |
| 指纹 | 不是已经没有指纹 | 不是已经是共识（144） |
| 交差 | 不是已经交差 | 不是已经是共识门（1188） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-69 habit-order not already lex-standard / not already no-fingerprint / not already settled 正式三事（291 余量），必须分开是不是已经是字典序标准、是不是已经没有指纹、是不是已经交差。可以跳过「看见排过就已经没有指纹」。不要另写怎样按前交易哈希排输入。291 order vs lex bundled unbundling 在本页 item 1 启动；续 [`worked-example-lex69-notcons-vs-bundled.md`](worked-example-lex69-notcons-vs-bundled.md)（不变量 1188 item 2）。

## 本页不抄

- 比较算法、反字节序、金额优先、例交易哈希、脚本十六进制、语言库名单。
- 怎样按前交易哈希排输入、怎样按金额排输出、怎样审计随机排。
