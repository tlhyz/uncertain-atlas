# 例：看见应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名不是已经按原样签；看见会构造并签名 CanonicalVote 不是已经验过扩展；看见用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit 并广播不是已经写进 last_commit

**层次**：实现 / ExtendVote When 正式流程。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名不是已经按原样签 / 会构造并签名 CanonicalVote 不是已经验过扩展 / 用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit 并广播不是已经写进 last_commit」，不是回了一串字节共识算法不解释就已经包进 CanonicalVoteExtension，也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。不要另写怎样写 ExtendVote When 正式流程。

## 官方三件事

规范把回包后填 CanonicalVoteExtension 并签名、再构造 CanonicalVote、再用两者构造 Precommit 并广播写成三件独立的实现事，不是「看见 ExtendVote 回了 extension 就已经按原样签、已经验过扩展、已经写进 last_commit」一件事：

1. **看见应用回 extension 后 CometBFT 会把它填进 `CanonicalVoteExtension`、填其它字段并签名 / 看见填进包装 不是已经按原样签，也不是已经广播 Precommit。**  
   官方写：应用回 `ExtendVoteResponse.extension`，共识算法不解释。接着 *p* 把这份 extension 填进 `CanonicalVoteExtension` 的 `extension` 字段，填 Height、Round、ChainID 等其它字段，再签这份结构。看见填进包装，不是已经按应用给的字节原样签。看见会签 CanonicalVoteExtension，不是已经广播 Precommit。
2. **看见会构造并签名 `CanonicalVote` / 看见有 CanonicalVote 不是已经验过扩展，也不是已经 Accept。**  
   官方写：*p* 构造并签名 `CanonicalVote`。看见有票结构，不是已经 Verify 过扩展。看见签了 CanonicalVote，不是已经验过他人扩展。看见本地票，不是已经写进 last_commit。
3. **看见用 `CanonicalVoteExtension` 和 `CanonicalVote` 构造 Precommit 并广播 / 看见广播了 不是已经写进 last_commit，也不是已经 Verify 过迟到扩展。**  
   官方写：*p* 用 `CanonicalVoteExtension` 和 `CanonicalVote` 构造 Precommit（`Vote` 结构），再广播。看见构造 Precommit，不是已经写进 last_commit。看见广播了，不是已经 Verify 过他人扩展。看见发出去，不是已经交差。

怎样写 ExtendVote When 正式流程、怎样填 CanonicalVoteExtension、怎样构造 Precommit 是规范里的做法，本页不抄。回了一串字节共识算法不解释就已经包进 CanonicalVoteExtension是不变量 361，本页不抄。

## 官方为什么这样拆

- **填进 CanonicalVoteExtension 并签名 ≠ 已经按原样签：** 官方把包装签名和按原样签分开。
- **构造并签名 CanonicalVote ≠ 已经验过扩展：** 官方把本地造票和 Verify 他人扩展分开。
- **用两者构造 Precommit 并广播 ≠ 已经写进 last_commit：** 官方把广播 Precommit 和 last_commit 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填进 CanonicalVoteExtension 并签名 | 不是已经按原样签 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| 构造并签名 CanonicalVote | 不是已经验过扩展 | 不是 CanonicalVoteExtension 就已经是 CanonicalVote（34） |
| 用两者构造 Precommit 并广播 | 不是已经写进 last_commit | 不是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 就已经会调（361） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 ExtendVote 回了 extension 就已经按原样签、已经验过扩展、已经写进 last_commit」，必须分开应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名是不是已经按原样签、会构造并签名 CanonicalVote 是不是已经验过扩展、用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit 并广播是不是已经写进 last_commit。可以跳过「看见 ExtendVote 回了 extension 就已经广播 Precommit」。不要另写怎样写 ExtendVote When 正式流程。

## 本页不抄

- 怎样写 ExtendVote When 正式流程、怎样填 CanonicalVoteExtension、怎样构造 Precommit。
- 回了一串字节共识算法不解释就已经包进 CanonicalVoteExtension。那是不变量 361。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- CanonicalVoteExtension 就已经是 CanonicalVote。那是不变量 34。
