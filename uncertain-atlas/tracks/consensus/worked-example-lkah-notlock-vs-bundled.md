# 例：看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程不是已经锁死下一纪元出块日程；看见known RANDAO seed is not already a locked proposer schedule不是已经是不变量 157；看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程不是已经 205 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7917](https://eips.ethereum.org/EIPS/eip-7917)（Deterministic proposer lookahead）。  
**对应课文**：[L5.2](../../courses/level-05-ethereum/L05-M02-el-cl-finality.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7917 seed-known not already schedule-locked / not already 157 / not already 205-bundled 正式三事（205 余量）/ not 1482 lkah-notlock interchangeable / not 205 lookahead-vs-randao bundled interchangeable」，不是 lookahead vs randao bundled（205），也不是已经 PREVRANDAO≠无偏骰子（157），也不是已经 有效余额上限≠已取消最低激活（196）。不要另写 怎样打磨有效余额。

## 官方三件事

1. **看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程 / 看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程 这份对象 is not already 已经锁死下一纪元出块日程 interchangeable，也不是已经 lookahead vs randao bundled（205） interchangeable / 1482 lkah-notlock interchangeable / 1483 lkah-notbal interchangeable，也不是已经 EIP-7917 seed-known not already schedule-locked / not already 157 / not already 205-bundled 正式三事 bundled（205 item 1 余量） interchangeable / 205 lkah item 1 interchangeable。**  
   官方把RANDAO种子已经提前知道不是已经锁死下一纪元出块日程和已经锁死下一纪元出块日程写成两件。看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程，不是已经锁死下一纪元出块日程。

2. **看见known RANDAO seed is not already a locked proposer schedule / 看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程 / 这份对象 is not already 已经是不变量 157 interchangeable，也不是已经 lookahead vs randao bundled（205） interchangeable / 1482 lkah-notlock interchangeable / 1484 lkah-notpc interchangeable，也不是已经 PREVRANDAO≠无偏骰子 interchangeable / 157 PREVRANDAO≠无偏骰子 interchangeable。**  
   官方把known RANDAO seed is not already a locked proposer schedule和已经是不变量 157写成两件。看见known RANDAO seed is not already a locked proposer schedule，不是已经是不变量 157。

3. **看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程 / 看见known RANDAO seed is not already a locked proposer schedule / 这份对象 is not already 已经 205 bundled interchangeable，也不是已经 lookahead vs randao bundled（205） interchangeable / 1482 lkah-notlock interchangeable / 1483 lkah-notbal interchangeable，也不是已经 有效余额上限≠已取消最低激活 interchangeable / 196 有效余额上限≠已取消最低激活 interchangeable。**  
   官方把RANDAO种子已经提前知道不是已经锁死下一纪元出块日程和已经 205 bundled写成两件。看见RANDAO种子已经提前知道不是已经锁死下一纪元出块日程，不是已经 205 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样打磨有效余额。

## 官方为什么这样拆

- **RANDAO种子已经提前知道不是已经锁死下一纪元出块日程 interchangeable：官方写种子至少提前一截就能确定，但 N+1 日程并不能从当时状态完全预知。**
- **看见本页不是已经是不变量 157。**
- **看见读数旋钮不是已经 205 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经锁死下一纪元出块日程 | 不是已经锁死下一纪元出块日程 | 不是已经PREVRANDAO≠无偏骰子（157） |
| 已经是不变量 157 | 不是已经是不变量 157 | 不是已经有效余额上限≠已取消最低激活（196） |
| 已经 205 bundled | 不是已经 205 bundled | 不是已经1483 lkah-notbal |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7917 seed-known not already schedule-locked / not already 157 / not already 205-bundled 正式三事（205 余量），必须分开是不是已经锁死下一纪元出块日程、是不是已经是不变量 157、是不是已经 205 bundled。可以跳过「看见 7917 就已经锁死下一纪元出块人」。不要另写 怎样打磨有效余额。205 lookahead vs randao bundled unbundling 在本页 item 1 启动；续 [`worked-example-lkah-notbal-vs-bundled.md`](worked-example-lkah-notbal-vs-bundled.md)（不变量 1483 item 2）。

## 本页不抄

- 种子前瞻纪元数、有效余额台阶、每纪元槽数、向量长度。
- 怎样打磨有效余额。
