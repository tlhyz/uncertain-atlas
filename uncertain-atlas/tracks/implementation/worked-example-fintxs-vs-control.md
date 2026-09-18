# 例：看见 Finalize 按应用自己的规则确定地执行 txs、再交还控制权不是已经交差；看见 Process 含提案块上执行所需的全部信息不是已经是刚决定那块的字段；看见 Process 可以像在处理 Finalize 那样整块执行不是已经是 ExecuteTxState

**层次**：实现 / Finalize 执行余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 按应用自己的规则确定地执行 txs、再交还控制权不是已经交差 / Process 含提案块上执行所需的全部信息不是已经是刚决定那块的字段 / Process 可以像在处理 Finalize 那样整块执行不是已经是 ExecuteTxState」，不是 Finalize 实现必须确定因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样，也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。不要另写怎样写 Finalize 执行余量。

## 官方三件事

规范把 Finalize 按应用自己的规则确定地执行 txs 再交还控制权、Process 含提案块上执行所需的全部信息、Process 可以像在处理 Finalize 那样整块执行写成三件独立的实现事，不是「看见填了 Finalize 执行余量就已经交差、已经是刚决定那块的字段、已经是 ExecuteTxState」一件事：

1. **看见 Finalize 按应用自己的规则确定地执行 `txs`、再交还控制权 / 看见先跑了 不是已经交差，也不是已经可以像 Prepare 那样。**  
   官方写：应用按自己定的规则，确定地执行 `FinalizeBlockRequest.txs` 里的交易，再把控制权交还给 CometBFT。看见先跑了，不是已经交差。看见必须确定，不是已经是 Usage 那句因为它在状态机复制里推进应用状态。看见按自己的规则，不是已经是 Req 11–12 那种只依赖上一份状态和决定块。
2. **看见 Process 含提案块上执行所需的全部信息 / 看见填了信息 不是已经是刚决定那块的字段，也不是已经跑过 Process。**  
   官方写：`ProcessProposal` 含提案块上执行所需的全部信息。看见填了信息，不是已经是 Finalize 含刚决定那块的字段那种四门齐了。看见能执行，不是已经 Prepare / Process / Finalize 同一套字段就已经跑过 Process。看见有提案块，不是已经交差。
3. **看见 Process 可以像在处理 Finalize 那样整块执行 / 看见整块跑了 不是已经是 ExecuteTxState，也不是已经交差。**  
   官方写：应用可以像在处理 `FinalizeBlock` 那样整块执行。看见整块跑了，不是已经立刻执行出候选就已经是 ExecuteTxState。看见像 Finalize，不是已经 Finalize + Commit。看见能跑，不是已经交差。

怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行是规范里的做法，本页不抄。Finalize 实现必须确定、因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样是不变量 407，本页不抄。

## 官方为什么这样拆

- **Finalize 按应用自己的规则确定地执行 txs、再交还控制权 ≠ 已经交差：** 官方把交还控制权和已经交差分开。
- **Process 含提案块上执行所需的全部信息 ≠ 已经是刚决定那块的字段：** 官方把提案块上执行所需的全部信息和刚决定那块的字段分开。
- **Process 可以像在处理 Finalize 那样整块执行 ≠ 已经是 ExecuteTxState：** 官方把像 Finalize 那样整块执行和候选已经是工作状态分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 按应用自己的规则确定地执行 txs、再交还控制权 | 不是已经交差 | 不是 Finalize 实现必须确定、因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样（407） |
| Process 含提案块上执行所需的全部信息 | 不是已经是刚决定那块的字段 | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| Process 可以像在处理 Finalize 那样整块执行 | 不是已经是 ExecuteTxState | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 执行余量就已经交差、已经是刚决定那块的字段、已经是 ExecuteTxState」，必须分开 Finalize 按应用自己的规则确定地执行 txs、再交还控制权是不是已经交差、Process 含提案块上执行所需的全部信息是不是已经是刚决定那块的字段、Process 可以像在处理 Finalize 那样整块执行是不是已经是 ExecuteTxState。可以跳过「看见填了 Finalize 执行余量就已经交差」。不要另写怎样写 Finalize 执行余量。408 fintxs vs control bundled unbundling 完成（1112 item 1 / 1113 item 2 / 1114 item 3）；精读 [`worked-example-ftxs-notsettle-vs-bundled.md`](worked-example-ftxs-notsettle-vs-bundled.md)（不变量 1112 item 1）。

## 本页不抄

- 怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行。
- Finalize 实现必须确定、因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样。那是不变量 407。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- 候选已经是 ExecuteTxState。那是不变量 311。
