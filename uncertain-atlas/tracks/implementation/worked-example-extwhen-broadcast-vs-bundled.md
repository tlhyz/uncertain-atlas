# 例：看见 broadcasts the Precommit message / step 7 after constructs Precommit / 不是已经 construct Precommit bundled interchangeable / 已经 ExtendVote When 正式流程 interchangeable / 已经写进 last_commit interchangeable

**层次**：实现 / ExtendVote When broadcast Precommit 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「broadcasts Precommit / step 7 顺序 不是 construct Precommit bundled interchangeable / 不是 ExtendVote When 正式流程 interchangeable / 不是写进 last_commit interchangeable」，不是 ExtendVote When construct Precommit（512），也不是 ExtendVote When 正式流程（438）。不要另写怎样广播 Precommit、怎样写 last_commit、怎样验迟到扩展。

## 官方三件事

规范把 ExtendVote When step 7 里广播 Precommit 消息、与 step 6 / 写进 last_commit / Verify 的边界写成三件独立的实现事，不是「看见构造了 Precommit 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 ExtendVote 回了 extension 就已经交差 interchangeable」一件事：

1. **看见 _p_ broadcasts the Precommit message / 看见广播 Precommit 消息 不是已经 constructs Precommit using both bundled（512） interchangeable / 已经 construct CanonicalVote interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经用两者构造 Precommit interchangeable / 已经写进 last_commit interchangeable，也不是已经 return extension bundled（509） interchangeable / 已经 ExtendVote 回了 extension 就已经广播 interchangeable，也不是已经一轮最多一张 Precommit（350） interchangeable / 已经每一高度一份 interchangeable。**  
   官方 When step 7 写：_p_ broadcasts the Precommit message。看见 broadcasts Precommit，不是已经 constructs Precommit using both（512） interchangeable——512 钉 step 6 构造 Precommit，本页钉 step 7 广播单句。看见广播消息，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 steps 6–7 构造并广播 bundled，本页钉 step 7 broadcast 单句。看见发出去，不是已经 return extension（509） interchangeable——509 钉 step 3 return，本页钉 step 7 广播已构造好的 Precommit。
2. **看见 step 7 after constructs the Precommit message using both (step 6) / 看见 step 7 在用两者构造 Precommit 之后 不是已经 construct CanonicalVote bundled（511） interchangeable / 已经 fill CanonicalVoteExtension interchangeable，也不是已经 constructs and signs CanonicalVote interchangeable / 已经 signs populated CanonicalVoteExtension interchangeable，也不是已经 Precommit 没有带有效签的扩展就会当非法丢掉（435） interchangeable / 已经跳过 Verify interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info（352） interchangeable / 已经 Verify 过 interchangeable。**  
   官方 When 把 step 7 接在 step 6 之后。看见 step 7 在 step 6 之后，不是已经 construct CanonicalVote（511） interchangeable——511 钉 step 5，本页钉 step 7 在构造 Precommit 之后。看见广播，不是已经 fill CanonicalVoteExtension（510） interchangeable——510 钉 step 4，本页钉 step 7 顺序单句。看见发 Precommit，不是已经 Verify 过扩展（438 第二件事 bundled） interchangeable——438 钉「有 CanonicalVote 不是已经验过」，本页钉 step 7 广播单句。
3. **看见 broadcasts is not write into last_commit / not Verify late-arriving extension / 看见广播了 不是已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经交差 interchangeable，也不是已经 VerifyVoteExtension ACCEPT 留给 h+1 Prepare（435） interchangeable / 已经 REJECT 丢掉 Precommit interchangeable，也不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362） interchangeable / 已经会调 Finalize interchangeable。**  
   官方 When step 7 只写 broadcast，不写 last_commit 或 Verify。看见广播了，不是已经写进 last_commit（438 第三件事 bundled） interchangeable——438 钉「广播了不是已经写进 last_commit」，本页钉 step 7 broadcast 单句。看见发出去，不是已经 Verify 过迟到扩展（438 bundled） interchangeable——438 钉「不是已经 Verify 过迟到扩展」，本页钉 step 7 广播单句。看见广播 Precommit，不是已经 Finalize 决定（362） interchangeable——362 钉 +2/3 precommit 才调 Finalize，本页钉 step 7 只是广播。

怎样做广播 Precommit、怎样写 last_commit、怎样验迟到扩展 是规范里的做法，本页不抄。ExtendVote When construct Precommit（512）、ExtendVote When 正式流程（438）、Verify 拒扩展丢票（34 / 435）是另外那套，本页不抄。

## 官方为什么这样拆

- **broadcasts Precommit ≠ construct Precommit bundled interchangeable：** 官方把 step 7 广播和 step 6 构造 Precommit 分开。
- **step 7 after step 6 ≠ construct CanonicalVote / fill bundled interchangeable：** 官方把 step 7 顺序和 step 4/5 单对象步骤分开。
- **broadcasts ≠ write into last_commit / Verify late extension interchangeable：** 官方把 step 7 广播单句和 last_commit / Verify 后效 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| broadcasts Precommit message | 不是 construct Precommit（512） | 不是 return extension（509） |
| step 7 after constructs Precommit | 不是 construct CanonicalVote（511） | 不是 fill CanonicalVoteExtension（510） |
| broadcasts | 不是 write into last_commit（438） | 不是 Verify late extension（438） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事，必须分开 broadcasts Precommit 是不是 construct Precommit bundled interchangeable、step 7 after step 6 是不是 construct CanonicalVote interchangeable / fill bundled interchangeable、broadcasts 是不是已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable。可以跳过「看见构造了 Precommit 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 ExtendVote 回了 extension 就已经交差 interchangeable」。不要另写怎样广播 Precommit。

## 本页不抄

- 怎样做广播 Precommit、怎样写 last_commit、怎样验迟到扩展。
- ExtendVote When construct Precommit。那是不变量 512。
- ExtendVote When 正式流程 / 写进 last_commit / Verify 迟到扩展。那是不变量 438。
- Verify 拒扩展丢票 / ACCEPT 留给 h+1 Prepare。那是不变量 34 / 435。
