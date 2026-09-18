# 例：看见 PrepareProposalRequest.proposer_address is not already made interchangeable / not already header-known interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量）/ not 1056 preprend-notmade interchangeable / not 426 prepreqend-vs-finreq bundled interchangeable」，不是 Prepare 请求末栏 bundled（426），也不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413），也不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359）。不要另写怎样写 Prepare 请求末栏。

## 官方三件事

1. **看见 PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址 / 看见填了 proposer_address 这份栏 is not already 已经造了这份提案 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1056 preprend-notmade interchangeable / 1055 preprend-nothash interchangeable / 426 prepreqend item 1 next_hash interchangeable，也不是已经 PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事 bundled（426 item 2 余量） interchangeable / 426 prepreqend item 2 interchangeable。**  
   官方写：proposer_address 是正在造这份提案的验证者地址。看见填了 proposer_address，不是已经 ExtendVoteRequest.proposer_address 那种已经知道本头哈希 interchangeable——本页从 426 item 2 侧钉 not already made 单句。426 prepreqend vs finreq bundled unbundling 在本页 item 2 续。

2. **看见正在造 / 看见填了 proposer_address / 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1056 preprend-notmade interchangeable / 426 prepreqend item 3 fintime interchangeable / 1057 preprend-notts interchangeable，也不是已经 ExtendVoteRequest.proposer_address 就已经知道本头哈希 interchangeable / 413 extmis interchangeable。**  
   官方把正在造和已经知道本头哈希分开。看见正在造，不是已经知道本头哈希 interchangeable。本页钉 not already header-known 单句。

3. **看见能指正在造的人 / 看见填了 proposer_address / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1056 preprend-notmade interchangeable / 1055 preprend-nothash interchangeable，也不是已经 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希 interchangeable / 359 samefields interchangeable。**  
   官方把能指正在造的人和已经交差分开。看见能指正在造的人，不是已经交差 interchangeable。426 prepreqend vs finreq bundled unbundling 在本页 item 2 续。

怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.proposer_address not already made ≠ 已经造了这份提案 interchangeable：** 官方把正在造这份提案的验证者地址和已经造了这份提案分开。
- **看见正在造 not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把正在造和已经知道本头哈希分开。
- **看见能指正在造的人 not already settled ≠ 已经交差 interchangeable：** 官方把能指正在造的人和已经交差分开；426 prepreqend vs finreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.proposer_address 是正在造这份提案的验证者地址 | 不是已经造了这份提案 | 不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413） |
| 看见正在造 | 不是已经知道本头哈希 | 不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359） |
| 看见能指正在造的人 | 不是已经交差 | 不是 FinalizeBlockRequest.time 就已经对上了拟议块头（1057） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.proposer_address not already made / not already header-known / not already settled 正式三事（426 余量），必须分开是不是已经造了这份提案、是不是已经知道本头哈希、是不是已经交差。可以跳过「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash」。不要另写怎样写 Prepare 请求末栏。426 prepreqend vs finreq bundled unbundling 在本页 item 2 续；续 [`worked-example-preprend-notts-vs-bundled.md`](worked-example-preprend-notts-vs-bundled.md)（不变量 1057 item 3）。

## 本页不抄

- 怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- Prepare 请求末栏 bundled。那是不变量 426。
- ExtendVoteRequest.proposer_address 就已经知道本头哈希。那是不变量 413。
- Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希。那是不变量 359。
