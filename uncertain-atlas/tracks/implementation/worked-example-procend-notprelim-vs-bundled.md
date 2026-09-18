# 例：看见 PrepareProposalResponse.txs is not already preliminary interchangeable / not already same-round interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量）/ not 1060 procend-notprelim interchangeable / not 427 procreqend-vs-prepreq bundled interchangeable」，不是 Process 请求末栏 bundled（427），也不是 PrepareProposalRequest.txs 就已经跑过 Process（423），也不是 FinalizeBlockRequest.txs 就已经执行那些交易（422）。不要另写怎样写 Process 请求末栏。

## 官方三件事

1. **看见 PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表 / 看见回了 txs 这份栏 is not already 已经是初步交易列表 interchangeable，也不是已经 Process 请求末栏 bundled（427） interchangeable / 1060 procend-notprelim interchangeable / 1058 procend-nothash interchangeable / 427 procreqend item 1 next_hash interchangeable，也不是已经 PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事 bundled（427 item 3 余量） interchangeable / 427 procreqend item 3 interchangeable。**  
   官方写：txs 是可能改过的、挑进拟议块的交易列表。看见回了 txs，不是已经 PrepareProposalRequest.txs 那种已经跑过 Process interchangeable——本页从 427 item 3 侧钉 not already preliminary 单句。427 procreqend vs prepreq bundled unbundling 在本页 item 3 完成。

2. **看见可能改过 / 看见回了 txs / 这份栏 is not already 已经保证是这一次 interchangeable，也不是已经 Process 请求末栏 bundled（427） interchangeable / 1060 procend-notprelim interchangeable / 427 procreqend item 2 proposer interchangeable / 1059 procend-notmaking interchangeable，也不是已经 PrepareProposalRequest.txs 就已经跑过 Process interchangeable / 423 prepreqcol interchangeable。**  
   官方把可能改过和已经保证是这一次分开。看见可能改过，不是已经保证是这一次 interchangeable。本页钉 not already same-round 单句。

3. **看见能指回包列表 / 看见回了 txs / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求末栏 bundled（427） interchangeable / 1060 procend-notprelim interchangeable / 1058 procend-nothash interchangeable，也不是已经 FinalizeBlockRequest.txs 就已经执行那些交易 interchangeable / 422 finreqcol interchangeable。**  
   官方把能指回包列表和已经交差分开。看见能指回包列表，不是已经交差 interchangeable。427 procreqend vs prepreq bundled unbundling 在本页 item 3 完成。

怎样写 Process 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalResponse.txs not already preliminary ≠ 已经是初步交易列表 interchangeable：** 官方把可能改过的、挑进拟议块的交易列表和已经是初步交易列表分开。
- **看见可能改过 not already same-round ≠ 已经保证是这一次 interchangeable：** 官方把可能改过和已经保证是这一次分开。
- **看见能指回包列表 not already settled ≠ 已经交差 interchangeable：** 官方把能指回包列表和已经交差分开；427 procreqend vs prepreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalResponse.txs 是可能改过的、挑进拟议块的交易列表 | 不是已经是初步交易列表 | 不是 PrepareProposalRequest.txs 就已经跑过 Process（423） |
| 看见可能改过 | 不是已经保证是这一次 | 不是 ProcessProposalRequest.txs 等于 PrepareProposalResponse.txs 就已经保证是这一次 |
| 看见能指回包列表 | 不是已经交差 | 不是 FinalizeBlockRequest.txs 就已经执行那些交易（422） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量），必须分开是不是已经是初步交易列表、是不是已经保证是这一次、是不是已经交差。可以跳过「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash」。不要另写怎样写 Process 请求末栏。427 procreqend vs prepreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Process 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- Process 请求末栏 bundled。那是不变量 427。
- PrepareProposalRequest.txs 就已经跑过 Process。那是不变量 423。
- FinalizeBlockRequest.txs 就已经执行那些交易。那是不变量 422。
