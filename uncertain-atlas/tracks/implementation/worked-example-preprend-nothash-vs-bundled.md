# 例：看见 PrepareProposalRequest.next_validators_hash is not already finalize-hash interchangeable / not already rotated interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事（426 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事（426 余量）/ not 1055 preprend-nothash interchangeable / not 426 prepreqend-vs-finreq bundled interchangeable」，不是 Prepare 请求末栏 bundled（426），也不是 Finalize 请求 next_validators_hash 就已经是同一套字段（394），也不是 ExtendVoteRequest.next_validators_hash 就已经是 Finalize 请求栏（411）。不要另写怎样写 Prepare 请求末栏。

## 官方三件事

1. **看见 PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根 / 看见填了 next_validators_hash 这份栏 is not already 已经是 Finalize 请求栏的 next_validators_hash interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1055 preprend-nothash interchangeable / 1056 preprend-notmade interchangeable / 426 prepreqend item 2 proposer interchangeable，也不是已经 PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事 bundled（426 item 1 余量） interchangeable / 426 prepreqend item 1 interchangeable。**  
   官方写：next_validators_hash 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经 Finalize 请求 next_validators_hash 那种已经是同一套字段 interchangeable——本页从 426 item 1 侧钉 not already finalize-hash 单句。426 prepreqend vs finreq bundled unbundling 在本页 item 1 启动。

2. **看见能指下一份集合 / 看见填了 next_validators_hash / 这份栏 is not already 已经换了人 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1055 preprend-nothash interchangeable / 426 prepreqend item 3 fintime interchangeable / 1057 preprend-notts interchangeable，也不是已经 Finalize 请求 next_validators_hash 就已经是同一套字段 interchangeable / 394 nextval interchangeable。**  
   官方把能指下一份集合和已经换了人分开。看见能指下一份集合，不是已经换了人 interchangeable。本页钉 not already rotated 单句。

3. **看见字段名对得上 / 看见填了 next_validators_hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1055 preprend-nothash interchangeable / 1056 preprend-notmade interchangeable，也不是已经 ExtendVoteRequest.next_validators_hash 就已经是 Finalize 请求栏 interchangeable / 411 extrest interchangeable。**  
   官方把字段名对得上和已经交差分开。看见字段名对得上，不是已经交差 interchangeable。426 prepreqend vs finreq bundled unbundling 在本页 item 1 启动。

怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.next_validators_hash not already finalize-hash ≠ 已经是 Finalize 请求栏的 next_validators_hash interchangeable：** 官方把 Prepare 这份下一验证者集合默克尔根和已经是 Finalize 请求栏分开。
- **看见能指下一份集合 not already rotated ≠ 已经换了人 interchangeable：** 官方把能指下一份集合和已经换了人分开。
- **看见字段名对得上 not already settled ≠ 已经交差 interchangeable：** 官方把字段名对得上和已经交差分开；426 prepreqend vs finreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.next_validators_hash 是下一验证者集合默克尔根 | 不是已经是 Finalize 请求栏的 next_validators_hash | 不是 Finalize 请求 next_validators_hash 就已经是同一套字段（394） |
| 看见能指下一份集合 | 不是已经换了人 | 不是 ExtendVoteRequest.next_validators_hash 就已经是 Finalize 请求栏（411） |
| 看见字段名对得上 | 不是已经交差 | 不是 proposer_address 就已经造了这份提案（1056） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.next_validators_hash not already finalize-hash / not already rotated / not already settled 正式三事（426 余量），必须分开是不是已经是 Finalize 请求栏的 next_validators_hash、是不是已经换了人、是不是已经交差。可以跳过「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash」。不要另写怎样写 Prepare 请求末栏。426 prepreqend vs finreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-preprend-notmade-vs-bundled.md`](worked-example-preprend-notmade-vs-bundled.md)（不变量 1056 item 2）。

## 本页不抄

- 怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- Prepare 请求末栏 bundled。那是不变量 426。
- Finalize 请求 next_validators_hash 就已经是同一套字段。那是不变量 394。
- ExtendVoteRequest.next_validators_hash 就已经是 Finalize 请求栏。那是不变量 411。
