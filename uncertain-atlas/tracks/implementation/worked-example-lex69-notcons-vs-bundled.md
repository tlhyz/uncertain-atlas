# 例：看见按字典序排了不是已经是共识；看见顺序变了不是已经决定这笔能不能花；看见排过了不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-69 lex-order not already consensus / not already spend-gate / not already settled 正式三事（291 余量）/ not 1188 lex69-notcons interchangeable / not 291 order-vs-lex bundled interchangeable」，不是输入输出字典序 bundled（291），也不是策略就已经是共识（144），也不是替换信号就已经换掉（166）。不要另写怎样按前交易哈希排输入。

## 官方三件事

1. **看见按字典序排了 / 看见排过了 这份顺序 is not already 已经是共识 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1188 lex69-notcons interchangeable / 1187 lex69-nothabit interchangeable / 291 lex item 1 habit-not-std interchangeable，也不是已经 BIP-69 lex-order not already consensus / not already spend-gate / not already settled 正式三事 bundled（291 item 2 余量） interchangeable / 291 lex item 2 interchangeable。**  
   官方写：本页适用于输入输出顺序并不影响这笔功能的交易。本页是信息 BIP，不是共识规则。看见排过了，不是块里已经要这一套。

2. **看见顺序变了 / 看见按字典序排了 / 这份顺序 is not already 已经决定这笔能不能花 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1188 lex69-notcons interchangeable / 291 lex item 3 lex-not-priv interchangeable / 1189 lex69-notpriv interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方另写：输入输出怎么排，并不影响这笔属于它的功能，所以随机排也行得通。SIGHASH_ANYONECANPAY / SIGHASH_NONE 以后还可能被别人改，但合规软件仍应当先按字典序交出去。看见顺序变了，不是这笔已经废。

3. **看见排过了 / 看见按字典序排了 / 这份顺序 is not already 已经交差 interchangeable，也不是已经输入输出字典序 bundled（291） interchangeable / 1188 lex69-notcons interchangeable / 1187 lex69-nothabit interchangeable，也不是已经替换信号就已经换掉 interchangeable / 166 replace interchangeable。**  
   官方把顺序不影响功能写成适用范围。看见排过了，不是已经交差。

比较算法、反字节序哈希、金额优先、例交易、脚本十六进制是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **按字典序排了 不是已经是共识：** 官方把本页写成信息 BIP。
- **顺序变了 不是已经决定这笔能不能花：** 官方把顺序写成不影响功能。
- **排过了 不是已经交差：** 官方把共识门和能不能花写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 共识 | 不是已经是共识 | 不是已经是策略共识（144） |
| 能不能花 | 不是已经决定这笔能不能花 | 不是已经换掉（166） |
| 交差 | 不是已经交差 | 不是已经是标准（1187） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-69 lex-order not already consensus / not already spend-gate / not already settled 正式三事（291 余量），必须分开是不是已经是共识、是不是已经决定这笔能不能花、是不是已经交差。可以跳过「看见排过就已经没有指纹」。不要另写怎样按前交易哈希排输入。291 order vs lex bundled unbundling 在本页 item 2 续；续 [`worked-example-lex69-notpriv-vs-bundled.md`](worked-example-lex69-notpriv-vs-bundled.md)（不变量 1189 item 3）。

## 本页不抄

- 比较算法、反字节序、金额优先、例交易哈希、脚本十六进制、语言库名单。
- 怎样按前交易哈希排输入、怎样按金额排输出、怎样审计随机排。
