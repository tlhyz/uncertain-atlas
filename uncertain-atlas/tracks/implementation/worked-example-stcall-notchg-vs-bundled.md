# 例：看见静态帧里改状态不是已经改成不是已经改成；看见static state change is not already applied不是已经和 CALLCODE 带值同一盏灯；看见静态帧里改状态不是已经改成不是已经是 140 回滚

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-214](https://eips.ethereum.org/EIPS/eip-214)（Final, Core, STATICCALL）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-214 static-state-change not already applied / not already CALLCODE-value / not already 140 正式三事（178 余量）/ not 1385 stcall-notchg interchangeable / not 178 static-vs-view bundled interchangeable」，不是 static vs view bundled（178），也不是已经 自毁≠已删（160），也不是已经 回滚≠烧光（177）。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。

## 官方三件事

1. **看见静态帧里改状态不是已经改成 / 看见静态帧里改状态不是已经改成 这份对象 is not already 已经改成 interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1385 stcall-notchg interchangeable / 1383 stcall-notview interchangeable，也不是已经 EIP-214 static-state-change not already applied / not already CALLCODE-value / not already 140 正式三事 bundled（178 item 3 余量） interchangeable / 178 stcall item 3 interchangeable。**  
   官方把静态帧里改状态不是已经改成和已经改成写成两件。看见静态帧里改状态不是已经改成，不是已经改成。

2. **看见static state change is not already applied / 看见静态帧里改状态不是已经改成 / 这份对象 is not already 已经和 CALLCODE 带值同一盏灯 interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1385 stcall-notchg interchangeable / 1384 stcall-notxfer interchangeable，也不是已经 自毁≠已删 interchangeable / 160 自毁≠已删 interchangeable。**  
   官方把static state change is not already applied和已经和 CALLCODE 带值同一盏灯写成两件。看见static state change is not already applied，不是已经和 CALLCODE 带值同一盏灯。

3. **看见静态帧里改状态不是已经改成 / 看见static state change is not already applied / 这份对象 is not already 已经是 140 回滚 interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1385 stcall-notchg interchangeable / 1383 stcall-notview interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把静态帧里改状态不是已经改成和已经是 140 回滚写成两件。看见静态帧里改状态不是已经改成，不是已经是 140 回滚。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。

## 官方为什么这样拆

- **静态帧里改状态不是已经改成 interchangeable：官方写谁要改就异常。**
- **看见 CALLCODE 带非零值不是已经和普通 CALL 带值同一盏灯。**
- **看见 214 不是已经是 140 回滚。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改成 | 不是已经改成 | 不是已经自毁≠已删（160） |
| 已经和 CALLCODE 带值同一盏灯 | 不是已经和 CALLCODE 带值同一盏灯 | 不是已经回滚≠烧光（177） |
| 已经是 140 回滚 | 不是已经是 140 回滚 | 不是已经1383 stcall-notview |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-214 static-state-change not already applied / not already CALLCODE-value / not already 140 正式三事（178 余量），必须分开是不是已经改成、是不是已经和 CALLCODE 带值同一盏灯、是不是已经是 140 回滚。可以跳过「看见 view 就已经开了静态旗」。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。178 STATICCALL flag vs view bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-211 返回缓冲（232）。

## 本页不抄

- 操作码号、参数个数、例调用。
- 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。
