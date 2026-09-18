# 例：看见候选很多 / 还没 Finalize is not already already can unboundedly accumulate interchangeable / already never need re-execute interchangeable / already bound by spec interchangeable

**层次**：实现 / 丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量）/ not 694 candidate-notdiscarded interchangeable / not 311 candidate bundled interchangeable」，不是候选 ≠ ExecuteTxState bundled（311），也不是 Prepare 没有头哈希（692 item 1 余量）或候选不是已经是 ExecuteTxState（693 item 2 余量）。不要另写怎样限制内存或怎样再执行。

## 官方三件事

规范把 Requirements 里恶劣条件下一轮高度会披露很多提案、某一高度收到的提案数**没有上界**、开发者必须自己限制内存、作为通例应准备在 `FinalizeBlock` 之前丢掉候选即使其中一份以后可能对上决定块因而还要在 `FinalizeBlock` 再执行一次 和「已经是候选很多就已经能无界攒着 interchangeable / 已经是丢掉了就已经永远不用再跑 interchangeable / 已经是看见有上界就已经是规范写死条数 interchangeable / 已经是候选 ≠ ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见还没 Finalize 就已经能一直攒 interchangeable / 就已经永远不用再跑 interchangeable / 就已经规范写死条数 interchangeable」一件事：

1. **看见候选很多 / 看见还没 Finalize / 看见一轮高度披露很多提案 is not already 已经能无界攒着 interchangeable / 已经 can unboundedly accumulate interchangeable / 已经能一直攒 interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 694 candidate-notdiscarded interchangeable / 311 candidate item 3 interchangeable，也不是已经丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事 bundled（311 item 3 余量） interchangeable / 311 candidate item 3 interchangeable，也不是已经 Prepare 没有头哈希（692） interchangeable / 693 candidate-notexecute interchangeable / 5 half-write atomic interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：恶劣条件下一轮高度会披露很多提案；某一高度收到的提案数**没有上界**，开发者必须自己限制内存。看见还没 Finalize，不是已经能一直攒 interchangeable——311 钉 bundled 三事，本页从 item 3 侧钉 not already can unboundedly accumulate 单句。看见候选很多，不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable——311 钉 bundled，本页钉 item 3 第一件事。看见一轮高度披露很多提案，不是已经候选不是已经是 ExecuteTxState（693） interchangeable——693 另钉 item 2，本页钉 item 3 第一件事。311 candidate vs execute bundled unbundling 在本页 item 3 启动。

2. **看见丢掉了 / 看见 Finalize 之前丢掉候选 / 看见丢了内存里那份 is not already 已经永远不用再跑 interchangeable / 已经 never need re-execute interchangeable / 已经永远不用再执行 interchangeable / 311 candidate bundled interchangeable / 693 candidate-notexecute interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 694 candidate-notdiscarded interchangeable / 311 candidate item 1 头哈希 interchangeable / 311 candidate item 2 ExecuteTxState interchangeable，也不是已经丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事 bundled（311 item 3 余量） interchangeable / 311 candidate item 3 interchangeable，也不是已经能无界攒着（本页第一件事） interchangeable。**  
   官方把 Finalize 之前丢掉候选 和已经永远不用再跑路径分开——即使丢掉的那份以后可能对上决定块，因而还要在 `FinalizeBlock` 再执行一次。看见丢掉了，不是已经永远不用再跑 interchangeable——本页钉 not already never need re-execute 单句。看见 Finalize 之前丢掉候选，不是已经 Prepare 没有头哈希（692） interchangeable——692 另钉 item 1，本页钉 item 3 第二件事。看见丢了内存里那份，不是已经候选不是已经是 ExecuteTxState（693） interchangeable——693 另钉 item 2，本页钉 item 3 第二件事。311 candidate vs execute bundled unbundling 在本页 item 3 启动。

3. **看见有上界 / 看见自己限制了内存 / 看见开发者设了候选上限 is not already 规范已经写死条数 interchangeable / 已经 bound by spec interchangeable / 已经协议写死上界 interchangeable / 311 candidate bundled interchangeable / 5 half-write atomic interchangeable，也不是已经候选 ≠ ExecuteTxState bundled（311） interchangeable / 694 candidate-notdiscarded interchangeable / 311 candidate item 1 / 311 candidate item 2，也不是已经丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事 bundled（311 item 3 余量） interchangeable / 311 candidate item 3 interchangeable，也不是已经能无界攒着（本页第一件事） interchangeable / 已经永远不用再跑（本页第二件事） interchangeable。**  
   官方把开发者必须自己限制内存 和规范已经写死条数路径分开——提案数没有上界是规范事实；自己设上限是实现做法，不等于规范已经写死条数。看见有上界，不是规范已经写死条数 interchangeable——本页钉 not already bound by spec 单句。看见自己限制了内存，不是已经能无界攒着（本页第一件事） interchangeable——三件事分开钉。看见开发者设了候选上限，不是已经半写已经原子（5） interchangeable——5 另钉。311 candidate vs execute bundled unbundling 在本页 item 3 完成。

怎样限制内存、怎样再执行、怎样写四门是规范里的做法，本页不抄。候选 ≠ ExecuteTxState bundled（311）、Prepare 没有头哈希（311 item 1 余量 / 692）、候选不是已经是 ExecuteTxState（311 item 2 余量 / 693）、四门已经结算（33）、默认锁已经 RPC 安全（310）、半写已经原子（5）是另外那套，本页不抄。

## 官方为什么这样拆

- **还没 Finalize not already can unboundedly accumulate ≠ 311 / 33 interchangeable：** 官方把候选很多单句和已经能无界攒着路径分开。
- **丢掉了 not already never need re-execute ≠ 已经永远不用再跑 interchangeable：** 官方把丢掉候选单句和已经永远不用再执行路径分开。
- **看见有上界 not already bound by spec ≠ 规范已经写死条数 interchangeable：** 官方把自己限制内存单句和规范写死条数路径分开；311 candidate vs execute bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 还没 Finalize / 候选很多 | 不是 already can unboundedly accumulate | 不是候选 already ExecuteTxState alone（693） |
| 丢掉候选 | 不是 already never need re-execute | 不是 Prepare 没有头哈希 alone（692） |
| 自己设了上限 | 不是 already bound by spec | 不是半写已经原子（5） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉候选 not already can unboundedly accumulate / not already never need re-execute / not already bound by spec 正式三事（311 余量），必须分开还没 Finalize 是不是 already can unboundedly accumulate interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable、丢掉了 是不是 already never need re-execute interchangeable、看见有上界 是不是 already bound by spec interchangeable。可以跳过「看见还没 Finalize 就已经能一直攒 interchangeable / 就已经永远不用再跑 interchangeable / 就已经规范写死条数 interchangeable」。不要另写怎样限制内存。311 candidate vs execute bundled unbundling 在本页 item 3 完成（692 + 693 + 694）。

## 本页不抄

- 怎样限制内存、怎样再执行、怎样写四门。
- 候选 ≠ ExecuteTxState bundled。那是不变量 311。
- Prepare 没有头哈希。那是不变量 311 item 1 余量 / 692。
- 候选不是已经是 ExecuteTxState。那是不变量 311 item 2 余量 / 693。
- 四门已经结算。那是不变量 33。
- 默认锁已经 RPC 安全。那是不变量 310。
- 半写已经原子。那是不变量 5。
