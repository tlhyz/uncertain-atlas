# 例：看见 FinalizeBlockRequest.next_validators_hash is not already process-hash interchangeable / not already prepare-hash interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量）/ not 1063 finrestr-notproc interchangeable / not 428 finreqrest-vs-procreq bundled interchangeable」，不是 Finalize 请求余栏 bundled（428），也不是 ProcessProposalRequest.next_validators_hash 就已经是 Prepare 请求末栏（427），也不是 PrepareProposalRequest.next_validators_hash 就已经是 Finalize 请求栏（426）。不要另写怎样写 Finalize 请求余栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根 / 看见填了 next_validators_hash 这份栏 is not already 已经是 Process 请求末栏的 next_validators_hash interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1063 finrestr-notproc interchangeable / 1061 finrestr-nothash interchangeable / 428 finreqrest item 1 hash interchangeable，也不是已经 FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事 bundled（428 item 3 余量） interchangeable / 428 finreqrest item 3 interchangeable。**  
   官方写：next_validators_hash 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经 ProcessProposalRequest.next_validators_hash 那种已经是 Prepare 请求末栏 interchangeable——本页从 428 item 3 侧钉 not already process-hash 单句。428 finreqrest vs procreq bundled unbundling 在本页 item 3 完成。

2. **看见能指下一份集合 / 看见填了 next_validators_hash / 这份栏 is not already 已经是 Prepare 请求末栏的 next_validators_hash interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1063 finrestr-notproc interchangeable / 428 finreqrest item 2 misbehavior interchangeable / 1062 finrestr-notpunish interchangeable，也不是已经 ProcessProposalRequest.next_validators_hash 就已经是 Prepare 请求末栏 interchangeable / 427 procend interchangeable。**  
   官方把能指下一份集合和已经是 Prepare 请求末栏分开。看见能指下一份集合，不是已经是 Prepare 请求末栏 interchangeable。本页钉 not already prepare-hash 单句。

3. **看见字段名对得上 / 看见填了 next_validators_hash / 这份栏 is not already 已经换了人 interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1063 finrestr-notproc interchangeable / 1061 finrestr-nothash interchangeable，也不是已经 PrepareProposalRequest.next_validators_hash 就已经是 Finalize 请求栏 interchangeable / 426 preprend interchangeable。**  
   官方把字段名对得上和已经换了人分开。看见字段名对得上，不是已经换了人 interchangeable。428 finreqrest vs procreq bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.next_validators_hash not already process-hash ≠ 已经是 Process 请求末栏的 next_validators_hash interchangeable：** 官方把 Finalize 这份下一验证者集合默克尔根和已经是 Process 请求末栏分开。
- **看见能指下一份集合 not already prepare-hash ≠ 已经是 Prepare 请求末栏的 next_validators_hash interchangeable：** 官方把能指下一份集合和已经是 Prepare 请求末栏分开。
- **看见字段名对得上 not already settled ≠ 已经换了人 interchangeable：** 官方把字段名对得上和已经换了人分开；428 finreqrest vs procreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.next_validators_hash 是下一验证者集合默克尔根 | 不是已经是 Process 请求末栏的 next_validators_hash | 不是 ProcessProposalRequest.next_validators_hash 就已经是 Prepare 请求末栏（427） |
| 看见能指下一份集合 | 不是已经是 Prepare 请求末栏的 next_validators_hash | 不是 PrepareProposalRequest.next_validators_hash 就已经是 Finalize 请求栏（426） |
| 看见字段名对得上 | 不是已经换了人 | 不是 hash 就已经是 ProcessProposalRequest.hash（1061） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量），必须分开是不是已经是 Process 请求末栏的 next_validators_hash、是不是已经是 Prepare 请求末栏的 next_validators_hash、是不是已经换了人。可以跳过「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash」。不要另写怎样写 Finalize 请求余栏。428 finreqrest vs procreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior。
- Finalize 请求余栏 bundled。那是不变量 428。
- ProcessProposalRequest.next_validators_hash 就已经是 Prepare 请求末栏。那是不变量 427。
- PrepareProposalRequest.next_validators_hash 就已经是 Finalize 请求栏。那是不变量 426。
