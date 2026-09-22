# 例：看见高度 h 的 PrepareProposal 不得改已提交状态 / 看见立刻执行了 / 看见 Prepare 回了 is not already already settled interchangeable / already finalize-commit interchangeable / already mutate-s interchangeable

**层次**：实现 / Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量）/ not 800 req9-notsettled interchangeable / not 349 req9noside bundled interchangeable」，不是四门无副作用 bundled（349），也不是 Process 不得改已提交状态不是已经 Accept 就已经改了（801 item 2 余量）或 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态（802 item 3 余量）。不要另写怎样守 Req 9。

## 官方三件事

规范把 Requirements 里高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>*、立刻执行了 和「已经是立刻执行了就已经交差 interchangeable / 已经是 Prepare 回了就已经是 Finalize + Commit interchangeable / 已经是能改列表就已经能改 *s* interchangeable / 已经是 req9noside bundled interchangeable」分开写成三件独立的实现事，不是「看见立刻执行了就已经交差 interchangeable / 就已经是 Finalize + Commit interchangeable / 就已经能改 *s* interchangeable」一件事：

1. **看见高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>* / 看见立刻执行了 / 看见 Prepare 回了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 349 req9noside bundled interchangeable / 33 fourgates interchangeable / req9noside-sold-as-commit interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 800 req9-notsettled interchangeable / 349 req9 item 1 interchangeable，也不是已经 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事 bundled（349 item 1 余量） interchangeable / 349 req9 item 1 interchangeable，也不是已经 Process 不得改（801） interchangeable / 802 req9-notextstate interchangeable / 338 prepare interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：正确进程 *p* 在高度 *h* 叫 `PrepareProposal`，**不得**改上一份已提交状态 *s<sub>p,h-1</sub>*。看见立刻执行了，不是已经换了已提交状态。看见 Prepare 回了，不是已经交差。看见立刻执行了，不是已经 settled interchangeable——349 钉 bundled 三事，本页从 item 1 侧钉 not already settled 单句。看见高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>*，不是已经四门无副作用 bundled（349） interchangeable——349 钉 bundled，本页钉 item 1 第一件事。看见立刻执行了，不是已经四门已经结算（33） interchangeable——33 另钉。349 req9 vs commit bundled unbundling 在本页 item 1 启动。

2. **看见立刻执行了 / 看见 Prepare 回了 / 看见能立刻执行 is not already 已经是 Finalize + Commit interchangeable / 已经 finalize-commit interchangeable / 已经 Finalize 交差 interchangeable / 349 req9noside bundled interchangeable / 33 fourgates interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 800 req9-notsettled interchangeable / 349 req9 item 2 Process interchangeable / 349 req9 item 3 扩展 interchangeable，也不是已经 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事 bundled（349 item 1 余量） interchangeable / 349 req9 item 1 interchangeable，也不是已经交差（本页第一件事） interchangeable。**  
   官方写：看见立刻执行了，不是已经是 Finalize + Commit。看见 Prepare 回了，不是已经 finalize-commit interchangeable——本页钉 not already finalize-commit 单句。看见能立刻执行，不是已经交差（本页第一件事） interchangeable——三件事分开钉。349 req9 vs commit bundled unbundling 在本页 item 1 启动。

3. **看见能改列表 / 看见 Prepare 能改交易列表 / 看见回了列表 is not already 已经能改 *s* interchangeable / 已经 mutate-s interchangeable / 已经改状态交差 interchangeable / 349 req9noside bundled interchangeable / 311 candidate interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 800 req9-notsettled interchangeable / 349 req9 item 2 / 349 req9 item 3，也不是已经 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事 bundled（349 item 1 余量） interchangeable / 349 req9 item 1 interchangeable，也不是已经交差（本页第一件事） interchangeable / 已经是 Finalize + Commit（本页第二件事） interchangeable。**  
   官方写：看见能改列表，不是已经能改 *s*。看见 Prepare 能改交易列表，不是已经 mutate-s interchangeable——本页钉 not already mutate-s 单句。看见回了列表，不是已经是 Finalize + Commit（本页第二件事） interchangeable——三件事分开钉。349 req9 vs commit bundled unbundling 在本页 item 1 启动。

怎样守这道禁令、怎样写四门、怎样测副作用是规范里的做法，本页不抄。四门无副作用 bundled（349）、Process 不得改已提交状态不是已经 Accept 就已经改了（349 item 2 余量 / 801）、Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态（349 item 3 余量 / 802）、四门已经结算（33）、候选已经是 ExecuteTxState（311）、本高度状态不得依赖本高度收到的扩展（34）是另外那套，本页不抄。

## 官方为什么这样拆

- **Prepare 不得改已提交状态 not already settled ≠ 349 / 33 interchangeable：** 官方把立刻执行了和已经交差分开。
- **立刻执行了 not already finalize-commit ≠ 已经是 Finalize + Commit interchangeable：** 官方把立刻执行了和已经是 Finalize + Commit 分开。
- **能改列表 not already mutate-s ≠ 已经能改 *s* interchangeable：** 官方把能改列表和已经能改已提交状态分开；349 req9 vs commit bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 不得改已提交状态 | 不是 already settled | 不是四门已经结算 alone（33） |
| 立刻执行了 | 不是 already finalize-commit | 不是 Process 不得改 already Accept 改了 alone（801） |
| 能改列表 | 不是 already mutate-s | 不是候选已经是 ExecuteTxState alone（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量），必须分开 Prepare 不得改已提交状态 是不是 already settled interchangeable / 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable、立刻执行了 是不是 already finalize-commit interchangeable、能改列表 是不是 already mutate-s interchangeable。可以跳过「看见立刻执行了就已经交差 interchangeable / 就已经是 Finalize + Commit interchangeable / 就已经能改 *s* interchangeable」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 在本页 item 1 启动；续 [`worked-example-req9-notaccept-vs-bundled.md`](worked-example-req9-notaccept-vs-bundled.md)（不变量 801 item 2）；完成见 802。

## 本页不抄

- 怎样守这道禁令、怎样写四门、怎样测副作用。
- 四门无副作用 bundled。那是不变量 349。
- Process 不得改已提交状态不是已经 Accept 就已经改了。那是不变量 349 item 2 余量 / 801。
- Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态。那是不变量 349 item 3 余量 / 802。
- 四门已经结算。那是不变量 33。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 本高度状态不得依赖本高度收到的扩展。那是不变量 34。
