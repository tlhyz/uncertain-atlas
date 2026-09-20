# 例：看见返回的运行时代码超界不是已经是 initcode 超界不是已经是 initcode 超界；看见returned-code bound is not already initcode bound不是已经是 3860；看见返回的运行时代码超界不是已经是 initcode 超界不是已经 185 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-170](https://eips.ethereum.org/EIPS/eip-170)（Final, Core, Contract code size limit）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-170 returned-bound not already initcode-bound / not already 3860 / not already 185-bundled 正式三事（185 余量）/ not 1440 retc-notinit interchangeable / not 185 returned-vs-initcode bundled interchangeable」，不是 returned vs initcode bundled（185），也不是已经 initcode≠运行时代码（176），也不是已经 保留首字节≠已是对象格式（188）。不要另写 怎样造超长返回代码。

## 官方三件事

1. **看见返回的运行时代码超界不是已经是 initcode 超界 / 看见返回的运行时代码超界不是已经是 initcode 超界 这份对象 is not already 已经是 initcode 超界 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1440 retc-notinit interchangeable / 1441 retc-nottx interchangeable，也不是已经 EIP-170 returned-bound not already initcode-bound / not already 3860 / not already 185-bundled 正式三事 bundled（185 item 1 余量） interchangeable / 185 retc item 1 interchangeable。**  
   官方把返回的运行时代码超界不是已经是 initcode 超界和已经是 initcode 超界写成两件。看见返回的运行时代码超界不是已经是 initcode 超界，不是已经是 initcode 超界。

2. **看见returned-code bound is not already initcode bound / 看见返回的运行时代码超界不是已经是 initcode 超界 / 这份对象 is not already 已经是 3860 interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1440 retc-notinit interchangeable / 1442 retc-notfree interchangeable，也不是已经 initcode≠运行时代码 interchangeable / 176 initcode≠运行时代码 interchangeable。**  
   官方把returned-code bound is not already initcode bound和已经是 3860写成两件。看见returned-code bound is not already initcode bound，不是已经是 3860。

3. **看见返回的运行时代码超界不是已经是 initcode 超界 / 看见returned-code bound is not already initcode bound / 这份对象 is not already 已经 185 bundled interchangeable，也不是已经 returned vs initcode bundled（185） interchangeable / 1440 retc-notinit interchangeable / 1441 retc-nottx interchangeable，也不是已经 保留首字节≠已是对象格式 interchangeable / 188 保留首字节≠已是对象格式 interchangeable。**  
   官方把返回的运行时代码超界不是已经是 initcode 超界和已经 185 bundled写成两件。看见返回的运行时代码超界不是已经是 initcode 超界，不是已经 185 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造超长返回代码。

## 官方为什么这样拆

- **返回的运行时代码超界不是已经是 initcode 超界 interchangeable：官方写本页管创建结束要存上链的返回代码，initcode 界是后来的 3860。**
- **看见本页不是已经是 3860。**
- **看见读数旋钮不是已经 185 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 initcode 超界 | 不是已经是 initcode 超界 | 不是已经initcode≠运行时代码（176） |
| 已经是 3860 | 不是已经是 3860 | 不是已经保留首字节≠已是对象格式（188） |
| 已经 185 bundled | 不是已经 185 bundled | 不是已经1441 retc-nottx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-170 returned-bound not already initcode-bound / not already 3860 / not already 185-bundled 正式三事（185 余量），必须分开是不是已经是 initcode 超界、是不是已经是 3860、是不是已经 185 bundled。可以跳过「规范 170 就已经是不变量 170」。不要另写 怎样造超长返回代码。185 returned vs initcode bundled unbundling 在本页 item 1 启动；续 [`worked-example-retc-nottx-vs-bundled.md`](worked-example-retc-nottx-vs-bundled.md)（不变量 1441 item 2）。

## 本页不抄

- 上限字节、分叉高度、链号、气价表。
- 怎样造超长返回代码。
