# 例：看见Prepare MAY 产出事件不是已经在回包里交回不是已经在 PrepareProposalResponse 里交回；看见Prepare MAY produce events is not already in the response不是已经 Prepare 返回时引擎收到；看见Prepare MAY 产出事件不是已经在回包里交回不是已经验过重复

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事（448 余量）/ not 1368 prepev-notret interchangeable / not 448 prepevents-vs-finalize bundled interchangeable」，不是 prepevents vs finalize bundled（448），也不是已经 Prepare 回包校验就已经验过重复（357），也不是已经 PrepareUsage raw proposal（503）。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。

## 官方三件事

1. **看见Prepare MAY 产出事件不是已经在回包里交回 / 看见Prepare MAY 产出事件不是已经在回包里交回 这份对象 is not already 已经在 PrepareProposalResponse 里交回 interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1368 prepev-notret interchangeable / 1369 prepev-notkeep interchangeable，也不是已经 PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事 bundled（448 item 1 余量） interchangeable / 448 prepev item 1 interchangeable。**  
   官方把Prepare MAY 产出事件不是已经在回包里交回和已经在 PrepareProposalResponse 里交回写成两件。看见Prepare MAY 产出事件不是已经在回包里交回，不是已经在 PrepareProposalResponse 里交回。

2. **看见Prepare MAY produce events is not already in the response / 看见Prepare MAY 产出事件不是已经在回包里交回 / 这份对象 is not already 已经 Prepare 返回时引擎收到 interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1368 prepev-notret interchangeable / 1370 prepev-notfin interchangeable，也不是已经 Prepare 回包校验就已经验过重复 interchangeable / 357 Prepare 回包校验就已经验过重复 interchangeable。**  
   官方把Prepare MAY produce events is not already in the response和已经 Prepare 返回时引擎收到写成两件。看见Prepare MAY produce events is not already in the response，不是已经 Prepare 返回时引擎收到。

3. **看见Prepare MAY 产出事件不是已经在回包里交回 / 看见Prepare MAY produce events is not already in the response / 这份对象 is not already 已经验过重复 interchangeable，也不是已经 prepevents vs finalize bundled（448） interchangeable / 1368 prepev-notret interchangeable / 1369 prepev-notkeep interchangeable，也不是已经 PrepareUsage raw proposal interchangeable / 503 PrepareUsage raw proposal interchangeable。**  
   官方把Prepare MAY 产出事件不是已经在回包里交回和已经验过重复写成两件。看见Prepare MAY 产出事件不是已经在回包里交回，不是已经验过重复。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。

## 官方为什么这样拆

- **MAY 产出 不是已经在回包里 interchangeable：官方写 PrepareProposalResponse 只有 txs。**
- **看见先跑了 不是已经 Prepare 返回时就交给引擎。**
- **看见产出事件 不是已经 357 回包校验就已经验过重复。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在 PrepareProposalResponse 里交回 | 不是已经在 PrepareProposalResponse 里交回 | 不是已经Prepare 回包校验就已经验过重复（357） |
| 已经 Prepare 返回时引擎收到 | 不是已经 Prepare 返回时引擎收到 | 不是已经PrepareUsage raw proposal（503） |
| 已经验过重复 | 不是已经验过重复 | 不是已经1369 prepev-notkeep |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepEv Prepare MAY produce events not already in PrepareProposalResponse / not already engine-received / not already 357-checked 正式三事（448 余量），必须分开是不是已经在 PrepareProposalResponse 里交回、是不是已经 Prepare 返回时引擎收到、是不是已经验过重复。可以跳过「看见 Prepare 里产出了事件就已经交给引擎」。不要另写 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。448 Prepare events retention until Finalize bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepev-notkeep-vs-bundled.md`](worked-example-prepev-notkeep-vs-bundled.md)（不变量 1369 item 2）。

## 本页不抄

- 怎样攒 Prepare 事件、怎样等块决定、怎样在 Finalize 交回。
- 怎样把 Prepare 事件写进回包、怎样在 Process 时就索引、怎样把 Finalize events 写成 CheckTx events。
