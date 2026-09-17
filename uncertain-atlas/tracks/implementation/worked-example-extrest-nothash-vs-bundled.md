# 例：看见 ExtendVoteRequest.next_validators_hash is not already same-field interchangeable / not already swapped interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量）/ not 1036 extrest-nothash interchangeable / not 411 extreqtxs-vs-fintxs bundled interchangeable」，不是 ExtendVote 请求余栏 bundled（411），也不是 Finalize 请求 next_validators_hash 就已经是同一套字段（394），也不是 ValidatorUpdate 就已经换集合（318）。不要另写怎样写 ExtendVote 请求余栏。

## 官方三件事

1. **看见 ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希 / 看见填了 next_validators_hash 这份栏 is not already 已经是 Finalize 请求栏的 next_validators_hash interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1036 extrest-nothash interchangeable / 1034 extrest-notexec interchangeable / 411 extreqtxs item 1 txs interchangeable，也不是已经 ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事 bundled（411 item 3 余量） interchangeable / 411 extreqtxs item 3 interchangeable。**  
   官方写：next_validators_hash 是下一份验证者集合的哈希。看见填了 next_validators_hash，不是已经 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根那种已经是同一套字段 interchangeable——本页从 411 item 3 侧钉 not already same-field 单句。411 extreqtxs vs fintxs bundled unbundling 在本页 item 3 完成。

2. **看见能指下一份集合 / 看见填了 next_validators_hash / 这份栏 is not already 已经换了人 interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1036 extrest-nothash interchangeable / 411 extreqtxs item 2 last commit interchangeable / 1035 extrest-notlocal interchangeable，也不是已经 Finalize 请求 next_validators_hash 就已经是同一套字段 interchangeable / 394 finnexthash interchangeable。**  
   官方把能指下一份集合和已经换了人分开。看见能指下一份集合，不是已经换了人 interchangeable。本页钉 not already swapped 单句。

3. **看见有哈希 / 看见填了 next_validators_hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1036 extrest-nothash interchangeable / 1034 extrest-notexec interchangeable，也不是已经 ValidatorUpdate 就已经换集合 interchangeable / 318 validatorupdate interchangeable。**  
   官方把有哈希和已经交差分开。看见有哈希，不是已经交差 interchangeable。411 extreqtxs vs fintxs bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.next_validators_hash not already same-field ≠ 已经是 Finalize 请求栏的 next_validators_hash interchangeable：** 官方把 ExtendVote 上的下一份集合哈希和 Finalize 请求栏已经填了 next_validators_hash 分开。
- **看见能指下一份集合 not already swapped ≠ 已经换了人 interchangeable：** 官方把能指下一份集合和已经换了人分开。
- **看见有哈希 not already settled ≠ 已经交差 interchangeable：** 官方把有哈希和已经交差分开；411 extreqtxs vs fintxs bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.next_validators_hash 是下一份验证者集合的哈希 | 不是已经是 Finalize 请求栏的 next_validators_hash | 不是 Finalize 请求 next_validators_hash 就已经是同一套字段（394） |
| 看见能指下一份集合 | 不是已经换了人 | 不是 ValidatorUpdate 就已经换集合（318） |
| 看见有哈希 | 不是已经交差 | 不是 txs 就已经执行那些交易（1034） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量），必须分开是不是已经是 Finalize 请求栏的 next_validators_hash、是不是已经换了人、是不是已经交差。可以跳过「看见填了 ExtendVote 请求余栏就已经执行那些交易」。不要另写怎样写 ExtendVote 请求余栏。411 extreqtxs vs fintxs bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit。
- ExtendVote 请求余栏 bundled。那是不变量 411。
- Finalize 请求 next_validators_hash 就已经是同一套字段。那是不变量 394。
- ValidatorUpdate 就已经换集合。那是不变量 318。
