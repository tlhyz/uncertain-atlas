# 例：看见没调 Prepare is not already packed another raw proposal interchangeable / not already dropped tx from proposal interchangeable / not already settled interchangeable

**层次**：实现 / 没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事（356 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事（356 余量）/ not 853 validvalue-notraw interchangeable / not 356 validvalue-vs-prepare bundled interchangeable」，不是 validValue 跳过 Prepare bundled（356），也不是从提案拿掉 tx 就已经从内存池删掉（355），也不是候选已经是 ExecuteTxState（311）。不要另写怎样设 validValue。

## 官方三件事

1. **看见 validValue 非 nil 时不会再从池子按优先级收交易、不会再造头 / 看见没调 Prepare 这份跳过 is not already 已经又装了一份 raw 提案 interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 853 validvalue-notraw interchangeable / 851 validvalue-notcall interchangeable / 356 validvalue item 1 非 nil interchangeable，也不是已经没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事 bundled（356 item 3 余量） interchangeable / 356 validvalue item 3 interchangeable。**  
   官方写：只有走 Prepare 那条路时，引擎才从内存池按优先级收未决交易并造头。看见没调 Prepare，不是已经又收了一遍池子 interchangeable——本页从 356 item 3 侧钉 not already packed another raw proposal 单句。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见没调 Prepare / 看见用了 validValue / 这份跳过 is not already 已经从提案拿掉 tx interchangeable / 355 prepdrop interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 853 validvalue-notraw interchangeable / 356 validvalue item 2 提议者 interchangeable / 852 validvalue-notevery interchangeable，也不是已经从提案拿掉 tx 就已经从内存池删掉 interchangeable / 355 prepdrop interchangeable。**  
   官方把用了 validValue 和已经从提案拿掉 tx 分开——356 bundled 第三件事常与 355 混成「看见没调 Prepare 就已经又装了一份 raw 提案或已经从提案拿掉 tx interchangeable」，本页钉 not already dropped tx from proposal 单句。

3. **看见没调 Prepare / 看见跳过了 / 这份跳过 is not already 已经交差 interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 853 validvalue-notraw interchangeable / 851 validvalue-notcall interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把跳过了和已经交差分开。看见跳过了，不是已经交差 interchangeable。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **没调 Prepare not already packed another raw proposal ≠ 已经又装了一份 raw 提案 interchangeable：** 官方把跳过 Prepare 和从池子再收一遍分开。
- **看见用了 validValue not already dropped tx from proposal ≠ 355 interchangeable：** 官方把用了 validValue 和已经从提案拿掉 tx 分开。
- **看见跳过了 not already settled ≠ 已经交差 interchangeable：** 官方把跳过了和已经交差分开；356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没调 Prepare | 不是已经又装了一份 raw 提案 | 不是从提案拿掉 tx 就已经从内存池删掉（355） |
| 看见用了 validValue | 不是已经从提案拿掉 tx | 不是候选已经是 ExecuteTxState（311） |
| 看见跳过了 | 不是已经交差 | 不是 Prepare 没有确定性要求（338） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事（356 余量），必须分开是不是已经又装了一份 raw 提案、是不是已经从提案拿掉 tx interchangeable / 355、是不是已经交差。可以跳过「看见没调 Prepare 就已经又装了一份 raw 提案」。不要另写怎样设 validValue。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- validValue 跳过 Prepare bundled。那是不变量 356。
- validValue 非 nil 不是已经还会调。那是不变量 356 item 1 余量 / 851。
- 从提案拿掉 tx 就已经从内存池删掉。那是不变量 355。
- 候选已经是 ExecuteTxState。那是不变量 311。
