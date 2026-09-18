# 例：看见原来值 / 当前值 / 新值不是已经只有当前值不是已经只有当前值；看见three values are not already current-only不是已经是这一上下文第一次写；看见原来值 / 当前值 / 新值不是已经只有当前值不是已经是 2929

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2200](https://eips.ethereum.org/EIPS/eip-2200)（Final, Core, Structured Definitions for Net Gas Metering）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2200 orig-cur-new not already current-only / not already first-write / not already 2929 正式三事（225 余量）/ not 1420 nmet-notcur interchangeable / not 225 net-meter-vs-transient bundled interchangeable」，不是 net meter vs transient bundled（225），也不是已经 本笔第一次碰≠已经热（169），也不是已经 退款削减（223）。不要另写 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。

## 官方三件事

1. **看见原来值 / 当前值 / 新值不是已经只有当前值 / 看见原来值 / 当前值 / 新值不是已经只有当前值 这份对象 is not already 已经只有当前值 interchangeable，也不是已经 net meter vs transient bundled（225） interchangeable / 1420 nmet-notcur interchangeable / 1419 nmet-not1153 interchangeable，也不是已经 EIP-2200 orig-cur-new not already current-only / not already first-write / not already 2929 正式三事 bundled（225 item 2 余量） interchangeable / 225 nmet item 2 interchangeable。**  
   官方把原来值 / 当前值 / 新值不是已经只有当前值和已经只有当前值写成两件。看见原来值 / 当前值 / 新值不是已经只有当前值，不是已经只有当前值。

2. **看见three values are not already current-only / 看见原来值 / 当前值 / 新值不是已经只有当前值 / 这份对象 is not already 已经是这一上下文第一次写 interchangeable，也不是已经 net meter vs transient bundled（225） interchangeable / 1420 nmet-notcur interchangeable / 1421 nmet-notstip interchangeable，也不是已经 本笔第一次碰≠已经热 interchangeable / 169 本笔第一次碰≠已经热 interchangeable。**  
   官方把three values are not already current-only和已经是这一上下文第一次写写成两件。看见three values are not already current-only，不是已经是这一上下文第一次写。

3. **看见原来值 / 当前值 / 新值不是已经只有当前值 / 看见three values are not already current-only / 这份对象 is not already 已经是 2929 interchangeable，也不是已经 net meter vs transient bundled（225） interchangeable / 1420 nmet-notcur interchangeable / 1419 nmet-not1153 interchangeable，也不是已经 退款削减 interchangeable / 223 退款削减 interchangeable。**  
   官方把原来值 / 当前值 / 新值不是已经只有当前值和已经是 2929写成两件。看见原来值 / 当前值 / 新值不是已经只有当前值，不是已经是 2929。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。

## 官方为什么这样拆

- **原来值 / 当前值 / 新值不是已经只有当前值 interchangeable：官方把三值和只谈当前值写成两件。**
- **看见原来值不等于当前值不是已经是这一上下文第一次写。**
- **看见本页不是已经是 2929。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经只有当前值 | 不是已经只有当前值 | 不是已经本笔第一次碰≠已经热（169） |
| 已经是这一上下文第一次写 | 不是已经是这一上下文第一次写 | 不是已经退款削减（223） |
| 已经是 2929 | 不是已经是 2929 | 不是已经1419 nmet-not1153 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2200 orig-cur-new not already current-only / not already first-write / not already 2929 正式三事（225 余量），必须分开是不是已经只有当前值、是不是已经是这一上下文第一次写、是不是已经是 2929。可以跳过「看见 2200 就已经是 1153」。不要另写 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。225 net-meter vs transient bundled unbundling 在本页 item 2 续；续 [`worked-example-nmet-notstip-vs-bundled.md`](worked-example-nmet-notstip-vs-bundled.md)（不变量 1421 item 3）。

## 本页不抄

- 气价名取值、津贴数字、测试向量。
- 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。
