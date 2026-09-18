# 例：看见压零指令不是已经是带立即数的压 0不是已经是带立即数的压 0；看见PUSH0 is not already immediate push-0不是已经是不变量 216；看见压零指令不是已经是带立即数的压 0不是已经 217 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3855](https://eips.ethereum.org/EIPS/eip-3855)（Final, Core, PUSH0 instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3855 PUSH0 not already immediate-push0 / not already 216 / not already 217-bundled 正式三事（217 余量）/ not 1407 psh0-notimm interchangeable / not 217 push0-vs-push1 bundled interchangeable」，不是 push0 vs push1 bundled（217），也不是已经 内存拷≠身份预编译（216），也不是已经 数前导零≠已便宜 ZK（208）。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。

## 官方三件事

1. **看见压零指令不是已经是带立即数的压 0 / 看见压零指令不是已经是带立即数的压 0 这份对象 is not already 已经是带立即数的压 0 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1407 psh0-notimm interchangeable / 1408 psh0-notjump interchangeable，也不是已经 EIP-3855 PUSH0 not already immediate-push0 / not already 216 / not already 217-bundled 正式三事 bundled（217 item 1 余量） interchangeable / 217 psh0 item 1 interchangeable。**  
   官方把压零指令不是已经是带立即数的压 0和已经是带立即数的压 0写成两件。看见压零指令不是已经是带立即数的压 0，不是已经是带立即数的压 0。

2. **看见PUSH0 is not already immediate push-0 / 看见压零指令不是已经是带立即数的压 0 / 这份对象 is not already 已经是不变量 216 interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1407 psh0-notimm interchangeable / 1409 psh0-notold interchangeable，也不是已经 内存拷≠身份预编译 interchangeable / 216 内存拷≠身份预编译 interchangeable。**  
   官方把PUSH0 is not already immediate push-0和已经是不变量 216写成两件。看见PUSH0 is not already immediate push-0，不是已经是不变量 216。

3. **看见压零指令不是已经是带立即数的压 0 / 看见PUSH0 is not already immediate push-0 / 这份对象 is not already 已经 217 bundled interchangeable，也不是已经 push0 vs push1 bundled（217） interchangeable / 1407 psh0-notimm interchangeable / 1408 psh0-notjump interchangeable，也不是已经 数前导零≠已便宜 ZK interchangeable / 208 数前导零≠已便宜 ZK interchangeable。**  
   官方把压零指令不是已经是带立即数的压 0和已经 217 bundled写成两件。看见压零指令不是已经是带立即数的压 0，不是已经 217 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。

## 官方为什么这样拆

- **压零指令不是已经是带立即数的压 0 interchangeable：官方把专用常数零和带立即数再压一个零写成两件。**
- **看见能压零不是已经是不变量 216。**
- **看见读数旋钮不是已经 217 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是带立即数的压 0 | 不是已经是带立即数的压 0 | 不是已经内存拷≠身份预编译（216） |
| 已经是不变量 216 | 不是已经是不变量 216 | 不是已经数前导零≠已便宜 ZK（208） |
| 已经 217 bundled | 不是已经 217 bundled | 不是已经1408 psh0-notjump |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3855 PUSH0 not already immediate-push0 / not already 216 / not already 217-bundled 正式三事（217 余量），必须分开是不是已经是带立即数的压 0、是不是已经是不变量 216、是不是已经 217 bundled。可以跳过「看见 3855 就已经是带立即数的压 0」。不要另写 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。217 PUSH0 vs PUSH1 bundled unbundling 在本页 item 1 启动；续 [`worked-example-psh0-notjump-vs-bundled.md`](worked-example-psh0-notjump-vs-bundled.md)（不变量 1408 item 2）。

## 本页不抄

- 操作码号、气价、百分比、块号区间、浪费字节统计、栈深测试向量、规范提交哈希。
- 怎样在旧字节上赌分叉后行为、怎样用上下文指令凑零、怎样改跳转目的分析。
