# 例：看见能读本块 blob 基础费不是已经并成一套气不是已经并成一套气；看见readable blob basefee is not already one gas不是已经是不变量 145；看见能读本块 blob 基础费不是已经并成一套气不是已经是不变量 201

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7516](https://eips.ethereum.org/EIPS/eip-7516)（Final, Core, BLOBBASEFEE instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7516 read-blobbasefee not already one-gas / not already 145-bundled / not already 201 正式三事（219 余量）/ not 1402 bbfee-notone interchangeable / not 219 blobbasefee-vs-basefee bundled interchangeable」，不是 blobbasefee vs basefee bundled（219），也不是已经 blob gas≠普通执行 gas（145），也不是已经 blob 底价≠已并账（201）。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。

## 官方三件事

1. **看见能读本块 blob 基础费不是已经并成一套气 / 看见能读本块 blob 基础费不是已经并成一套气 这份对象 is not already 已经并成一套气 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1402 bbfee-notone interchangeable / 1401 bbfee-not3198 interchangeable，也不是已经 EIP-7516 read-blobbasefee not already one-gas / not already 145-bundled / not already 201 正式三事 bundled（219 item 2 余量） interchangeable / 219 bbfee item 2 interchangeable。**  
   官方把能读本块 blob 基础费不是已经并成一套气和已经并成一套气写成两件。看见能读本块 blob 基础费不是已经并成一套气，不是已经并成一套气。

2. **看见readable blob basefee is not already one gas / 看见能读本块 blob 基础费不是已经并成一套气 / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1402 bbfee-notone interchangeable / 1403 bbfee-not4844 interchangeable，也不是已经 blob gas≠普通执行 gas interchangeable / 145 blob gas≠普通执行 gas interchangeable。**  
   官方把readable blob basefee is not already one gas和已经是不变量 145写成两件。看见readable blob basefee is not already one gas，不是已经是不变量 145。

3. **看见能读本块 blob 基础费不是已经并成一套气 / 看见readable blob basefee is not already one gas / 这份对象 is not already 已经是不变量 201 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1402 bbfee-notone interchangeable / 1401 bbfee-not3198 interchangeable，也不是已经 blob 底价≠已并账 interchangeable / 201 blob 底价≠已并账 interchangeable。**  
   官方把能读本块 blob 基础费不是已经并成一套气和已经是不变量 201写成两件。看见能读本块 blob 基础费不是已经并成一套气，不是已经是不变量 201。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。

## 官方为什么这样拆

- **能读本块 blob 基础费不是已经并成一套气 interchangeable：官方把头上公开的 blob 价和并账写成两件。**
- **看见能读到不是已经是不变量 145。**
- **看见合约读数不是已经是不变量 201。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经并成一套气 | 不是已经并成一套气 | 不是已经blob gas≠普通执行 gas（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经blob 底价≠已并账（201） |
| 已经是不变量 201 | 不是已经是不变量 201 | 不是已经1401 bbfee-not3198 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7516 read-blobbasefee not already one-gas / not already 145-bundled / not already 201 正式三事（219 余量），必须分开是不是已经并成一套气、是不是已经是不变量 145、是不是已经是不变量 201。可以跳过「看见 7516 就已经是 3198」。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。219 BLOBBASEFEE vs BASEFEE bundled unbundling 在本页 item 2 续；续 [`worked-example-bbfee-not4844-vs-bundled.md`](worked-example-bbfee-not4844-vs-bundled.md)（不变量 1403 item 3）。

## 本页不抄

- 操作码号、气价档、测试向量、规范提交哈希。
- 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。
