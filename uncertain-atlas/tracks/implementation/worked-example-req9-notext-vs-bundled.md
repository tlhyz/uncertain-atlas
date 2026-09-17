# 例：看见 Extend 和 Verify 不得改已提交状态 is not already signed into state interchangeable / not already sh independent of e interchangeable / not already settled interchangeable

**层次**：实现 / Extend 和 Verify 不得改已提交状态 not already signed into state / not already sh independent of e / not already settled 正式三事（349 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Extend 和 Verify 不得改已提交状态 not already signed into state / not already sh independent of e / not already settled 正式三事（349 余量）/ not 868 req9-notext interchangeable / not 349 req9-noside-vs-commit bundled interchangeable」，不是四门无副作用 bundled（349），也不是本高度状态不得依赖本高度收到的扩展（34），也不是一轮一份扩展（350/865）。不要另写怎样守 Req 9。

## 官方三件事

1. **看见高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>* / 看见签了扩展 这份禁令 is not already 已经进状态 interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 868 req9-notext interchangeable / 866 req9-notprep interchangeable / 349 req9 item 1 Prepare interchangeable，也不是已经 Extend 和 Verify 不得改已提交状态 not already signed into state / not already sh independent of e / not already settled 正式三事 bundled（349 item 3 余量） interchangeable / 349 req9 item 3 interchangeable。**  
   官方写：同一高度的 `ExtendVote` 和 `VerifyVoteExtension` 同样不得改 *s<sub>p,h-1</sub>*。看见签了扩展，不是已经写进已提交状态 interchangeable——本页从 349 item 3 侧钉 not already signed into state 单句。349 req9 vs commit bundled unbundling 在本页 item 3 完成。

2. **看见签了扩展 / 看见 Verify 过了 / 这份禁令 is not already 已经是 *s<sub>h</sub>* 不依赖本高度 *e* interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 868 req9-notext interchangeable / 349 req9 item 2 Process interchangeable / 867 req9-notproc interchangeable，也不是已经本高度状态不得依赖本高度收到的扩展 interchangeable / 34 voteext interchangeable。**  
   官方把 Verify 过了和已经是 34 那种本高度状态不得依赖本高度收到的扩展分开——349 bundled 第三件事常与 34 混成「看见签了扩展就已经进状态或已经是 sh 不依赖 e interchangeable」，本页钉 not already sh independent of e 单句。

3. **看见签了扩展 / 看见扩展在 / 这份禁令 is not already 已经交差 interchangeable，也不是已经四门无副作用 bundled（349） interchangeable / 868 req9-notext interchangeable / 866 req9-notprep interchangeable，也不是已经一轮一份扩展 interchangeable / 350 extend-once / 865 extend-once-notperheight interchangeable。**  
   官方把扩展在和已经交差分开。看见扩展在，不是已经交差 interchangeable。349 req9 vs commit bundled unbundling 在本页 item 3 完成。

怎样守 Req 9、怎样写四门、怎样测副作用是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Extend 和 Verify 不得改已提交状态 not already signed into state ≠ 已经签了扩展就已经进状态 interchangeable：** 官方把扩展两门和不得换已提交状态分开。
- **看见 Verify 过了 not already sh independent of e ≠ 已经是 34 interchangeable：** 官方把 Verify 过了和已经是 sh 不依赖 e 分开。
- **看见扩展在 not already settled ≠ 已经交差 interchangeable：** 官方把扩展在和已经交差分开；349 req9 vs commit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Extend 和 Verify 不得改已提交状态 | 不是已经签了扩展就已经进状态 | 不是本高度状态不得依赖本高度收到的扩展（34） |
| 看见 Verify 过了 | 不是已经是 sh 不依赖 e | 不是一轮一份扩展（350/865） |
| 看见扩展在 | 不是已经交差 | 不是 Prepare 不得改就已经交差（866） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 和 Verify 不得改已提交状态 not already signed into state / not already sh independent of e / not already settled 正式三事（349 余量），必须分开是不是已经签了扩展就已经进状态、是不是已经是 sh 不依赖 e、是不是已经交差。可以跳过「看见签了扩展就已经进状态」。不要另写怎样守 Req 9。349 req9 vs commit bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样守 Req 9、怎样写四门、怎样测副作用。
- 四门无副作用 bundled。那是不变量 349。
- Prepare 不得改已提交状态。那是不变量 349 item 1 余量 / 866。
- 本高度状态不得依赖本高度收到的扩展。那是不变量 34。
- 一轮一份扩展。那是不变量 350 / 865。
