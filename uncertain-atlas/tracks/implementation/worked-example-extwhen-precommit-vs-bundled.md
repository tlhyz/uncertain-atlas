# 例：看见 constructs Precommit using CanonicalVoteExtension and CanonicalVote / step 6 after signed CanonicalVote / before broadcasts 不是已经 construct CanonicalVote bundled interchangeable / 已经 ExtendVote When 正式流程 interchangeable / 已经写进 last_commit interchangeable

**层次**：实现 / ExtendVote When construct Precommit 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 6。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「constructs Precommit using both / step 6 顺序 不是 construct CanonicalVote bundled interchangeable / 不是 ExtendVote When 正式流程 interchangeable / 不是写进 last_commit interchangeable」，不是 ExtendVote When construct CanonicalVote（511），也不是 ExtendVote When 正式流程（438）。不要另写怎样构造 Precommit、怎样广播 Precommit、怎样写 last_commit。

## 官方三件事

规范把 ExtendVote When step 6 里用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit（Vote 结构）、与 step 5 / step 7 的边界写成三件独立的实现事，不是「看见签了 CanonicalVote 就已经广播 Precommit interchangeable、已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」一件事：

1. **看见 _p_ constructs the Precommit message (i.e. `Vote` structure) / 看见构造 Precommit 消息、也就是 Vote 结构 不是已经 constructs and signs CanonicalVote bundled（511） interchangeable / 已经 fill CanonicalVoteExtension interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable / 已经写进 last_commit interchangeable，也不是已经 CanonicalVote 就是 Precommit interchangeable / 已经只有 CanonicalVote interchangeable，也不是已经一轮最多一张 Precommit（350） interchangeable / 已经每一高度一份 interchangeable。**  
   官方 When step 6 写：_p_ constructs the Precommit message (i.e. Vote structure)。看见 constructs Precommit，不是已经 constructs and signs CanonicalVote（511） interchangeable——511 钉 step 5 构造并签 CanonicalVote，本页钉 step 6 构造 Precommit 单句。看见构造 Vote 结构，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 steps 6–7 构造并广播 bundled，本页钉 step 6 construct Precommit 单句。看见 Precommit 消息，不是已经 CanonicalVote 就是 Precommit interchangeable——511 钉 CanonicalVote 对象，本页钉 Vote/Precommit 对象。
2. **看见 using `CanonicalVoteExtension` and `CanonicalVote` / 看见用 CanonicalVoteExtension 和 CanonicalVote 两者 不是已经只有 CanonicalVoteExtension interchangeable / 已经 signs populated CanonicalVoteExtension interchangeable，也不是已经只有 CanonicalVote interchangeable / 已经 construct CanonicalVote bundled interchangeable，也不是已经 CanonicalVoteExtension 就是 CanonicalVote interchangeable / 已经包装就是票 interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension（358） interchangeable / 已经按原样签 interchangeable，也不是已经 Verify 过他人扩展（353） interchangeable / 已经 Accept interchangeable。**  
   官方 When step 6 续：using CanonicalVoteExtension and CanonicalVote。看见 using both，不是已经只有 fill CanonicalVoteExtension（510） interchangeable——510 钉 step 4 填包装，本页钉 step 6 用两者构造 Precommit。看见两者一起，不是已经 construct CanonicalVote alone（511） interchangeable——511 钉 step 5 单对象，本页钉 step 6 双对象组合。看见 CanonicalVoteExtension and CanonicalVote，不是已经 CanonicalVoteExtension 就是 CanonicalVote（34） interchangeable——34 钉两者不是同一对象，本页钉 step 6 用两者构造 Precommit 单句。
3. **看见 step 6 after constructs and signs CanonicalVote (step 5) and before broadcasts the Precommit message (step 7) / 看见 step 6 在签完 CanonicalVote 之后、在广播 Precommit 之前 不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable，也不是已经 construct CanonicalVote bundled（511） interchangeable / 已经 fill CanonicalVoteExtension interchangeable，也不是已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info（352） interchangeable / 已经 Verify 过 interchangeable。**  
   官方 When 把 step 6 夹在 step 5 和 step 7 之间。看见 step 6 在中间，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 step 7 broadcast bundled，本页钉 step 6 在 broadcast 之前。看见构造 Precommit，不是已经 construct CanonicalVote（511） interchangeable——511 钉 step 5，本页钉 step 6 顺序单句。看见还没广播，不是已经写进 last_commit（438 第三件事 bundled） interchangeable——438 钉 broadcast/写进 last_commit，本页钉 step 6 在 broadcast 之前。

怎样做构造 Precommit、怎样广播 Precommit、怎样写 last_commit 是规范里的做法，本页不抄。ExtendVote When construct CanonicalVote（511）、ExtendVote When 正式流程（438）、CanonicalVoteExtension 不是 CanonicalVote（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **constructs Precommit (Vote) ≠ construct CanonicalVote bundled interchangeable：** 官方把 step 6 构造 Precommit 和 step 5 构造 CanonicalVote 分开。
- **using both CanonicalVoteExtension and CanonicalVote ≠ 只有包装或只有票 interchangeable：** 官方把 step 6 用两者组合和 step 4/5 单对象步骤分开。
- **step 6 before broadcasts ≠ ExtendVote When 正式流程 bundled interchangeable：** 官方把 step 6 构造 Precommit 单句和 step 7 广播 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| constructs Precommit (Vote) | 不是 construct CanonicalVote（511） | 不是 CanonicalVote 就是 Precommit |
| using CanonicalVoteExtension and CanonicalVote | 不是只有 CanonicalVoteExtension（510） | 不是 CanonicalVoteExtension 就是 CanonicalVote（34） |
| step 6 before broadcasts | 不是 broadcast Precommit（438） | 不是写进 last_commit（438） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When construct Precommit 正式三事，必须分开 constructs Precommit 是不是 construct CanonicalVote bundled interchangeable、using both 是不是只有 CanonicalVoteExtension interchangeable / 只有 CanonicalVote interchangeable、step 6 before broadcasts 是不是 ExtendVote When 正式流程 bundled interchangeable / 已经写进 last_commit interchangeable。可以跳过「看见签了 CanonicalVote 就已经广播 Precommit interchangeable、已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」。不要另写怎样构造 Precommit。

## 本页不抄

- 怎样做构造 Precommit、怎样广播 Precommit、怎样写 last_commit。
- ExtendVote When construct CanonicalVote。那是不变量 511。
- ExtendVote When 正式流程 / 广播 Precommit 并写进 last_commit。那是不变量 438。
- CanonicalVoteExtension 不是 CanonicalVote。那是不变量 34。
