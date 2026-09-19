# 例：看见线上收据没有布隆不是已经改了共识收据编码不是已经改了共识收据编码；看见wire receipts without bloom are not already consensus receipt encoding不是已经是不变量 25；看见线上收据没有布隆不是已经改了共识收据编码不是已经是不变量 195

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7642](https://eips.ethereum.org/EIPS/eip-7642)（history expiry and simpler receipts）。  
**对应课文**：[L5.3](../../courses/level-05-ethereum/L05-M03-multi-client.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7642 wire-no-bloom not already consensus-receipt / not already 25 / not already 195 正式三事（207 余量）/ not 1489 hwin-notenc interchangeable / not 207 history-window-vs-consensus bundled interchangeable」，不是 history window vs consensus bundled（207），也不是已经 跳过须点名（25），也不是已经 历史执行哈希≠BLOCKHASH（195）。不要另写 怎样丢历史、怎样谎报最早块。

## 官方三件事

1. **看见线上收据没有布隆不是已经改了共识收据编码 / 看见线上收据没有布隆不是已经改了共识收据编码 这份对象 is not already 已经改了共识收据编码 interchangeable，也不是已经 history window vs consensus bundled（207） interchangeable / 1489 hwin-notenc interchangeable / 1488 hwin-notcons interchangeable，也不是已经 EIP-7642 wire-no-bloom not already consensus-receipt / not already 25 / not already 195 正式三事 bundled（207 item 2 余量） interchangeable / 207 hwin item 2 interchangeable。**  
   官方把线上收据没有布隆不是已经改了共识收据编码和已经改了共识收据编码写成两件。看见线上收据没有布隆不是已经改了共识收据编码，不是已经改了共识收据编码。

2. **看见wire receipts without bloom are not already consensus receipt encoding / 看见线上收据没有布隆不是已经改了共识收据编码 / 这份对象 is not already 已经是不变量 25 interchangeable，也不是已经 history window vs consensus bundled（207） interchangeable / 1489 hwin-notenc interchangeable / 1490 hwin-notsync interchangeable，也不是已经 跳过须点名 interchangeable / 25 跳过须点名 interchangeable。**  
   官方把wire receipts without bloom are not already consensus receipt encoding和已经是不变量 25写成两件。看见wire receipts without bloom are not already consensus receipt encoding，不是已经是不变量 25。

3. **看见线上收据没有布隆不是已经改了共识收据编码 / 看见wire receipts without bloom are not already consensus receipt encoding / 这份对象 is not already 已经是不变量 195 interchangeable，也不是已经 history window vs consensus bundled（207） interchangeable / 1489 hwin-notenc interchangeable / 1488 hwin-notcons interchangeable，也不是已经 历史执行哈希≠BLOCKHASH interchangeable / 195 历史执行哈希≠BLOCKHASH interchangeable。**  
   官方把线上收据没有布隆不是已经改了共识收据编码和已经是不变量 195写成两件。看见线上收据没有布隆不是已经改了共识收据编码，不是已经是不变量 195。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样丢历史、怎样谎报最早块。

## 官方为什么这样拆

- **线上收据没有布隆不是已经改了共识收据编码 interchangeable：官方写线协议从此偏离共识用的收据编码，收的人必须自己重算布隆。**
- **看见本页不是已经是不变量 25。**
- **看见本页不是已经是不变量 195。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了共识收据编码 | 不是已经改了共识收据编码 | 不是已经跳过须点名（25） |
| 已经是不变量 25 | 不是已经是不变量 25 | 不是已经历史执行哈希≠BLOCKHASH（195） |
| 已经是不变量 195 | 不是已经是不变量 195 | 不是已经1488 hwin-notcons |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7642 wire-no-bloom not already consensus-receipt / not already 25 / not already 195 正式三事（207 余量），必须分开是不是已经改了共识收据编码、是不是已经是不变量 25、是不是已经是不变量 195。可以跳过「看见 7642 就已经改了共识历史」。不要另写 怎样丢历史、怎样谎报最早块。207 history-window vs consensus bundled unbundling 在本页 item 2 续；续 [`worked-example-hwin-notsync-vs-bundled.md`](worked-example-hwin-notsync-vs-bundled.md)（不变量 1490 item 3）。

## 本页不抄

- 服务截止日期、带宽估算、每纪元块数、消息号、布隆宽度。
- 怎样丢历史、怎样谎报最早块。
