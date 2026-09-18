# 例：看见没转账的普通调用不是已经是静态帧不是已经打开静态旗；看见zero-value CALL is not already static不是已经只读；看见没转账的普通调用不是已经是静态帧不是已经 214 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-214](https://eips.ethereum.org/EIPS/eip-214)（Final, Core, STATICCALL）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-214 zero-value-CALL not already static-flag / not already readonly / not already 214-bundled 正式三事（178 余量）/ not 1384 stcall-notxfer interchangeable / not 178 static-vs-view bundled interchangeable」，不是 static vs view bundled（178），也不是已经 EIP-140 REVERT（177），也不是已经 DELEGATECALL（233）。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。

## 官方三件事

1. **看见没转账的普通调用不是已经是静态帧 / 看见没转账的普通调用不是已经是静态帧 这份对象 is not already 已经打开静态旗 interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1384 stcall-notxfer interchangeable / 1383 stcall-notview interchangeable，也不是已经 EIP-214 zero-value-CALL not already static-flag / not already readonly / not already 214-bundled 正式三事 bundled（178 item 2 余量） interchangeable / 178 stcall item 2 interchangeable。**  
   官方把没转账的普通调用不是已经是静态帧和已经打开静态旗写成两件。看见没转账的普通调用不是已经是静态帧，不是已经打开静态旗。

2. **看见zero-value CALL is not already static / 看见没转账的普通调用不是已经是静态帧 / 这份对象 is not already 已经只读 interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1384 stcall-notxfer interchangeable / 1385 stcall-notchg interchangeable，也不是已经 EIP-140 REVERT interchangeable / 177 EIP-140 REVERT interchangeable。**  
   官方把zero-value CALL is not already static和已经只读写成两件。看见zero-value CALL is not already static，不是已经只读。

3. **看见没转账的普通调用不是已经是静态帧 / 看见zero-value CALL is not already static / 这份对象 is not already 已经 214 bundled interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1384 stcall-notxfer interchangeable / 1383 stcall-notview interchangeable，也不是已经 DELEGATECALL interchangeable / 233 DELEGATECALL interchangeable。**  
   官方把没转账的普通调用不是已经是静态帧和已经 214 bundled写成两件。看见没转账的普通调用不是已经是静态帧，不是已经 214 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。

## 官方为什么这样拆

- **没转账的普通调用不是已经是静态帧 interchangeable：官方把转账为 0 的 CALL 和打开静态旗分开。**
- **看见没转账不是已经只读。**
- **看见普通调用不是已经 214 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经打开静态旗 | 不是已经打开静态旗 | 不是已经EIP-140 REVERT（177） |
| 已经只读 | 不是已经只读 | 不是已经DELEGATECALL（233） |
| 已经 214 bundled | 不是已经 214 bundled | 不是已经1383 stcall-notview |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-214 zero-value-CALL not already static-flag / not already readonly / not already 214-bundled 正式三事（178 余量），必须分开是不是已经打开静态旗、是不是已经只读、是不是已经 214 bundled。可以跳过「看见 view 就已经开了静态旗」。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。178 STATICCALL flag vs view bundled unbundling 在本页 item 2 续；续 [`worked-example-stcall-notchg-vs-bundled.md`](worked-example-stcall-notchg-vs-bundled.md)（不变量 1385 item 3）。

## 本页不抄

- 操作码号、参数个数、例调用。
- 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。
