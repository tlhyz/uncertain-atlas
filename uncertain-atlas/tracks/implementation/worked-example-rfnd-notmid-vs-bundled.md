# 例：看见退款计数不是已经能在执行当中用不是已经能在执行当中用；看见refund counter is not already mid-exec spendable不是已经是本块实际能烧掉的上限；看见退款计数不是已经能在执行当中用不是已经是不变量 158

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3529](https://eips.ethereum.org/EIPS/eip-3529)（Final, Core, Reduction in refunds）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3529 refund-counter not already mid-exec-spendable / not already gaslimit-cap / not already 158 正式三事（223 余量）/ not 1415 rfnd-notmid interchangeable / not 223 refund-vs-gone bundled interchangeable」，不是 refund vs gone bundled（223），也不是已经 基础费≠小费（158），也不是已经 本笔第一次碰≠已经热（169）。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。

## 官方三件事

1. **看见退款计数不是已经能在执行当中用 / 看见退款计数不是已经能在执行当中用 这份对象 is not already 已经能在执行当中用 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1415 rfnd-notmid interchangeable / 1413 rfnd-notgone interchangeable，也不是已经 EIP-3529 refund-counter not already mid-exec-spendable / not already gaslimit-cap / not already 158 正式三事 bundled（223 item 3 余量） interchangeable / 223 rfnd item 3 interchangeable。**  
   官方把退款计数不是已经能在执行当中用和已经能在执行当中用写成两件。看见退款计数不是已经能在执行当中用，不是已经能在执行当中用。

2. **看见refund counter is not already mid-exec spendable / 看见退款计数不是已经能在执行当中用 / 这份对象 is not already 已经是本块实际能烧掉的上限 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1415 rfnd-notmid interchangeable / 1414 rfnd-not6780 interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把refund counter is not already mid-exec spendable和已经是本块实际能烧掉的上限写成两件。看见refund counter is not already mid-exec spendable，不是已经是本块实际能烧掉的上限。

3. **看见退款计数不是已经能在执行当中用 / 看见refund counter is not already mid-exec spendable / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1415 rfnd-notmid interchangeable / 1413 rfnd-notgone interchangeable，也不是已经 本笔第一次碰≠已经热 interchangeable / 169 本笔第一次碰≠已经热 interchangeable。**  
   官方把退款计数不是已经能在执行当中用和已经是不变量 158写成两件。看见退款计数不是已经能在执行当中用，不是已经是不变量 158。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。

## 官方为什么这样拆

- **退款计数不是已经能在执行当中用 interchangeable：官方写退款只在整笔执行之后结算。**
- **看见账面气限不是已经是本块实际能烧掉的上限。**
- **看见本页不是已经是不变量 158。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经能在执行当中用 | 不是已经能在执行当中用 | 不是已经基础费≠小费（158） |
| 已经是本块实际能烧掉的上限 | 不是已经是本块实际能烧掉的上限 | 不是已经本笔第一次碰≠已经热（169） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经1413 rfnd-notgone |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3529 refund-counter not already mid-exec-spendable / not already gaslimit-cap / not already 158 正式三事（223 余量），必须分开是不是已经能在执行当中用、是不是已经是本块实际能烧掉的上限、是不是已经是不变量 158。可以跳过「看见 3529 就已经没有退款」。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。223 refund vs gone bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：废弃≠已改语义（224）。

## 本页不抄

- 退款比例、气价表、测试向量、百分比。
- 怎样做气代币、怎样留灰、怎样用退款打满一块。
