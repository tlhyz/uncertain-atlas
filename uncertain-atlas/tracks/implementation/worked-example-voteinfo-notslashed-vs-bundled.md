# 例：看见 VoteInfo 能按到场定奖惩 is not already slashed interchangeable / not already settled interchangeable / not already decided_last_commit computed interchangeable

**层次**：实现 / VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事（365 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事（365 余量）/ not 830 voteinfo-notslashed interchangeable / not 365 voteinfo-vs-reward bundled interchangeable」，不是 VoteInfo bundled（365），也不是证据上链就已经罚没（21），也不是 Misbehavior.type 就已经罚没（372/809），也不是 total_voting_power 就已经按到场定奖惩（372/811）。不要另写怎样写 VoteInfo。

## 官方三件事

1. **看见 VoteInfo 标明上一块有没有签、能按到场定奖惩 / 看见有 `block_id_flag` / 这份奖惩 is not already 已经罚没 interchangeable / 21 slashed interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 830 voteinfo-notslashed interchangeable / 831 voteinfo-notpubkey interchangeable / 365 voteinfo item 2 抽出 interchangeable，也不是已经 VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事 bundled（365 item 1 余量） interchangeable / 365 voteinfo item 1 interchangeable。**  
   官方写：`VoteInfo` 标明验证者有没有签上一块，好按到场定奖惩。看见有这列，不是已经罚没 interchangeable——本页从 365 item 1 侧钉 not already slashed 单句。365 voteinfo vs reward bundled unbundling 在本页 item 1 启动。

2. **看见有 `block_id_flag` / 看见能定奖惩 / 这份奖惩 is not already 已经交差 interchangeable / 21 slashed interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 830 voteinfo-notslashed interchangeable / 365 voteinfo item 3 降序 interchangeable / 832 voteinfo-notinblock interchangeable，也不是已经 Misbehavior.type 就已经罚没 interchangeable / 372 misbehavior / 809 misbehavior-notslashed interchangeable，也不是已经 total_voting_power 就已经按到场定奖惩 interchangeable / 372 misbehavior / 811 misbehavior-notreward interchangeable。**  
   官方把能定奖惩和已经交差分开——365 bundled 第一件事常与 21 / 372 混成「看见 CommitInfo 里有票就已经罚没或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见有 `block_id_flag` / 看见能定奖惩 / 这份奖惩 is not already 已经是应用已经用 decided_last_commit 算完 interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 830 voteinfo-notslashed interchangeable / 831 voteinfo-notpubkey interchangeable，也不是已经必须回四列就已经改了集合 interchangeable / 363 finresp interchangeable。**  
   官方把能定奖惩和已经用 decided_last_commit 算完分开。看见能定奖惩，不是已经算完 interchangeable。365 voteinfo vs reward bundled unbundling 在本页 item 1 启动。

怎样编 VoteInfo、怎样排 votes、怎样从 store 再装是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VoteInfo 定奖惩 not already slashed ≠ 21 interchangeable：** 官方把能定奖惩和已经罚没分开。
- **看见能定奖惩 not already settled ≠ 已经交差 interchangeable：** 官方把能定奖惩和已经交差分开。
- **看见能定奖惩 not already decided_last_commit computed ≠ 已经算完 interchangeable：** 官方把能定奖惩和已经用 decided_last_commit 算完分开；365 voteinfo vs reward bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VoteInfo 能按到场定奖惩 | 不是已经罚没（21） | 不是从块抽出（831/365 item 2） |
| 看见能定奖惩 | 不是已经交差 | 不是 Misbehavior.type 就已经罚没（372/809） |
| 看见有 block_id_flag | 不是已经用 decided_last_commit 算完 | 不是必须回四列就已经改了集合（363） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事（365 余量），必须分开是不是已经罚没 interchangeable / 21、是不是已经交差、是不是已经用 decided_last_commit 算完。可以跳过「看见有 block_id_flag 就已经罚没」。不要另写怎样写 VoteInfo。365 voteinfo vs reward bundled unbundling 在本页 item 1 启动；续 [`worked-example-voteinfo-notpubkey-vs-bundled.md`](worked-example-voteinfo-notpubkey-vs-bundled.md)（不变量 831 item 2）。

## 本页不抄

- 怎样编 VoteInfo、怎样排 votes、怎样从 store 再装。
- VoteInfo bundled。那是不变量 365。
- 从拟议块或已决块抽出。那是不变量 365 item 2 余量 / 831。
- 证据上链就已经罚没。那是不变量 21。
- Misbehavior.type 就已经罚没。那是不变量 372 / 809。
