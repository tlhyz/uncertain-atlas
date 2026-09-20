# 例：看见状态里的历史执行哈希不是已经是BLOCKHASH不是已经是BLOCKHASH；看见a state history hash is not already BLOCKHASH不是已经是不变量 156；看见状态里的历史执行哈希不是已经是BLOCKHASH不是已经 195 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)（Serve historical block hashes from state）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.1、L5.1。本页是「EIP-2935 state-hash not already BLOCKHASH / not already 156 / not already 195-bundled 正式三事（195 余量）/ not 1500 hhash-notbh interchangeable / not 195 history-hash-vs-blockhash bundled interchangeable」，不是 history hash vs blockhash bundled（195），也不是已经 父信标根≠当前头（156），也不是已经 PREVRANDAO≠工作量（157）。不要另写 怎样构造系统调用、怎样填环、怎样打见证。

## 官方三件事

1. **看见状态里的历史执行哈希不是已经是BLOCKHASH / 看见状态里的历史执行哈希不是已经是BLOCKHASH 这份对象 is not already 已经是BLOCKHASH interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1500 hhash-notbh interchangeable / 1501 hhash-notfill interchangeable，也不是已经 EIP-2935 state-hash not already BLOCKHASH / not already 156 / not already 195-bundled 正式三事 bundled（195 item 1 余量） interchangeable / 195 hhash item 1 interchangeable。**  
   官方把状态里的历史执行哈希不是已经是BLOCKHASH和已经是BLOCKHASH写成两件。看见状态里的历史执行哈希不是已经是BLOCKHASH，不是已经是BLOCKHASH。

2. **看见a state history hash is not already BLOCKHASH / 看见状态里的历史执行哈希不是已经是BLOCKHASH / 这份对象 is not already 已经是不变量 156 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1500 hhash-notbh interchangeable / 1502 hhash-notsem interchangeable，也不是已经 父信标根≠当前头 interchangeable / 156 父信标根≠当前头 interchangeable。**  
   官方把a state history hash is not already BLOCKHASH和已经是不变量 156写成两件。看见a state history hash is not already BLOCKHASH，不是已经是不变量 156。

3. **看见状态里的历史执行哈希不是已经是BLOCKHASH / 看见a state history hash is not already BLOCKHASH / 这份对象 is not already 已经 195 bundled interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1500 hhash-notbh interchangeable / 1501 hhash-notfill interchangeable，也不是已经 PREVRANDAO≠工作量 interchangeable / 157 PREVRANDAO≠工作量 interchangeable。**  
   官方把状态里的历史执行哈希不是已经是BLOCKHASH和已经 195 bundled写成两件。看见状态里的历史执行哈希不是已经是BLOCKHASH，不是已经 195 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造系统调用、怎样填环、怎样打见证。

## 官方为什么这样拆

- **状态里的历史执行哈希不是已经是BLOCKHASH interchangeable：官方写本页是合约存储，BLOCKHASH 解析机制不动。**
- **看见本页不是已经是不变量 156。**
- **看见状态槽不是已经 195 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是BLOCKHASH | 不是已经是BLOCKHASH | 不是已经父信标根≠当前头（156） |
| 已经是不变量 156 | 不是已经是不变量 156 | 不是已经PREVRANDAO≠工作量（157） |
| 已经 195 bundled | 不是已经 195 bundled | 不是已经1501 hhash-notfill |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2935 state-hash not already BLOCKHASH / not already 156 / not already 195-bundled 正式三事（195 余量），必须分开是不是已经是BLOCKHASH、是不是已经是不变量 156、是不是已经 195 bundled。可以跳过「看见状态槽就已经是 BLOCKHASH」。不要另写 怎样构造系统调用、怎样填环、怎样打见证。195 history-hash vs blockhash bundled unbundling 在本页 item 1 启动；续 [`worked-example-hhash-notfill-vs-bundled.md`](worked-example-hhash-notfill-vs-bundled.md)（不变量 1501 item 2）。

## 本页不抄

- 系统地址、历史合约地址、窗口数字、气限、字节码、部署交易。
- 怎样构造系统调用、怎样填环、怎样打见证。
