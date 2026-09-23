# 例：看见 Vote.Type 是票类型不是已经按那条路径验过；看见 CanonicalVote.Type 是同一个枚举不是已经是同一个对象；看见枚举里写着 PREVOTE 不是已经证明签名只在这一步有效

**层次**：实现 / SignedMsgType。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) SignedMsgType / Vote / CanonicalVote。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Vote.Type 是票类型不是已经按那条路径验过 / CanonicalVote.Type 是同一个枚举不是已经是同一个对象 / 枚举里写着 PREVOTE 不是已经证明签名只在这一步有效」，不是验证者投票字节不能被当成用户交易，也不是投票步类型必须进被签字节。不要另写怎样写 SignedMsgType。

## 官方三件事

规范把 `Vote.Type` 是这张票的类型、`CanonicalVote.Type` 是**另一个结构里**的同一个枚举、以及 `SignedMsgType` 枚举本身只有三个值，写成三件独立的实现事，不是「看见票上写了 PREVOTE 就已经按 prevote 路径验过、已经和 CanonicalVote 同一对象、已经证明这一步有效」一件事：

1. **看见 `Vote.Type` 是这张票的类型 / 看见写了类型 不是已经按那条路径验过，也不是已经交差。**  
   官方写：`Type` 是这张票指向的消息类型。校验要求它必须是 Prevote 或 Precommit。看见类型对，不是已经按 Prevote 那条 `Verify` 走。看见字段在，不是已经验过。看见填了，不是已经交差。
2. **看见 `CanonicalVote.Type` 是同一个枚举 / 看见两边值一样 不是已经是同一个对象，也不是已经同一种序列化。**  
   官方写：`CanonicalVote` 是给验证者签名用的，这种类型**不会出现在块里**。票用 `CanonicalVote` 表示，并经 `type.SignBytes` 用 protobuf 编码；`SignBytes` 含 `ChainID`，而且字段顺序不同。看见两个结构里都有 `Type`，不是已经是同一份字节。看见值一样，不是已经同一套字段顺序。看见同名，不是已经同一种编码。
3. **看见枚举里写着 PREVOTE / 看见只有三个值 不是已经证明签名只在这一步有效，也不是已经不能当另一用途。**  
   官方写：`SignedMsgType` 是共识里被签消息的种类，列了 `SIGNED_MSG_TYPE_UNKNOWN = 0`、`SIGNED_MSG_TYPE_PREVOTE = 1`、`SIGNED_MSG_TYPE_PRECOMMIT = 2`、`SIGNED_MSG_TYPE_PROPOSAL = 32`。看见枚举在，不是已经验过域分离。看见只有三个值，不是已经证明这条签在别处验不过。看见是步类型，不是已经进了被签字节。

怎样编 `SignedMsgType`、怎样构造 `CanonicalVote`、怎样算 `SignBytes` 是规范里的做法，本页不抄。验证者投票字节不能被当成用户交易是不变量 6，本页不抄。投票步类型必须进被签字节是不变量 19，本页不抄。

## 官方为什么这样拆

- **`Vote.Type` 是这张票的类型 ≠ 已经按那条路径验过：** 官方把「字段里写着哪种票」和「验签走的是哪条路径」分开。
- **`CanonicalVote.Type` 是同一个枚举 ≠ 已经是同一个对象：** 官方把「块里那张 `Vote`」和「签名用的 `CanonicalVote`」分开，并写明后者字段顺序不同、含 `ChainID`。
- **枚举里写着 PREVOTE ≠ 已经证明签名只在这一步有效：** 官方把「枚举值」和「域分离已经成立」分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Vote.Type 是这张票的类型 | 不是已经按那条路径验过 | 不是投票字节可以被当成用户交易（6） |
| CanonicalVote.Type 是同一个枚举 | 不是已经是同一个对象 | 不是把扩展签写成 CanonicalVote（见 [`worked-example-extresp-vs-wrap.md`](worked-example-extresp-vs-wrap.md)，不变量 34） |
| 枚举里写着 PREVOTE | 不是已经证明签名只在这一步有效 | 不是投票步类型已经进了被签字节（见 [`../consensus/worked-example-vote-signbytes.md`](../consensus/worked-example-vote-signbytes.md)，不变量 19） |
| 本页不涉及 | — | 不是 Commit 每个槽位都对本块有效（65） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见票上写了 PREVOTE 就已经按那条路径验过、已经和 CanonicalVote 同一对象、已经证明这一步有效」，必须分开 Vote.Type 是这张票的类型是不是已经按那条路径验过、CanonicalVote.Type 是同一个枚举是不是已经是同一个对象、枚举里写着 PREVOTE 是不是已经证明签名只在这一步有效。可以跳过「看见票上写了 PREVOTE 就已经按那条路径验过」。不要另写怎样写 SignedMsgType。

## 本页不抄

- 怎样编 `SignedMsgType`、怎样构造 `CanonicalVote`、怎样算 `SignBytes`。
- 验证者投票字节不能被当成用户交易。那是不变量 6。
- 投票步类型必须进被签字节。那是不变量 19。
- Commit 每个槽位必须对本块本 ChainID 有效。那是不变量 65。
