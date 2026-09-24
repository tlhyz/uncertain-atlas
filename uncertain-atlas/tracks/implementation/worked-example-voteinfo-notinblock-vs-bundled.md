# 例：看见排好了 / 看见从 store 再装 / 看见顺序在 is not already already in-block interchangeable / already settled interchangeable / already slashed interchangeable

**层次**：实现 / 按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量）/ not 844 voteinfo-notinblock interchangeable / not 365 voteinfo bundled interchangeable」，不是 VoteInfo bundled（365），也不是 VoteInfo 能按到场定奖惩不是已经罚没（842 item 1 余量）或从拟议块或已决块抽出不是已经带了公钥（843 item 2 余量）。不要另写怎样写 VoteInfo。

## 官方三件事

规范把 Methods 里 `CommitInfo.votes` 里的 `VoteInfo` 按投票权从高到低排、集合写入 store 时顺序也落盘、造 `CommitInfo` 时从 store 再装集合 和「已经是排好了就已经进了块 interchangeable / 已经是从 store 再装就已经交差 interchangeable / 已经是顺序在就已经罚没 interchangeable / 已经是 voteinfo bundled interchangeable」分开写成三件独立的实现事，不是「看见排好了就已经进了块 interchangeable / 就已经交差 interchangeable / 就已经罚没 interchangeable」一件事：

1. **看见排好了 / 看见 `votes` 按投票权降序排、落盘后再从 store 装回 / 看见按投票权从高到低排 is not already 已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable / 365 voteinfo bundled interchangeable / 300 localstate interchangeable / voteinfo-sold-as-rewarded interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 844 voteinfo-notinblock interchangeable / 365 voteinfo item 3 interchangeable，也不是已经按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事 bundled（365 item 3 余量） interchangeable / 365 voteinfo item 3 interchangeable，也不是已经罚没（842） interchangeable / 843 voteinfo-notpubkey interchangeable / 21 evidence interchangeable，也不是已经本地 State 就已经进了块（300） interchangeable。**  
   官方写：`CommitInfo.votes` 里的 `VoteInfo` 按投票权从高到低排。更新集合的逻辑保证这个顺序。集合写入 store 时顺序也落盘。造 `CommitInfo` 时从 store 再装集合，好保住这份顺序。看见排好了，不是已经进了块。看见排好了，不是已经 in-block interchangeable——365 钉 bundled 三事，本页从 item 3 侧钉 not already in-block 单句。看见 `votes` 按投票权降序排、落盘后再从 store 装回，不是已经 VoteInfo bundled（365） interchangeable——365 钉 bundled，本页钉 item 3 第一件事。看见排好了，不是已经罚没（842） interchangeable——842 另钉 item 1。看见排好了，不是已经从块抽出带了公钥（843） interchangeable——843 另钉 item 2。365 voteinfo-vs-reward bundled unbundling 在本页 item 3 完成。

2. **看见从 store 再装 / 看见造 CommitInfo 时从 store 再装集合 / 看见从 store 装回 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 365 voteinfo bundled interchangeable / 300 localstate interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 844 voteinfo-notinblock interchangeable / 365 voteinfo item 1 到场 interchangeable / 365 voteinfo item 2 抽出 interchangeable，也不是已经按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事 bundled（365 item 3 余量） interchangeable / 365 voteinfo item 3 interchangeable，也不是已经进了块（本页第一件事） interchangeable。**  
   官方写：看见从 store 再装，不是已经交差。看见造 CommitInfo 时从 store 再装集合，不是已经 settled interchangeable——本页钉 not already settled 单句。看见从 store 装回，不是已经进了块（本页第一件事） interchangeable——三件事分开钉。365 voteinfo-vs-reward bundled unbundling 在本页 item 3 完成。

3. **看见顺序在 / 看见顺序落盘 / 看见保住这份顺序 is not already 已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable / 365 voteinfo bundled interchangeable / 33 fourgates interchangeable，也不是已经 VoteInfo bundled（365） interchangeable / 844 voteinfo-notinblock interchangeable / 365 voteinfo item 1 / 365 voteinfo item 2，也不是已经按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事 bundled（365 item 3 余量） interchangeable / 365 voteinfo item 3 interchangeable，也不是已经进了块（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见顺序在，不是已经罚没。看见顺序落盘，不是已经 slashed interchangeable——本页钉 not already slashed 单句。看见保住这份顺序，不是已经交差（本页第二件事） interchangeable——三件事分开钉。365 voteinfo-vs-reward bundled unbundling 在本页 item 3 完成。

怎样编 `VoteInfo`、怎样排 `votes`、怎样从 store 再装是规范里的做法，本页不抄。VoteInfo bundled（365）、VoteInfo 能按到场定奖惩不是已经罚没（365 item 1 余量 / 842）、从拟议块或已决块抽出不是已经带了公钥（365 item 2 余量 / 843）、必须回四列就已经改了集合（363）、Validator 用 address 认人就已经带了公钥（364）、本地 State 就已经进了块（300）是另外那套，本页不抄。

## 官方为什么这样拆

- **排好了 not already in-block ≠ 365 / 300 interchangeable：** 官方把排好了和已经进了块分开。
- **从 store 再装 not already settled ≠ 已经交差 interchangeable：** 官方把从 store 再装和已经交差分开。
- **顺序在 not already slashed ≠ 已经罚没 interchangeable：** 官方把顺序在和已经罚没分开；365 voteinfo-vs-reward bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 排好了 | 不是 already in-block | 不是本地 State 就已经进了块 alone（300） |
| 从 store 再装 | 不是 already settled | 不是有这列 already slashed alone（842） |
| 顺序在 | 不是 already slashed | 不是从块抽出 already pubkey alone（843） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量），必须分开排好了 是不是 already in-block interchangeable / 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable、从 store 再装 是不是 already settled interchangeable、顺序在 是不是 already slashed interchangeable。可以跳过「看见排好了就已经进了块 interchangeable / 就已经交差 interchangeable / 就已经罚没 interchangeable」。不要另写怎样写 VoteInfo。365 voteinfo-vs-reward bundled unbundling 在本页 item 3 完成（842 + 843 + 844）。

## 本页不抄

- 怎样编 `VoteInfo`、怎样排 `votes`、怎样从 store 再装。
- VoteInfo bundled。那是不变量 365。
- VoteInfo 能按到场定奖惩不是已经罚没。那是不变量 365 item 1 余量 / 842。
- 从拟议块或已决块抽出不是已经带了公钥。那是不变量 365 item 2 余量 / 843。
- 必须回四列就已经改了集合。那是不变量 363。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- 本地 State 就已经进了块。那是不变量 300。
