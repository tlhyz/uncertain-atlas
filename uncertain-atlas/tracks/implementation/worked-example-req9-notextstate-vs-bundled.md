# 例：看见高度 h 的 ExtendVote 和 VerifyVoteExtension 不得改已提交状态 / 看见签了扩展 / 看见 Verify 过了 is not already already into-state interchangeable / already verified-in interchangeable / already ve-dep-34 interchangeable

**层次**：实现 / Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量）/ not 802 req9-notextstate interchangeable / not 349 req9noside bundled interchangeable」，不是四门无副作用 bundled（349），也不是 Prepare 不得改已提交状态不是已经立刻执行就已经交差（800 item 1 余量）或 Process 不得改已提交状态不是已经 Accept 就已经改了（801 item 2 余量）。不要另写怎样守 Req 9。

## 官方三件事

规范把 Requirements 里高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>*、签了扩展 和「已经是签了扩展就已经写进已提交状态 interchangeable / 已经是 Verify 过了就已经进状态 interchangeable / 已经是扩展在就已经是 34 那种本高度状态不得依赖本高度收到的扩展 interchangeable / 已经是 req9noside bundled interchangeable」分开写成三件独立的实现事，不是「看见签了扩展就已经进状态 interchangeable / 就已经进状态 interchangeable / 就已经是 34 interchangeable」一件事：

1. **看见高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>* / 看见签了扩展 / 看见扩展签了 is not already 已经写进已提交状态 interchangeable / 已经 into-state interchangeable / 已经进状态交差 interchangeable / 349 req9noside bundled interchangeable / 34 voteext interchangeable / req9noside-sold-as-commit interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 802 req9-notextstate interchangeable / 349 req9 item 3 interchangeable，也不是已经 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事 bundled（349 item 3 余量） interchangeable / 349 req9 item 3 interchangeable，也不是已经 Prepare 不得改（800） interchangeable / 801 req9-notaccept interchangeable / 350 extend-once interchangeable，也不是已经本高度状态不得依赖本高度收到的扩展（34） interchangeable。**  
   官方写：同一高度的 `ExtendVote` 和 `VerifyVoteExtension` 同样**不得**改 *s<sub>p,h-1</sub>*。看见签了扩展，不是已经写进已提交状态。看见签了扩展，不是已经 into-state interchangeable——349 钉 bundled 三事，本页从 item 3 侧钉 not already into-state 单句。看见高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>*，不是已经四门无副作用 bundled（349） interchangeable——349 钉 bundled，本页钉 item 3 第一件事。看见签了扩展，不是已经 Prepare 不得改（800） interchangeable——800 另钉 item 1。看见签了扩展，不是已经 Process 不得改（801） interchangeable——801 另钉 item 2。349 req9 vs commit bundled unbundling 在本页 item 3 完成。

2. **看见 Verify 过了 / 看见 VerifyVoteExtension 过了 / 看见扩展验过了 is not already 已经进状态 interchangeable / 已经 verified-in interchangeable / 已经 Verify 进状态交差 interchangeable / 349 req9noside bundled interchangeable / 34 voteext interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 802 req9-notextstate interchangeable / 349 req9 item 1 Prepare interchangeable / 349 req9 item 2 Process interchangeable，也不是已经 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事 bundled（349 item 3 余量） interchangeable / 349 req9 item 3 interchangeable，也不是已经写进已提交状态（本页第一件事） interchangeable。**  
   官方写：看见 Verify 过了，不是已经进状态。看见 VerifyVoteExtension 过了，不是已经 verified-in interchangeable——本页钉 not already verified-in 单句。看见扩展验过了，不是已经写进已提交状态（本页第一件事） interchangeable——三件事分开钉。349 req9 vs commit bundled unbundling 在本页 item 3 完成。

3. **看见扩展在 / 看见扩展写在票上 / 看见本高度有扩展 is not already 已经是 34 那种本高度状态不得依赖本高度收到的扩展 interchangeable / 已经 ve-dep-34 interchangeable / 已经 34 交差 interchangeable / 349 req9noside bundled interchangeable / 34 vote-extension-sold-as-block interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 802 req9-notextstate interchangeable / 349 req9 item 1 / 349 req9 item 2，也不是已经 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事 bundled（349 item 3 余量） interchangeable / 349 req9 item 3 interchangeable，也不是已经写进已提交状态（本页第一件事） interchangeable / 已经进状态（本页第二件事） interchangeable。**  
   官方写：看见扩展在，不是已经是 34 那种本高度状态不得依赖本高度收到的扩展。看见扩展写在票上，不是已经 ve-dep-34 interchangeable——本页钉 not already ve-dep-34 单句。看见本高度有扩展，不是已经进状态（本页第二件事） interchangeable——三件事分开钉。349 req9 vs commit bundled unbundling 在本页 item 3 完成。

怎样守这道禁令、怎样写四门、怎样测副作用是规范里的做法，本页不抄。四门无副作用 bundled（349）、Prepare 不得改已提交状态不是已经立刻执行就已经交差（349 item 1 余量 / 800）、Process 不得改已提交状态不是已经 Accept 就已经改了（349 item 2 余量 / 801）、四门已经结算（33）、候选已经是 ExecuteTxState（311）、本高度状态不得依赖本高度收到的扩展（34）、一轮最多一张 Precommit（350）是另外那套，本页不抄。

## 官方为什么这样拆

- **Extend 和 Verify 不得改已提交状态 not already into-state ≠ 349 / 34 interchangeable：** 官方把签了扩展和已经写进已提交状态分开。
- **Verify 过了 not already verified-in ≠ 已经进状态 interchangeable：** 官方把 Verify 过了和已经进状态分开。
- **扩展在 not already ve-dep-34 ≠ 已经是 34 interchangeable：** 官方把扩展在和已经是本高度状态不得依赖本高度收到的扩展分开；349 req9 vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Extend 和 Verify 不得改已提交状态 | 不是 already into-state | 不是本高度状态不得依赖本高度收到的扩展 alone（34） |
| Verify 过了 | 不是 already verified-in | 不是 Process 不得改 already accept-mutated alone（801） |
| 扩展在 | 不是 already ve-dep-34 | 不是一轮最多一张 Precommit alone（350） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量），必须分开 Extend 和 Verify 不得改已提交状态 是不是 already into-state interchangeable / 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable、Verify 过了 是不是 already verified-in interchangeable、扩展在 是不是 already ve-dep-34 interchangeable。可以跳过「看见签了扩展就已经进状态 interchangeable / 就已经进状态 interchangeable / 就已经是 34 interchangeable」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 在本页 item 3 完成（800 + 801 + 802）。

## 本页不抄

- 怎样守这道禁令、怎样写四门、怎样测副作用。
- 四门无副作用 bundled。那是不变量 349。
- Prepare 不得改已提交状态不是已经立刻执行就已经交差。那是不变量 349 item 1 余量 / 800。
- Process 不得改已提交状态不是已经 Accept 就已经改了。那是不变量 349 item 2 余量 / 801。
- 四门已经结算。那是不变量 33。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 本高度状态不得依赖本高度收到的扩展。那是不变量 34。
- 一轮最多一张 Precommit。那是不变量 350。
