# 例：看见 PrepareProposal 披露了提案 / 两门给的字段差不多 is not already already have header hash interchangeable / Prepare already had hash interchangeable / already decided block identity interchangeable

**层次**：实现 / Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量）/ not 692 candidate-notheader interchangeable / not 311 candidate bundled interchangeable」，不是候选 ≠ ExecuteTxState bundled（311），也不是候选不是已经是 ExecuteTxState（693 item 2 余量）或丢掉不是已经永远不用再执行（694 item 3 余量）。不要另写怎样缓存候选或怎样算头哈希。

## 官方三件事

规范把 Requirements 里 `PrepareProposal` / `ProcessProposal` 披露给应用的提案数据（交易列表、上一块 `LastCommit`、作恶名单、块时间、`NextValidatorsHash`、提议者地址、**块头哈希也交但 Prepare 里还不知道**）和「已经是 Prepare 来了就已经有本头哈希 interchangeable / 已经是 Process 有哈希就已经是 Prepare 当时已经有 interchangeable / 已经是字段齐了就已经能当决定块的身份 interchangeable / 已经是候选 ≠ ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见 Prepare 披露了 就已经知道本头 interchangeable / 就已经 Prepare 当时有哈希 interchangeable / 就已经是决定块身份 interchangeable」一件事：

1. **看见 PrepareProposal 披露了提案 / 看见 Prepare 来了 / 看见两门给的字段差不多 is not already 已经有本头哈希 interchangeable / 已经 have header hash interchangeable / 已经知道本头 interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 692 candidate-notheader interchangeable / 311 candidate item 1 interchangeable，也不是已经 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事 bundled（311 item 1 余量） interchangeable / 311 candidate item 1 interchangeable，也不是已经候选不是已经是 ExecuteTxState（693） interchangeable / 694 candidate-notdiscarded interchangeable / 310 commitlock interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：两门会把交易列表、上一块 `LastCommit`、作恶名单、块时间、`NextValidatorsHash`、提议者地址交给应用。**块头哈希也交，但 `PrepareProposal` 里还不知道。** 看见 Prepare 来了，不是已经有本头哈希 interchangeable——311 钉 bundled 三事，本页从 item 1 侧钉 not already have header hash 单句。看见两门给的字段差不多，不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable——311 钉 bundled，本页钉 item 1 第一件事。看见 PrepareProposal 披露了提案，不是已经四门已经结算（33） interchangeable——33 钉四门，本页钉头哈希边界单句。311 candidate vs execute bundled unbundling 在本页 item 1 启动。

2. **看见 ProcessProposal 有哈希 / 看见 Process 交了块头哈希 / 看见 Process 字段里有 hash is not already Prepare 当时已经有 interchangeable / 已经 Prepare already had hash interchangeable / 已经两门同一时刻都有哈希 interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 692 candidate-notheader interchangeable / 311 candidate item 2 候选状态 interchangeable / 311 candidate item 3 丢掉候选 interchangeable，也不是已经 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事 bundled（311 item 1 余量） interchangeable / 311 candidate item 1 interchangeable，也不是已经 Prepare 来了就已经有本头哈希（本页第一件事） interchangeable。**  
   官方把 Process 有哈希 和 Prepare 当时已经有路径分开——Process 交哈希不等于 Prepare 那一次调用就已经知道。看见 Process 有哈希，不是 Prepare 当时已经有 interchangeable——本页钉 not Prepare already had hash 单句。看见 Process 交了块头哈希，不是已经候选不是已经是 ExecuteTxState（693） interchangeable——693 另钉 item 2，本页钉 item 1 第二件事。看见 Process 字段里有 hash，不是已经丢掉不是已经永远不用再执行（694） interchangeable——694 另钉 item 3，本页钉 item 1 第二件事。311 candidate vs execute bundled unbundling 在本页 item 1 启动。

3. **看见字段齐了 / 看见交易列表 LastCommit 时间 NextValidatorsHash 提议者都有了 / 看见两门给的数据齐了 is not already 已经能当决定块的身份 interchangeable / 已经 decided block identity interchangeable / 已经是本高度最终块身份 interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 692 candidate-notheader interchangeable / 311 candidate item 2 / 311 candidate item 3，也不是已经 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事 bundled（311 item 1 余量） interchangeable / 311 candidate item 1 interchangeable，也不是已经有本头哈希（本页第一件事） interchangeable / 已经 Prepare 当时已经有（本页第二件事） interchangeable。**  
   官方把字段清单齐了 和已经能当决定块的身份路径分开——字段齐了不等于已经有本头哈希，更不等于已经是决定块身份。看见字段齐了，不是已经能当决定块的身份 interchangeable——本页钉 not already decided block identity 单句。看见交易列表等都有了，不是已经 have header hash（本页第一件事） interchangeable——三件事分开钉。看见两门给的数据齐了，不是已经 Finalize 交差（403） interchangeable——403 另钉。311 candidate vs execute bundled unbundling 在本页 item 1 完成。

怎样缓存候选、怎样算头哈希、怎样写四门是规范里的做法，本页不抄。候选 ≠ ExecuteTxState bundled（311）、候选不是已经是 ExecuteTxState（311 item 2 余量 / 693）、丢掉不是已经永远不用再执行（311 item 3 余量 / 694）、四门已经结算（33）、默认锁已经 RPC 安全（310）、半写已经原子（5）是另外那套，本页不抄。

## 官方为什么这样拆

- **Prepare 披露 not already have header hash ≠ 311 / 33 interchangeable：** 官方把 Prepare 来了单句和已经有本头哈希路径分开。
- **Process 有哈希 not Prepare already had hash ≠ Prepare 当时已经有 interchangeable：** 官方把 Process 交哈希单句和 Prepare 当时已经有路径分开。
- **字段齐了 not already decided block identity ≠ 已经是决定块身份 interchangeable：** 官方把字段清单单句和决定块身份路径分开；311 candidate vs execute bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposal 披露 | 不是 already have header hash | 不是四门已经结算（33） |
| Process 有哈希 | 不是 Prepare already had hash | 不是候选 already ExecuteTxState alone（693） |
| 字段齐了 | 不是 already decided block identity | 不是丢掉候选 alone（694） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量），必须分开 Prepare 来了 是不是 already have header hash interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable、Process 有哈希 是不是 Prepare already had hash interchangeable、字段齐了 是不是 already decided block identity interchangeable。可以跳过「看见 Prepare 披露了 就已经知道本头 interchangeable / 就已经 Prepare 当时有哈希 interchangeable / 就已经是决定块身份 interchangeable」。不要另写怎样算头哈希。311 candidate vs execute bundled unbundling 在本页 item 1 完成；续 [`worked-example-candidate-notexecute-vs-bundled.md`](worked-example-candidate-notexecute-vs-bundled.md)（不变量 693 item 2）。

## 本页不抄

- 怎样缓存候选、怎样算头哈希、怎样写四门。
- 候选 ≠ ExecuteTxState bundled。那是不变量 311。
- 候选不是已经是 ExecuteTxState。那是不变量 311 item 2 余量 / 693。
- 丢掉不是已经永远不用再执行。那是不变量 311 item 3 余量 / 694。
- 四门已经结算。那是不变量 33。
- 默认锁已经 RPC 安全。那是不变量 310。
- 半写已经原子。那是不变量 5。
