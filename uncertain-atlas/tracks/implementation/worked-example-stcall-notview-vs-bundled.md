# 例：看见静态帧不是已经是高级语言只读不是已经是高级语言的只读函数；看见static frame is not already view不是已经是编译器 view；看见静态帧不是已经是高级语言只读不是已经 178 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-214](https://eips.ethereum.org/EIPS/eip-214)（Final, Core, STATICCALL）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-214 static-frame not already high-level-view / not already compiler-readonly / not already 178-bundled 正式三事（178 余量）/ not 1383 stcall-notview interchangeable / not 178 static-vs-view bundled interchangeable」，不是 static vs view bundled（178），也不是已经 回滚≠烧光（177），也不是已经 瞬时≠持久（159）。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。

## 官方三件事

1. **看见静态帧不是已经是高级语言只读 / 看见静态帧不是已经是高级语言只读 这份对象 is not already 已经是高级语言的只读函数 interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1383 stcall-notview interchangeable / 1384 stcall-notxfer interchangeable，也不是已经 EIP-214 static-frame not already high-level-view / not already compiler-readonly / not already 178-bundled 正式三事 bundled（178 item 1 余量） interchangeable / 178 stcall item 1 interchangeable。**  
   官方把静态帧不是已经是高级语言只读和已经是高级语言的只读函数写成两件。看见静态帧不是已经是高级语言只读，不是已经是高级语言的只读函数。

2. **看见static frame is not already view / 看见静态帧不是已经是高级语言只读 / 这份对象 is not already 已经是编译器 view interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1383 stcall-notview interchangeable / 1385 stcall-notchg interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把static frame is not already view和已经是编译器 view写成两件。看见static frame is not already view，不是已经是编译器 view。

3. **看见静态帧不是已经是高级语言只读 / 看见static frame is not already view / 这份对象 is not already 已经 178 bundled interchangeable，也不是已经 static vs view bundled（178） interchangeable / 1383 stcall-notview interchangeable / 1384 stcall-notxfer interchangeable，也不是已经 瞬时≠持久 interchangeable / 159 瞬时≠持久 interchangeable。**  
   官方把静态帧不是已经是高级语言只读和已经 178 bundled写成两件。看见静态帧不是已经是高级语言只读，不是已经 178 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。

## 官方为什么这样拆

- **静态帧不是已经是高级语言只读 interchangeable：官方把虚拟机旗和编译器 view 写成两件。**
- **看见只读文案不是已经是编译器 view 已经开旗。**
- **看见静态旋钮不是已经 178 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是高级语言的只读函数 | 不是已经是高级语言的只读函数 | 不是已经回滚≠烧光（177） |
| 已经是编译器 view | 不是已经是编译器 view | 不是已经瞬时≠持久（159） |
| 已经 178 bundled | 不是已经 178 bundled | 不是已经1384 stcall-notxfer |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-214 static-frame not already high-level-view / not already compiler-readonly / not already 178-bundled 正式三事（178 余量），必须分开是不是已经是高级语言的只读函数、是不是已经是编译器 view、是不是已经 178 bundled。可以跳过「看见 view 就已经开了静态旗」。不要另写 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。178 STATICCALL flag vs view bundled unbundling 在本页 item 1 启动；续 [`worked-example-stcall-notxfer-vs-bundled.md`](worked-example-stcall-notxfer-vs-bundled.md)（不变量 1384 item 2）。

## 本页不抄

- 操作码号、参数个数、例调用。
- 怎样把会改状态的被调包进静态帧、怎样靠 CALLCODE 带值。
