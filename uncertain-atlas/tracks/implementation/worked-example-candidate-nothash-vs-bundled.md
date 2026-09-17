# 例：看见 Prepare 里没有头哈希 is not already this-header interchangeable / not already process-had-it interchangeable / not already settled interchangeable

**层次**：实现 / Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量）/ not 971 candidate-nothash interchangeable / not 311 candidate-vs-execute bundled interchangeable」，不是候选 bundled（311），也不是四门已经结算（33），也不是 CheckTx 过了就已经按 ExecuteTxState 验过（312/968）。不要另写怎样缓存候选或怎样算头哈希。

## 官方三件事

1. **看见 PrepareProposal 披露了提案 / 看见两门给的字段差不多 这份披露 is not already 已经知道本头哈希 interchangeable，也不是已经候选 bundled（311） interchangeable / 971 candidate-nothash interchangeable / 972 candidate-notexec interchangeable / 311 candidate item 2 立刻执行 interchangeable，也不是已经 Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事 bundled（311 item 1 余量） interchangeable / 311 candidate item 1 interchangeable。**  
   官方写：PrepareProposal 和 ProcessProposal 会把交易列表、上一块 LastCommit、作恶名单、块时间、NextValidatorsHash、提议者地址交给应用。块头哈希也交，但 PrepareProposal 里还不知道。看见 Prepare 来了，不是已经有本头哈希 interchangeable——本页从 311 item 1 侧钉 not already this-header 单句。311 candidate vs execute bundled unbundling 在本页 item 1 启动。

2. **看见 Process 有哈希 / 看见 Prepare 来了 / 这份披露 is not already 已经是 Prepare 当时已经有 interchangeable，也不是已经候选 bundled（311） interchangeable / 971 candidate-nothash interchangeable / 311 candidate item 3 丢掉候选 interchangeable / 973 candidate-notdrop interchangeable，也不是已经四门已经结算 interchangeable / 33 four-gates interchangeable。**  
   官方把 Process 有哈希和 Prepare 当时已经有分开——311 bundled 第一件事常与 33 混成「看见 Prepare 来了就已经知道本头或已经结算 interchangeable」，本页钉 not already process-had-it 单句。

3. **看见字段齐了 / 看见 Prepare 来了 / 这份披露 is not already 已经交差 interchangeable，也不是已经候选 bundled（311） interchangeable / 971 candidate-nothash interchangeable / 972 candidate-notexec interchangeable，也不是已经 CheckTx 过了就已经按 ExecuteTxState 验过 interchangeable / 312/968 checktxstate-notexec interchangeable。**  
   官方把字段齐了和已经能当决定块的身份分开。看见字段齐了，不是已经交差 interchangeable。311 candidate vs execute bundled unbundling 在本页 item 1 启动。

字段表、怎样实现缓存、内存上限取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Prepare 没有头哈希 not already this-header ≠ 已经知道本头 interchangeable：** 官方把两门能给的字段和 Prepare 还不知道头哈希分开。
- **看见 Process 有哈希 not already process-had-it ≠ Prepare 当时已经有 interchangeable：** 官方把 Process 有哈希和 Prepare 当时已经有分开。
- **看见字段齐了 not already settled ≠ 已经交差 interchangeable：** 官方把字段齐了和已经能当决定块身份分开；311 candidate vs execute bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 没有头哈希 | 不是已经知道本头 | 不是四门已经结算（33） |
| 看见 Process 有哈希 | 不是 Prepare 当时已经有 | 不是 CheckTx 过了就已经按 ExecuteTxState 验过（312/968） |
| 看见字段齐了 | 不是已经交差 | 不是立刻执行就已经是 ExecuteTxState（972） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量），必须分开是不是已经知道本头、是不是 Prepare 当时已经有、是不是已经交差。可以跳过「看见立刻执行就已经是本高度最终」。不要另写怎样缓存候选或怎样算头哈希。311 candidate vs execute bundled unbundling 在本页 item 1 启动；续 [`worked-example-candidate-notexec-vs-bundled.md`](worked-example-candidate-notexec-vs-bundled.md)（不变量 972 item 2）。

## 本页不抄

- 字段表、怎样实现候选缓存、内存上限取值。
- 候选 bundled。那是不变量 311。
- 四门已经结算。那是不变量 33。
- CheckTx 过了就已经按 ExecuteTxState 验过。那是不变量 312/968。
