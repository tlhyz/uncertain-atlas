# 例：看见 FinalizeBlockRequest.time is not already header-aligned interchangeable / not already prepare-time interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量）/ not 1057 preprend-notts interchangeable / not 426 prepreqend-vs-finreq bundled interchangeable」，不是 Prepare 请求末栏 bundled（426），也不是 PrepareProposalRequest.time 就已经对上了拟议块头（424），也不是 ProcessProposalRequest.time 就已经验过票上时间（420）。不要另写怎样写 Prepare 请求末栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.time 是已决块的时间戳 / 看见填了 time 这份栏 is not already 已经对上了拟议块头 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1057 preprend-notts interchangeable / 1055 preprend-nothash interchangeable / 426 prepreqend item 1 next_hash interchangeable，也不是已经 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事 bundled（426 item 3 余量） interchangeable / 426 prepreqend item 3 interchangeable。**  
   官方写：time 是已决块的时间戳。看见填了 time，不是已经 PrepareProposalRequest.time 那种已经对上了拟议块头 interchangeable——本页从 426 item 3 侧钉 not already header-aligned 单句。426 prepreqend vs finreq bundled unbundling 在本页 item 3 完成。

2. **看见有已决块时间戳 / 看见填了 time / 这份栏 is not already 已经是 PrepareProposalRequest.time interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1057 preprend-notts interchangeable / 426 prepreqend item 2 proposer interchangeable / 1056 preprend-notmade interchangeable，也不是已经 PrepareProposalRequest.time 就已经对上了拟议块头 interchangeable / 424 preprestr interchangeable。**  
   官方把有已决块时间戳和已经是 PrepareProposalRequest.time 分开。看见有已决块时间戳，不是已经是 PrepareProposalRequest.time interchangeable。本页钉 not already prepare-time 单句。

3. **看见能指已决时间 / 看见填了 time / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求末栏 bundled（426） interchangeable / 1057 preprend-notts interchangeable / 1055 preprend-nothash interchangeable，也不是已经 ProcessProposalRequest.time 就已经验过票上时间 interchangeable / 420 procrestr interchangeable。**  
   官方把能指已决时间和已经交差分开。看见能指已决时间，不是已经交差 interchangeable。426 prepreqend vs finreq bundled unbundling 在本页 item 3 完成。

怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.time not already header-aligned ≠ 已经对上了拟议块头 interchangeable：** 官方把已决块的时间戳和已经对上了拟议块头分开。
- **看见有已决块时间戳 not already prepare-time ≠ 已经是 PrepareProposalRequest.time interchangeable：** 官方把有已决块时间戳和已经是 PrepareProposalRequest.time 分开。
- **看见能指已决时间 not already settled ≠ 已经交差 interchangeable：** 官方把能指已决时间和已经交差分开；426 prepreqend vs finreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.time 是已决块的时间戳 | 不是已经对上了拟议块头 | 不是 PrepareProposalRequest.time 就已经对上了拟议块头（424） |
| 看见有已决块时间戳 | 不是已经是 PrepareProposalRequest.time | 不是 ProcessProposalRequest.time 就已经验过票上时间（420） |
| 看见能指已决时间 | 不是已经交差 | 不是 next_validators_hash 就已经是 Finalize 请求栏（1055） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量），必须分开是不是已经对上了拟议块头、是不是已经是 PrepareProposalRequest.time、是不是已经交差。可以跳过「看见填了 Prepare 请求末栏就已经是 Finalize 请求栏的 next_validators_hash」。不要另写怎样写 Prepare 请求末栏。426 prepreqend vs finreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Prepare 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- Prepare 请求末栏 bundled。那是不变量 426。
- PrepareProposalRequest.time 就已经对上了拟议块头。那是不变量 424。
- ProcessProposalRequest.time 就已经验过票上时间。那是不变量 420。
