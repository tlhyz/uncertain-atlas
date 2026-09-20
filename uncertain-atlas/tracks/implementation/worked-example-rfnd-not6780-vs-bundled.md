# 例：看见去掉自毁退款不是已经改了自毁语义不是已经改了自毁语义；看见drop selfdestruct refund is not already 6780不是已经是不变量 160；看见去掉自毁退款不是已经改了自毁语义不是已经是 1559

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3529](https://eips.ethereum.org/EIPS/eip-3529)（Final, Core, Reduction in refunds）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3529 drop-selfdestruct-refund not already 6780-semantics / not already 160 / not already 1559 正式三事（223 余量）/ not 1414 rfnd-not6780 interchangeable / not 223 refund-vs-gone bundled interchangeable」，不是 refund vs gone bundled（223），也不是已经 SELFDESTRUCT≠已删（160），也不是已经 瞬时存储≠持久存储（159）。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。

## 官方三件事

1. **看见去掉自毁退款不是已经改了自毁语义 / 看见去掉自毁退款不是已经改了自毁语义 这份对象 is not already 已经改了自毁语义 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1414 rfnd-not6780 interchangeable / 1413 rfnd-notgone interchangeable，也不是已经 EIP-3529 drop-selfdestruct-refund not already 6780-semantics / not already 160 / not already 1559 正式三事 bundled（223 item 2 余量） interchangeable / 223 rfnd item 2 interchangeable。**  
   官方把去掉自毁退款不是已经改了自毁语义和已经改了自毁语义写成两件。看见去掉自毁退款不是已经改了自毁语义，不是已经改了自毁语义。

2. **看见drop selfdestruct refund is not already 6780 / 看见去掉自毁退款不是已经改了自毁语义 / 这份对象 is not already 已经是不变量 160 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1414 rfnd-not6780 interchangeable / 1415 rfnd-notmid interchangeable，也不是已经 SELFDESTRUCT≠已删 interchangeable / 160 SELFDESTRUCT≠已删 interchangeable。**  
   官方把drop selfdestruct refund is not already 6780和已经是不变量 160写成两件。看见drop selfdestruct refund is not already 6780，不是已经是不变量 160。

3. **看见去掉自毁退款不是已经改了自毁语义 / 看见drop selfdestruct refund is not already 6780 / 这份对象 is not already 已经是 1559 interchangeable，也不是已经 refund vs gone bundled（223） interchangeable / 1414 rfnd-not6780 interchangeable / 1413 rfnd-notgone interchangeable，也不是已经 瞬时存储≠持久存储 interchangeable / 159 瞬时存储≠持久存储 interchangeable。**  
   官方把去掉自毁退款不是已经改了自毁语义和已经是 1559写成两件。看见去掉自毁退款不是已经改了自毁语义，不是已经是 1559。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。

## 官方为什么这样拆

- **去掉自毁退款不是已经改了自毁语义 interchangeable：官方只拿掉自毁那笔退款，不是已经按 6780 改语义。**
- **看见本页不是已经是不变量 160。**
- **看见本页不是已经是 1559。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了自毁语义 | 不是已经改了自毁语义 | 不是已经SELFDESTRUCT≠已删（160） |
| 已经是不变量 160 | 不是已经是不变量 160 | 不是已经瞬时存储≠持久存储（159） |
| 已经是 1559 | 不是已经是 1559 | 不是已经1413 rfnd-notgone |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3529 drop-selfdestruct-refund not already 6780-semantics / not already 160 / not already 1559 正式三事（223 余量），必须分开是不是已经改了自毁语义、是不是已经是不变量 160、是不是已经是 1559。可以跳过「看见 3529 就已经没有退款」。不要另写 怎样做气代币、怎样留灰、怎样用退款打满一块。223 refund vs gone bundled unbundling 在本页 item 2 续；续 [`worked-example-rfnd-notmid-vs-bundled.md`](worked-example-rfnd-notmid-vs-bundled.md)（不变量 1415 item 3）。

## 本页不抄

- 退款比例、气价表、测试向量、百分比。
- 怎样做气代币、怎样留灰、怎样用退款打满一块。
