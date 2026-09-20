# 例：看见nLockTime能证明将来能花不是已经证明现在不能花不是已经证明现在不能花；看见nLockTime proving a future spend is not already proving it cannot be spent now不是已经是不变量 163；看见nLockTime能证明将来能花不是已经证明现在不能花不是已经是不变量 41

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki)（OP_CHECKLOCKTIMEVERIFY）。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-65 nlocktime-future-spend not already present-unspendable / not already 163 / not already 41 正式三事（164 余量）/ not 1531 cl65-notnow interchangeable / not 164 cltv-vs-nlocktime bundled interchangeable」，不是 cltv vs nlocktime bundled（164），也不是已经 coinbase成熟≠能花（163），也不是已经 MTP三把尺（41）。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。

## 官方三件事

1. **看见nLockTime能证明将来能花不是已经证明现在不能花 / 看见nLockTime能证明将来能花不是已经证明现在不能花 这份对象 is not already 已经证明现在不能花 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1531 cl65-notnow interchangeable / 1530 cl65-notfld interchangeable，也不是已经 BIP-65 nlocktime-future-spend not already present-unspendable / not already 163 / not already 41 正式三事 bundled（164 item 2 余量） interchangeable / 164 cl65 item 2 interchangeable。**  
   官方把nLockTime能证明将来能花不是已经证明现在不能花和已经证明现在不能花写成两件。看见nLockTime能证明将来能花不是已经证明现在不能花，不是已经证明现在不能花。

2. **看见nLockTime proving a future spend is not already proving it cannot be spent now / 看见nLockTime能证明将来能花不是已经证明现在不能花 / 这份对象 is not already 已经是不变量 163 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1531 cl65-notnow interchangeable / 1532 cl65-notclk interchangeable，也不是已经 coinbase成熟≠能花 interchangeable / 163 coinbase成熟≠能花 interchangeable。**  
   官方把nLockTime proving a future spend is not already proving it cannot be spent now和已经是不变量 163写成两件。看见nLockTime proving a future spend is not already proving it cannot be spent now，不是已经是不变量 163。

3. **看见nLockTime能证明将来能花不是已经证明现在不能花 / 看见nLockTime proving a future spend is not already proving it cannot be spent now / 这份对象 is not already 已经是不变量 41 interchangeable，也不是已经 cltv vs nlocktime bundled（164） interchangeable / 1531 cl65-notnow interchangeable / 1530 cl65-notfld interchangeable，也不是已经 MTP三把尺 interchangeable / 41 MTP三把尺 interchangeable。**  
   官方把nLockTime能证明将来能花不是已经证明现在不能花和已经是不变量 41写成两件。看见nLockTime能证明将来能花不是已经证明现在不能花，不是已经是不变量 41。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。

## 官方为什么这样拆

- **nLockTime能证明将来能花不是已经证明现在不能花 interchangeable：官方写它不能证明在那之前不可能另签一笔现在就能花的交易。**
- **看见本页不是已经是不变量 163。**
- **看见本页不是已经是不变量 41。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经证明现在不能花 | 不是已经证明现在不能花 | 不是已经coinbase成熟≠能花（163） |
| 已经是不变量 163 | 不是已经是不变量 163 | 不是已经MTP三把尺（41） |
| 已经是不变量 41 | 不是已经是不变量 41 | 不是已经1530 cl65-notfld |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-65 nlocktime-future-spend not already present-unspendable / not already 163 / not already 41 正式三事（164 余量），必须分开是不是已经证明现在不能花、是不是已经是不变量 163、是不是已经是不变量 41。可以跳过「看见填了 nLockTime 就已经锁住输出」。不要另写 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。164 cltv vs nlocktime bundled unbundling 在本页 item 2 续；续 [`worked-example-cl65-notclk-vs-bundled.md`](worked-example-cl65-notclk-vs-bundled.md)（不变量 1532 item 3）。

## 本页不抄

- 类型阈值、激活票数、例脚本、实现字节宽度。
- 怎样用final输入绕过CLTV、怎样拼托管或支付通道退款。
