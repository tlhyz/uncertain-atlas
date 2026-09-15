# 例：看见 constructs and signs CanonicalVote / step 5 after signed CanonicalVoteExtension / before constructs Precommit 不是已经 fill CanonicalVoteExtension bundled interchangeable / 已经 ExtendVote When 正式流程 interchangeable / 已经验过扩展 interchangeable

**层次**：实现 / ExtendVote When construct CanonicalVote 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 5。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「constructs and signs CanonicalVote / step 5 顺序 不是 fill CanonicalVoteExtension bundled interchangeable / 不是 ExtendVote When 正式流程 interchangeable / 不是验过扩展 interchangeable」，不是 ExtendVote When fill CanonicalVoteExtension（510），也不是 ExtendVote When 正式流程（438）。不要另写怎样构造 CanonicalVote、怎样构造 Precommit、怎样广播。

## 官方三件事

规范把 ExtendVote When step 5 里构造并签名 CanonicalVote、与 step 4 / step 6 的边界写成三件独立的实现事，不是「看见签了 CanonicalVoteExtension 就已经验过扩展 interchangeable、已经构造 Precommit interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」一件事：

1. **看见 _p_ constructs the `CanonicalVote` structure / 看见构造 CanonicalVote 结构 不是已经 fill CanonicalVoteExtension bundled（510） interchangeable / 已经 signs populated CanonicalVoteExtension interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经填进包装并签名 interchangeable / 已经广播 Precommit interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension（358） interchangeable / 已经按原样签 interchangeable，也不是已经 CanonicalVoteExtension 就是 CanonicalVote interchangeable / 已经只有 extension 包装 interchangeable。**  
   官方 When step 5 写：_p_ constructs and signs the CanonicalVote structure。看见 constructs CanonicalVote，不是已经 sets extension into CanonicalVoteExtension（510） interchangeable——510 钉 step 4 填包装并签 populated structure，本页钉 step 5 构造 CanonicalVote 单句。看见构造票结构，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 steps 4–7 bundled，本页钉 step 5 construct 单句。看见 CanonicalVote 结构，不是已经 CanonicalVoteExtension 就是 CanonicalVote interchangeable——510 钉包装对象，本页钉 CanonicalVote 对象。
2. **看见 and signs the CanonicalVote structure / 看见签 CanonicalVote 结构 不是已经 signs populated CanonicalVoteExtension interchangeable / 已经按原样签 application bytes interchangeable，也不是已经 Verify 过他人扩展（353） interchangeable / 已经 Accept interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经验过扩展 interchangeable / 已经写进 last_commit interchangeable，也不是已经 domain separation（6） interchangeable / 已经用户交易 interchangeable。**  
   官方 When step 5 把 construct 和 sign 写在同一句。看见 signs CanonicalVote，不是已经 signs populated CanonicalVoteExtension（510） interchangeable——510 钉 step 4 sign 包装，本页钉 step 5 sign 票单句。看见签了 CanonicalVote，不是已经 Verify 过扩展（438 第二件事 bundled） interchangeable——438 钉「有 CanonicalVote 不是已经验过扩展」，本页钉 step 5 sign 单句。看见本地票签名，不是已经写进 last_commit（438 第三件事 bundled） interchangeable——438 钉广播/写进 last_commit，本页钉 step 5 sign 单句。
3. **看见 step 5 after signs populated CanonicalVoteExtension (step 4) and before constructs Precommit using both (step 6) / 看见 step 5 在签完 CanonicalVoteExtension 之后、在用两者构造 Precommit 之前 不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable，也不是已经 fill CanonicalVoteExtension bundled（510） interchangeable / 已经 return extension bundled（509） interchangeable，也不是已经一轮最多一张 Precommit（350） interchangeable / 已经每一高度一份 interchangeable，也不是已经 Precommit 没有带有效签的扩展就会当非法丢掉（435） interchangeable / 已经跳过 Verify interchangeable。**  
   官方 When 把 step 5 夹在 step 4 和 step 6 之间。看见 step 5 在中间，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉构造 Precommit 并广播 bundled，本页钉 step 5 在构造 Precommit 之前。看见构造并签名 CanonicalVote，不是已经 fill CanonicalVoteExtension（510） interchangeable——510 钉 step 4，本页钉 step 5 顺序单句。看见还没广播，不是已经广播 Precommit（438 第三件事） interchangeable——438 钉 step 7 broadcast，本页钉 step 5 在 broadcast 之前。

怎样做构造 CanonicalVote、怎样构造 Precommit、怎样广播 Precommit 是规范里的做法，本页不抄。ExtendVote When fill CanonicalVoteExtension（510）、ExtendVote When 正式流程（438）、Verify 拒扩展丢票（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **constructs CanonicalVote ≠ fill CanonicalVoteExtension bundled interchangeable：** 官方把 step 5 构造票结构和 step 4 填包装分开。
- **signs CanonicalVote ≠ signs populated CanonicalVoteExtension interchangeable：** 官方把 step 5 签票和 step 4 签包装分开。
- **step 5 before constructs Precommit ≠ ExtendVote When 正式流程 bundled interchangeable：** 官方把 step 5 单句和 steps 6–7 构造 Precommit/广播 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| constructs CanonicalVote | 不是 fill CanonicalVoteExtension（510） | 不是 CanonicalVoteExtension 就是 CanonicalVote |
| signs CanonicalVote | 不是 signs populated CanonicalVoteExtension（510） | 不是已经验过扩展（438 bundled） |
| step 5 before constructs Precommit | 不是 broadcast Precommit（438） | 不是 return extension bundled（509） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When construct CanonicalVote 正式三事，必须分开 constructs CanonicalVote 是不是 fill CanonicalVoteExtension bundled interchangeable、signs CanonicalVote 是不是 signs populated CanonicalVoteExtension interchangeable / 已经验过扩展 interchangeable、step 5 before constructs Precommit 是不是 ExtendVote When 正式流程 bundled interchangeable / 已经广播 Precommit interchangeable。可以跳过「看见签了 CanonicalVoteExtension 就已经验过扩展 interchangeable、已经构造 Precommit interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」。不要另写怎样构造 CanonicalVote。

## 本页不抄

- 怎样做构造 CanonicalVote、怎样构造 Precommit、怎样广播 Precommit。
- ExtendVote When fill CanonicalVoteExtension。那是不变量 510。
- ExtendVote When 正式流程 / 构造 Precommit 并广播。那是不变量 438。
- Verify 拒扩展丢票 / CanonicalVoteExtension 不是 CanonicalVote。那是不变量 34。
