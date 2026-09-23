# 例：看见直接用了 / 看见有 validValue / 看见锁住了 is not already already still-prepare interchangeable / already can-revise interchangeable / already settled interchangeable

**层次**：实现 / validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量）/ not 821 vv-notstillprepare interchangeable / not 356 validvalue bundled interchangeable」，不是 validValue 跳过 Prepare bundled（356），也不是自己是提议者不是已经每轮都会调 Prepare（822 item 2 余量）或没调 Prepare 不是已经又装了一份 raw 提案（823 item 3 余量）。不要另写怎样设 validValue。

## 官方三件事

规范把 Methods 里若 *p* 有非 `nil` 的 *validValue* 就用它当提案、不再调 `PrepareProposal` 和「已经是直接用了就已经还会调 Prepare interchangeable / 已经是有 validValue 就已经能再改列表 interchangeable / 已经是锁住了就已经交差 interchangeable / 已经是 validvalue bundled interchangeable」分开写成三件独立的实现事，不是「看见本轮直接用它就已经还会调 Prepare interchangeable / 就已经能再改列表 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 validValue 非 nil / 看见本轮直接用它 / 看见直接用了 is not already 已经还会调 Prepare interchangeable / 已经 still-prepare interchangeable / 已经还会调 Prepare 交差 interchangeable / 356 validvalue bundled interchangeable / 311 candidate interchangeable / validvalue-sold-as-prepared interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 821 vv-notstillprepare interchangeable / 356 validvalue item 1 interchangeable，也不是已经 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事 bundled（356 item 1 余量） interchangeable / 356 validvalue item 1 interchangeable，也不是已经每轮都会调（822） interchangeable / 823 vv-notraw interchangeable / 33 fourgates interchangeable，也不是已经候选已经是 ExecuteTxState（311） interchangeable。**  
   官方写：若 *p* 在一轮 *r*、高度 *h* 有非 `nil` 的 *validValue*，共识算法用它当提案，**不**再调 `PrepareProposal`。看见直接用了，不是已经还会调。看见直接用了，不是已经 still-prepare interchangeable——356 钉 bundled 三事，本页从 item 1 侧钉 not already still-prepare 单句。看见 validValue 非 nil，不是已经 validValue 跳过 Prepare bundled（356） interchangeable——356 钉 bundled，本页钉 item 1 第一件事。看见直接用了，不是已经每轮都会调（822） interchangeable——822 另钉 item 2。看见直接用了，不是已经候选已经是 ExecuteTxState（311） interchangeable——311 另钉。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见有 validValue / 看见非 nil / 看见本轮有 validValue is not already 已经能再改列表 interchangeable / 已经 can-revise interchangeable / 已经能再改列表交差 interchangeable / 356 validvalue bundled interchangeable / 355 preparedrop interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 821 vv-notstillprepare interchangeable / 356 validvalue item 2 提议者 interchangeable / 356 validvalue item 3 没调 interchangeable，也不是已经 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事 bundled（356 item 1 余量） interchangeable / 356 validvalue item 1 interchangeable，也不是已经还会调 Prepare（本页第一件事） interchangeable。**  
   官方写：看见有 validValue，不是已经能再改列表。看见非 nil，不是已经 can-revise interchangeable——本页钉 not already can-revise 单句。看见本轮有 validValue，不是已经还会调 Prepare（本页第一件事） interchangeable——三件事分开钉。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

3. **看见锁住了 / 看见用了 validValue / 看见本轮锁住 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 356 validvalue bundled interchangeable / 33 fourgates interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 821 vv-notstillprepare interchangeable / 356 validvalue item 2 / 356 validvalue item 3，也不是已经 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事 bundled（356 item 1 余量） interchangeable / 356 validvalue item 1 interchangeable，也不是已经还会调 Prepare（本页第一件事） interchangeable / 已经能再改列表（本页第二件事） interchangeable。**  
   官方写：看见锁住了，不是已经交差。看见用了 validValue，不是已经 settled interchangeable——本页钉 not already settled 单句。看见本轮锁住，不是已经能再改列表（本页第二件事） interchangeable——三件事分开钉。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。validValue 跳过 Prepare bundled（356）、自己是提议者不是已经每轮都会调 Prepare（356 item 2 余量 / 822）、没调 Prepare 不是已经又装了一份 raw 提案（356 item 3 余量 / 823）、候选已经是 ExecuteTxState（311）、Prepare 没有确定性要求（338）、从提案拿掉 tx 就已经从内存池删掉（355）是另外那套，本页不抄。

## 官方为什么这样拆

- **直接用了 not already still-prepare ≠ 356 / 311 interchangeable：** 官方把直接用 validValue 和还会调 Prepare 分开。
- **有 validValue not already can-revise ≠ 已经能再改列表 interchangeable：** 官方把有 validValue 和已经能再改列表分开。
- **锁住了 not already settled ≠ 已经交差 interchangeable：** 官方把锁住了和已经交差分开；356 validvalue vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 直接用了 | 不是 already still-prepare | 不是候选已经是 ExecuteTxState alone（311） |
| 有 validValue | 不是 already can-revise | 不是提议者 already every-round alone（822） |
| 锁住了 | 不是 already settled | 不是没调 Prepare already new-raw alone（823） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validValue 非 nil 不是已经还会调 Prepare not already still-prepare / not already can-revise / not already settled 正式三事（356 余量），必须分开直接用了 是不是 already still-prepare interchangeable / 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable、有 validValue 是不是 already can-revise interchangeable、锁住了 是不是 already settled interchangeable。可以跳过「看见直接用了就已经还会调 Prepare interchangeable / 就已经能再改列表 interchangeable / 就已经交差 interchangeable」。不要另写怎样设 validValue。356 validvalue vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-vv-noteveryround-vs-bundled.md`](worked-example-vv-noteveryround-vs-bundled.md)（不变量 822 item 2）；完成见 823。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- validValue 跳过 Prepare bundled。那是不变量 356。
- 自己是提议者不是已经每轮都会调 Prepare。那是不变量 356 item 2 余量 / 822。
- 没调 Prepare 不是已经又装了一份 raw 提案。那是不变量 356 item 3 余量 / 823。
- 候选已经是 ExecuteTxState。那是不变量 311。
- Prepare 没有确定性要求。那是不变量 338。
- 从提案拿掉 tx 就已经从内存池删掉。那是不变量 355。
