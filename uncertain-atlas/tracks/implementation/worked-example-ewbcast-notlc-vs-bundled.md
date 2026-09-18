# 例：看见广播了不是已经写进 last_commit不是已经写进 last_commit；看见broadcasts is not write into last_commit不是已经 Verify 过迟到扩展；看见广播了不是已经写进 last_commit不是已经 ExtendVote When 正式流程 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事（513 余量）/ not 1345 ewbcast-notlc interchangeable / not 513 extwhen-broadcast-vs-bundled bundled interchangeable」，不是 extwhen broadcast vs bundled bundled（513），也不是已经 ExtendVote When 正式流程 / last_commit（438），也不是已经 Verify When ACCEPT keep（435）。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方三件事

1. **看见广播了不是已经写进 last_commit / 看见广播了不是已经写进 last_commit 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1345 ewbcast-notlc interchangeable / 1343 ewbcast-notpre interchangeable，也不是已经 ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事 bundled（513 item 3 余量） interchangeable / 513 ewbcast item 3 interchangeable。**  
   官方把广播了不是已经写进 last_commit和已经写进 last_commit写成两件。看见广播了不是已经写进 last_commit，不是已经写进 last_commit。

2. **看见broadcasts is not write into last_commit / 看见广播了不是已经写进 last_commit / 这份对象 is not already 已经 Verify 过迟到扩展 interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1345 ewbcast-notlc interchangeable / 1344 ewbcast-notord interchangeable，也不是已经 ExtendVote When 正式流程 / last_commit interchangeable / 438 ExtendVote When 正式流程 / last_commit interchangeable。**  
   官方把broadcasts is not write into last_commit和已经 Verify 过迟到扩展写成两件。看见broadcasts is not write into last_commit，不是已经 Verify 过迟到扩展。

3. **看见广播了不是已经写进 last_commit / 看见broadcasts is not write into last_commit / 这份对象 is not already 已经 ExtendVote When 正式流程 bundled interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1345 ewbcast-notlc interchangeable / 1343 ewbcast-notpre interchangeable，也不是已经 Verify When ACCEPT keep interchangeable / 435 Verify When ACCEPT keep interchangeable。**  
   官方把广播了不是已经写进 last_commit和已经 ExtendVote When 正式流程 bundled写成两件。看见广播了不是已经写进 last_commit，不是已经 ExtendVote When 正式流程 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方为什么这样拆

- **broadcasts 不是已经写进 last_commit interchangeable：官方把 step 7 广播单句和 last_commit 后效分开。**
- **看见发出去 不是已经 Verify 过迟到扩展：438 钉「不是已经 Verify 过迟到扩展」，本页钉 step 7 广播单句。**
- **看见广播 Precommit 不是已经 Finalize 决定：362 钉 +2/3 precommit 才调 Finalize，本页钉 step 7 只是广播。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经ExtendVote When 正式流程 / last_commit（438） |
| 已经 Verify 过迟到扩展 | 不是已经 Verify 过迟到扩展 | 不是已经Verify When ACCEPT keep（435） |
| 已经 ExtendVote When 正式流程 bundled | 不是已经 ExtendVote When 正式流程 bundled | 不是已经1343 ewbcast-notpre |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtWhenBcast broadcast not already last_commit / not already late-Verify / not already 438-bundled 正式三事（513 余量），必须分开是不是已经写进 last_commit、是不是已经 Verify 过迟到扩展、是不是已经 ExtendVote When 正式流程 bundled。可以跳过「看见构造了 Precommit 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 ExtendVote 回了 extension 就已经交差 interchangeable」。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。513 ExtendVote When broadcast Precommit bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
- 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
