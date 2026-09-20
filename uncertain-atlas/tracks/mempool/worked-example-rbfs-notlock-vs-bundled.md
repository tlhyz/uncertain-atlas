# 例：看见nSequence用来示意可替换不是已经是相对锁不是已经是相对锁；看见using nSequence to signal replaceability is not already a relative lock不是已经是不变量 165；看见nSequence用来示意可替换不是已经是相对锁不是已经是不变量 164

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-125](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki)（Opt-in Full Replace-by-Fee Signaling）。  
**对应课文**：[L3.2](../../courses/level-03-bitcoin/L03-M02-fees-and-standardness.md)。  
**不要写进**：`index/03` 共识行、M3.2、L3.2。本页是「BIP-125 nsequence-signal not already relative-lock / not already 165 / not already 164 正式三事（166 余量）/ not 1525 rbfs-notlock interchangeable / not 166 rbf-signal-vs-replaced bundled interchangeable」，不是 rbf signal vs replaced bundled（166），也不是已经 CSV≠绝对锁（165），也不是已经 CLTV≠nLockTime已锁（164）。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。

## 官方三件事

1. **看见nSequence用来示意可替换不是已经是相对锁 / 看见nSequence用来示意可替换不是已经是相对锁 这份对象 is not already 已经是相对锁 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1525 rbfs-notlock interchangeable / 1524 rbfs-notrep interchangeable，也不是已经 BIP-125 nsequence-signal not already relative-lock / not already 165 / not already 164 正式三事 bundled（166 item 2 余量） interchangeable / 166 rbfs item 2 interchangeable。**  
   官方把nSequence用来示意可替换不是已经是相对锁和已经是相对锁写成两件。看见nSequence用来示意可替换不是已经是相对锁，不是已经是相对锁。

2. **看见using nSequence to signal replaceability is not already a relative lock / 看见nSequence用来示意可替换不是已经是相对锁 / 这份对象 is not already 已经是不变量 165 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1525 rbfs-notlock interchangeable / 1526 rbfs-notjoin interchangeable，也不是已经 CSV≠绝对锁 interchangeable / 165 CSV≠绝对锁 interchangeable。**  
   官方把using nSequence to signal replaceability is not already a relative lock和已经是不变量 165写成两件。看见using nSequence to signal replaceability is not already a relative lock，不是已经是不变量 165。

3. **看见nSequence用来示意可替换不是已经是相对锁 / 看见using nSequence to signal replaceability is not already a relative lock / 这份对象 is not already 已经是不变量 164 interchangeable，也不是已经 rbf signal vs replaced bundled（166） interchangeable / 1525 rbfs-notlock interchangeable / 1524 rbfs-notrep interchangeable，也不是已经 CLTV≠nLockTime已锁 interchangeable / 164 CLTV≠nLockTime已锁 interchangeable。**  
   官方把nSequence用来示意可替换不是已经是相对锁和已经是不变量 164写成两件。看见nSequence用来示意可替换不是已经是相对锁，不是已经是不变量 164。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。

## 官方为什么这样拆

- **nSequence用来示意可替换不是已经是相对锁 interchangeable：官方写与 BIP-68 没有已知麻烦互动，同一字段三种对象。**
- **看见本页不是已经是不变量 165。**
- **看见本页不是已经是不变量 164。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是相对锁 | 不是已经是相对锁 | 不是已经CSV≠绝对锁（165） |
| 已经是不变量 165 | 不是已经是不变量 165 | 不是已经CLTV≠nLockTime已锁（164） |
| 已经是不变量 164 | 不是已经是不变量 164 | 不是已经1524 rbfs-notrep |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-125 nsequence-signal not already relative-lock / not already 165 / not already 164 正式三事（166 余量），必须分开是不是已经是相对锁、是不是已经是不变量 165、是不是已经是不变量 164。可以跳过「看见带了 RBF 就已经换掉」。不要另写 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。166 rbf-signal vs replaced bundled unbundling 在本页 item 2 续；续 [`worked-example-rbfs-notjoin-vs-bundled.md`](worked-example-rbfs-notjoin-vs-bundled.md)（不变量 1526 item 3）。

## 本页不抄

- 终值常数、替换条数、最低中继费率例子。
- 怎样构造替换、怎样钉死、怎样挤掉商家看见的那笔。
