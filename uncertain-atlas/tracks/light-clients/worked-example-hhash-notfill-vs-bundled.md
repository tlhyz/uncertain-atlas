# 例：看见系统写入父哈希不是已经填满窗口不是已经填满窗口；看见a system write of the parent hash is not already a full window不是已经是不变量 169；看见系统写入父哈希不是已经填满窗口不是已经是不变量 157

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)（Serve historical block hashes from state）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.1、L5.1。本页是「EIP-2935 sys-write not already window-full / not already 169 / not already 157 正式三事（195 余量）/ not 1501 hhash-notfill interchangeable / not 195 history-hash-vs-blockhash bundled interchangeable」，不是 history hash vs blockhash bundled（195），也不是已经 第一次≠已热（169），也不是已经 PREVRANDAO≠工作量（157）。不要另写 怎样构造系统调用、怎样填环、怎样打见证。

## 官方三件事

1. **看见系统写入父哈希不是已经填满窗口 / 看见系统写入父哈希不是已经填满窗口 这份对象 is not already 已经填满窗口 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1501 hhash-notfill interchangeable / 1500 hhash-notbh interchangeable，也不是已经 EIP-2935 sys-write not already window-full / not already 169 / not already 157 正式三事 bundled（195 item 2 余量） interchangeable / 195 hhash item 2 interchangeable。**  
   官方把系统写入父哈希不是已经填满窗口和已经填满窗口写成两件。看见系统写入父哈希不是已经填满窗口，不是已经填满窗口。

2. **看见a system write of the parent hash is not already a full window / 看见系统写入父哈希不是已经填满窗口 / 这份对象 is not already 已经是不变量 169 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1501 hhash-notfill interchangeable / 1502 hhash-notsem interchangeable，也不是已经 第一次≠已热 interchangeable / 169 第一次≠已热 interchangeable。**  
   官方把a system write of the parent hash is not already a full window和已经是不变量 169写成两件。看见a system write of the parent hash is not already a full window，不是已经是不变量 169。

3. **看见系统写入父哈希不是已经填满窗口 / 看见a system write of the parent hash is not already a full window / 这份对象 is not already 已经是不变量 157 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1501 hhash-notfill interchangeable / 1500 hhash-notbh interchangeable，也不是已经 PREVRANDAO≠工作量 interchangeable / 157 PREVRANDAO≠工作量 interchangeable。**  
   官方把系统写入父哈希不是已经填满窗口和已经是不变量 157写成两件。看见系统写入父哈希不是已经填满窗口，不是已经是不变量 157。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造系统调用、怎样填环、怎样打见证。

## 官方为什么这样拆

- **系统写入父哈希不是已经填满窗口 interchangeable：官方写激活后要等一整窗，分叉块之前没有更早的。**
- **看见本页不是已经是不变量 169。**
- **看见本页不是已经是不变量 157。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经填满窗口 | 不是已经填满窗口 | 不是已经第一次≠已热（169） |
| 已经是不变量 169 | 不是已经是不变量 169 | 不是已经PREVRANDAO≠工作量（157） |
| 已经是不变量 157 | 不是已经是不变量 157 | 不是已经1500 hhash-notbh |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2935 sys-write not already window-full / not already 169 / not already 157 正式三事（195 余量），必须分开是不是已经填满窗口、是不是已经是不变量 169、是不是已经是不变量 157。可以跳过「看见状态槽就已经是 BLOCKHASH」。不要另写 怎样构造系统调用、怎样填环、怎样打见证。195 history-hash vs blockhash bundled unbundling 在本页 item 2 续；续 [`worked-example-hhash-notsem-vs-bundled.md`](worked-example-hhash-notsem-vs-bundled.md)（不变量 1502 item 3）。

## 本页不抄

- 系统地址、历史合约地址、窗口数字、气限、字节码、部署交易。
- 怎样构造系统调用、怎样填环、怎样打见证。
