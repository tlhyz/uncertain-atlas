# 例：看见没有立即数不是已经改了跳转目的分析不是已经改了跳转目的分析；看见no immediate is not already jumpdest-changed不是已经共用实现；看见没有立即数不是已经改了跳转目的分析不是已经是 5656

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3855](https://eips.ethereum.org/EIPS/eip-3855)（Final, Core, PUSH0 instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3855 no-immediate not already jumpdest-changed / not already shared-impl / not already 5656 正式三事（217 余量）/ not 1408 psh0-notjump interchangeable / not 217 push0-vs-push1 bundled interchangeable」，不是 push0 vs push1 bundled（217），也不是已经 内存拷（216），也不是已经 initcode 超界（176）。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。

## 官方三件事

1. **看见没有立即数不是已经改了跳转目的分析 / 看见没有立即数不是已经改了跳转目的分析 这份对象 is not already 已经改了跳转目的分析 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1408 psh0-notjump interchangeable / 1407 psh0-notimm interchangeable，也不是已经 EIP-3855 no-immediate not already jumpdest-changed / not already shared-impl / not already 5656 正式三事 bundled（217 item 2 余量） interchangeable / 217 psh0 item 2 interchangeable。**  
   官方把没有立即数不是已经改了跳转目的分析和已经改了跳转目的分析写成两件。看见没有立即数不是已经改了跳转目的分析，不是已经改了跳转目的分析。

2. **看见no immediate is not already jumpdest-changed / 看见没有立即数不是已经改了跳转目的分析 / 这份对象 is not already 已经共用实现 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1408 psh0-notjump interchangeable / 1409 psh0-notold interchangeable，也不是已经 内存拷 interchangeable / 216 内存拷 interchangeable。**  
   官方把no immediate is not already jumpdest-changed和已经共用实现写成两件。看见no immediate is not already jumpdest-changed，不是已经共用实现。

3. **看见没有立即数不是已经改了跳转目的分析 / 看见no immediate is not already jumpdest-changed / 这份对象 is not already 已经是 5656 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1408 psh0-notjump interchangeable / 1407 psh0-notimm interchangeable，也不是已经 initcode 超界 interchangeable / 176 initcode 超界 interchangeable。**  
   官方把没有立即数不是已经改了跳转目的分析和已经是 5656写成两件。看见没有立即数不是已经改了跳转目的分析，不是已经是 5656。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。

## 官方为什么这样拆

- **没有立即数不是已经改了跳转目的分析 interchangeable：官方写跳转目的分析不受影响，因为没有立即数字节。**
- **看见挨着其余压栈码不是已经共用实现。**
- **看见规范编号不是已经是 5656。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了跳转目的分析 | 不是已经改了跳转目的分析 | 不是已经内存拷（216） |
| 已经共用实现 | 不是已经共用实现 | 不是已经initcode 超界（176） |
| 已经是 5656 | 不是已经是 5656 | 不是已经1407 psh0-notimm |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3855 no-immediate not already jumpdest-changed / not already shared-impl / not already 5656 正式三事（217 余量），必须分开是不是已经改了跳转目的分析、是不是已经共用实现、是不是已经是 5656。可以跳过「看见 3855 就已经是带立即数的压 0」。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。217 PUSH0 vs PUSH1 bundled unbundling 在本页 item 2 续；续 [`worked-example-psh0-notold-vs-bundled.md`](worked-example-psh0-notold-vs-bundled.md)（不变量 1409 item 3）。

## 本页不抄

- 操作码号、气价、百分比、块号区间、浪费字节统计、栈深测试向量、规范提交哈希。
- 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。
