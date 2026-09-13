# 例：看见 ProcessProposal Contains all information on the proposed block needed to fully execute it 不是已经执行那些交易；看见 ProcessProposalRequest 八栏齐不是已经只有 PrepareProposalResponse.txs；看见含执行所需全部信息不是已经是 FinalizeBlockRequest 刚决定那块的字段

**层次**：实现 / ProcessProposal 含执行所需全部信息正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Contains all information on the proposed block needed to fully execute it 不是已经执行那些交易 / ProcessProposalRequest 八栏齐不是已经只有 PrepareProposalResponse.txs / 含执行所需全部信息不是已经是 FinalizeBlockRequest 刚决定那块的字段」，不是 Finalize 执行余量那套 bundled，也不是 Process 请求栏单栏定义，也不是 Process MAY 整块执行须留 candidate state 那套。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 官方三件事

规范把 ProcessProposal 含执行所需全部信息、Request 八栏齐、能整块执行所需信息写成三件独立的实现事，不是「看见 Process 含全部信息就已经执行那些交易、已经只有 txs、已经是 Finalize 字段 interchangeable」一件事：

1. **看见 ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见含执行所需全部信息 不是已经执行那些交易，也不是已经 Finalize 跑过。**  
   官方写：Contains all information on the proposed block needed to fully execute it。看见能整块执行所需信息，不是已经 `FinalizeBlockRequest.txs` 已经按应用自己的规则确定地执行过。看见有全部信息，不是已经 Process MAY 像 Finalize 整块执行（452）就已经是同一句 interchangeable。看见能 fully execute，不是已经交差。
2. **看见 `ProcessProposalRequest` 有 `txs` + `proposed_last_commit` + `misbehavior` + `hash` + `height` + `time` + `next_validators_hash` + `proposer_address` / 看见八栏齐 不是已经只有 `PrepareProposalResponse.txs`，也不是已经只有 raw proposal。**  
   官方 Request 表写八栏：`txs` 是拟议块的交易列表；`proposed_last_commit` 是从拟议块里的信息拿到的上一份提交信息；`misbehavior` 是过错验证者信息列表；`hash` 是拟议块的哈希；`height` / `time` 是拟议块的高度和时间戳；`next_validators_hash` 是下一验证者集合默克尔根；`proposer_address` 是造了这份提案的验证者地址。`PrepareProposalResponse` 只有 `txs`。看见八栏齐，不是已经 Prepare 回包就已经齐。看见能 fully execute，不是已经只有交易列表就够。
3. **看见含提案块上执行所需的全部信息 / 看见填了信息 不是已经是 FinalizeBlockRequest 刚决定那块的字段，也不是已经只有 txs 字段就够。**  
   官方写：Contains all information on the proposed block needed to fully execute it。看见拟议块上执行所需，不是已经是 `FinalizeBlockRequest.decided_last_commit` 从刚决定那块拿到那种已经交差。看见全部信息，不是已经 `FinalizeBlockRequest.hash` 是已决块的哈希那种 interchangeable。看见能执行，不是已经 Finalize 含刚决定那块的字段（363）就已经是同一句 interchangeable。

怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐是规范里的做法，本页不抄。Finalize 执行余量里 Process 含提案块上执行所需的全部信息（408）是 bundled 三事之一，Process 请求栏（419–420 / 427）是单栏定义，ProcessProposal 候选执行（452）是 MAY 整块执行 / candidate state / read-only 那套另一切片，本页不抄。

## 官方为什么这样拆

- **Contains all information needed to fully execute ≠ 已经执行那些交易 / 已经 Finalize 跑过：** 官方把「信息够执行」和「已经执行」分开。
- **Request 八栏齐 ≠ 已经只有 PrepareProposalResponse.txs / 已经只有 raw proposal：** 官方把 Process 请求八栏和 Prepare 回包只有 txs 分开。
- **含执行所需全部信息 ≠ 已经是 FinalizeBlockRequest 刚决定那块的字段：** 官方把拟议块上执行所需信息和已决块字段分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Contains all information needed to fully execute | 不是已经执行那些交易 | 不是 Process MAY 整块执行就已经交差（452） |
| Request 八栏齐 | 不是已经只有 PrepareProposalResponse.txs | 不是 ProcessProposalRequest.txs 是拟议块的交易列表就已经执行那些交易（419） |
| 含执行所需全部信息 | 不是已经是 FinalizeBlockRequest 刚决定那块的字段 | 不是 Finalize 执行余量 bundled 三事（408） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 含全部信息就已经执行那些交易、已经只有 txs、已经是 Finalize 字段 interchangeable」，必须分开 Contains all information needed to fully execute 是不是已经执行那些交易、Request 八栏齐是不是已经只有 PrepareProposalResponse.txs、含执行所需全部信息是不是已经是 FinalizeBlockRequest 刚决定那块的字段。可以跳过「看见 Process 含全部信息就已经执行那些交易」。不要另写怎样从 ProcessProposalRequest 拿齐八栏。

## 本页不抄

- 怎样从 ProcessProposalRequest 拿齐八栏、怎样和 Finalize 请求栏对齐。
- Finalize 执行余量 bundled 三事。那是不变量 408。
- Process 请求栏 / 请求余栏 / 请求末栏单栏定义。那是不变量 419–420 / 427。
- Process MAY 整块执行 / 须留 candidate state / read-only 处理。那是不变量 452。
