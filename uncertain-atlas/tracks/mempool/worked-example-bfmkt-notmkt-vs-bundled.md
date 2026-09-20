# 例：看见弹性块大小不是整套费用市场已经齐不是已经齐；看见elastic block size is not already a complete fee market不是已经是不变量 101；看见弹性块大小不是整套费用市场已经齐不是已经是不变量 27

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)（Fee market change for ETH 1.0 chain）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1559 elastic-size not already market-complete / not already 101 / not already 27 正式三事（158 余量）/ not 1486 bfmkt-notmkt interchangeable / not 158 basefee-vs-tip bundled interchangeable」，不是 basefee vs tip bundled（158），也不是已经 气≠墙钟（101），也不是已经 谁写列表（27）。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。

## 官方三件事

1. **看见弹性块大小不是整套费用市场已经齐 / 看见弹性块大小不是整套费用市场已经齐 这份对象 is not already 已经齐 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1486 bfmkt-notmkt interchangeable / 1485 bfmkt-notpay interchangeable，也不是已经 EIP-1559 elastic-size not already market-complete / not already 101 / not already 27 正式三事 bundled（158 item 2 余量） interchangeable / 158 bfmkt item 2 interchangeable。**  
   官方把弹性块大小不是整套费用市场已经齐和已经齐写成两件。看见弹性块大小不是整套费用市场已经齐，不是已经齐。

2. **看见elastic block size is not already a complete fee market / 看见弹性块大小不是整套费用市场已经齐 / 这份对象 is not already 已经是不变量 101 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1486 bfmkt-notmkt interchangeable / 1487 bfmkt-notmev interchangeable，也不是已经 气≠墙钟 interchangeable / 101 气≠墙钟 interchangeable。**  
   官方把elastic block size is not already a complete fee market和已经是不变量 101写成两件。看见elastic block size is not already a complete fee market，不是已经是不变量 101。

3. **看见弹性块大小不是整套费用市场已经齐 / 看见elastic block size is not already a complete fee market / 这份对象 is not already 已经是不变量 27 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1486 bfmkt-notmkt interchangeable / 1485 bfmkt-notpay interchangeable，也不是已经 谁写列表 interchangeable / 27 谁写列表 interchangeable。**  
   官方把弹性块大小不是整套费用市场已经齐和已经是不变量 27写成两件。看见弹性块大小不是整套费用市场已经齐，不是已经是不变量 27。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。

## 官方为什么这样拆

- **弹性块大小不是整套费用市场已经齐 interchangeable：官方写弹性只应对短期尖峰，长期平均应大致回到没有该 EIP 时的样子。**
- **看见本页不是已经是不变量 101。**
- **看见本页不是已经是不变量 27。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经齐 | 不是已经齐 | 不是已经气≠墙钟（101） |
| 已经是不变量 101 | 不是已经是不变量 101 | 不是已经谁写列表（27） |
| 已经是不变量 27 | 不是已经是不变量 27 | 不是已经1485 bfmkt-notpay |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1559 elastic-size not already market-complete / not already 101 / not already 27 正式三事（158 余量），必须分开是不是已经齐、是不是已经是不变量 101、是不是已经是不变量 27。可以跳过「烧掉 = MEV 已解决」。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。158 basefee vs tip bundled unbundling 在本页 item 2 续；续 [`worked-example-bfmkt-notmev-vs-bundled.md`](worked-example-bfmkt-notmev-vs-bundled.md)（不变量 1487 item 3）。

## 本页不抄

- 弹性倍数、调价分母、初始基础费、固有 gas 表。
- 怎样抬基础费、怎样排空块、怎样抢排序。
