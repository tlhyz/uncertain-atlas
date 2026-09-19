# 例：看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时不是已经把输出锁住；看见script CLTV is not already an output locked by nLockTime不是已经是不变量 165；看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时不是已经 164 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事（164 余量）/ not 1530 cl65-notfld interchangeable / not 164 cltv-vs-nlocktime bundled interchangeable」，不是 cltv vs nlocktime bundled（164），也不是已经 CSV≠绝对锁（165），也不是已经 coinbase成熟≠能花（163）。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。

## 官方三件事

1. **看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时 / 看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时 这份对象 is not already 已经把输出锁住 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1530 cl65-notfld interchangeable / 1531 cl65-notnow interchangeable，也不是已经 BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事 bundled（164 item 1 余量） interchangeable / 164 cl65 item 1 interchangeable。**  
   官方把脚本里的CLTV不是交易nLockTime已经把输出锁到那时和已经把输出锁住写成两件。看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时，不是已经把输出锁住。

2. **看见script CLTV is not already an output locked by nLockTime / 看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时 / 这份对象 is not already 已经是不变量 165 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1530 cl65-notfld interchangeable / 1532 cl65-notclk interchangeable，也不是已经 CSV≠绝对锁 interchangeable / 165 CSV≠绝对锁 interchangeable。**  
   官方把script CLTV is not already an output locked by nLockTime和已经是不变量 165写成两件。看见script CLTV is not already an output locked by nLockTime，不是已经是不变量 165。

3. **看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时 / 看见script CLTV is not already an output locked by nLockTime / 这份对象 is not already 已经 164 bundled interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1530 cl65-notfld interchangeable / 1531 cl65-notnow interchangeable，也不是已经 coinbase成熟≠能花 interchangeable / 163 coinbase成熟≠能花 interchangeable。**  
   官方把脚本里的CLTV不是交易nLockTime已经把输出锁到那时和已经 164 bundled写成两件。看见脚本里的CLTV不是交易nLockTime已经把输出锁到那时，不是已经 164 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。

## 官方为什么这样拆

- **脚本里的CLTV不是交易nLockTime已经把输出锁到那时 interchangeable：官方写 nLockTime 只约束这一笔何时能进块，不是输出已经锁住。**
- **看见本页不是已经是不变量 165。**
- **看见脚本旋钮不是已经 164 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经把输出锁住 | 不是已经把输出锁住 | 不是已经CSV≠绝对锁（165） |
| 已经是不变量 165 | 不是已经是不变量 165 | 不是已经coinbase成熟≠能花（163） |
| 已经 164 bundled | 不是已经 164 bundled | 不是已经1531 cl65-notnow |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 script-cltv not already nlocktime-locked / not already 165 / not already 164-bundled 正式三事（164 余量），必须分开是不是已经把输出锁住、是不是已经是不变量 165、是不是已经 164 bundled。可以跳过「看见填了 nLockTime 就已经锁住输出」。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。164 cltv vs nlocktime bundled unbundling 在本页 item 1 启动；续 [`worked-example-cl65-notnow-vs-bundled.md`](worked-example-cl65-notnow-vs-bundled.md)（不变量 1531 item 2）。

## 本页不抄

- 类型阈值、激活票数、例脚本、实现字节宽度。
- 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。
