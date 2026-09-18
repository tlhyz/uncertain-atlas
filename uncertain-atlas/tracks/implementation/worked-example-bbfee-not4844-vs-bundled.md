# 例：看见跑 EVM 前就已经有这个数不是已经改了 4844 日程不是已经改了 4844 日程；看见pre-EVM value is not already 4844-changed不是已经改了费用市场；看见跑 EVM 前就已经有这个数不是已经改了 4844 日程不是已经是 7918 底价规则

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7516](https://eips.ethereum.org/EIPS/eip-7516)（Final, Core, BLOBBASEFEE instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7516 pre-evm-value not already 4844-changed / not already market-changed / not already 7918 正式三事（219 余量）/ not 1403 bbfee-not4844 interchangeable / not 219 blobbasefee-vs-basefee bundled interchangeable」，不是 blobbasefee vs basefee bundled（219），也不是已经 EIP-3198 BASEFEE（218），也不是已经 blob 底价规则（201）。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。

## 官方三件事

1. **看见跑 EVM 前就已经有这个数不是已经改了 4844 日程 / 看见跑 EVM 前就已经有这个数不是已经改了 4844 日程 这份对象 is not already 已经改了 4844 日程 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1403 bbfee-not4844 interchangeable / 1401 bbfee-not3198 interchangeable，也不是已经 EIP-7516 pre-evm-value not already 4844-changed / not already market-changed / not already 7918 正式三事 bundled（219 item 3 余量） interchangeable / 219 bbfee item 3 interchangeable。**  
   官方把跑 EVM 前就已经有这个数不是已经改了 4844 日程和已经改了 4844 日程写成两件。看见跑 EVM 前就已经有这个数不是已经改了 4844 日程，不是已经改了 4844 日程。

2. **看见pre-EVM value is not already 4844-changed / 看见跑 EVM 前就已经有这个数不是已经改了 4844 日程 / 这份对象 is not already 已经改了费用市场 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1403 bbfee-not4844 interchangeable / 1402 bbfee-notone interchangeable，也不是已经 EIP-3198 BASEFEE interchangeable / 218 EIP-3198 BASEFEE interchangeable。**  
   官方把pre-EVM value is not already 4844-changed和已经改了费用市场写成两件。看见pre-EVM value is not already 4844-changed，不是已经改了费用市场。

3. **看见跑 EVM 前就已经有这个数不是已经改了 4844 日程 / 看见pre-EVM value is not already 4844-changed / 这份对象 is not already 已经是 7918 底价规则 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1403 bbfee-not4844 interchangeable / 1401 bbfee-not3198 interchangeable，也不是已经 blob 底价规则 interchangeable / 201 blob 底价规则 interchangeable。**  
   官方把跑 EVM 前就已经有这个数不是已经改了 4844 日程和已经是 7918 底价规则写成两件。看见跑 EVM 前就已经有这个数不是已经改了 4844 日程，不是已经是 7918 底价规则。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。

## 官方为什么这样拆

- **跑 EVM 前就已经有这个数不是已经改了 4844 日程 interchangeable：官方写处理 blob 交易本来就要用，不额外改日程。**
- **看见动机写记账不是已经改了费用市场。**
- **看见本页不是已经是 7918 底价规则。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了 4844 日程 | 不是已经改了 4844 日程 | 不是已经EIP-3198 BASEFEE（218） |
| 已经改了费用市场 | 不是已经改了费用市场 | 不是已经blob 底价规则（201） |
| 已经是 7918 底价规则 | 不是已经是 7918 底价规则 | 不是已经1401 bbfee-not3198 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7516 pre-evm-value not already 4844-changed / not already market-changed / not already 7918 正式三事（219 余量），必须分开是不是已经改了 4844 日程、是不是已经改了费用市场、是不是已经是 7918 底价规则。可以跳过「看见 7516 就已经是 3198」。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。219 BLOBBASEFEE vs BASEFEE bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-145 SHIFT（231）。

## 本页不抄

- 操作码号、气价档、测试向量、规范提交哈希。
- 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。
