# 例：看见读树涨价不是磁盘已经是常数时间；看见本页不是已经写了后来那次树依赖涨价；看见读树涨价不是已经写了本笔冷热

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-150](https://eips.ethereum.org/EIPS/eip-150)（Final, Core；Tangerine Whistle）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-150 reprice not already disk-O1 / not already 1884 / not already cold-hot 正式三事（237 余量）/ not 1298 c63-notprice interchangeable / not 237 call-63rds-vs-oog bundled interchangeable」，不是 call 63rds vs oog bundled（237），也不是已经 tree-reprice（229），也不是已经 cold-warm（169）。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。

## 官方三件事

1. **看见读树涨价 / 看见读树涨价 这份对象 is not already 磁盘已经是常数时间 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1298 c63-notprice interchangeable / 1299 c63-notoog interchangeable，也不是已经 EIP-150 reprice not already disk-O1 / not already 1884 / not already cold-hot 正式三事 bundled（237 item 1 余量） interchangeable / 237 c63 item 1 interchangeable。**  
   官方把读树涨价和磁盘已经是常数时间写成两件。看见读树涨价，不是磁盘已经是常数时间。

2. **看见本页 / 看见读树涨价 / 这份对象 is not already 已经写了后来那次树依赖涨价 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1298 c63-notprice interchangeable / 1300 c63-notcap interchangeable，也不是已经 tree-reprice interchangeable / 229 tree-reprice interchangeable。**  
   官方把本页和已经写了后来那次树依赖涨价写成两件。看见本页，不是已经写了后来那次树依赖涨价。

3. **看见读树涨价 / 看见本页 / 这份对象 is not already 已经写了本笔冷热 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1298 c63-notprice interchangeable / 1299 c63-notoog interchangeable，也不是已经 cold-warm interchangeable / 169 cold-warm interchangeable。**  
   官方把读树涨价和已经写了本笔冷热写成两件。看见读树涨价，不是已经写了本笔冷热。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。

## 官方为什么这样拆

- **读树涨价 不是已经齐了：官方说还会靠软件缓解，但读树仍会是最容易的拖慢面。**
- **本页 不是已经写了后来树依赖涨价：官方写看见读树涨价，不是已经写了后来那次树依赖涨价。**
- **读树涨价 不是已经写了本笔冷热：官方写不是已经写了本笔冷热。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 磁盘已经是常数时间 | 不是磁盘已经是常数时间 | 不是已经tree-reprice（229） |
| 已经写了后来那次树依赖涨价 | 不是已经写了后来那次树依赖涨价 | 不是已经cold-warm（169） |
| 已经写了本笔冷热 | 不是已经写了本笔冷热 | 不是已经1299 c63-notoog |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-150 reprice not already disk-O1 / not already 1884 / not already cold-hot 正式三事（237 余量），必须分开是不是磁盘已经是常数时间、是不是已经写了后来那次树依赖涨价、是不是已经写了本笔冷热。可以跳过「看见读树涨价就已经齐了」。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。237 call 63rds vs oog bundled unbundling 在本页 item 1 启动；续 [`worked-example-c63-notoog-vs-bundled.md`](worked-example-c63-notoog-vs-bundled.md)（不变量 1299 item 2）。

## 本页不抄

- 分叉高度、操作码新旧气价、建议气限取值、读盘字节估计、软深度大约能到几层。
- 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。
