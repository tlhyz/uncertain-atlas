# 例：看见没调 Prepare / 看见用了 validValue / 看见跳过了 is not already already reap-again interchangeable / already new-raw interchangeable / already preparedrop interchangeable

**层次**：实现 / 没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量）/ not 823 vv-notraw interchangeable / not 356 validvalue bundled interchangeable」，不是 validValue 跳过 Prepare bundled（356），也不是 validValue 非 nil 不是已经还会调 Prepare（821 item 1 余量）或自己是提议者不是已经每轮都会调 Prepare（822 item 2 余量）。不要另写怎样设 validValue。

## 官方三件事

规范把 Methods 里只有走 Prepare 那条路时引擎才从内存池按优先级收未决交易并造头、validValue 非 nil 时不会再收、不会再造头 和「已经是没调 Prepare 就已经又收了一遍池子 interchangeable / 已经是用了 validValue 就已经是一份新的 raw 提案 interchangeable / 已经是跳过了就已经从提案拿掉 tx interchangeable / 已经是 validvalue bundled interchangeable」分开写成三件独立的实现事，不是「看见没调 Prepare 就已经又装了一份 raw 提案 interchangeable / 就已经是一份新的 raw 提案 interchangeable / 就已经从提案拿掉 tx interchangeable」一件事：

1. **看见没调 Prepare / 看见 validValue 非 nil 时不会再从池子收 / 看见不会再从池子按优先级收 is not already 已经又收了一遍池子 interchangeable / 已经 reap-again interchangeable / 已经又收池子交差 interchangeable / 356 validvalue bundled interchangeable / 355 preparedrop interchangeable / validvalue-sold-as-prepared interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 823 vv-notraw interchangeable / 356 validvalue item 3 interchangeable，也不是已经没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事 bundled（356 item 3 余量） interchangeable / 356 validvalue item 3 interchangeable，也不是已经还会调 Prepare（821） interchangeable / 822 vv-noteveryround interchangeable / 311 candidate interchangeable，也不是已经从提案拿掉 tx 就已经从内存池删掉（355） interchangeable。**  
   官方写：只有走 Prepare 那条路时，引擎才从内存池按优先级收未决交易并造头。看见没调 Prepare，不是已经又收了一遍池子。看见没调 Prepare，不是已经 reap-again interchangeable——356 钉 bundled 三事，本页从 item 3 侧钉 not already reap-again 单句。看见没调 Prepare，不是已经 validValue 跳过 Prepare bundled（356） interchangeable——356 钉 bundled，本页钉 item 3 第一件事。看见没调 Prepare，不是已经还会调 Prepare（821） interchangeable——821 另钉 item 1。看见没调 Prepare，不是已经每轮都会调（822） interchangeable——822 另钉 item 2。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见用了 validValue / 看见不会再造头 / 看见用 validValue 当提案 is not already 已经是一份新的 raw 提案 interchangeable / 已经 new-raw interchangeable / 已经新 raw 交差 interchangeable / 356 validvalue bundled interchangeable / 311 candidate interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 823 vv-notraw interchangeable / 356 validvalue item 1 非 nil interchangeable / 356 validvalue item 2 提议者 interchangeable，也不是已经没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事 bundled（356 item 3 余量） interchangeable / 356 validvalue item 3 interchangeable，也不是已经又收了一遍池子（本页第一件事） interchangeable。**  
   官方写：看见用了 validValue，不是已经是一份新的 raw 提案。看见不会再造头，不是已经 new-raw interchangeable——本页钉 not already new-raw 单句。看见用 validValue 当提案，不是已经又收了一遍池子（本页第一件事） interchangeable——三件事分开钉。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

3. **看见跳过了 / 看见跳过 Prepare / 看见没走 Prepare 那条路 is not already 已经从提案拿掉 tx interchangeable / 已经 preparedrop interchangeable / 已经从提案拿掉交差 interchangeable / 356 validvalue bundled interchangeable / 355 preparedrop interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 823 vv-notraw interchangeable / 356 validvalue item 1 / 356 validvalue item 2，也不是已经没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事 bundled（356 item 3 余量） interchangeable / 356 validvalue item 3 interchangeable，也不是已经又收了一遍池子（本页第一件事） interchangeable / 已经是一份新的 raw 提案（本页第二件事） interchangeable。**  
   官方写：看见跳过了，不是已经从提案拿掉 tx。看见跳过 Prepare，不是已经 preparedrop interchangeable——本页钉 not already preparedrop 单句。看见没走 Prepare 那条路，不是已经是一份新的 raw 提案（本页第二件事） interchangeable——三件事分开钉。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。validValue 跳过 Prepare bundled（356）、validValue 非 nil 不是已经还会调 Prepare（356 item 1 余量 / 821）、自己是提议者不是已经每轮都会调 Prepare（356 item 2 余量 / 822）、候选已经是 ExecuteTxState（311）、Prepare 没有确定性要求（338）、从提案拿掉 tx 就已经从内存池删掉（355）是另外那套，本页不抄。

## 官方为什么这样拆

- **没调 Prepare not already reap-again ≠ 356 / 355 interchangeable：** 官方把没调 Prepare 和又收了一遍池子分开。
- **用了 validValue not already new-raw ≠ 已经是一份新的 raw 提案 interchangeable：** 官方把用了 validValue 和已经是一份新的 raw 提案分开。
- **跳过了 not already preparedrop ≠ 已经从提案拿掉 tx interchangeable：** 官方把跳过了和已经从提案拿掉 tx 分开；356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 没调 Prepare | 不是 already reap-again | 不是从提案拿掉 tx 就已经从内存池删掉 alone（355） |
| 用了 validValue | 不是 already new-raw | 不是直接用了 already still-prepare alone（821） |
| 跳过了 | 不是 already preparedrop | 不是是提议者 already every-round alone（822） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没调 Prepare 不是已经又装了一份 raw 提案 not already reap-again / not already new-raw / not already preparedrop 正式三事（356 余量），必须分开没调 Prepare 是不是 already reap-again interchangeable / 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable、用了 validValue 是不是 already new-raw interchangeable、跳过了 是不是 already preparedrop interchangeable。可以跳过「看见没调 Prepare 就已经又收了一遍池子 interchangeable / 就已经是一份新的 raw 提案 interchangeable / 就已经从提案拿掉 tx interchangeable」。不要另写怎样设 validValue。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成（821 + 822 + 823）。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- validValue 跳过 Prepare bundled。那是不变量 356。
- validValue 非 nil 不是已经还会调 Prepare。那是不变量 356 item 1 余量 / 821。
- 自己是提议者不是已经每轮都会调 Prepare。那是不变量 356 item 2 余量 / 822。
- 候选已经是 ExecuteTxState。那是不变量 311。
- Prepare 没有确定性要求。那是不变量 338。
- 从提案拿掉 tx 就已经从内存池删掉。那是不变量 355。
