# 例：看见 FinalizeBlockRequest.txs is not already executed interchangeable / not already process-txs interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量）/ not 1042 finreqcol-notexec interchangeable / not 422 finreq-vs-procreq bundled interchangeable」，不是 Finalize 请求栏 bundled（422），也不是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差（408），也不是 ExtendVoteRequest.txs 就已经执行那些交易（411）。不要另写怎样写 Finalize 请求栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表 / 看见填了 txs 这份栏 is not already 已经执行那些交易 interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1042 finreqcol-notexec interchangeable / 1040 finreqcol-notlocal interchangeable / 422 finreq item 1 decided_last_commit interchangeable，也不是已经 FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事 bundled（422 item 3 余量） interchangeable / 422 finreq item 3 interchangeable。**  
   官方写：txs 是作为这块一部分提交的交易列表。看见填了 txs，不是已经 Finalize 按应用自己的规则确定地执行 txs、再交还控制权那种已经交差 interchangeable——本页从 422 item 3 侧钉 not already executed 单句。422 finreq vs procreq bundled unbundling 在本页 item 3 完成。

2. **看见有交易列表 / 看见填了 txs / 这份栏 is not already 已经是 ProcessProposalRequest.txs interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1042 finreqcol-notexec interchangeable / 422 finreq item 2 height interchangeable / 1041 finreqcol-nothead interchangeable，也不是已经 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差 interchangeable / 408 fintxs interchangeable。**  
   官方把有交易列表和已经是 ProcessProposalRequest.txs 分开。看见有交易列表，不是已经是 ProcessProposalRequest.txs interchangeable。本页钉 not already process-txs 单句。

3. **看见能指交易 / 看见填了 txs / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1042 finreqcol-notexec interchangeable / 1040 finreqcol-notlocal interchangeable，也不是已经 ExtendVoteRequest.txs 就已经执行那些交易 interchangeable / 411 extrest interchangeable。**  
   官方把能指交易和已经交差分开。看见能指交易，不是已经交差 interchangeable。422 finreq vs procreq bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.txs not already executed ≠ 已经执行那些交易 interchangeable：** 官方把作为这块一部分提交的交易列表和已经执行那些交易分开。
- **看见有交易列表 not already process-txs ≠ 已经是 ProcessProposalRequest.txs interchangeable：** 官方把有交易列表和已经是 ProcessProposalRequest.txs 分开。
- **看见能指交易 not already settled ≠ 已经交差 interchangeable：** 官方把能指交易和已经交差分开；422 finreq vs procreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表 | 不是已经执行那些交易 | 不是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差（408） |
| 看见有交易列表 | 不是已经是 ProcessProposalRequest.txs | 不是 ProcessProposalRequest.txs 就已经执行那些交易（419） |
| 看见能指交易 | 不是已经交差 | 不是 ExtendVoteRequest.txs 就已经执行那些交易（411） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.txs not already executed / not already process-txs / not already settled 正式三事（422 余量），必须分开是不是已经执行那些交易、是不是已经是 ProcessProposalRequest.txs、是不是已经交差。可以跳过「看见填了 Finalize 请求栏就已经交差 local_last_commit」。不要另写怎样写 Finalize 请求栏。422 finreq vs procreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs。
- Finalize 请求栏 bundled。那是不变量 422。
- Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差。那是不变量 408。
- ExtendVoteRequest.txs 就已经执行那些交易。那是不变量 411。
