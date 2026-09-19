# 例：看见相对锁不是已经是绝对锁不是已经是绝对锁；看见a relative lock is not already an absolute lock不是已经是不变量 164；看见相对锁不是已经是绝对锁不是已经是不变量 163

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)（CHECKSEQUENCEVERIFY）。对照 [BIP-68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-112 relative-lock not already absolute-lock / not already 164 / not already 163 正式三事（165 余量）/ not 1528 csvd-notabs interchangeable / not 165 csv-vs-cltv bundled interchangeable」，不是 csv vs cltv bundled（165），也不是已经 CLTV≠nLockTime已锁（164），也不是已经 coinbase成熟≠能花（163）。不要另写 怎样绕过相对锁。

## 官方三件事

1. **看见相对锁不是已经是绝对锁 / 看见相对锁不是已经是绝对锁 这份对象 is not already 已经是绝对锁 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1528 csvd-notabs interchangeable / 1527 csvd-notseq interchangeable，也不是已经 BIP-112 relative-lock not already absolute-lock / not already 164 / not already 163 正式三事 bundled（165 item 2 余量） interchangeable / 165 csvd item 2 interchangeable。**  
   官方把相对锁不是已经是绝对锁和已经是绝对锁写成两件。看见相对锁不是已经是绝对锁，不是已经是绝对锁。

2. **看见a relative lock is not already an absolute lock / 看见相对锁不是已经是绝对锁 / 这份对象 is not already 已经是不变量 164 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1528 csvd-notabs interchangeable / 1529 csvd-notdep interchangeable，也不是已经 CLTV≠nLockTime已锁 interchangeable / 164 CLTV≠nLockTime已锁 interchangeable。**  
   官方把a relative lock is not already an absolute lock和已经是不变量 164写成两件。看见a relative lock is not already an absolute lock，不是已经是不变量 164。

3. **看见相对锁不是已经是绝对锁 / 看见a relative lock is not already an absolute lock / 这份对象 is not already 已经是不变量 163 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1528 csvd-notabs interchangeable / 1527 csvd-notseq interchangeable，也不是已经 coinbase成熟≠能花 interchangeable / 163 coinbase成熟≠能花 interchangeable。**  
   官方把相对锁不是已经是绝对锁和已经是不变量 163写成两件。看见相对锁不是已经是绝对锁，不是已经是不变量 163。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样绕过相对锁。

## 官方为什么这样拆

- **相对锁不是已经是绝对锁 interchangeable：官方写 nLockTime 挡日期，nSequence 挡被花输出还不够老。**
- **看见本页不是已经是不变量 164。**
- **看见本页不是已经是不变量 163。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是绝对锁 | 不是已经是绝对锁 | 不是已经CLTV≠nLockTime已锁（164） |
| 已经是不变量 164 | 不是已经是不变量 164 | 不是已经coinbase成熟≠能花（163） |
| 已经是不变量 163 | 不是已经是不变量 163 | 不是已经1527 csvd-notseq |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-112 relative-lock not already absolute-lock / not already 164 / not already 163 正式三事（165 余量），必须分开是不是已经是绝对锁、是不是已经是不变量 164、是不是已经是不变量 163。可以跳过「看见 CSV 就已经是 CLTV」。不要另写 怎样绕过相对锁。165 csv vs cltv bundled unbundling 在本页 item 2 续；续 [`worked-example-csvd-notdep-vs-bundled.md`](worked-example-csvd-notdep-vs-bundled.md)（不变量 1529 item 3）。

## 本页不抄

- 位旗、粒度、例脚本。
- 怎样绕过相对锁。
