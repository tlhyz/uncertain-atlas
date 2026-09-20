# 例：看见委托调用不是已经是 CALLCODE不是已经是 CALLCODE；看见DELEGATECALL is not already CALLCODE不是已经是同一发送者的 CALLCODE；看见委托调用不是已经是 CALLCODE不是已经 Homestead 委托 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7](https://eips.ethereum.org/EIPS/eip-7)（Final, Core, Homestead, DELEGATECALL）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7 DELEGATECALL not already CALLCODE / not already same-sender-CALLCODE / not already 233-bundled 正式三事（233 余量）/ not 1377 dcall-notcode interchangeable / not 233 delegatecall-vs-callcode bundled interchangeable」，不是 delegatecall vs callcode bundled（233），也不是已经 正确兑现委托≠预编译信任已改（119），也不是已经 授权名单≠已委托（190）。不要另写 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。

## 官方三件事

1. **看见委托调用不是已经是 CALLCODE / 看见委托调用不是已经是 CALLCODE 这份对象 is not already 已经是 CALLCODE interchangeable，也不是已经 delegatecall vs callcode bundled（233） interchangeable / 1377 dcall-notcode interchangeable / 1378 dcall-notcall interchangeable，也不是已经 EIP-7 DELEGATECALL not already CALLCODE / not already same-sender-CALLCODE / not already 233-bundled 正式三事 bundled（233 item 1 余量） interchangeable / 233 dcall item 1 interchangeable。**  
   官方把委托调用不是已经是 CALLCODE和已经是 CALLCODE写成两件。看见委托调用不是已经是 CALLCODE，不是已经是 CALLCODE。

2. **看见DELEGATECALL is not already CALLCODE / 看见委托调用不是已经是 CALLCODE / 这份对象 is not already 已经是同一发送者的 CALLCODE interchangeable，也不是已经 delegatecall vs callcode bundled（233） interchangeable / 1377 dcall-notcode interchangeable / 1379 dcall-not7702 interchangeable，也不是已经 正确兑现委托≠预编译信任已改 interchangeable / 119 正确兑现委托≠预编译信任已改 interchangeable。**  
   官方把DELEGATECALL is not already CALLCODE和已经是同一发送者的 CALLCODE写成两件。看见DELEGATECALL is not already CALLCODE，不是已经是同一发送者的 CALLCODE。

3. **看见委托调用不是已经是 CALLCODE / 看见DELEGATECALL is not already CALLCODE / 这份对象 is not already 已经 Homestead 委托 bundled interchangeable，也不是已经 delegatecall vs callcode bundled（233） interchangeable / 1377 dcall-notcode interchangeable / 1378 dcall-notcall interchangeable，也不是已经 授权名单≠已委托 interchangeable / 190 授权名单≠已委托 interchangeable。**  
   官方把委托调用不是已经是 CALLCODE和已经 Homestead 委托 bundled写成两件。看见委托调用不是已经是 CALLCODE，不是已经 Homestead 委托 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。

## 官方为什么这样拆

- **委托调用不是已经是 CALLCODE interchangeable：官方把新指令和 CALLCODE 写成两件。**
- **看见委托调用不是已经是同一发送者的 CALLCODE。**
- **看见委托调用旋钮不是已经 Homestead 委托 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 CALLCODE | 不是已经是 CALLCODE | 不是已经正确兑现委托≠预编译信任已改（119） |
| 已经是同一发送者的 CALLCODE | 不是已经是同一发送者的 CALLCODE | 不是已经授权名单≠已委托（190） |
| 已经 Homestead 委托 bundled | 不是已经 Homestead 委托 bundled | 不是已经1378 dcall-notcall |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL not already CALLCODE / not already same-sender-CALLCODE / not already 233-bundled 正式三事（233 余量），必须分开是不是已经是 CALLCODE、是不是已经是同一发送者的 CALLCODE、是不是已经 Homestead 委托 bundled。可以跳过「看见委托调用就已经是 CALLCODE」。不要另写 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。233 DELEGATECALL four objects bundled unbundling 在本页 item 1 启动；续 [`worked-example-dcall-notcall-vs-bundled.md`](worked-example-dcall-notcall-vs-bundled.md)（不变量 1378 item 2）。

## 本页不抄

- 操作码号、操作数表、分叉块号、深度上限数字。
- 怎样做可变代码源、怎样拆代码绕过计量墙、怎样靠调用数据复刻发送者。
