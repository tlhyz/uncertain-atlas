# 例：看见blob 基础费指令不是已经是执行层基础费指令不是已经是执行层基础费指令；看见BLOBBASEFEE is not already BASEFEE不是已经是不变量 218；看见blob 基础费指令不是已经是执行层基础费指令不是已经 219 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7516](https://eips.ethereum.org/EIPS/eip-7516)（Final, Core, BLOBBASEFEE instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7516 BLOBBASEFEE opcode not already 3198-basefee / not already 218-bundled / not already 219-bundled 正式三事（219 余量）/ not 1401 bbfee-not3198 interchangeable / not 219 blobbasefee-vs-basefee bundled interchangeable」，不是 blobbasefee vs basefee bundled（219），也不是已经 基础费指令≠已改市场（218），也不是已经 基础费≠小费（158）。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。

## 官方三件事

1. **看见blob 基础费指令不是已经是执行层基础费指令 / 看见blob 基础费指令不是已经是执行层基础费指令 这份对象 is not already 已经是执行层基础费指令 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1401 bbfee-not3198 interchangeable / 1402 bbfee-notone interchangeable，也不是已经 EIP-7516 BLOBBASEFEE opcode not already 3198-basefee / not already 218-bundled / not already 219-bundled 正式三事 bundled（219 item 1 余量） interchangeable / 219 bbfee item 1 interchangeable。**  
   官方把blob 基础费指令不是已经是执行层基础费指令和已经是执行层基础费指令写成两件。看见blob 基础费指令不是已经是执行层基础费指令，不是已经是执行层基础费指令。

2. **看见BLOBBASEFEE is not already BASEFEE / 看见blob 基础费指令不是已经是执行层基础费指令 / 这份对象 is not already 已经是不变量 218 interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1401 bbfee-not3198 interchangeable / 1403 bbfee-not4844 interchangeable，也不是已经 基础费指令≠已改市场 interchangeable / 218 基础费指令≠已改市场 interchangeable。**  
   官方把BLOBBASEFEE is not already BASEFEE和已经是不变量 218写成两件。看见BLOBBASEFEE is not already BASEFEE，不是已经是不变量 218。

3. **看见blob 基础费指令不是已经是执行层基础费指令 / 看见BLOBBASEFEE is not already BASEFEE / 这份对象 is not already 已经 219 bundled interchangeable，也不是已经 blobbasefee vs basefee bundled（219） interchangeable / 1401 bbfee-not3198 interchangeable / 1402 bbfee-notone interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把blob 基础费指令不是已经是执行层基础费指令和已经 219 bundled写成两件。看见blob 基础费指令不是已经是执行层基础费指令，不是已经 219 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。

## 官方为什么这样拆

- **blob 基础费指令不是已经是执行层基础费指令 interchangeable：官方写和 3198 一样，只是返回 blob 基础费。**
- **看见能读 blob 价不是已经是不变量 218。**
- **看见读数旋钮不是已经 219 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是执行层基础费指令 | 不是已经是执行层基础费指令 | 不是已经基础费指令≠已改市场（218） |
| 已经是不变量 218 | 不是已经是不变量 218 | 不是已经基础费≠小费（158） |
| 已经 219 bundled | 不是已经 219 bundled | 不是已经1402 bbfee-notone |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7516 BLOBBASEFEE opcode not already 3198-basefee / not already 218-bundled / not already 219-bundled 正式三事（219 余量），必须分开是不是已经是执行层基础费指令、是不是已经是不变量 218、是不是已经 219 bundled。可以跳过「看见 7516 就已经是 3198」。不要另写 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。219 BLOBBASEFEE vs BASEFEE bundled unbundling 在本页 item 1 启动；续 [`worked-example-bbfee-notone-vs-bundled.md`](worked-example-bbfee-notone-vs-bundled.md)（不变量 1402 item 2）。

## 本页不抄

- 操作码号、气价档、测试向量、规范提交哈希。
- 怎样按 blob 价做产品、怎样绕过两套气、怎样改 4844 日程。
