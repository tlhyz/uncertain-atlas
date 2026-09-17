# 例：看见 Prepare 不得改已提交状态 is not already immediate exec settled interchangeable / not already Finalize+Commit interchangeable / not already can mutate s interchangeable

**层次**：实现 / Prepare 不得改已提交状态 not already immediate exec settled / not already Finalize+Commit / not already can mutate s 正式三事（349 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 不得改已提交状态 not already immediate exec settled / not already Finalize+Commit / not already can mutate s 正式三事（349 余量）/ not 866 req9-notprep interchangeable / not 349 req9-noside-vs-commit bundled interchangeable」，不是四门无副作用 bundled（349），也不是四门已经结算（33），也不是一轮一份扩展（350/863）。不要另写怎样守 Req 9。

## 官方三件事

1. **看见高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>* / 看见立刻执行了 这份禁令 is not already 已经交差 interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 866 req9-notprep interchangeable / 867 req9-notproc interchangeable / 349 req9 item 2 Process interchangeable，也不是已经 Prepare 不得改已提交状态 not already immediate exec settled / not already Finalize+Commit / not already can mutate s 正式三事 bundled（349 item 1 余量） interchangeable / 349 req9 item 1 interchangeable。**  
   官方写：正确进程 *p* 在高度 *h* 叫 `PrepareProposal`，不得改上一份已提交状态 *s<sub>p,h-1</sub>*。看见立刻执行了，不是已经换了已提交状态 interchangeable——本页从 349 item 1 侧钉 not already immediate exec settled 单句。349 req9 vs commit bundled unbundling 在本页 item 1 启动。

2. **看见立刻执行了 / 看见 Prepare 回了 / 这份禁令 is not already 已经是 Finalize + Commit interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 866 req9-notprep interchangeable / 349 req9 item 3 Extend interchangeable / 868 req9-notext interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把 Prepare 回了和已经是 Finalize + Commit 分开——349 bundled 第一件事常与 33 混成「看见立刻执行了就已经交差或已经是 Finalize+Commit interchangeable」，本页钉 not already Finalize+Commit 单句。

3. **看见立刻执行了 / 看见能改列表 / 这份禁令 is not already 已经能改 *s* interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 866 req9-notprep interchangeable / 867 req9-notproc interchangeable，也不是已经一轮一份扩展 interchangeable / 350 extend-once / 863 extend-once-notresign interchangeable。**  
   官方把能改列表和已经能改 *s* 分开。看见能改列表，不是已经能改已提交状态 interchangeable。349 req9 vs commit bundled unbundling 在本页 item 1 启动。

怎样守 Req 9、怎样写四门、怎样测副作用是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Prepare 不得改已提交状态 not already immediate exec settled ≠ 已经立刻执行就已经交差 interchangeable：** 官方把 Prepare 可以立刻执行和不得换已提交状态分开。
- **看见 Prepare 回了 not already Finalize+Commit ≠ 已经是 Finalize + Commit interchangeable：** 官方把 Prepare 回了和已经是 Finalize + Commit 分开。
- **看见能改列表 not already can mutate s ≠ 已经能改已提交状态 interchangeable：** 官方把能改列表和已经能改 s 分开；349 req9 vs commit bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 不得改已提交状态 | 不是已经立刻执行就已经交差 | 不是四门已经结算（33） |
| 看见 Prepare 回了 | 不是已经是 Finalize + Commit | 不是一轮一份扩展（350/863） |
| 看见能改列表 | 不是已经能改已提交状态 | 不是候选已经是 ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 不得改已提交状态 not already immediate exec settled / not already Finalize+Commit / not already can mutate s 正式三事（349 余量），必须分开是不是已经立刻执行就已经交差、是不是已经是 Finalize + Commit、是不是已经能改已提交状态。可以跳过「看见立刻执行了就已经交差」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 在本页 item 1 启动；续 [`worked-example-req9-notproc-vs-bundled.md`](worked-example-req9-notproc-vs-bundled.md)（不变量 867 item 2）。

## 本页不抄

- 怎样守 Req 9、怎样写四门、怎样测副作用。
- 四门无副作用 bundled。那是不变量 349。
- Process 不得改已提交状态。那是不变量 349 item 2 余量 / 867。
- 四门已经结算。那是不变量 33。
- 一轮一份扩展。那是不变量 350 / 863。
