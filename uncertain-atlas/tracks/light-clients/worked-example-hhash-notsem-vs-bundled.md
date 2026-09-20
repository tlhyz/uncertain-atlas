# 例：看见合约能查更长窗口不是已经改了操作码语义不是已经改了操作码语义；看见a longer contract window is not already an opcode change不是已经是不变量 156；看见合约能查更长窗口不是已经改了操作码语义不是已经是不变量 207

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)（Serve historical block hashes from state）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.1、L5.1。本页是「EIP-2935 longer-contract not already opcode-changed / not already 156 / not already 207 正式三事（195 余量）/ not 1502 hhash-notsem interchangeable / not 195 history-hash-vs-blockhash bundled interchangeable」，不是 history hash vs blockhash bundled（195），也不是已经 父信标根≠当前头（156），也不是已经 对等窗≠已改共识（207）。不要另写 怎样构造系统调用、怎样填环、怎样打见证。

## 官方三件事

1. **看见合约能查更长窗口不是已经改了操作码语义 / 看见合约能查更长窗口不是已经改了操作码语义 这份对象 is not already 已经改了操作码语义 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1502 hhash-notsem interchangeable / 1500 hhash-notbh interchangeable，也不是已经 EIP-2935 longer-contract not already opcode-changed / not already 156 / not already 207 正式三事 bundled（195 item 3 余量） interchangeable / 195 hhash item 3 interchangeable。**  
   官方把合约能查更长窗口不是已经改了操作码语义和已经改了操作码语义写成两件。看见合约能查更长窗口不是已经改了操作码语义，不是已经改了操作码语义。

2. **看见a longer contract window is not already an opcode change / 看见合约能查更长窗口不是已经改了操作码语义 / 这份对象 is not already 已经是不变量 156 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1502 hhash-notsem interchangeable / 1501 hhash-notfill interchangeable，也不是已经 父信标根≠当前头 interchangeable / 156 父信标根≠当前头 interchangeable。**  
   官方把a longer contract window is not already an opcode change和已经是不变量 156写成两件。看见a longer contract window is not already an opcode change，不是已经是不变量 156。

3. **看见合约能查更长窗口不是已经改了操作码语义 / 看见a longer contract window is not already an opcode change / 这份对象 is not already 已经是不变量 207 interchangeable，也不是已经 history hash vs blockhash bundled（195） interchangeable / 1502 hhash-notsem interchangeable / 1500 hhash-notbh interchangeable，也不是已经 对等窗≠已改共识 interchangeable / 207 对等窗≠已改共识 interchangeable。**  
   官方把合约能查更长窗口不是已经改了操作码语义和已经是不变量 207写成两件。看见合约能查更长窗口不是已经改了操作码语义，不是已经是不变量 207。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造系统调用、怎样填环、怎样打见证。

## 官方为什么这样拆

- **合约能查更长窗口不是已经改了操作码语义 interchangeable：官方写拉长 BLOCKHASH 窗口才是语义变更。**
- **看见本页不是已经是不变量 156。**
- **看见本页不是已经是不变量 207。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了操作码语义 | 不是已经改了操作码语义 | 不是已经父信标根≠当前头（156） |
| 已经是不变量 156 | 不是已经是不变量 156 | 不是已经对等窗≠已改共识（207） |
| 已经是不变量 207 | 不是已经是不变量 207 | 不是已经1500 hhash-notbh |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2935 longer-contract not already opcode-changed / not already 156 / not already 207 正式三事（195 余量），必须分开是不是已经改了操作码语义、是不是已经是不变量 156、是不是已经是不变量 207。可以跳过「看见状态槽就已经是 BLOCKHASH」。不要另写 怎样构造系统调用、怎样填环、怎样打见证。195 history-hash vs blockhash bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：bpo-vs-hardfork（209）。

## 本页不抄

- 系统地址、历史合约地址、窗口数字、气限、字节码、部署交易。
- 怎样构造系统调用、怎样填环、怎样打见证。
