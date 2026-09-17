# 例：看见按投票权降序排 is not already in-block interchangeable / not already settled interchangeable / not already slashed interchangeable

**层次**：实现 / 按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 余量）/ not 832 voteinfo-notinblock interchangeable / not 365 voteinfo-vs-reward bundled interchangeable」，不是 VoteInfo bundled（365），也不是本地 State 就已经进了块（300），也不是必须回四列就已经改了集合（363），也不是证据上链就已经罚没（21）。不要另写怎样写 VoteInfo。

## 官方三件事

1. **看见 `votes` 按投票权降序排、落盘后再从 store 装回 / 看见顺序在 / 这份顺序 is not already 已经进了块 interchangeable / 300 localstate interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 832 voteinfo-notinblock interchangeable / 830 voteinfo-notslashed interchangeable / 365 voteinfo item 1 定奖惩 interchangeable，也不是已经按投票权降序排 not already in-block / not already settled / not already slashed 正式三事 bundled（365 item 3 余量） interchangeable / 365 voteinfo item 3 interchangeable。**  
   官方写：`CommitInfo.votes` 里的 `VoteInfo` 按投票权从高到低排。更新集合的逻辑保证这个顺序。看见排好了，不是已经进了块 interchangeable——本页从 365 item 3 侧钉 not already in-block 单句。365 voteinfo vs reward bundled unbundling 在本页 item 3 完成。

2. **看见顺序在 / 看见从 store 再装 / 这份顺序 is not already 已经交差 interchangeable / 300 localstate interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 832 voteinfo-notinblock interchangeable / 365 voteinfo item 2 抽出 interchangeable / 831 voteinfo-notpubkey interchangeable，也不是已经本地 State 就已经进了块 interchangeable / 300 localstate interchangeable，也不是已经必须回四列就已经改了集合 interchangeable / 363 finresp interchangeable。**  
   官方把从 store 再装和已经交差分开——365 bundled 第三件事常与 300 / 363 混成「看见顺序在就已经进了块或已经交差 interchangeable」，本页钉 not already settled 单句。

3. **看见顺序在 / 看见排好了 / 这份顺序 is not already 已经罚没 interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 832 voteinfo-notinblock interchangeable / 830 voteinfo-notslashed interchangeable，也不是已经证据上链就已经罚没 interchangeable / 21 slashed interchangeable。**  
   官方把排好了和已经罚没分开。看见排好了，不是已经罚没 interchangeable。365 voteinfo vs reward bundled unbundling 在本页 item 3 完成。

怎样编 VoteInfo、怎样排 votes、怎样从 store 再装是规范里的做法，本页不抄。

## 官方为什么这样拆

- **按投票权降序排 not already in-block ≠ 300 interchangeable：** 官方把顺序和已经进规范分开。
- **看见从 store 再装 not already settled ≠ 已经交差 interchangeable：** 官方把从 store 再装和已经交差分开。
- **看见排好了 not already slashed ≠ 已经罚没 interchangeable：** 官方把排好了和已经罚没分开；365 voteinfo vs reward bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 按投票权降序排 | 不是已经进了块（300） | 不是定奖惩（830/365 item 1） |
| 看见从 store 再装 | 不是已经交差 | 不是必须回四列就已经改了集合（363） |
| 看见排好了 | 不是已经罚没 | 不是证据上链就已经罚没（21） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 余量），必须分开是不是已经进了块 interchangeable / 300、是不是已经交差、是不是已经罚没。可以跳过「看见顺序在就已经进了块」。不要另写怎样写 VoteInfo。365 voteinfo vs reward bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 VoteInfo、怎样排 votes、怎样从 store 再装。
- VoteInfo bundled。那是不变量 365。
- VoteInfo 能按到场定奖惩。那是不变量 365 item 1 余量 / 830。
- 本地 State 就已经进了块。那是不变量 300。
- 必须回四列就已经改了集合。那是不变量 363。
