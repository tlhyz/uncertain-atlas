# 例：看见 Process 不得改已提交状态 is not already Accept mutated interchangeable / not already candidate ExecuteTxState interchangeable / not already settled interchangeable

**层次**：实现 / Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事（349 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事（349 余量）/ not 867 req9-notproc interchangeable / not 349 req9-noside-vs-commit bundled interchangeable」，不是四门无副作用 bundled（349），也不是候选已经是 ExecuteTxState（311），也不是四门已经结算（33）。不要另写怎样守 Req 9。

## 官方三件事

1. **看见高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>* / 看见回了 Accept 这份禁令 is not already 已经改了已提交状态 interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 867 req9-notproc interchangeable / 866 req9-notprep interchangeable / 349 req9 item 1 Prepare interchangeable，也不是已经 Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事 bundled（349 item 2 余量） interchangeable / 349 req9 item 2 interchangeable。**  
   官方写：同一高度的 `ProcessProposal` 也不得改 *s<sub>p,h-1</sub>*。看见 Accept 了，不是已经改了已提交状态 interchangeable——本页从 349 item 2 侧钉 not already Accept mutated 单句。349 req9 vs commit bundled unbundling 在本页 item 2 续。

2. **看见回了 Accept / 看见 Reject 了 / 这份禁令 is not already 已经是候选已经是 ExecuteTxState interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 867 req9-notproc interchangeable / 349 req9 item 3 Extend interchangeable / 868 req9-notext interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把 Reject 了和已经回滚了已提交状态 / 已经是 ExecuteTxState 分开——349 bundled 第二件事常与 311 混成「看见 Accept 就已经改了或已经是候选 ExecuteTxState interchangeable」，本页钉 not already candidate ExecuteTxState 单句。

3. **看见回了 Accept / 看见跑过了 / 这份禁令 is not already 已经交差 interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 867 req9-notproc interchangeable / 866 req9-notprep interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把跑过了和已经进工作状态 / 已经交差分开。看见跑过了，不是已经进工作状态 interchangeable。349 req9 vs commit bundled unbundling 在本页 item 2 续。

怎样守 Req 9、怎样写四门、怎样测副作用是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process 不得改已提交状态 not already Accept mutated ≠ 已经 Accept 就已经改了 interchangeable：** 官方把 Process 可以立刻执行和不得换已提交状态分开。
- **看见 Reject 了 not already candidate ExecuteTxState ≠ 已经是 ExecuteTxState interchangeable：** 官方把 Reject 了和已经是候选 ExecuteTxState 分开。
- **看见跑过了 not already settled ≠ 已经交差 interchangeable：** 官方把跑过了和已经交差分开；349 req9 vs commit bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 不得改已提交状态 | 不是已经 Accept 就已经改了 | 不是候选已经是 ExecuteTxState（311） |
| 看见 Reject 了 | 不是已经回滚了已提交状态 | 不是四门已经结算（33） |
| 看见跑过了 | 不是已经交差 | 不是 Prepare 不得改就已经交差（866） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事（349 余量），必须分开是不是已经 Accept 就已经改了、是不是已经是候选 ExecuteTxState、是不是已经交差。可以跳过「看见 Accept 就已经改了已提交状态」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 在本页 item 2 续；续 [`worked-example-req9-notext-vs-bundled.md`](worked-example-req9-notext-vs-bundled.md)（不变量 868 item 3）。

## 本页不抄

- 怎样守 Req 9、怎样写四门、怎样测副作用。
- 四门无副作用 bundled。那是不变量 349。
- Prepare 不得改已提交状态。那是不变量 349 item 1 余量 / 866。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 四门已经结算。那是不变量 33。
