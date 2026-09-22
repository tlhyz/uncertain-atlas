# 例：看见 Prepare 不得改已提交状态不是已经立刻执行就已经交差；看见 Process 不得改已提交状态不是已经 Accept 就已经改了；看见 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态

**层次**：实现 / 四门无副作用。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Prepare 不得改已提交状态不是已经立刻执行就已经交差 / Process 不得改已提交状态不是已经 Accept 就已经改了 / Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态」，不是四门已经结算，也不是候选已经是 ExecuteTxState。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 完成（800+801+802）；精读 [`worked-example-req9-notsettled-vs-bundled.md`](worked-example-req9-notsettled-vs-bundled.md)（不变量 800 item 1）；精读 [`worked-example-req9-notaccept-vs-bundled.md`](worked-example-req9-notaccept-vs-bundled.md)（不变量 801 item 2）；精读 [`worked-example-req9-notextstate-vs-bundled.md`](worked-example-req9-notextstate-vs-bundled.md)（不变量 802 item 3）。

## 官方三件事

规范把四门不得改已提交状态写成三件独立的实现事，不是「看见立刻执行了就已经交差、已经 Accept 就已经改了、已经签了扩展就已经进状态」一件事：

1. **看见高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>* / 看见立刻执行了 不是已经交差，也不是已经是 Finalize + Commit。**  
   官方写：正确进程 *p* 在高度 *h* 叫 `PrepareProposal`，**不得**改上一份已提交状态 *s<sub>p,h-1</sub>*。看见立刻执行了，不是已经换了已提交状态。看见 Prepare 回了，不是已经交差。看见能改列表，不是已经能改 *s*。
2. **看见高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>* / 看见回了 Accept 不是已经改了已提交状态，也不是已经是候选已经是 ExecuteTxState。**  
   官方写：同一高度的 `ProcessProposal` 也**不得**改 *s<sub>p,h-1</sub>*。看见 Accept 了，不是已经改了已提交状态。看见 Reject 了，不是已经回滚了已提交状态。看见跑过了，不是已经进工作状态。
3. **看见高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>* / 看见签了扩展 不是已经进状态，也不是已经是 *s<sub>h</sub>* 不依赖本高度 *e*。**  
   官方写：同一高度的 `ExtendVote` 和 `VerifyVoteExtension` 同样**不得**改 *s<sub>p,h-1</sub>*。看见签了扩展，不是已经写进已提交状态。看见 Verify 过了，不是已经进状态。看见扩展在，不是已经是 34 那种本高度状态不得依赖本高度收到的扩展。

怎样守这道禁令、怎样写四门、怎样测副作用是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **Prepare 不得改已提交状态 ≠ 已经立刻执行就已经交差：** 官方把 Prepare 可以立刻执行和不得换已提交状态分开。
- **Process 不得改已提交状态 ≠ 已经 Accept 就已经改了：** 官方把 Process 可以立刻执行和不得换已提交状态分开。
- **Extend 和 Verify 不得改已提交状态 ≠ 已经签了扩展就已经进状态：** 官方把扩展两门和不得换已提交状态分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 不得改已提交状态 | 不是已经立刻执行就已经交差 | 不是四门已经结算（33） |
| Process 不得改已提交状态 | 不是已经 Accept 就已经改了 | 不是候选已经是 ExecuteTxState（311） |
| Extend 和 Verify 不得改已提交状态 | 不是已经签了扩展就已经进状态 | 不是本高度状态不得依赖本高度收到的扩展（34） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见立刻执行了就已经交差、已经 Accept 就已经改了、已经签了扩展就已经进状态」，必须分开 Prepare 不得改已提交状态是不是已经立刻执行就已经交差、Process 不得改已提交状态是不是已经 Accept 就已经改了、Extend 和 Verify 不得改已提交状态是不是已经签了扩展就已经进状态。可以跳过「看见立刻执行了就已经交差」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 完成（800+801+802）。

## 本页不抄

- 怎样守这道禁令、怎样写四门、怎样测副作用。
- 四门已经结算。那是不变量 33。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 本高度状态不得依赖本高度收到的扩展。那是不变量 34。
