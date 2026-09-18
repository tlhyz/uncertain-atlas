# 例：看见已经部署碰巧用了这个字节不是行为已经不变不是行为已经不变；看见old byte is not already unchanged不是已经是常数零；看见已经部署碰巧用了这个字节不是行为已经不变不是已经是不变量 208

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3855](https://eips.ethereum.org/EIPS/eip-3855)（Final, Core, PUSH0 instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3855 old-byte not already unchanged / not already context-zero / not already 208 正式三事（217 余量）/ not 1409 psh0-notold interchangeable / not 217 push0-vs-push1 bundled interchangeable」，不是 push0 vs push1 bundled（217），也不是已经 数前导零（208），也不是已经 保留首字节（188）。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。

## 官方三件事

1. **看见已经部署碰巧用了这个字节不是行为已经不变 / 看见已经部署碰巧用了这个字节不是行为已经不变 这份对象 is not already 行为已经不变 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1409 psh0-notold interchangeable / 1407 psh0-notimm interchangeable，也不是已经 EIP-3855 old-byte not already unchanged / not already context-zero / not already 208 正式三事 bundled（217 item 3 余量） interchangeable / 217 psh0 item 3 interchangeable。**  
   官方把已经部署碰巧用了这个字节不是行为已经不变和行为已经不变写成两件。看见已经部署碰巧用了这个字节不是行为已经不变，不是行为已经不变。

2. **看见old byte is not already unchanged / 看见已经部署碰巧用了这个字节不是行为已经不变 / 这份对象 is not already 已经是常数零 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1409 psh0-notold interchangeable / 1408 psh0-notjump interchangeable，也不是已经 数前导零 interchangeable / 208 数前导零 interchangeable。**  
   官方把old byte is not already unchanged和已经是常数零写成两件。看见old byte is not already unchanged，不是已经是常数零。

3. **看见已经部署碰巧用了这个字节不是行为已经不变 / 看见old byte is not already unchanged / 这份对象 is not already 已经是不变量 208 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1409 psh0-notold interchangeable / 1407 psh0-notimm interchangeable，也不是已经 保留首字节 interchangeable / 188 保留首字节 interchangeable。**  
   官方把已经部署碰巧用了这个字节不是行为已经不变和已经是不变量 208写成两件。看见已经部署碰巧用了这个字节不是行为已经不变，不是已经是不变量 208。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。

## 官方为什么这样拆

- **已经部署碰巧用了这个字节不是行为已经不变 interchangeable：官方写分叉后行为可能变。**
- **看见用上下文相关指令凑零不是已经是常数零。**
- **看见本页不是已经是不变量 208。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 行为已经不变 | 不是行为已经不变 | 不是已经数前导零（208） |
| 已经是常数零 | 不是已经是常数零 | 不是已经保留首字节（188） |
| 已经是不变量 208 | 不是已经是不变量 208 | 不是已经1407 psh0-notimm |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3855 old-byte not already unchanged / not already context-zero / not already 208 正式三事（217 余量），必须分开是不是行为已经不变、是不是已经是常数零、是不是已经是不变量 208。可以跳过「看见 3855 就已经是带立即数的压 0」。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。217 PUSH0 vs PUSH1 bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-5656 MCOPY（216）。

## 本页不抄

- 操作码号、气价、百分比、块号区间、浪费字节统计、栈深测试向量、规范提交哈希。
- 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。
