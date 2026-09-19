# 例：看见烧掉不是MEV已经解决不是已经解决MEV；看见burning is not already MEV solved不是已经更安全；看见烧掉不是MEV已经解决不是已经是不变量 144

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559)（Fee market change for ETH 1.0 chain）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1559 burn not already mev-solved / not already safer / not already 144 正式三事（158 余量）/ not 1487 bfmkt-notmev interchangeable / not 158 basefee-vs-tip bundled interchangeable」，不是 basefee vs tip bundled（158），也不是已经 类型信封≠1559（167），也不是已经 出块者热≠已付给（187）。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。

## 官方三件事

1. **看见烧掉不是MEV已经解决 / 看见烧掉不是MEV已经解决 这份对象 is not already 已经解决MEV interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1487 bfmkt-notmev interchangeable / 1485 bfmkt-notpay interchangeable，也不是已经 EIP-1559 burn not already mev-solved / not already safer / not already 144 正式三事 bundled（158 item 3 余量） interchangeable / 158 bfmkt item 3 interchangeable。**  
   官方把烧掉不是MEV已经解决和已经解决MEV写成两件。看见烧掉不是MEV已经解决，不是已经解决MEV。

2. **看见burning is not already MEV solved / 看见烧掉不是MEV已经解决 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1487 bfmkt-notmev interchangeable / 1486 bfmkt-notmkt interchangeable，也不是已经 类型信封≠1559 interchangeable / 167 类型信封≠1559 interchangeable。**  
   官方把burning is not already MEV solved和已经更安全写成两件。看见burning is not already MEV solved，不是已经更安全。

3. **看见烧掉不是MEV已经解决 / 看见burning is not already MEV solved / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 basefee vs tip bundled（158） interchangeable / 1487 bfmkt-notmev interchangeable / 1485 bfmkt-notpay interchangeable，也不是已经 出块者热≠已付给 interchangeable / 187 出块者热≠已付给 interchangeable。**  
   官方把烧掉不是MEV已经解决和已经是不变量 144写成两件。看见烧掉不是MEV已经解决，不是已经是不变量 144。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。

## 官方为什么这样拆

- **烧掉不是MEV已经解决 interchangeable：官方写降低与 MEV 相关的风险，不是 MEV 已经解决。**
- **看见烧掉不是已经更安全。**
- **看见本页不是已经是不变量 144。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经解决MEV | 不是已经解决MEV | 不是已经类型信封≠1559（167） |
| 已经更安全 | 不是已经更安全 | 不是已经出块者热≠已付给（187） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经1485 bfmkt-notpay |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1559 burn not already mev-solved / not already safer / not already 144 正式三事（158 余量），必须分开是不是已经解决MEV、是不是已经更安全、是不是已经是不变量 144。可以跳过「烧掉 = MEV 已解决」。不要另写 怎样抬基础费、怎样排空块、怎样抢排序。158 basefee vs tip bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：history-window（或其他仍无官方三事的父页）。

## 本页不抄

- 弹性倍数、调价分母、初始基础费、固有 gas 表。
- 怎样抬基础费、怎样排空块、怎样抢排序。
