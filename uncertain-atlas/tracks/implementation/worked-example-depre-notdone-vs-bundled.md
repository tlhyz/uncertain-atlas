# 例：看见「以后可能变」不是已经变了不是已经变了；看见later-may-change is not already changed不是已经是不变量 160；看见「以后可能变」不是已经变了不是已经是不变量 223

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-6049](https://eips.ethereum.org/EIPS/eip-6049)（Final, Meta, Deprecate SELFDESTRUCT）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-6049 later-may-change not already changed / not already 160 / not already 223 正式三事（224 余量）/ not 1418 depre-notdone interchangeable / not 224 deprecate-vs-changed bundled interchangeable」，不是 deprecate vs changed bundled（224），也不是已经 6780 自毁语义（160），也不是已经 3529 退款（223）。不要另写 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。

## 官方三件事

1. **看见「以后可能变」不是已经变了 / 看见「以后可能变」不是已经变了 这份对象 is not already 已经变了 interchangeable，也不是已经 deprecate vs changed bundled（224） interchangeable / 1418 depre-notdone interchangeable / 1416 depre-notcons interchangeable，也不是已经 EIP-6049 later-may-change not already changed / not already 160 / not already 223 正式三事 bundled（224 item 3 余量） interchangeable / 224 depre item 3 interchangeable。**  
   官方把「以后可能变」不是已经变了和已经变了写成两件。看见「以后可能变」不是已经变了，不是已经变了。

2. **看见later-may-change is not already changed / 看见「以后可能变」不是已经变了 / 这份对象 is not already 已经是不变量 160 interchangeable，也不是已经 deprecate vs changed bundled（224） interchangeable / 1418 depre-notdone interchangeable / 1417 depre-notcli interchangeable，也不是已经 6780 自毁语义 interchangeable / 160 6780 自毁语义 interchangeable。**  
   官方把later-may-change is not already changed和已经是不变量 160写成两件。看见later-may-change is not already changed，不是已经是不变量 160。

3. **看见「以后可能变」不是已经变了 / 看见later-may-change is not already changed / 这份对象 is not already 已经是不变量 223 interchangeable，也不是已经 deprecate vs changed bundled（224） interchangeable / 1418 depre-notdone interchangeable / 1416 depre-notcons interchangeable，也不是已经 3529 退款 interchangeable / 223 3529 退款 interchangeable。**  
   官方把「以后可能变」不是已经变了和已经是不变量 223写成两件。看见「以后可能变」不是已经变了，不是已经是不变量 223。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。

## 官方为什么这样拆

- **「以后可能变」不是已经变了 interchangeable：官方写讨论还在进行，共识是会改点什么，不是已经改完。**
- **看见本页不是已经是不变量 160。**
- **看见本页不是已经是不变量 223。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经变了 | 不是已经变了 | 不是已经6780 自毁语义（160） |
| 已经是不变量 160 | 不是已经是不变量 160 | 不是已经3529 退款（223） |
| 已经是不变量 223 | 不是已经是不变量 223 | 不是已经1416 depre-notcons |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-6049 later-may-change not already changed / not already 160 / not already 223 正式三事（224 余量），必须分开是不是已经变了、是不是已经是不变量 160、是不是已经是不变量 223。可以跳过「看见 6049 就已经改了行为」。不要另写 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。224 deprecate vs changed bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：净计量≠瞬时存储（225）。

## 本页不抄

- 黄皮书章节号、操作码号、气价。
- 怎样继续用自毁、怎样迁合约、怎样实现以后那次破坏性改动。
