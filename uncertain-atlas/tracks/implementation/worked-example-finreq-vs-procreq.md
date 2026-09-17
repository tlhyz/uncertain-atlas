# 例：看见 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息不是已经交差 local_last_commit；看见 FinalizeBlockRequest.height 是已决块的高度不是已经对上了拟议块头；看见 FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表不是已经执行那些交易

**层次**：实现 / Finalize 请求栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息不是已经交差 local_last_commit / FinalizeBlockRequest.height 是已决块的高度不是已经对上了拟议块头 / FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表不是已经执行那些交易」，不是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit，也不是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差。不要另写怎样写 Finalize 请求栏。

## 官方三件事

规范把 FinalizeBlock Request 表上 `decided_last_commit` 是从刚决定那块拿到的上一份提交信息、`height` 是已决块的高度、`txs` 是作为这块一部分提交的交易列表写成三件独立的实现事，不是「看见填了 Finalize 请求栏就已经交差 local_last_commit、已经对上了拟议块头、已经执行那些交易」一件事：

1. **看见 `FinalizeBlockRequest.decided_last_commit` 是从刚决定那块拿到的上一份提交信息 / 看见填了 decided_last_commit 不是已经交差 local_last_commit，也不是已经是 ProcessProposalRequest.proposed_last_commit。**  
   官方写：`decided_last_commit` 是上一份提交信息，从刚决定那块拿到。看见填了 decided_last_commit，不是已经 `ProcessProposalRequest.proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息那种已经交差 local_last_commit。看见从刚决定那块拿到，不是已经可以用 `decided_last_commit` 和 `misbehavior` 定奖惩那种已经罚没。看见能指上一份提交，不是已经交差。
2. **看见 `FinalizeBlockRequest.height` 是已决块的高度 / 看见填了 height 不是已经对上了拟议块头，也不是已经是 ProcessProposalRequest.height。**  
   官方写：`height` 是已决块的高度。看见填了 height，不是已经 `ProcessProposalRequest.height` 是拟议块的高度那种已经对上了拟议块头。看见有已决块高度，不是已经 Finalize 的 height / time 对上拟议块头那种已经验过块头。看见能指高度，不是已经交差。
3. **看见 `FinalizeBlockRequest.txs` 是作为这块一部分提交的交易列表 / 看见填了 txs 不是已经执行那些交易，也不是已经是 ProcessProposalRequest.txs。**  
   官方写：`txs` 是作为这块一部分提交的交易列表。看见填了 txs，不是已经 Finalize 按应用自己的规则确定地执行 `txs`、再交还控制权那种已经交差。看见有交易列表，不是已经 `ProcessProposalRequest.txs` 是拟议块的交易列表那种已经执行那些交易。看见能指交易，不是已经交差。

怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs 是规范里的做法，本页不抄。ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit 是不变量 420，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 ≠ 已经交差 local_last_commit：** 官方把 Finalize 请求表上这份从刚决定那块拿到的上一份提交和 Process 请求表上那份从拟议块拿到的上一份提交分开。
- **FinalizeBlockRequest.height 是已决块的高度 ≠ 已经对上了拟议块头：** 官方把 Finalize 请求表上这份已决块高度和 Process 请求表上那份拟议块高度分开。
- **FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表 ≠ 已经执行那些交易：** 官方把 Finalize 请求表上这份作为这块一部分提交的交易列表和 Usage 里那份确定地执行 txs、再交还控制权分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息 | 不是已经交差 local_last_commit | 不是 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit（420） |
| FinalizeBlockRequest.height 是已决块的高度 | 不是已经对上了拟议块头 | 不是 ProcessProposalRequest.height 是拟议块的高度就已经对上了拟议块头（419） |
| FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表 | 不是已经执行那些交易 | 不是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差（408） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 请求栏就已经交差 local_last_commit、已经对上了拟议块头、已经执行那些交易」，必须分开 FinalizeBlockRequest.decided_last_commit 是从刚决定那块拿到的上一份提交信息是不是已经交差 local_last_commit、FinalizeBlockRequest.height 是已决块的高度是不是已经对上了拟议块头、FinalizeBlockRequest.txs 是作为这块一部分提交的交易列表是不是已经执行那些交易。可以跳过「看见填了 Finalize 请求栏就已经交差 local_last_commit」。不要另写怎样写 Finalize 请求栏。422 finreq vs procreq bundled unbundling 完成（1040 item 1 / 1041 item 2 / 1042 item 3）；精读 [`worked-example-finreqcol-notlocal-vs-bundled.md`](worked-example-finreqcol-notlocal-vs-bundled.md)（不变量 1040 item 1）。

## 本页不抄

- 怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs。
- ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息就已经交差 local_last_commit。那是不变量 420。
- ProcessProposalRequest.height 是拟议块的高度就已经对上了拟议块头。那是不变量 419。
- Finalize 按应用自己的规则确定地执行 txs、再交还控制权就已经交差。那是不变量 408。
