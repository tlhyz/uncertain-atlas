# 例：看见有效余额还能在本纪元变不是种子已知就已经排完不是已经排完；看见balances still moving is not already a finished schedule不是已经是不变量 196；看见有效余额还能在本纪元变不是种子已知就已经排完不是已经是不变量 27

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7917](https://eips.ethereum.org/EIPS/eip-7917)（Deterministic proposer lookahead）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7917 balance-still-moves not already scheduled / not already 196 / not already 27 正式三事（205 余量）/ not 1483 lkah-notbal interchangeable / not 205 lookahead-vs-randao bundled interchangeable」，不是 lookahead vs randao bundled（205），也不是已经 有效余额上限≠已取消最低激活（196），也不是已经 排序权必须点名（27）。不要另写 怎样打磨有效余额。

## 官方三件事

1. **看见有效余额还能在本纪元变不是种子已知就已经排完 / 看见有效余额还能在本纪元变不是种子已知就已经排完 这份对象 is not already 已经排完 interchangeable，也不是已经 lookahead vs randao bundled（205） interchangeable / 1483 lkah-notbal interchangeable / 1482 lkah-notlock interchangeable，也不是已经 EIP-7917 balance-still-moves not already scheduled / not already 196 / not already 27 正式三事 bundled（205 item 2 余量） interchangeable / 205 lkah item 2 interchangeable。**  
   官方把有效余额还能在本纪元变不是种子已知就已经排完和已经排完写成两件。看见有效余额还能在本纪元变不是种子已知就已经排完，不是已经排完。

2. **看见balances still moving is not already a finished schedule / 看见有效余额还能在本纪元变不是种子已知就已经排完 / 这份对象 is not already 已经是不变量 196 interchangeable，也不是已经 lookahead vs randao bundled（205） interchangeable / 1483 lkah-notbal interchangeable / 1484 lkah-notpc interchangeable，也不是已经 有效余额上限≠已取消最低激活 interchangeable / 196 有效余额上限≠已取消最低激活 interchangeable。**  
   官方把balances still moving is not already a finished schedule和已经是不变量 196写成两件。看见balances still moving is not already a finished schedule，不是已经是不变量 196。

3. **看见有效余额还能在本纪元变不是种子已知就已经排完 / 看见balances still moving is not already a finished schedule / 这份对象 is not already 已经是不变量 27 interchangeable，也不是已经 lookahead vs randao bundled（205） interchangeable / 1483 lkah-notbal interchangeable / 1482 lkah-notlock interchangeable，也不是已经 排序权必须点名 interchangeable / 27 排序权必须点名 interchangeable。**  
   官方把有效余额还能在本纪元变不是种子已知就已经排完和已经是不变量 27写成两件。看见有效余额还能在本纪元变不是种子已知就已经排完，不是已经是不变量 27。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样打磨有效余额。

## 官方为什么这样拆

- **有效余额还能在本纪元变不是种子已知就已经排完 interchangeable：官方写有效余额正是 N+1 纪元选人的输入，本纪元还能变。**
- **看见本页不是已经是不变量 196。**
- **看见本页不是已经是不变量 27。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经排完 | 不是已经排完 | 不是已经有效余额上限≠已取消最低激活（196） |
| 已经是不变量 196 | 不是已经是不变量 196 | 不是已经排序权必须点名（27） |
| 已经是不变量 27 | 不是已经是不变量 27 | 不是已经1482 lkah-notlock |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7917 balance-still-moves not already scheduled / not already 196 / not already 27 正式三事（205 余量），必须分开是不是已经排完、是不是已经是不变量 196、是不是已经是不变量 27。可以跳过「看见 7917 就已经锁死下一纪元出块人」。不要另写 怎样打磨有效余额。205 lookahead vs randao bundled unbundling 在本页 item 2 续；续 [`worked-example-lkah-notpc-vs-bundled.md`](worked-example-lkah-notpc-vs-bundled.md)（不变量 1484 item 3）。

## 本页不抄

- 种子前瞻纪元数、有效余额台阶、每纪元槽数、向量长度。
- 怎样打磨有效余额。
