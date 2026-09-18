# 例：看见父作用域发送者传到子作用域不是已经是普通 CALL不是已经是普通 CALL；看见parent sender to child is not already CALL不是已经有 CALL 那笔津贴；看见父作用域发送者传到子作用域不是已经是普通 CALL不是已经因此创建账户

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7](https://eips.ethereum.org/EIPS/eip-7)（Final, Core, Homestead, DELEGATECALL）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7 parent-sender not already CALL / not already stipend / not already creates-account 正式三事（233 余量）/ not 1378 dcall-notcall interchangeable / not 233 delegatecall-vs-callcode bundled interchangeable」，不是 delegatecall vs callcode bundled（233），也不是已经 静态帧≠view（178），也不是已经 返回缓冲≠已是内存（232）。不要另写 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。

## 官方三件事

1. **看见父作用域发送者传到子作用域不是已经是普通 CALL / 看见父作用域发送者传到子作用域不是已经是普通 CALL 这份对象 is not already 已经是普通 CALL interchangeable，也不是已经 delegatecall vs callcode bundled（233） interchangeable / 1378 dcall-notcall interchangeable / 1377 dcall-notcode interchangeable，也不是已经 EIP-7 parent-sender not already CALL / not already stipend / not already creates-account 正式三事 bundled（233 item 2 余量） interchangeable / 233 dcall item 2 interchangeable。**  
   官方把父作用域发送者传到子作用域不是已经是普通 CALL和已经是普通 CALL写成两件。看见父作用域发送者传到子作用域不是已经是普通 CALL，不是已经是普通 CALL。

2. **看见parent sender to child is not already CALL / 看见父作用域发送者传到子作用域不是已经是普通 CALL / 这份对象 is not already 已经有 CALL 那笔津贴 interchangeable，也不是已经 delegatecall vs callcode bundled（233） interchangeable / 1378 dcall-notcall interchangeable / 1379 dcall-not7702 interchangeable，也不是已经 静态帧≠view interchangeable / 178 静态帧≠view interchangeable。**  
   官方把parent sender to child is not already CALL和已经有 CALL 那笔津贴写成两件。看见parent sender to child is not already CALL，不是已经有 CALL 那笔津贴。

3. **看见父作用域发送者传到子作用域不是已经是普通 CALL / 看见parent sender to child is not already CALL / 这份对象 is not already 已经因此创建账户 interchangeable，也不是已经 delegatecall vs callcode bundled（233） interchangeable / 1378 dcall-notcall interchangeable / 1377 dcall-notcode interchangeable，也不是已经 返回缓冲≠已是内存 interchangeable / 232 返回缓冲≠已是内存 interchangeable。**  
   官方把父作用域发送者传到子作用域不是已经是普通 CALL和已经因此创建账户写成两件。看见父作用域发送者传到子作用域不是已经是普通 CALL，不是已经因此创建账户。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。

## 官方为什么这样拆

- **父作用域发送者传到子作用域不是已经是普通 CALL interchangeable：官方把传到子作用域和换发送者的 CALL 分开。**
- **看见同一发送者不是已经有 CALL 那笔津贴。**
- **看见本页不是已经因此创建账户。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是普通 CALL | 不是已经是普通 CALL | 不是已经静态帧≠view（178） |
| 已经有 CALL 那笔津贴 | 不是已经有 CALL 那笔津贴 | 不是已经返回缓冲≠已是内存（232） |
| 已经因此创建账户 | 不是已经因此创建账户 | 不是已经1377 dcall-notcode |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 parent-sender not already CALL / not already stipend / not already creates-account 正式三事（233 余量），必须分开是不是已经是普通 CALL、是不是已经有 CALL 那笔津贴、是不是已经因此创建账户。可以跳过「看见委托调用就已经是 CALLCODE」。不要另写 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。233 DELEGATECALL four objects bundled unbundling 在本页 item 2 续；续 [`worked-example-dcall-not7702-vs-bundled.md`](worked-example-dcall-not7702-vs-bundled.md)（不变量 1379 item 3）。

## 本页不抄

- 操作码号、操作数表、分叉块号、深度上限数字。
- 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。
