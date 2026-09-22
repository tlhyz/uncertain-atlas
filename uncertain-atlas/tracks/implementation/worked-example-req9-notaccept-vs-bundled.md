# 例：看见高度 h 的 ProcessProposal 不得改已提交状态 / 看见回了 Accept / 看见 Reject 了 is not already already accept-mutated interchangeable / already reject-rollback interchangeable / already workstate interchangeable

**层次**：实现 / Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量）/ not 801 req9-notaccept interchangeable / not 349 req9noside bundled interchangeable」，不是四门无副作用 bundled（349），也不是 Prepare 不得改已提交状态不是已经立刻执行就已经交差（800 item 1 余量）或 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态（802 item 3 余量）。不要另写怎样守 Req 9。

## 官方三件事

规范把 Requirements 里高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>*、回了 Accept 和「已经是 Accept 了就已经改了已提交状态 interchangeable / 已经是 Reject 了就已经回滚了已提交状态 interchangeable / 已经是跑过了就已经进工作状态 interchangeable / 已经是 req9noside bundled interchangeable」分开写成三件独立的实现事，不是「看见 Accept 了就已经改了 interchangeable / 就已经回滚了 interchangeable / 就已经进工作状态 interchangeable」一件事：

1. **看见高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>* / 看见回了 Accept / 看见 Accept 了 is not already 已经改了已提交状态 interchangeable / 已经 accept-mutated interchangeable / 已经 Accept 改状态交差 interchangeable / 349 req9noside bundled interchangeable / 311 candidate interchangeable / req9noside-sold-as-commit interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 801 req9-notaccept interchangeable / 349 req9 item 2 interchangeable，也不是已经 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事 bundled（349 item 2 余量） interchangeable / 349 req9 item 2 interchangeable，也不是已经 Prepare 不得改（800） interchangeable / 802 req9-notextstate interchangeable / 340 processdet interchangeable，也不是已经候选已经是 ExecuteTxState（311） interchangeable。**  
   官方写：同一高度的 `ProcessProposal` 也**不得**改 *s<sub>p,h-1</sub>*。看见 Accept 了，不是已经改了已提交状态。看见回了 Accept，不是已经 accept-mutated interchangeable——349 钉 bundled 三事，本页从 item 2 侧钉 not already accept-mutated 单句。看见高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>*，不是已经四门无副作用 bundled（349） interchangeable——349 钉 bundled，本页钉 item 2 第一件事。看见 Accept 了，不是已经候选已经是 ExecuteTxState（311） interchangeable——311 另钉。看见 Accept 了，不是已经 Prepare 不得改（800） interchangeable——800 另钉 item 1。349 req9 vs commit bundled unbundling 在本页 item 2 续。

2. **看见 Reject 了 / 看见回了 Reject / 看见拒了提案 is not already 已经回滚了已提交状态 interchangeable / 已经 reject-rollback interchangeable / 已经 Reject 回滚交差 interchangeable / 349 req9noside bundled interchangeable / 33 fourgates interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 801 req9-notaccept interchangeable / 349 req9 item 1 Prepare interchangeable / 349 req9 item 3 扩展 interchangeable，也不是已经 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事 bundled（349 item 2 余量） interchangeable / 349 req9 item 2 interchangeable，也不是已经改了已提交状态（本页第一件事） interchangeable。**  
   官方写：看见 Reject 了，不是已经回滚了已提交状态。看见回了 Reject，不是已经 reject-rollback interchangeable——本页钉 not already reject-rollback 单句。看见拒了提案，不是已经改了已提交状态（本页第一件事） interchangeable——三件事分开钉。349 req9 vs commit bundled unbundling 在本页 item 2 续。

3. **看见跑过了 / 看见 Process 跑过了 / 看见处理过提案 is not already 已经进工作状态 interchangeable / 已经 workstate interchangeable / 已经工作状态交差 interchangeable / 349 req9noside bundled interchangeable / 311 candidate interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 801 req9-notaccept interchangeable / 349 req9 item 1 / 349 req9 item 3，也不是已经 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事 bundled（349 item 2 余量） interchangeable / 349 req9 item 2 interchangeable，也不是已经改了已提交状态（本页第一件事） interchangeable / 已经回滚了已提交状态（本页第二件事） interchangeable。**  
   官方写：看见跑过了，不是已经进工作状态。看见 Process 跑过了，不是已经 workstate interchangeable——本页钉 not already workstate 单句。看见处理过提案，不是已经回滚了已提交状态（本页第二件事） interchangeable——三件事分开钉。349 req9 vs commit bundled unbundling 在本页 item 2 续。

怎样守这道禁令、怎样写四门、怎样测副作用是规范里的做法，本页不抄。四门无副作用 bundled（349）、Prepare 不得改已提交状态不是已经立刻执行就已经交差（349 item 1 余量 / 800）、Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态（349 item 3 余量 / 802）、四门已经结算（33）、候选已经是 ExecuteTxState（311）、本高度状态不得依赖本高度收到的扩展（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **Process 不得改已提交状态 not already accept-mutated ≠ 349 / 311 interchangeable：** 官方把 Accept 了和已经改了已提交状态分开。
- **Reject 了 not already reject-rollback ≠ 已经回滚了已提交状态 interchangeable：** 官方把 Reject 了和已经回滚了已提交状态分开。
- **跑过了 not already workstate ≠ 已经进工作状态 interchangeable：** 官方把跑过了和已经进工作状态分开；349 req9 vs commit bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 不得改已提交状态 | 不是 already accept-mutated | 不是候选已经是 ExecuteTxState alone（311） |
| Reject 了 | 不是 already reject-rollback | 不是 Prepare 不得改 already settled alone（800） |
| 跑过了 | 不是 already workstate | 不是扩展两门 already into-state alone（802） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量），必须分开 Process 不得改已提交状态 是不是 already accept-mutated interchangeable / 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable、Reject 了 是不是 already reject-rollback interchangeable、跑过了 是不是 already workstate interchangeable。可以跳过「看见 Accept 了就已经改了 interchangeable / 就已经回滚了 interchangeable / 就已经进工作状态 interchangeable」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 在本页 item 2 续（800 + 801）；续 [`worked-example-req9-notextstate-vs-bundled.md`](worked-example-req9-notextstate-vs-bundled.md)（不变量 802 item 3）；完成见 802。

## 本页不抄

- 怎样守这道禁令、怎样写四门、怎样测副作用。
- 四门无副作用 bundled。那是不变量 349。
- Prepare 不得改已提交状态不是已经立刻执行就已经交差。那是不变量 349 item 1 余量 / 800。
- Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态。那是不变量 349 item 3 余量 / 802。
- 四门已经结算。那是不变量 33。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 本高度状态不得依赖本高度收到的扩展。那是不变量 34。
