# 例：看见改见证不是已经改交易身份不是已经改txid；看见changing the witness is not already changing the txid不是已经是不变量 144；看见改见证不是已经改交易身份不是已经是不变量 12

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki)（Segregated Witness Consensus layer）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-141 change-witness not already change-txid / not already 144 / not already 12 正式三事（152 余量）/ not 1552 twid-notchg interchangeable / not 152 txid-vs-wtxid bundled interchangeable」，不是 txid vs wtxid bundled（152），也不是已经 策略≠共识（144），也不是已经 同根不同列表（12）。不要另写 怎样改见证编码。

## 官方三件事

1. **看见改见证不是已经改交易身份 / 看见改见证不是已经改交易身份 这份对象 is not already 已经改txid interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1552 twid-notchg interchangeable / 1551 twid-noteq interchangeable，也不是已经 BIP-141 change-witness not already change-txid / not already 144 / not already 12 正式三事 bundled（152 item 2 余量） interchangeable / 152 twid item 2 interchangeable。**  
   官方把改见证不是已经改交易身份和已经改txid写成两件。看见改见证不是已经改交易身份，不是已经改txid。

2. **看见changing the witness is not already changing the txid / 看见改见证不是已经改交易身份 / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1552 twid-notchg interchangeable / 1553 twid-notmer interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把changing the witness is not already changing the txid和已经是不变量 144写成两件。看见changing the witness is not already changing the txid，不是已经是不变量 144。

3. **看见改见证不是已经改交易身份 / 看见changing the witness is not already changing the txid / 这份对象 is not already 已经是不变量 12 interchangeable，也不是已经 txid vs wtxid bundled（152） interchangeable / 1552 twid-notchg interchangeable / 1551 twid-noteq interchangeable，也不是已经 同根不同列表 interchangeable / 12 同根不同列表 interchangeable。**  
   官方把改见证不是已经改交易身份和已经是不变量 12写成两件。看见改见证不是已经改交易身份，不是已经是不变量 12。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样改见证编码。

## 官方为什么这样拆

- **改见证不是已经改交易身份 interchangeable：官方写签名数据不再是交易哈希的一部分，签名方式怎么变都不再改交易身份。**
- **看见本页不是已经是不变量 144。**
- **看见本页不是已经是不变量 12。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改txid | 不是已经改txid | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经同根不同列表（12） |
| 已经是不变量 12 | 不是已经是不变量 12 | 不是已经1551 twid-noteq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-141 change-witness not already change-txid / not already 144 / not already 12 正式三事（152 余量），必须分开是不是已经改txid、是不是已经是不变量 144、是不是已经是不变量 12。可以跳过「看见旧节点也验了见证」。不要另写 怎样改见证编码。152 txid vs wtxid bundled unbundling 在本页 item 2 续；续 [`worked-example-twid-notmer-vs-bundled.md`](worked-example-twid-notmer-vs-bundled.md)（不变量 1553 item 3）。

## 本页不抄

- 承诺魔数、重量公式、版本0程序长度。
- 怎样改见证编码。
