# 例：看见广播 Precommit 不是已经 constructs Precommit不是已经 constructs Precommit bundled；看见broadcasts Precommit is not construct Precommit不是已经 ExtendVote When 正式流程 bundled；看见广播 Precommit 不是已经 constructs Precommit不是已经 return extension bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7 broadcasts the Precommit message 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtWhenBcast broadcast not already construct-Precommit / not already 438-bundled / not already return-ext 正式三事（513 余量）/ not 1343 ewbcast-notpre interchangeable / not 513 extwhen-broadcast-vs-bundled bundled interchangeable」，不是 extwhen broadcast vs bundled bundled（513），也不是已经 ExtendVote When construct Precommit（512），也不是已经 ExtendVote When return extension（509）。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方三件事

1. **看见广播 Precommit 不是已经 constructs Precommit / 看见广播 Precommit 不是已经 constructs Precommit 这份对象 is not already 已经 constructs Precommit bundled interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1343 ewbcast-notpre interchangeable / 1344 ewbcast-notord interchangeable，也不是已经 ExtWhenBcast broadcast not already construct-Precommit / not already 438-bundled / not already return-ext 正式三事 bundled（513 item 1 余量） interchangeable / 513 ewbcast item 1 interchangeable。**  
   官方把广播 Precommit 不是已经 constructs Precommit和已经 constructs Precommit bundled写成两件。看见广播 Precommit 不是已经 constructs Precommit，不是已经 constructs Precommit bundled。

2. **看见broadcasts Precommit is not construct Precommit / 看见广播 Precommit 不是已经 constructs Precommit / 这份对象 is not already 已经 ExtendVote When 正式流程 bundled interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1343 ewbcast-notpre interchangeable / 1345 ewbcast-notlc interchangeable，也不是已经 ExtendVote When construct Precommit interchangeable / 512 ExtendVote When construct Precommit interchangeable。**  
   官方把broadcasts Precommit is not construct Precommit和已经 ExtendVote When 正式流程 bundled写成两件。看见broadcasts Precommit is not construct Precommit，不是已经 ExtendVote When 正式流程 bundled。

3. **看见广播 Precommit 不是已经 constructs Precommit / 看见broadcasts Precommit is not construct Precommit / 这份对象 is not already 已经 return extension bundled interchangeable，也不是已经 extwhen broadcast vs bundled bundled（513） interchangeable / 1343 ewbcast-notpre interchangeable / 1344 ewbcast-notord interchangeable，也不是已经 ExtendVote When return extension interchangeable / 509 ExtendVote When return extension interchangeable。**  
   官方把广播 Precommit 不是已经 constructs Precommit和已经 return extension bundled写成两件。看见广播 Precommit 不是已经 constructs Precommit，不是已经 return extension bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方为什么这样拆

- **broadcasts Precommit 不是已经 constructs Precommit interchangeable：官方把 step 7 广播和 step 6 构造 Precommit 分开。**
- **看见广播消息 不是已经 ExtendVote When 正式流程：438 钉 steps 6–7 构造并广播 bundled，本页钉 step 7 broadcast 单句。**
- **看见发出去 不是已经 return extension：509 钉 step 3 return，本页钉 step 7 广播已构造好的 Precommit。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 constructs Precommit bundled | 不是已经 constructs Precommit bundled | 不是已经ExtendVote When construct Precommit（512） |
| 已经 ExtendVote When 正式流程 bundled | 不是已经 ExtendVote When 正式流程 bundled | 不是已经ExtendVote When return extension（509） |
| 已经 return extension bundled | 不是已经 return extension bundled | 不是已经1344 ewbcast-notord |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtWhenBcast broadcast not already construct-Precommit / not already 438-bundled / not already return-ext 正式三事（513 余量），必须分开是不是已经 constructs Precommit bundled、是不是已经 ExtendVote When 正式流程 bundled、是不是已经 return extension bundled。可以跳过「看见构造了 Precommit 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 ExtendVote 回了 extension 就已经交差 interchangeable」。不要另写 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。513 ExtendVote When broadcast Precommit bundled unbundling 在本页 item 1 启动；续 [`worked-example-ewbcast-notord-vs-bundled.md`](worked-example-ewbcast-notord-vs-bundled.md)（不变量 1344 item 2）。

## 本页不抄

- 怎样做广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
- 怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
