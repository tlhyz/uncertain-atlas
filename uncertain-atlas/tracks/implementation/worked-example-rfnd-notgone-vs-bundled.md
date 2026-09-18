# 例：看见退款削减不是已经没有退款不是已经没有退款；看见refund cut is not already no refunds不是已经重写 2200；看见退款削减不是已经没有退款不是已经 223 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3529](https://eips.ethereum.org/EIPS/eip-3529)（Final, Core, Reduction in refunds）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3529 refund-cut not already no-refund / not already 2200-rewritten / not already 223-bundled 正式三事（223 余量）/ not 1413 rfnd-notgone interchangeable / not 223 refund-vs-gone bundled interchangeable」，不是 refund vs gone bundled（223），也不是已经 后来自毁≠已删户（160），也不是已经 基础费≠小费（158）。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。

## 官方三件事

1. **看见退款削减不是已经没有退款 / 看见退款削减不是已经没有退款 这份对象 is not already 已经没有退款 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1413 rfnd-notgone interchangeable / 1414 rfnd-not6780 interchangeable，也不是已经 EIP-3529 refund-cut not already no-refund / not already 2200-rewritten / not already 223-bundled 正式三事 bundled（223 item 1 余量） interchangeable / 223 rfnd item 1 interchangeable。**  
   官方把退款削减不是已经没有退款和已经没有退款写成两件。看见退款削减不是已经没有退款，不是已经没有退款。

2. **看见refund cut is not already no refunds / 看见退款削减不是已经没有退款 / 这份对象 is not already 已经重写 2200 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1413 rfnd-notgone interchangeable / 1415 rfnd-notmid interchangeable，也不是已经 后来自毁≠已删户 interchangeable / 160 后来自毁≠已删户 interchangeable。**  
   官方把refund cut is not already no refunds和已经重写 2200写成两件。看见refund cut is not already no refunds，不是已经重写 2200。

3. **看见退款削减不是已经没有退款 / 看见refund cut is not already no refunds / 这份对象 is not already 已经 223 bundled interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1413 rfnd-notgone interchangeable / 1414 rfnd-not6780 interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把退款削减不是已经没有退款和已经 223 bundled写成两件。看见退款削减不是已经没有退款，不是已经 223 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。

## 官方为什么这样拆

- **退款削减不是已经没有退款 interchangeable：官方把清零退款削薄和已经没有退款写成两件。**
- **看见只动一档不是已经重写 2200。**
- **看见读数旋钮不是已经 223 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经没有退款 | 不是已经没有退款 | 不是已经后来自毁≠已删户（160） |
| 已经重写 2200 | 不是已经重写 2200 | 不是已经基础费≠小费（158） |
| 已经 223 bundled | 不是已经 223 bundled | 不是已经1414 rfnd-not6780 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3529 refund-cut not already no-refund / not already 2200-rewritten / not already 223-bundled 正式三事（223 余量），必须分开是不是已经没有退款、是不是已经重写 2200、是不是已经 223 bundled。可以跳过「看见 3529 就已经没有退款」。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。223 refund vs gone bundled unbundling 在本页 item 1 启动；续 [`worked-example-rfnd-not6780-vs-bundled.md`](worked-example-rfnd-not6780-vs-bundled.md)（不变量 1414 item 2）。

## 本页不抄

- 退款比例、气价表、测试向量、百分比。
- 怎样做气代币、怎样留灰、怎样用退款打满一块。
