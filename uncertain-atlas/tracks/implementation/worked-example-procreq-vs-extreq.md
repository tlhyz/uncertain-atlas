# 例：看见 ProcessProposalRequest.txs 是拟议块的交易列表不是已经执行那些交易；看见 ProcessProposalRequest.hash 是拟议块的哈希不是已经跑过 Process；看见 ProcessProposalRequest.height 是拟议块的高度不是已经对上了拟议块头

**层次**：实现 / Process 请求栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.txs 是拟议块的交易列表不是已经执行那些交易 / ProcessProposalRequest.hash 是拟议块的哈希不是已经跑过 Process / ProcessProposalRequest.height 是拟议块的高度不是已经对上了拟议块头」，不是 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表就已经执行那些交易，也不是 Process 的 height / time 对上拟议块头就已经验过块头。不要另写怎样写 Process 请求栏。

## 官方三件事

规范把 ProcessProposal Request 表上 `txs` 是拟议块的交易列表、`hash` 是拟议块的哈希、`height` 是拟议块的高度写成三件独立的实现事，不是「看见填了 Process 请求栏就已经执行那些交易、已经跑过 Process、已经对上了拟议块头」一件事：

1. **看见 `ProcessProposalRequest.txs` 是拟议块的交易列表 / 看见填了 txs 不是已经执行那些交易，也不是已经是 ExtendVoteRequest.txs。**  
   官方写：`txs` 是拟议块的交易列表。看见填了 txs，不是已经 `ExtendVoteRequest.txs` 是扩展要指的那份块的交易列表那种已经执行那些交易。看见有交易列表，不是已经整块跑了。看见能指，不是已经交差。
2. **看见 `ProcessProposalRequest.hash` 是拟议块的哈希 / 看见填了 hash 不是已经跑过 Process，也不是已经是 ExtendVoteRequest.hash。**  
   官方写：`hash` 是拟议块的哈希。看见填了 hash，不是已经 `ExtendVoteRequest.hash` 是扩展要指的那份拟议块头哈希那种已经跑过 Process。看见有拟议块哈希，不是已经请求里的 hash 那种不保证已经对该块跑过 Process。看见能指，不是已经交差。
3. **看见 `ProcessProposalRequest.height` 是拟议块的高度 / 看见填了 height 不是已经对上了拟议块头，也不是已经是 ExtendVoteRequest.height。**  
   官方写：`height` 是拟议块的高度。看见填了 height，不是已经 Process 的 height / time 对上拟议块头那种已经验过块头。看见有高度，不是已经 `ExtendVoteRequest.height` 是拟议块高度（用来对一下）那种已经对上了拟议块。看见能指，不是已经交差。

怎样写 Process 请求栏、怎样填 txs、怎样填 hash 是规范里的做法，本页不抄。ExtendVoteRequest.txs 是扩展要指的那份块的交易列表就已经执行那些交易是不变量 411，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.txs 是拟议块的交易列表 ≠ 已经执行那些交易：** 官方把 Process 请求表上这份交易列表和 ExtendVote 请求表上那份扩展要指的交易列表分开。
- **ProcessProposalRequest.hash 是拟议块的哈希 ≠ 已经跑过 Process：** 官方把 Process 请求表上这份拟议块哈希和 ExtendVote 请求表上那份扩展要指的头哈希分开。
- **ProcessProposalRequest.height 是拟议块的高度 ≠ 已经对上了拟议块头：** 官方把 Process 请求表上这份拟议块高度和 Usage 里那份 height / time 对上拟议块头分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.txs 是拟议块的交易列表 | 不是已经执行那些交易 | 不是 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表就已经执行那些交易（411） |
| ProcessProposalRequest.hash 是拟议块的哈希 | 不是已经跑过 Process | 不是 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希就已经跑过 Process（410） |
| ProcessProposalRequest.height 是拟议块的高度 | 不是已经对上了拟议块头 | 不是 Process 的 height / time 对上拟议块头就已经验过块头（417） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Process 请求栏就已经执行那些交易、已经跑过 Process、已经对上了拟议块头」，必须分开 ProcessProposalRequest.txs 是拟议块的交易列表是不是已经执行那些交易、ProcessProposalRequest.hash 是拟议块的哈希是不是已经跑过 Process、ProcessProposalRequest.height 是拟议块的高度是不是已经对上了拟议块头。可以跳过「看见填了 Process 请求栏就已经执行那些交易」。不要另写怎样写 Process 请求栏。419 procreq vs extreq bundled unbundling 完成（1025 item 1 / 1026 item 2 / 1027 item 3）；精读 [`worked-example-procreq-notexec-vs-bundled.md`](worked-example-procreq-notexec-vs-bundled.md)（不变量 1025 item 1）。

## 本页不抄

- 怎样写 Process 请求栏、怎样填 txs、怎样填 hash。
- ExtendVoteRequest.txs 是扩展要指的那份块的交易列表就已经执行那些交易。那是不变量 411。
- ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希就已经跑过 Process。那是不变量 410。
- Process 的 height / time 对上拟议块头就已经验过块头。那是不变量 417。
