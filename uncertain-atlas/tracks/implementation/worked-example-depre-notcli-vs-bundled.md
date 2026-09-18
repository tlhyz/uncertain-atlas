# 例：看见本页不是已经改了客户端不是已经改了客户端；看见this page is not already client-changed不是已经删掉这条指令；看见本页不是已经改了客户端不是已经是 3529

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-6049](https://eips.ethereum.org/EIPS/eip-6049)（Final, Meta, Deprecate SELFDESTRUCT）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-6049 meta-page not already client-changed / not already instruction-removed / not already 3529 正式三事（224 余量）/ not 1417 depre-notcli interchangeable / not 224 deprecate-vs-changed bundled interchangeable」，不是 deprecate vs changed bundled（224），也不是已经 SELFDESTRUCT≠已删（160），也不是已经 退款削减（223）。不要另写 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。

## 官方三件事

1. **看见本页不是已经改了客户端 / 看见本页不是已经改了客户端 这份对象 is not already 已经改了客户端 interchangeable，也不是已经 deprecate vs changed bundled（224） interchangeable / 1417 depre-notcli interchangeable / 1416 depre-notcons interchangeable，也不是已经 EIP-6049 meta-page not already client-changed / not already instruction-removed / not already 3529 正式三事 bundled（224 item 2 余量） interchangeable / 224 depre item 2 interchangeable。**  
   官方把本页不是已经改了客户端和已经改了客户端写成两件。看见本页不是已经改了客户端，不是已经改了客户端。

2. **看见this page is not already client-changed / 看见本页不是已经改了客户端 / 这份对象 is not already 已经删掉这条指令 interchangeable，也不是已经 deprecate vs changed bundled（224） interchangeable / 1417 depre-notcli interchangeable / 1418 depre-notdone interchangeable，也不是已经 SELFDESTRUCT≠已删 interchangeable / 160 SELFDESTRUCT≠已删 interchangeable。**  
   官方把this page is not already client-changed和已经删掉这条指令写成两件。看见this page is not already client-changed，不是已经删掉这条指令。

3. **看见本页不是已经改了客户端 / 看见this page is not already client-changed / 这份对象 is not already 已经是 3529 interchangeable，也不是已经 deprecate vs changed bundled（224） interchangeable / 1417 depre-notcli interchangeable / 1416 depre-notcons interchangeable，也不是已经 退款削减 interchangeable / 223 退款削减 interchangeable。**  
   官方把本页不是已经改了客户端和已经是 3529写成两件。看见本页不是已经改了客户端，不是已经是 3529。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。

## 官方为什么这样拆

- **本页不是已经改了客户端 interchangeable：官方写更新非规范文字，对客户端不适用任何改动。**
- **看见弃用不是已经删掉这条指令。**
- **看见本页不是已经是 3529。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了客户端 | 不是已经改了客户端 | 不是已经SELFDESTRUCT≠已删（160） |
| 已经删掉这条指令 | 不是已经删掉这条指令 | 不是已经退款削减（223） |
| 已经是 3529 | 不是已经是 3529 | 不是已经1416 depre-notcons |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-6049 meta-page not already client-changed / not already instruction-removed / not already 3529 正式三事（224 余量），必须分开是不是已经改了客户端、是不是已经删掉这条指令、是不是已经是 3529。可以跳过「看见 6049 就已经改了行为」。不要另写 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。224 deprecate vs changed bundled unbundling 在本页 item 2 续；续 [`worked-example-depre-notdone-vs-bundled.md`](worked-example-depre-notdone-vs-bundled.md)（不变量 1418 item 3）。

## 本页不抄

- 黄皮书章节号、操作码号、气价。
- 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。
