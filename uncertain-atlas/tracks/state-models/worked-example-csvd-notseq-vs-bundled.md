# 例：看见脚本里的CSV不是nSequence已经把输出相对锁住不是已经相对锁住；看见script CSV is not already a relative lock from nSequence不是已经是不变量 164；看见脚本里的CSV不是nSequence已经把输出相对锁住不是已经 165 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-112](https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki)（CHECKSEQUENCEVERIFY）。对照 [BIP-68](https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki)。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-112 script-csv not already nsequence-locked / not already 164 / not already 165-bundled 正式三事（165 余量）/ not 1527 csvd-notseq interchangeable / not 165 csv-vs-cltv bundled interchangeable」，不是 csv vs cltv bundled（165），也不是已经 CLTV≠nLockTime已锁（164），也不是已经 coinbase成熟≠能花（163）。不要另写 怎样绕过相对锁。

## 官方三件事

1. **看见脚本里的CSV不是nSequence已经把输出相对锁住 / 看见脚本里的CSV不是nSequence已经把输出相对锁住 这份对象 is not already 已经相对锁住 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1527 csvd-notseq interchangeable / 1528 csvd-notabs interchangeable，也不是已经 BIP-112 script-csv not already nsequence-locked / not already 164 / not already 165-bundled 正式三事 bundled（165 item 1 余量） interchangeable / 165 csvd item 1 interchangeable。**  
   官方把脚本里的CSV不是nSequence已经把输出相对锁住和已经相对锁住写成两件。看见脚本里的CSV不是nSequence已经把输出相对锁住，不是已经相对锁住。

2. **看见script CSV is not already a relative lock from nSequence / 看见脚本里的CSV不是nSequence已经把输出相对锁住 / 这份对象 is not already 已经是不变量 164 interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1527 csvd-notseq interchangeable / 1529 csvd-notdep interchangeable，也不是已经 CLTV≠nLockTime已锁 interchangeable / 164 CLTV≠nLockTime已锁 interchangeable。**  
   官方把script CSV is not already a relative lock from nSequence和已经是不变量 164写成两件。看见script CSV is not already a relative lock from nSequence，不是已经是不变量 164。

3. **看见脚本里的CSV不是nSequence已经把输出相对锁住 / 看见script CSV is not already a relative lock from nSequence / 这份对象 is not already 已经 165 bundled interchangeable，也不是已经 csv vs cltv bundled（165） interchangeable / 1527 csvd-notseq interchangeable / 1528 csvd-notabs interchangeable，也不是已经 coinbase成熟≠能花 interchangeable / 163 coinbase成熟≠能花 interchangeable。**  
   官方把脚本里的CSV不是nSequence已经把输出相对锁住和已经 165 bundled写成两件。看见脚本里的CSV不是nSequence已经把输出相对锁住，不是已经 165 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样绕过相对锁。

## 官方为什么这样拆

- **脚本里的CSV不是nSequence已经把输出相对锁住 interchangeable：官方写关掉相对锁则 nSequence 没有共识年龄含义。**
- **看见本页不是已经是不变量 164。**
- **看见脚本旋钮不是已经 165 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经相对锁住 | 不是已经相对锁住 | 不是已经CLTV≠nLockTime已锁（164） |
| 已经是不变量 164 | 不是已经是不变量 164 | 不是已经coinbase成熟≠能花（163） |
| 已经 165 bundled | 不是已经 165 bundled | 不是已经1528 csvd-notabs |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-112 script-csv not already nsequence-locked / not already 164 / not already 165-bundled 正式三事（165 余量），必须分开是不是已经相对锁住、是不是已经是不变量 164、是不是已经 165 bundled。可以跳过「看见 CSV 就已经是 CLTV」。不要另写 怎样绕过相对锁。165 csv vs cltv bundled unbundling 在本页 item 1 启动；续 [`worked-example-csvd-notabs-vs-bundled.md`](worked-example-csvd-notabs-vs-bundled.md)（不变量 1528 item 2）。

## 本页不抄

- 位旗、粒度、例脚本。
- 怎样绕过相对锁。
