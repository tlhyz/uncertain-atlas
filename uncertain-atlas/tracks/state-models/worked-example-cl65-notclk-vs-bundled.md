# 例：看见CLTV比的是花费交易的nLockTime不是墙上现在不是已经在跟墙上现在比；看见CLTV comparing against nLockTime is not already comparing against wall-clock now不是已经是不变量 41；看见CLTV比的是花费交易的nLockTime不是墙上现在不是已经是不变量 165

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事（164 余量）/ not 1532 cl65-notclk interchangeable / not 164 cltv-vs-nlocktime bundled interchangeable」，不是 cltv vs nlocktime bundled（164），也不是已经 MTP三把尺（41），也不是已经 CSV≠绝对锁（165）。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。

## 官方三件事

1. **看见CLTV比的是花费交易的nLockTime不是墙上现在 / 看见CLTV比的是花费交易的nLockTime不是墙上现在 这份对象 is not already 已经在跟墙上现在比 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1532 cl65-notclk interchangeable / 1530 cl65-notfld interchangeable，也不是已经 BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事 bundled（164 item 3 余量） interchangeable / 164 cl65 item 3 interchangeable。**  
   官方把CLTV比的是花费交易的nLockTime不是墙上现在和已经在跟墙上现在比写成两件。看见CLTV比的是花费交易的nLockTime不是墙上现在，不是已经在跟墙上现在比。

2. **看见CLTV comparing against nLockTime is not already comparing against wall-clock now / 看见CLTV比的是花费交易的nLockTime不是墙上现在 / 这份对象 is not already 已经是不变量 41 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1532 cl65-notclk interchangeable / 1531 cl65-notnow interchangeable，也不是已经 MTP三把尺 interchangeable / 41 MTP三把尺 interchangeable。**  
   官方把CLTV comparing against nLockTime is not already comparing against wall-clock now和已经是不变量 41写成两件。看见CLTV comparing against nLockTime is not already comparing against wall-clock now，不是已经是不变量 41。

3. **看见CLTV比的是花费交易的nLockTime不是墙上现在 / 看见CLTV comparing against nLockTime is not already comparing against wall-clock now / 这份对象 is not already 已经是不变量 165 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1532 cl65-notclk interchangeable / 1530 cl65-notfld interchangeable，也不是已经 CSV≠绝对锁 interchangeable / 165 CSV≠绝对锁 interchangeable。**  
   官方把CLTV比的是花费交易的nLockTime不是墙上现在和已经是不变量 165写成两件。看见CLTV比的是花费交易的nLockTime不是墙上现在，不是已经是不变量 165。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。

## 官方为什么这样拆

- **CLTV比的是花费交易的nLockTime不是墙上现在 interchangeable：官方写比的是本笔 nLockTime，不是墙上现在或本块时间。**
- **看见本页不是已经是不变量 41。**
- **看见本页不是已经是不变量 165。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在跟墙上现在比 | 不是已经在跟墙上现在比 | 不是已经MTP三把尺（41） |
| 已经是不变量 41 | 不是已经是不变量 41 | 不是已经CSV≠绝对锁（165） |
| 已经是不变量 165 | 不是已经是不变量 165 | 不是已经1530 cl65-notfld |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 cltv-compares-nlocktime not already wall-clock / not already 41 / not already 165 正式三事（164 余量），必须分开是不是已经在跟墙上现在比、是不是已经是不变量 41、是不是已经是不变量 165。可以跳过「看见填了 nLockTime 就已经锁住输出」。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。164 cltv vs nlocktime bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：p2sh-hash-vs-redeem（170）。

## 本页不抄

- 类型阈值、激活票数、例脚本、实现字节宽度。
- 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。
