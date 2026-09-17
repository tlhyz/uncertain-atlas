# 例：看见 validValue 非 nil is not already will still call Prepare interchangeable / not already can change list interchangeable / not already settled interchangeable

**层次**：实现 / validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事（356 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事（356 余量）/ not 851 validvalue-notcall interchangeable / not 356 validvalue-vs-prepare bundled interchangeable」，不是 validValue 跳过 Prepare bundled（356），也不是候选已经是 ExecuteTxState（311），也不是 Prepare 没有确定性要求（338）。不要另写怎样设 validValue。

## 官方三件事

1. **看见 validValue 非 nil / 看见本轮直接用它 这份直接用 is not already 已经还会调 Prepare interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 851 validvalue-notcall interchangeable / 852 validvalue-notevery interchangeable / 356 validvalue item 2 提议者 interchangeable，也不是已经 validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事 bundled（356 item 1 余量） interchangeable / 356 validvalue item 1 interchangeable。**  
   官方写：若 *p* 在一轮 *r*、高度 *h* 有非 `nil` 的 *validValue*，共识算法用它当提案，不再调 `PrepareProposal`。看见直接用了，不是已经还会调 interchangeable——本页从 356 item 1 侧钉 not already will still call Prepare 单句。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见本轮直接用它 / 看见有 validValue / 这份直接用 is not already 已经能再改列表 interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 851 validvalue-notcall interchangeable / 356 validvalue item 3 没调 Prepare interchangeable / 853 validvalue-notraw interchangeable，也不是已经从提案拿掉 tx 就已经从内存池删掉 interchangeable / 355 prepdrop interchangeable。**  
   官方把有 validValue 和已经能再改列表分开——356 bundled 第一件事常与 311 混成「看见本轮直接用它就已经还会调 Prepare 或已经能再改列表 interchangeable」，本页钉 not already can change list 单句。

3. **看见本轮直接用它 / 看见锁住了 / 这份直接用 is not already 已经交差 interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 851 validvalue-notcall interchangeable / 852 validvalue-notevery interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把锁住了和已经交差分开。看见锁住了，不是已经交差 interchangeable。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **validValue 非 nil not already will still call Prepare ≠ 已经还会调 Prepare interchangeable：** 官方把直接用 validValue 和还会调 Prepare 分开。
- **看见有 validValue not already can change list ≠ 已经能再改列表 interchangeable：** 官方把有 validValue 和已经能再改列表分开。
- **看见锁住了 not already settled ≠ 已经交差 interchangeable：** 官方把锁住了和已经交差分开；356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| validValue 非 nil | 不是已经还会调 Prepare | 不是候选已经是 ExecuteTxState（311） |
| 看见有 validValue | 不是已经能再改列表 | 不是从提案拿掉 tx（355） |
| 看见锁住了 | 不是已经交差 | 不是 Prepare 没有确定性要求（338） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validValue 非 nil not already will still call Prepare / not already can change list / not already settled 正式三事（356 余量），必须分开是不是已经还会调 Prepare、是不是已经能再改列表、是不是已经交差。可以跳过「看见本轮直接用它就已经还会调 Prepare」。不要另写怎样设 validValue。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-validvalue-notevery-vs-bundled.md`](worked-example-validvalue-notevery-vs-bundled.md)（不变量 852 item 2）。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- validValue 跳过 Prepare bundled。那是不变量 356。
- 自己是提议者不是已经每轮都会调。那是不变量 356 item 2 余量 / 852。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 从提案拿掉 tx 就已经从内存池删掉。那是不变量 355。
