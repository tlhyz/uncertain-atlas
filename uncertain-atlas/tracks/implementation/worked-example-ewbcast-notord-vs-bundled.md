# 例：看见step 7 在 step 6 之后不是已经 construct CanonicalVote不是已经 construct CanonicalVote bundled；看见step 7 after step 6 is not construct CanonicalVote不是已经 fill CanonicalVoteExtension bundled；看见step 7 在 step 6 之后不是已经 construct CanonicalVote不是已经 Verify 过扩展

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事（513 余量）/ not 1344 ewbcast-notord interchangeable / not 513 extwhen-broadcast-vs-bundled bundled interchangeable」，不是 extwhen broadcast vs bundled bundled（513），也不是已经 ExtendVote When construct CanonicalVote（511），也不是已经 ExtendVote When fill CanonicalVoteExtension（510）。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方三件事

1. **看见step 7 在 step 6 之后不是已经 construct CanonicalVote / 看见step 7 在 step 6 之后不是已经 construct CanonicalVote 这份对象 is not already 已经 construct CanonicalVote bundled interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1344 ewbcast-notord interchangeable / 1343 ewbcast-notpre interchangeable，也不是已经 ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事 bundled（513 item 2 余量） interchangeable / 513 ewbcast item 2 interchangeable。**  
   官方把step 7 在 step 6 之后不是已经 construct CanonicalVote和已经 construct CanonicalVote bundled写成两件。看见step 7 在 step 6 之后不是已经 construct CanonicalVote，不是已经 construct CanonicalVote bundled。

2. **看见step 7 after step 6 is not construct CanonicalVote / 看见step 7 在 step 6 之后不是已经 construct CanonicalVote / 这份对象 is not already 已经 fill CanonicalVoteExtension bundled interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1344 ewbcast-notord interchangeable / 1345 ewbcast-notlc interchangeable，也不是已经 ExtendVote When construct CanonicalVote interchangeable / 511 ExtendVote When construct CanonicalVote interchangeable。**  
   官方把step 7 after step 6 is not construct CanonicalVote和已经 fill CanonicalVoteExtension bundled写成两件。看见step 7 after step 6 is not construct CanonicalVote，不是已经 fill CanonicalVoteExtension bundled。

3. **看见step 7 在 step 6 之后不是已经 construct CanonicalVote / 看见step 7 after step 6 is not construct CanonicalVote / 这份对象 is not already 已经 Verify 过扩展 interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1344 ewbcast-notord interchangeable / 1343 ewbcast-notpre interchangeable，也不是已经 ExtendVote When fill CanonicalVoteExtension interchangeable / 510 ExtendVote When fill CanonicalVoteExtension interchangeable。**  
   官方把step 7 在 step 6 之后不是已经 construct CanonicalVote和已经 Verify 过扩展写成两件。看见step 7 在 step 6 之后不是已经 construct CanonicalVote，不是已经 Verify 过扩展。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方为什么这样拆

- **step 7 after step 6 不是已经 construct CanonicalVote interchangeable：官方把 step 7 顺序和 step 5 构造 CanonicalVote 分开。**
- **看见广播 不是已经 fill CanonicalVoteExtension：510 钉 step 4 fill，本页钉 step 7 顺序单句。**
- **看见发 Precommit 不是已经 Verify 过扩展：438 钉「有 CanonicalVote 不是已经验过」，本页钉 step 7 广播单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 construct CanonicalVote bundled | 不是已经 construct CanonicalVote bundled | 不是已经ExtendVote When construct CanonicalVote（511） |
| 已经 fill CanonicalVoteExtension bundled | 不是已经 fill CanonicalVoteExtension bundled | 不是已经ExtendVote When fill CanonicalVoteExtension（510） |
| 已经 Verify 过扩展 | 不是已经 Verify 过扩展 | 不是已经1343 ewbcast-notpre |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtWhenBcast step7-after-step6 not already construct-CanonicalVote / not already fill / not already Verify 正式三事（513 余量），必须分开是不是已经 construct CanonicalVote bundled、是不是已经 fill CanonicalVoteExtension bundled、是不是已经 Verify 过扩展。可以跳过「看见构造了 Precommit 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 ExtendVote 回了 extension 就已经交差 interchangeable」。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。513 ExtendVote When broadcast Precommit bundled unbundling 在本页 item 2 续；续 [`worked-example-ewbcast-notlc-vs-bundled.md`](worked-example-ewbcast-notlc-vs-bundled.md)（不变量 1345 item 3）。

## 本页不抄

- 怎样做广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
- 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
