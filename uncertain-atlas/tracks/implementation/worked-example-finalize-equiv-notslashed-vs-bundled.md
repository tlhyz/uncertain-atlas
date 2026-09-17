# 例：看见可以用 decided_last_commit 和 misbehavior 定奖惩 is not already slashed interchangeable / not already LastCommit +2/3 interchangeable / not already settled interchangeable

**层次**：实现 / 可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事（363 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事（363 余量）/ not 837 finalize-equiv-notslashed interchangeable / not 363 finalize-equiv-vs-gates bundled interchangeable」，不是 Finalize 回包义务 bundled（363），也不是证据上链就已经罚没（21），也不是 VoteInfo 定奖惩（365/830），也不是 Misbehavior 类型就已经罚没（372）。不要另写怎样写 Finalize 回包。

## 官方三件事

1. **看见可以用 `decided_last_commit` 和 `misbehavior` 定奖惩 / 看见有这两列 这份能定奖惩 is not already 已经罚没 interchangeable / 21 slashed interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 837 finalize-equiv-notslashed interchangeable / 836 finalize-equiv-notgates interchangeable / 363 finalize-equiv item 1 等价 interchangeable，也不是已经可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事 bundled（363 item 2 余量） interchangeable / 363 finalize-equiv item 2 interchangeable。**  
   官方写：应用可以用 `FinalizeBlockRequest.decided_last_commit` 和 `FinalizeBlockRequest.misbehavior` 来定验证者的奖惩。看见有这两列，不是已经罚没 interchangeable——本页从 363 item 2 侧钉 not already slashed 单句。363 finalize-equiv vs gates bundled unbundling 在本页 item 2 续。

2. **看见有这两列 / 看见有上一份 commit / 这份能定奖惩 is not already 已经是本头 LastCommit 就已经是本高 +2/3 interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 837 finalize-equiv-notslashed interchangeable / 363 finalize-equiv item 3 必须回四列 interchangeable / 838 finalize-equiv-notchanged interchangeable，也不是已经 VoteInfo 定奖惩 interchangeable / 365 voteinfo / 830 voteinfo-notslashed interchangeable，也不是已经证据上链就已经罚没 interchangeable / 21 slashed interchangeable。**  
   官方把有上一份 commit 和已经是本头 LastCommit 就已经是本高 +2/3 分开——363 bundled 第二件事常与 21 / 365 混成「看见能定奖惩就已经罚没或已经是本头 LastCommit interchangeable」，本页钉 not already LastCommit +2/3 单句。

3. **看见有这两列 / 看见能定奖惩 / 这份能定奖惩 is not already 已经交差 interchangeable，也不是已经 Finalize 回包义务 bundled（363） interchangeable / 837 finalize-equiv-notslashed interchangeable / 836 finalize-equiv-notgates interchangeable，也不是已经 Misbehavior 类型就已经罚没 interchangeable / 372 misbehavior interchangeable。**  
   官方把能定奖惩和已经交差分开。看见能定奖惩，不是已经交差 interchangeable。363 finalize-equiv vs gates bundled unbundling 在本页 item 2 续。

怎样写 Finalize 回包、怎样算奖惩、怎样填四列是规范里的做法，本页不抄。

## 官方为什么这样拆

- **可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed ≠ 21 interchangeable：** 官方把能定奖惩和已经罚没分开。
- **看见有上一份 commit not already LastCommit +2/3 ≠ 已经是本头 LastCommit interchangeable：** 官方把有上一份 commit 和已经是本头 LastCommit 就已经是本高 +2/3 分开。
- **看见能定奖惩 not already settled ≠ 已经交差 interchangeable：** 官方把能定奖惩和已经交差分开；363 finalize-equiv vs gates bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 可以用 decided_last_commit 和 misbehavior 定奖惩 | 不是已经罚没 | 不是证据上链就已经罚没（21） |
| 看见有上一份 commit | 不是已经是本头 LastCommit 就已经是本高 +2/3 | 不是 VoteInfo 定奖惩（365/830） |
| 看见能定奖惩 | 不是已经交差 | 不是 Misbehavior 类型就已经罚没（372） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事（363 余量），必须分开是不是已经罚没、是不是已经是本头 LastCommit 就已经是本高 +2/3、是不是已经交差。可以跳过「看见有这两列就已经罚没」。不要另写怎样写 Finalize 回包。363 finalize-equiv vs gates bundled unbundling 在本页 item 2 续；续 [`worked-example-finalize-equiv-notchanged-vs-bundled.md`](worked-example-finalize-equiv-notchanged-vs-bundled.md)（不变量 838 item 3）。

## 本页不抄

- 怎样写 Finalize 回包、怎样算奖惩、怎样填四列。
- Finalize 回包义务 bundled。那是不变量 363。
- Finalize 等价于 ABCI 1.0 那三步。那是不变量 363 item 1 余量 / 836。
- 证据上链就已经罚没。那是不变量 21。
- VoteInfo 定奖惩。那是不变量 365 / 830。
- Misbehavior 类型就已经罚没。那是不变量 372。
