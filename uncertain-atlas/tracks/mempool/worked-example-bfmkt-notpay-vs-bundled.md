# 例：看见基础费烧掉不是已经给了出块者不是已经给了出块者；看见burned basefee is not already paid to the proposer不是已经是不变量 145；看见基础费烧掉不是已经给了出块者不是已经 158 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)（Fee market change for ETH 1.0 chain）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1559 basefee-burned not already paid-to-proposer / not already 145 / not already 158-bundled 正式三事（158 余量）/ not 1485 bfmkt-notpay interchangeable / not 158 basefee-vs-tip bundled interchangeable」，不是 basefee vs tip bundled（158），也不是已经 blob费≠执行气（145），也不是已经 策略≠共识（144）。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。

## 官方三件事

1. **看见基础费烧掉不是已经给了出块者 / 看见基础费烧掉不是已经给了出块者 这份对象 is not already 已经给了出块者 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1485 bfmkt-notpay interchangeable / 1486 bfmkt-notmkt interchangeable，也不是已经 EIP-1559 basefee-burned not already paid-to-proposer / not already 145 / not already 158-bundled 正式三事 bundled（158 item 1 余量） interchangeable / 158 bfmkt item 1 interchangeable。**  
   官方把基础费烧掉不是已经给了出块者和已经给了出块者写成两件。看见基础费烧掉不是已经给了出块者，不是已经给了出块者。

2. **看见burned basefee is not already paid to the proposer / 看见基础费烧掉不是已经给了出块者 / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1485 bfmkt-notpay interchangeable / 1487 bfmkt-notmev interchangeable，也不是已经 blob费≠执行气 interchangeable / 145 blob费≠执行气 interchangeable。**  
   官方把burned basefee is not already paid to the proposer和已经是不变量 145写成两件。看见burned basefee is not already paid to the proposer，不是已经是不变量 145。

3. **看见基础费烧掉不是已经给了出块者 / 看见burned basefee is not already paid to the proposer / 这份对象 is not already 已经 158 bundled interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1485 bfmkt-notpay interchangeable / 1486 bfmkt-notmkt interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把基础费烧掉不是已经给了出块者和已经 158 bundled写成两件。看见基础费烧掉不是已经给了出块者，不是已经 158 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。

## 官方为什么这样拆

- **基础费烧掉不是已经给了出块者 interchangeable：官方写矿工只留小费，基础费总是烧掉，不给任何人。**
- **看见本页不是已经是不变量 145。**
- **看见读数旋钮不是已经 158 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经给了出块者 | 不是已经给了出块者 | 不是已经blob费≠执行气（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经策略≠共识（144） |
| 已经 158 bundled | 不是已经 158 bundled | 不是已经1486 bfmkt-notmkt |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1559 basefee-burned not already paid-to-proposer / not already 145 / not already 158-bundled 正式三事（158 余量），必须分开是不是已经给了出块者、是不是已经是不变量 145、是不是已经 158 bundled。可以跳过「烧掉 = MEV 已解决」。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。158 basefee vs tip bundled unbundling 在本页 item 1 启动；续 [`worked-example-bfmkt-notmkt-vs-bundled.md`](worked-example-bfmkt-notmkt-vs-bundled.md)（不变量 1486 item 2）。

## 本页不抄

- 弹性倍数、调价分母、初始基础费、固有 gas 表。
- 怎样抬基础费、怎样排空块、怎样抢排序。
