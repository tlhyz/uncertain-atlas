# 例：看见 FinalizeBlockRequest.decided_last_commit is not already local interchangeable / not already rewarded interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量）/ not 1040 finreqcol-notlocal interchangeable / not 422 finreq-vs-procreq bundled interchangeable」，不是 Finalize 请求栏 bundled（422），也不是 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit（420），也不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363）。不要另写怎样写 Finalize 请求栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 / 看见填了 decided_last_commit 这份栏 is not already 已经交差 local_last_commit interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1040 finreqcol-notlocal interchangeable / 1041 finreqcol-nothead interchangeable / 422 finreq item 2 height interchangeable，也不是已经 FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事 bundled（422 item 1 余量） interchangeable / 422 finreq item 1 interchangeable。**  
   官方写：decided_last_commit 是上一份提交信息，从刚决定那块拿到。看见填了 decided_last_commit，不是已经 ProcessProposalRequest.proposed_last_commit 那种已经交差 local_last_commit interchangeable——本页从 422 item 1 侧钉 not already local 单句。422 finreq vs procreq bundled unbundling 在本页 item 1 启动。

2. **看见从刚决定那块拿到 / 看见填了 decided_last_commit / 这份栏 is not already 已经定奖惩 interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1040 finreqcol-notlocal interchangeable / 422 finreq item 3 txs interchangeable / 1042 finreqcol-notexec interchangeable，也不是已经可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没 interchangeable / 363 finresp interchangeable。**  
   官方把从刚决定那块拿到和已经定奖惩分开。看见从刚决定那块拿到，不是已经定奖惩 interchangeable。本页钉 not already rewarded 单句。

3. **看见能指上一份提交 / 看见填了 decided_last_commit / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1040 finreqcol-notlocal interchangeable / 1041 finreqcol-nothead interchangeable，也不是已经 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit interchangeable / 420 procrestr interchangeable。**  
   官方把能指上一份提交和已经交差分开。看见能指上一份提交，不是已经交差 interchangeable。422 finreq vs procreq bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.decided_last_commit not already local ≠ 已经交差 local_last_commit interchangeable：** 官方把从刚决定那块拿到的上一份提交和已经交差 local_last_commit 分开。
- **看见从刚决定那块拿到 not already rewarded ≠ 已经定奖惩 interchangeable：** 官方把从刚决定那块拿到和已经定奖惩分开。
- **看见能指上一份提交 not already settled ≠ 已经交差 interchangeable：** 官方把能指上一份提交和已经交差分开；422 finreq vs procreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 | 不是已经交差 local_last_commit | 不是 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit（420） |
| 看见从刚决定那块拿到 | 不是已经定奖惩 | 不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363） |
| 看见能指上一份提交 | 不是已经交差 | 不是 height 就已经对上了拟议块头（1041） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量），必须分开是不是已经交差 local_last_commit、是不是已经定奖惩、是不是已经交差。可以跳过「看见填了 Finalize 请求栏就已经交差 local_last_commit」。不要另写怎样写 Finalize 请求栏。422 finreq vs procreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-finreqcol-nothead-vs-bundled.md`](worked-example-finreqcol-nothead-vs-bundled.md)（不变量 1041 item 2）。

## 本页不抄

- 怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs。
- Finalize 请求栏 bundled。那是不变量 422。
- ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit。那是不变量 420。
- 可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没。那是不变量 363。
