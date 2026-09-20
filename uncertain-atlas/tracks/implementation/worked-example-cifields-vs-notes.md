# 例：看见 CommitInfo.round 是提交轮不是已经按投票权排过；看见 CommitInfo.votes 是上一验证者集合里各人的投票信息不是已经进了块；看见 Fields 栏描述 round 和 votes 不是已经是 CommitInfo Notes 那套票序话

**层次**：实现 / CommitInfo Fields 栏正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CommitInfo.round 是提交轮不是已经按投票权排过 / CommitInfo.votes 是上一验证者集合里各人的投票信息不是已经进了块 / Fields 栏描述 round 和 votes 不是已经是 CommitInfo Notes 那套票序话」，不是 InitChain 回包 app_hash 就已经是本头 AppHash，也不是 Notes 里 votes 按投票权降序排就已经进了块。不要另写怎样写 CommitInfo Fields 栏。

## 官方三件事

规范把 CommitInfo Fields 里 `round` 是提交轮、`votes` 是上一验证者集合里各人的投票信息、Fields 栏和 Notes 分开写写成三件独立的实现事，不是「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮、已经按投票权排好、已经进了块」一件事：

1. **看见 `CommitInfo.round` 是提交轮 / 看见填了 round 不是已经按投票权排过，也不是已经罚没。**  
   官方写：`round` is Commit round. Reflects the round at which the block proposer decided in the previous height. 看见填了 round，不是已经按投票权降序排过。看见有轮次，不是已经按到场定奖惩。看见 Process / Finalize 里有 `CommitInfo.round`，不是已经 ExtendedCommitInfo.round  interchangeable。
2. **看见 `CommitInfo.votes` 是上一验证者集合里各人的投票信息 / 看见填了 votes 不是已经进了块，也不是已经交差。**  
   官方写：`votes` is List of validators' addresses in the last validator set with their voting information. 看见有 `VoteInfo` 列表，不是已经写进 last_commit。看见有投票信息，不是已经按 Notes 里 engine/store 排序那种已经进了块。看见 Process / Finalize 里有 `CommitInfo.votes`，不是已经 typically extracted from proposed or decided block 就已经交差。
3. **看见 Fields 栏描述 round 和 votes / 看见有 Fields 不是已经是 CommitInfo Notes 那套票序话就已经是同一句。**  
   官方把 Fields 表和 Notes 分开写。Fields 只描述 round 含义和 votes 列表内容。Notes 另写 votes 按投票权降序排、引擎保证并落盘、造 CommitInfo 时从 store 再装。看见 Fields 栏，不是已经 Notes 里 The validator set is loaded from the store when building the CommitInfo 那种路径就代替本页。看见 round + votes 都在，不是已经可以用不变量 444 代替本页 Fields 栏。

怎样写 CommitInfo Fields 栏、怎样填 round、怎样读 votes 是规范里的做法，本页不抄。InitChain 回包 app_hash 是起步应用哈希就已经是本头 AppHash 是不变量 392 的另一切片，CommitInfo Notes 票序正式三事是不变量 444，本页不抄。

## 官方为什么这样拆

- **CommitInfo.round 是提交轮 ≠ 已经按投票权排过 / 已经罚没：** 官方把提交轮和 Notes 票序分开。
- **CommitInfo.votes 是上一验证者集合里各人的投票信息 ≠ 已经进了块 / 已经交差：** 官方把 Fields 里 votes 列表含义和已经写进块分开。
- **Fields 栏 ≠ 已经是 CommitInfo Notes 那套票序话：** 官方把 Fields 表和 Notes 分开写，也把本页和 ExtendedCommitInfo.round 是提交轮（394）分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CommitInfo.round 是提交轮 | 不是已经按投票权排过 | 不是 InitChain 回包 app_hash 就已经是本头 AppHash（392） |
| CommitInfo.votes 是上一验证者集合里各人的投票信息 | 不是已经进了块 | 不是 VoteInfo 按投票权降序排就已经进了块（444 Notes） |
| Fields 栏描述 round 和 votes | 不是已经是 Notes 那套票序话 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮、已经按投票权排好、已经进了块」，必须分开 CommitInfo.round 是提交轮是不是已经按投票权排过 / 已经罚没、CommitInfo.votes 是上一验证者集合里各人的投票信息是不是已经进了块 / 已经交差、Fields 栏描述 round 和 votes 是不是已经是 CommitInfo Notes 那套票序话就已经是同一句。可以跳过「看见 Process / Finalize 里有 CommitInfo 就已经填了提交轮」。445 CommitInfo Fields round-and-votes bundled unbundling 完成（1359 item 1 / 1360 item 2 / 1361 item 3）；精读 [`worked-example-cifields-notrnd-vs-bundled.md`](worked-example-cifields-notrnd-vs-bundled.md)（不变量 1359 item 1）、[`worked-example-cifields-notlst-vs-bundled.md`](worked-example-cifields-notlst-vs-bundled.md)（不变量 1360 item 2）、[`worked-example-cifields-notnts-vs-bundled.md`](worked-example-cifields-notnts-vs-bundled.md)（不变量 1361 item 3）。不要另写怎样写 CommitInfo Fields 栏。

## 本页不抄

- 怎样写 CommitInfo Fields 栏、怎样填 round、怎样读 votes。
- InitChain 回包 app_hash 是起步应用哈希。那是不变量 392 的 InitChain 切片，不是本页 Fields 栏。
- CommitInfo Notes 票序正式三事。那是不变量 444。
- VoteInfo 能按到场定奖惩。那是不变量 365 的 Usage 路径，不是本页 Fields 里 votes 列表含义。
