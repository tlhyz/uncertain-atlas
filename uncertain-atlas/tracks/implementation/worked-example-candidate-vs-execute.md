# 例：看见 Prepare 里没有头哈希不是已经知道本头；看见立刻执行出候选不是已经是 ExecuteTxState；看见丢掉候选不是已经永远不用再执行

**层次**：实现 / 候选状态。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Prepare 没有头哈希不是已经知道本头 / 候选不是已经是 ExecuteTxState / 丢掉不是已经永远不用再执行」，不是四门已经结算，也不是默认锁已经 RPC 安全。不要另写怎样缓存候选或怎样算头哈希。

## 官方三件事

规范把立刻执行提案写成三件独立的实现事，不是「看见 Prepare / Process 跑过就已经是本高度最终、已经进 ExecuteTxState、已经能无界攒着」一件事：

1. **看见 PrepareProposal 披露了提案 / 看见两门给的字段差不多 不是已经知道本头哈希。**  
   官方写：`PrepareProposal` 和 `ProcessProposal` 会把交易列表、上一块 `LastCommit`、作恶名单、块时间、`NextValidatorsHash`、提议者地址交给应用。**块头哈希也交，但 `PrepareProposal` 里还不知道。** 看见 Prepare 来了，不是已经有本头哈希。看见 Process 有哈希，不是 Prepare 当时已经有。看见字段齐了，不是已经能当决定块的身份。
2. **看见立刻执行出一份候选 / 看见内存里有状态 不是已经是 ExecuteTxState，也不是已经能预测本高度 Finalize 会交哪一块。**  
   官方写：应用可以在 `PrepareProposal` / `ProcessProposal` 立刻执行，好避开非法交易，或让 `FinalizeBlock` 更快套用内存里那份。但这两门在同一高度可以叫很多次，**无法准确预测**哪一块会被决定、交到本高度的 `FinalizeBlock`。立刻执行的结果叫候选状态，应留在内存里当可能的最终。执行提案**不得**改 `ExecuteTxState`，要等 `FinalizeBlock` 确认哪一份（如果有）才能用来更新。看见跑过了，不是已经进工作状态。看见内存里有，不是已经能点名本高度最终。看见能加快 Finalize，不是已经交差。
3. **看见候选很多 / 看见还没 Finalize 不是已经能无界攒着，也不是丢掉就永远不用再执行。**  
   官方写：恶劣条件下一轮高度会披露很多提案。按目前 CometBFT 用的 Tendermint 共识，应用在某一高度收到的提案数**没有上界**，开发者必须自己限制内存。作为通例，应用应准备在 `FinalizeBlock` 之前丢掉候选，即使其中一份以后可能对上决定块，因而还要在 `FinalizeBlock` 再执行一次。看见还没 Finalize，不是已经能一直攒。看见丢掉了，不是已经永远不用再跑。看见有上界，不是规范已经写死条数。

字段表、怎样实现缓存、内存上限取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Prepare 披露 ≠ 已经有本头哈希：** 官方把两门能给的字段和 Prepare 还不知道头哈希分开。
- **立刻执行 ≠ 已经是 ExecuteTxState：** 官方把候选、工作状态、无法预测哪一块被决定分开。
- **丢掉候选 ≠ 已经永远不用再执行：** 官方把必须自己限制内存，和丢掉后仍可能在 Finalize 再执行分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 没有头哈希 | 不是已经知道本头 | 不是四门已经结算（33） |
| 候选状态 | 不是已经是 ExecuteTxState | 不是默认锁已经 RPC 安全（310） |
| 丢掉候选 | 不是已经永远不用再执行 | 不是半写已经原子（5） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Prepare 已经执行」，必须分开 Prepare 是不是已经有本头哈希、候选是不是已经是 ExecuteTxState、丢掉是不是已经永远不用再执行。可以跳过「看见立刻执行就已经是本高度最终」。不要另写怎样缓存候选或怎样算头哈希。311 candidate vs execute bundled unbundling 完成（971 item 1 / 972 item 2 / 973 item 3）；精读 [`worked-example-candidate-nothash-vs-bundled.md`](worked-example-candidate-nothash-vs-bundled.md)（不变量 971 item 1）。

## 本页不抄

- 字段表、怎样实现候选缓存、内存上限取值。
- 怎样算头哈希、怎样对上决定块、怎样再执行。
- 怎样写四门。那是不变量 33。
