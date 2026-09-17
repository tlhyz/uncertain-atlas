# 例：看见 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表不是已经执行那些交易；看见 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息不是已经交差 local_last_commit；看见 ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希不是已经是 Finalize 请求栏的 next_validators_hash

**层次**：实现 / ExtendVote 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.txs 是扩展要指的那份块的交易列表不是已经执行那些交易 / ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息不是已经交差 local_last_commit / ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希不是已经是 Finalize 请求栏的 next_validators_hash」，不是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差，也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。不要另写怎样写 ExtendVote 请求余栏。

## 官方三件事

规范把 `ExtendVoteRequest.txs` 是扩展要指的那份块的交易列表、`proposed_last_commit` 是上一份拟议块的 last commit 信息、`next_validators_hash` 是下一份验证者集合的哈希写成三件独立的实现事，不是「看见填了 ExtendVote 请求余栏就已经执行那些交易、已经交差 local_last_commit、已经是 Finalize 请求栏的 next_validators_hash」一件事：

1. **看见 `ExtendVoteRequest.txs` 是扩展要指的那份块的交易列表 / 看见填了 txs 不是已经执行那些交易，也不是已经交差。**  
   官方写：`txs` 是扩展要指的那份块的交易列表。看见填了 txs，不是已经 Finalize 按应用自己的规则确定地执行 `txs`、再交还控制权那种已经交差。看见有交易列表，不是已经交差。看见能指，不是已经整块跑了。
2. **看见 `ExtendVoteRequest.proposed_last_commit` 是上一份拟议块的 last commit 信息 / 看见填了 proposed_last_commit 不是已经交差 local_last_commit，也不是已经跑过 Process。**  
   官方写：`proposed_last_commit` 是上一份拟议块的 last commit 信息。看见填了 proposed_last_commit，不是已经 Prepare `local_last_commit` 是上一高度的预提交带扩展那种已经交差。看见有上一份拟议块的 last commit，不是已经字段名对上就已经跑过 Process。看见能指，不是已经是本头 LastCommit。
3. **看见 `ExtendVoteRequest.next_validators_hash` 是下一份验证者集合的哈希 / 看见填了 next_validators_hash 不是已经是 Finalize 请求栏的 next_validators_hash，也不是已经换了人。**  
   官方写：`next_validators_hash` 是下一份验证者集合的哈希。看见填了 next_validators_hash，不是已经 Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根那种已经是同一套字段。看见能指下一份集合，不是已经换了人。看见有哈希，不是已经交差。

怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit 是规范里的做法，本页不抄。Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差是不变量 408，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.txs 是扩展要指的那份块的交易列表 ≠ 已经执行那些交易：** 官方把扩展要指的交易列表和已经执行那些交易分开。
- **ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息 ≠ 已经交差 local_last_commit：** 官方把上一份拟议块的 last commit 和 Prepare 已经交差 local_last_commit 分开。
- **ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希 ≠ 已经是 Finalize 请求栏的 next_validators_hash：** 官方把 ExtendVote 上的下一份集合哈希和 Finalize 请求栏已经填了 next_validators_hash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.txs 是扩展要指的那份块的交易列表 | 不是已经执行那些交易 | 不是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差（408） |
| ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息 | 不是已经交差 local_last_commit | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希 | 不是已经是 Finalize 请求栏的 next_validators_hash | 不是 Finalize 请求 next_validators_hash 就已经是同一套字段（394） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求余栏就已经执行那些交易、已经交差 local_last_commit、已经是 Finalize 请求栏的 next_validators_hash」，必须分开 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表是不是已经执行那些交易、ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息是不是已经交差 local_last_commit、ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希是不是已经是 Finalize 请求栏的 next_validators_hash。可以跳过「看见填了 ExtendVote 请求余栏就已经执行那些交易」。不要另写怎样写 ExtendVote 请求余栏。

## 本页不抄

- 怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit。
- Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差。那是不变量 408。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- Finalize 请求 next_validators_hash 就已经是同一套字段。那是不变量 394。
