# 例：看见CommitInfo.round 是提交轮不是已经按投票权排过不是已经按投票权排过；看见CommitInfo.round is commit round is not already ordered by voting power不是已经罚没；看见CommitInfo.round 是提交轮不是已经按投票权排过不是已经是 ExtendedCommitInfo.round

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事（445 余量）/ not 1359 cifields-notrnd interchangeable / not 445 cifields-vs-notes bundled interchangeable」，不是 cifields vs notes bundled（445），也不是已经 InitChain 回包 app_hash 就已经是本头 AppHash（392），也不是已经 ExtendedCommitInfo.round 是提交轮（394）。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。

## 官方三件事

1. **看见CommitInfo.round 是提交轮不是已经按投票权排过 / 看见CommitInfo.round 是提交轮不是已经按投票权排过 这份对象 is not already 已经按投票权排过 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1359 cifields-notrnd interchangeable / 1360 cifields-notlst interchangeable，也不是已经 CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事 bundled（445 item 1 余量） interchangeable / 445 cifields item 1 interchangeable。**  
   官方把CommitInfo.round 是提交轮不是已经按投票权排过和已经按投票权排过写成两件。看见CommitInfo.round 是提交轮不是已经按投票权排过，不是已经按投票权排过。

2. **看见CommitInfo.round is commit round is not already ordered by voting power / 看见CommitInfo.round 是提交轮不是已经按投票权排过 / 这份对象 is not already 已经罚没 interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1359 cifields-notrnd interchangeable / 1361 cifields-notnts interchangeable，也不是已经 InitChain 回包 app_hash 就已经是本头 AppHash interchangeable / 392 InitChain 回包 app_hash 就已经是本头 AppHash interchangeable。**  
   官方把CommitInfo.round is commit round is not already ordered by voting power和已经罚没写成两件。看见CommitInfo.round is commit round is not already ordered by voting power，不是已经罚没。

3. **看见CommitInfo.round 是提交轮不是已经按投票权排过 / 看见CommitInfo.round is commit round is not already ordered by voting power / 这份对象 is not already 已经是 ExtendedCommitInfo.round interchangeable，也不是已经 cifields vs notes bundled（445） interchangeable / 1359 cifields-notrnd interchangeable / 1360 cifields-notlst interchangeable，也不是已经 ExtendedCommitInfo.round 是提交轮 interchangeable / 394 ExtendedCommitInfo.round 是提交轮 interchangeable。**  
   官方把CommitInfo.round 是提交轮不是已经按投票权排过和已经是 ExtendedCommitInfo.round写成两件。看见CommitInfo.round 是提交轮不是已经按投票权排过，不是已经是 ExtendedCommitInfo.round。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。

## 官方为什么这样拆

- **CommitInfo.round 是提交轮 不是已经按投票权排过 interchangeable：官方把 Fields 轮次和 Notes 票序分开。**
- **看见有轮次 不是已经罚没：round 不是 block_id_flag。**
- **看见 Process/Finalize 有 CommitInfo.round 不是已经 ExtendedCommitInfo.round interchangeable。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经按投票权排过 | 不是已经按投票权排过 | 不是已经InitChain 回包 app_hash 就已经是本头 AppHash（392） |
| 已经罚没 | 不是已经罚没 | 不是已经ExtendedCommitInfo.round 是提交轮（394） |
| 已经是 ExtendedCommitInfo.round | 不是已经是 ExtendedCommitInfo.round | 不是已经1360 cifields-notlst |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事（445 余量），必须分开是不是已经按投票权排过、是不是已经罚没、是不是已经是 ExtendedCommitInfo.round。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮」。不要另写 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。445 CommitInfo Fields round-and-votes bundled unbundling 在本页 item 1 启动；续 [`worked-example-cifields-notlst-vs-bundled.md`](worked-example-cifields-notlst-vs-bundled.md)（不变量 1360 item 2）。

## 本页不抄

- 怎样写 CommitInfo Fields 栏、怎样填 round、怎样读 votes。
- 怎样填 CommitInfo.round、怎样读 votes 列表、怎样把 Fields 写成 Notes。
