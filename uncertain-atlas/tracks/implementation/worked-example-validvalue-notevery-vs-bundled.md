# 例：看见自己是提议者 is not already every round calls Prepare interchangeable / not already validValue is nil interchangeable / not already settled interchangeable

**层次**：实现 / 自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事（356 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事（356 余量）/ not 852 validvalue-notevery interchangeable / not 356 validvalue-vs-prepare bundled interchangeable」，不是 validValue 跳过 Prepare bundled（356），也不是 Prepare 没有确定性要求（338），也不是 Process 也会在提议者那边叫（351）。不要另写怎样设 validValue。

## 官方三件事

1. **看见只有提议者且 validValue 为 nil 才会调 Prepare / 看见自己是提议者 这份提议者 is not already 已经每轮都会调 Prepare interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 852 validvalue-notevery interchangeable / 851 validvalue-notcall interchangeable / 356 validvalue item 1 非 nil interchangeable，也不是已经自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事 bundled（356 item 2 余量） interchangeable / 356 validvalue item 2 interchangeable。**  
   官方写：验证者 *p* 进入一轮 *r*、高度 *h*，且 *p* 是提议者，并且 *p* 的 *validValue* 为 `nil`，才会走 Prepare 这条路。看见是提议者，不是已经会调 interchangeable——本页从 356 item 2 侧钉 not already every round calls Prepare 单句。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

2. **看见自己是提议者 / 看见进了这一轮 / 这份提议者 is not already 已经是 validValue 为 nil interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 852 validvalue-notevery interchangeable / 356 validvalue item 3 没调 Prepare interchangeable / 853 validvalue-notraw interchangeable，也不是已经 Process 也会在提议者那边叫 interchangeable / 351 procalso interchangeable。**  
   官方把进了这一轮和已经是 validValue 为 nil 分开——356 bundled 第二件事常与 338 混成「看见是提议者就已经每轮都会调或已经是 validValue 为 nil interchangeable」，本页钉 not already validValue is nil 单句。

3. **看见自己是提议者 / 看见规范写了 When / 这份提议者 is not already 已经交差 interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 852 validvalue-notevery interchangeable / 851 validvalue-notcall interchangeable，也不是已经 Prepare 没有确定性要求 interchangeable / 338 prepnondet interchangeable。**  
   官方把 When 写了和已经交差分开。看见规范写了 When，不是已经交差 interchangeable。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **自己是提议者 not already every round calls Prepare ≠ 已经每轮都会调 Prepare interchangeable：** 官方把提议者和 validValue 为 nil 才调分开。
- **看见进了这一轮 not already validValue is nil ≠ 已经是 validValue 为 nil interchangeable：** 官方把进了这一轮和已经是 validValue 为 nil 分开。
- **看见规范写了 When not already settled ≠ 已经交差 interchangeable：** 官方把 When 写了和已经交差分开；356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 自己是提议者 | 不是已经每轮都会调 Prepare | 不是 Prepare 没有确定性要求（338） |
| 看见进了这一轮 | 不是已经是 validValue 为 nil | 不是 Process 也会在提议者那边叫（351） |
| 看见规范写了 When | 不是已经交差 | 不是 validValue 非 nil 就已经还会调（851） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事（356 余量），必须分开是不是已经每轮都会调 Prepare、是不是已经是 validValue 为 nil、是不是已经交差。可以跳过「看见是提议者就已经每轮都会调 Prepare」。不要另写怎样设 validValue。356 validvalue vs prepare bundled unbundling 在本页 item 2 续；续 [`worked-example-validvalue-notraw-vs-bundled.md`](worked-example-validvalue-notraw-vs-bundled.md)（不变量 853 item 3）。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- validValue 跳过 Prepare bundled。那是不变量 356。
- validValue 非 nil 不是已经还会调。那是不变量 356 item 1 余量 / 851。
- Prepare 没有确定性要求。那是不变量 338。
- Process 也会在提议者那边叫。那是不变量 351。
