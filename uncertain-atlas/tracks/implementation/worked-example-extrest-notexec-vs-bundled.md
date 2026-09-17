# 例：看见 ExtendVoteRequest.txs is not already executed interchangeable / not already settled interchangeable / not already whole-block interchangeable

**层次**：实现 / ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量）/ not 1034 extrest-notexec interchangeable / not 411 extreqtxs-vs-fintxs bundled interchangeable」，不是 ExtendVote 请求余栏 bundled（411），也不是 Finalize 按应用自己的规则确定地执行 txs 就已经交差（408），也不是 ProcessProposalRequest.txs 就已经执行那些交易（419）。不要另写怎样写 ExtendVote 请求余栏。

## 官方三件事

1. **看见 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表 / 看见填了 txs 这份栏 is not already 已经执行那些交易 interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1034 extrest-notexec interchangeable / 1035 extrest-notlocal interchangeable / 411 extreqtxs item 2 last commit interchangeable，也不是已经 ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事 bundled（411 item 1 余量） interchangeable / 411 extreqtxs item 1 interchangeable。**  
   官方写：txs 是扩展要指的那份块的交易列表。看见填了 txs，不是已经 Finalize 按应用自己的规则确定地执行 txs、再交还控制权那种已经交差 interchangeable——本页从 411 item 1 侧钉 not already executed 单句。411 extreqtxs vs fintxs bundled unbundling 在本页 item 1 启动。

2. **看见有交易列表 / 看见填了 txs / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1034 extrest-notexec interchangeable / 411 extreqtxs item 3 next hash interchangeable / 1036 extrest-nothash interchangeable，也不是已经 Finalize 按应用自己的规则确定地执行 txs 就已经交差 interchangeable / 408 finexec interchangeable。**  
   官方把有交易列表和已经交差分开。看见有交易列表，不是已经交差 interchangeable。本页钉 not already settled 单句。

3. **看见能指 / 看见填了 txs / 这份栏 is not already 已经整块跑了 interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1034 extrest-notexec interchangeable / 1035 extrest-notlocal interchangeable，也不是已经 ProcessProposalRequest.txs 就已经执行那些交易 interchangeable / 419 procreq interchangeable。**  
   官方把能指和已经整块跑了分开。看见能指，不是已经整块跑了 interchangeable。411 extreqtxs vs fintxs bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.txs not already executed ≠ 已经执行那些交易 interchangeable：** 官方把扩展要指的交易列表和已经执行那些交易分开。
- **看见有交易列表 not already settled ≠ 已经交差 interchangeable：** 官方把有交易列表和已经交差分开。
- **看见能指 not already whole-block ≠ 已经整块跑了 interchangeable：** 官方把能指和已经整块跑了分开；411 extreqtxs vs fintxs bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.txs 是扩展要指的那份块的交易列表 | 不是已经执行那些交易 | 不是 Finalize 按应用自己的规则确定地执行 txs 就已经交差（408） |
| 看见有交易列表 | 不是已经交差 | 不是 ProcessProposalRequest.txs 就已经执行那些交易（419） |
| 看见能指 | 不是已经整块跑了 | 不是 proposed_last_commit 就已经交差 local_last_commit（1035） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量），必须分开是不是已经执行那些交易、是不是已经交差、是不是已经整块跑了。可以跳过「看见填了 ExtendVote 请求余栏就已经执行那些交易」。不要另写怎样写 ExtendVote 请求余栏。411 extreqtxs vs fintxs bundled unbundling 在本页 item 1 启动；续 [`worked-example-extrest-notlocal-vs-bundled.md`](worked-example-extrest-notlocal-vs-bundled.md)（不变量 1035 item 2）。

## 本页不抄

- 怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit。
- ExtendVote 请求余栏 bundled。那是不变量 411。
- Finalize 按应用自己的规则确定地执行 txs 就已经交差。那是不变量 408。
- ProcessProposalRequest.txs 就已经执行那些交易。那是不变量 419。
