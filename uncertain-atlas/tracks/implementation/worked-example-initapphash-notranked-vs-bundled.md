# 例：看见 CommitInfo.round 是提交轮 is not already ranked interchangeable / not already slashed interchangeable / not already settled interchangeable

**层次**：实现 / CommitInfo.round not already ranked / not already slashed / not already settled 正式三事（392 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CommitInfo.round not already ranked / not already slashed / not already settled 正式三事（392 余量）/ not 757 initapphash-notranked interchangeable / not 392 initapphash-vs-header bundled interchangeable」，不是 InitChain 回包余栏 bundled（392），也不是 VoteInfo 按投票权降序排就已经进了块（365），也不是 ExtendedCommitInfo.round 就已经是 CommitInfo.round（394/749）。不要另写怎样写 InitChain 回包余栏。

## 官方三件事

1. **看见 CommitInfo `round` 是提交轮 / 看见填了 round / CommitInfo 这份提交轮 is not already 已经按投票权降序排过 interchangeable / 365 voteinfo interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 757 initapphash-notranked interchangeable / 755 initapphash-notheader interchangeable / 392 initapphash item 1 app_hash interchangeable，也不是已经 round not already ranked / not already slashed / not already settled 正式三事 bundled（392 item 3 余量） interchangeable / 392 initapphash item 3 interchangeable。**  
   官方写：`round` 是提交轮，反映上一高度块提议者决定时的那一轮。看见填了 round，不是已经按投票权降序排过 interchangeable——本页从 392 item 3 侧钉 not already ranked 单句。392 initapphash vs header bundled unbundling 在本页 item 3 完成。

2. **看见填了 round / 看见有轮次 / CommitInfo 这份提交轮 is not already 已经按到场定奖惩 interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 757 initapphash-notranked interchangeable / 392 initapphash item 2 Finalize hash interchangeable / 756 initapphash-notknownhash interchangeable，也不是已经 ExtendedCommitInfo.round 就已经是 CommitInfo.round interchangeable / 394 extcommitround / 749 extcommitround-notcommitinfo interchangeable。**  
   官方把提交轮和已经罚没分开——392 bundled 第三件事常与 365 / 394 混成「看见填了 CommitInfo.round 就已经按投票权排过或已经是 ExtendedCommitInfo.round interchangeable」，本页钉 not already slashed 单句。

3. **看见填了 round / 看见能填 / CommitInfo 这份提交轮 is not already 已经交差 interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 757 initapphash-notranked interchangeable / 755 initapphash-notheader interchangeable。**  
   官方把能填 CommitInfo.round 和已经交差分开。看见能填，不是已经交差 interchangeable。392 initapphash vs header bundled unbundling 在本页 item 3 完成。

怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮是规范里的做法，本页不抄。

## 官方为什么这样拆

- **round not already ranked ≠ 365 interchangeable：** 官方把提交轮和票序分开。
- **round not already slashed ≠ 已经罚没 interchangeable：** 官方把有轮次和已经按到场定奖惩分开。
- **round not already settled ≠ 已经交差 interchangeable：** 官方把能填 CommitInfo.round 和已经交差分开；392 initapphash vs header bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CommitInfo.round 是提交轮 | 不是已经按投票权排过（365） | 不是 InitChain 回包 app_hash（755/392 item 1） |
| 看见填了 round | 不是已经罚没 | 不是 ExtendedCommitInfo.round（394/749） |
| 看见能填 | 不是已经交差 | 不是 InitChain 回包余栏 bundled（392） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CommitInfo.round not already ranked / not already slashed / not already settled 正式三事（392 余量），必须分开 round 是不是已经按投票权排过 interchangeable / 365、是不是已经罚没、是不是已经交差。可以跳过「看见填了 CommitInfo.round 就已经按投票权排过」。不要另写怎样写 InitChain 回包余栏。392 initapphash vs header bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮。
- InitChain 回包余栏 bundled。那是不变量 392。
- InitChain 回包 app_hash。那是不变量 392 item 1 余量 / 755。
- Finalize 请求 hash。那是不变量 392 item 2 余量 / 756。
- VoteInfo 按投票权降序排就已经进了块。那是不变量 365。
- ExtendedCommitInfo.round 就已经是 CommitInfo.round。那是不变量 394 / 749。
