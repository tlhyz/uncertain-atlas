# 例：看见丢掉候选 is not already never-rerun interchangeable / not already unbounded-ok interchangeable / not already settled interchangeable

**层次**：实现 / 丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量）/ not 973 candidate-notdrop interchangeable / not 311 candidate-vs-execute bundled interchangeable」，不是候选 bundled（311），也不是半写已经原子（5），也不是 Prepare 已经不确定（338）。不要另写怎样缓存候选或怎样算头哈希。

## 官方三件事

1. **看见候选很多 / 看见还没 Finalize 这份保留 is not already 已经能无界攒着 interchangeable，也不是已经候选 bundled（311） interchangeable / 973 candidate-notdrop interchangeable / 971 candidate-nothash interchangeable / 972 candidate-notexec interchangeable / 311 candidate item 1 Prepare 没有头哈希 interchangeable，也不是已经丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事 bundled（311 item 3 余量） interchangeable / 311 candidate item 3 interchangeable。**  
   官方写：恶劣条件下一轮高度会披露很多提案。按目前 CometBFT 用的 Tendermint 共识，应用在某一高度收到的提案数没有上界，开发者必须自己限制内存。看见还没 Finalize，不是已经能一直攒 interchangeable——本页从 311 item 3 侧钉 not already unbounded-ok 的镜像：丢掉候选 not already never-rerun 从丢掉侧钉。311 candidate vs execute bundled unbundling 在本页 item 3 完成。

2. **看见丢掉了 / 看见还没 Finalize / 这份保留 is not already 已经永远不用再跑 interchangeable，也不是已经候选 bundled（311） interchangeable / 973 candidate-notdrop interchangeable / 311 candidate item 2 立刻执行 interchangeable / 972 candidate-notexec interchangeable，也不是已经半写已经原子 interchangeable / 5 atomic interchangeable。**  
   官方写：作为通例，应用应准备在 FinalizeBlock 之前丢掉候选，即使其中一份以后可能对上决定块，因而还要在 FinalizeBlock 再执行一次。看见丢掉了，不是已经永远不用再跑 interchangeable。本页钉 not already never-rerun 单句。

3. **看见有上界 / 看见丢掉了 / 这份保留 is not already 已经交差 interchangeable，也不是已经候选 bundled（311） interchangeable / 973 candidate-notdrop interchangeable / 971 candidate-nothash interchangeable，也不是已经 Prepare 已经不确定 interchangeable / 338 prepare-nondet interchangeable。**  
   官方把有上界和规范已经写死条数分开。看见有上界，不是已经交差 interchangeable。311 candidate vs execute bundled unbundling 在本页 item 3 完成。

字段表、怎样实现缓存、内存上限取值是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **丢掉候选 not already never-rerun ≠ 已经永远不用再执行 interchangeable：** 官方把必须自己限制内存，和丢掉后仍可能在 Finalize 再执行分开。
- **看见还没 Finalize not already unbounded-ok ≠ 已经能一直攒 interchangeable：** 官方把还没 Finalize 和已经能无界攒着分开。
- **看见有上界 not already settled ≠ 已经交差 interchangeable：** 官方把有上界和规范已经写死条数分开；311 candidate vs execute bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 丢掉候选 | 不是已经永远不用再执行 | 不是半写已经原子（5） |
| 看见还没 Finalize | 不是已经能一直攒 | 不是 Prepare 已经不确定（338） |
| 看见有上界 | 不是已经交差 | 不是 Prepare 没有头哈希就已经知道本头（971） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量），必须分开是不是已经永远不用再执行、是不是已经能一直攒、是不是已经交差。可以跳过「看见立刻执行就已经是本高度最终」。不要另写怎样缓存候选或怎样算头哈希。311 candidate vs execute bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 字段表、怎样实现候选缓存、内存上限取值。
- 候选 bundled。那是不变量 311。
- 半写已经原子。那是不变量 5。
- Prepare 已经不确定。那是不变量 338。
