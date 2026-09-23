# 例：看见是提议者 / 看见进了这一轮 / 看见规范写了 When is not already already will-call interchangeable / already vv-nil interchangeable / already every-round interchangeable

**层次**：实现 / 自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量）/ not 822 vv-noteveryround interchangeable / not 356 validvalue bundled interchangeable」，不是 validValue 跳过 Prepare bundled（356），也不是 validValue 非 nil 不是已经还会调 Prepare（821 item 1 余量）或没调 Prepare 不是已经又装了一份 raw 提案（823 item 3 余量）。不要另写怎样设 validValue。

## 官方三件事

规范把 Methods 里只有提议者且 validValue 为 nil 才会调 Prepare 和「已经是提议者就已经会调 interchangeable / 已经是进了这一轮就已经是 validValue 为 nil interchangeable / 已经是规范写了 When 就已经每轮都会叫 interchangeable / 已经是 validvalue bundled interchangeable」分开写成三件独立的实现事，不是「看见自己是提议者就已经每轮都会调 Prepare interchangeable / 就已经是 validValue 为 nil interchangeable / 就已经每轮都会叫 interchangeable」一件事：

1. **看见自己是提议者 / 看见是提议者 / 看见 *p* 是提议者 is not already 已经会调 Prepare interchangeable / 已经 will-call interchangeable / 已经会调 Prepare 交差 interchangeable / 356 validvalue bundled interchangeable / 338 preparenondet interchangeable / validvalue-sold-as-prepared interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 822 vv-noteveryround interchangeable / 356 validvalue item 2 interchangeable，也不是已经自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事 bundled（356 item 2 余量） interchangeable / 356 validvalue item 2 interchangeable，也不是已经还会调 Prepare（821） interchangeable / 823 vv-notraw interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 没有确定性要求（338） interchangeable。**  
   官方写：验证者 *p* 进入一轮 *r*、高度 *h*，且 *p* 是提议者，**并且** *p* 的 *validValue* 为 `nil`，才会走 Prepare 这条路。看见是提议者，不是已经会调。看见是提议者，不是已经 will-call interchangeable——356 钉 bundled 三事，本页从 item 2 侧钉 not already will-call 单句。看见自己是提议者，不是已经 validValue 跳过 Prepare bundled（356） interchangeable——356 钉 bundled，本页钉 item 2 第一件事。看见是提议者，不是已经还会调 Prepare（821） interchangeable——821 另钉 item 1。看见是提议者，不是已经 Prepare 没有确定性要求（338） interchangeable——338 另钉。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

2. **看见进了这一轮 / 看见进入一轮 *r* / 看见进了高度 *h* is not already 已经是 validValue 为 nil interchangeable / 已经 vv-nil interchangeable / 已经 validValue 为 nil 交差 interchangeable / 356 validvalue bundled interchangeable / 338 preparenondet interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 822 vv-noteveryround interchangeable / 356 validvalue item 1 非 nil interchangeable / 356 validvalue item 3 没调 interchangeable，也不是已经自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事 bundled（356 item 2 余量） interchangeable / 356 validvalue item 2 interchangeable，也不是已经会调 Prepare（本页第一件事） interchangeable。**  
   官方写：看见进了这一轮，不是已经是 validValue 为 nil。看见进入一轮 *r*，不是已经 vv-nil interchangeable——本页钉 not already vv-nil 单句。看见进了高度 *h*，不是已经会调 Prepare（本页第一件事） interchangeable——三件事分开钉。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

3. **看见规范写了 When / 看见 When 写了调 Prepare / 看见规范写了才会调 is not already 已经每轮都会调 Prepare interchangeable / 已经 every-round interchangeable / 已经每轮都会调交差 interchangeable / 356 validvalue bundled interchangeable / 33 fourgates interchangeable，也不是已经 validValue 跳过 Prepare bundled（356） interchangeable / 822 vv-noteveryround interchangeable / 356 validvalue item 1 / 356 validvalue item 3，也不是已经自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事 bundled（356 item 2 余量） interchangeable / 356 validvalue item 2 interchangeable，也不是已经会调 Prepare（本页第一件事） interchangeable / 已经是 validValue 为 nil（本页第二件事） interchangeable。**  
   官方写：看见规范写了 When，不是已经每轮都会叫。看见 When 写了调 Prepare，不是已经 every-round interchangeable——本页钉 not already every-round 单句。看见规范写了才会调，不是已经是 validValue 为 nil（本页第二件事） interchangeable——三件事分开钉。356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

怎样设 validValue、怎样从池子收交易、怎样造头是规范里的做法，本页不抄。validValue 跳过 Prepare bundled（356）、validValue 非 nil 不是已经还会调 Prepare（356 item 1 余量 / 821）、没调 Prepare 不是已经又装了一份 raw 提案（356 item 3 余量 / 823）、候选已经是 ExecuteTxState（311）、Prepare 没有确定性要求（338）、从提案拿掉 tx 就已经从内存池删掉（355）是另外那套，本页不抄。

## 官方为什么这样拆

- **是提议者 not already will-call ≠ 356 / 338 interchangeable：** 官方把是提议者和已经会调 Prepare 分开。
- **进了这一轮 not already vv-nil ≠ 已经是 validValue 为 nil interchangeable：** 官方把进了这一轮和已经是 validValue 为 nil 分开。
- **规范写了 When not already every-round ≠ 已经每轮都会调 interchangeable：** 官方把规范写了 When 和已经每轮都会调分开；356 validvalue vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 是提议者 | 不是 already will-call | 不是 Prepare 没有确定性要求 alone（338） |
| 进了这一轮 | 不是 already vv-nil | 不是直接用了 already still-prepare alone（821） |
| 规范写了 When | 不是 already every-round | 不是没调 Prepare already new-raw alone（823） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自己是提议者不是已经每轮都会调 Prepare not already will-call / not already vv-nil / not already every-round 正式三事（356 余量），必须分开是提议者 是不是 already will-call interchangeable / 356 validvalue bundled interchangeable / validvalue-sold-as-prepared interchangeable、进了这一轮 是不是 already vv-nil interchangeable、规范写了 When 是不是 already every-round interchangeable。可以跳过「看见是提议者就已经会调 interchangeable / 就已经是 validValue 为 nil interchangeable / 就已经每轮都会叫 interchangeable」。不要另写怎样设 validValue。356 validvalue vs prepare bundled unbundling 在本页 item 2 续（821 + 822）；完成 [`worked-example-vv-notraw-vs-bundled.md`](worked-example-vv-notraw-vs-bundled.md)（不变量 823 item 3）。

## 本页不抄

- 怎样设 validValue、怎样从池子收交易、怎样造头。
- validValue 跳过 Prepare bundled。那是不变量 356。
- validValue 非 nil 不是已经还会调 Prepare。那是不变量 356 item 1 余量 / 821。
- 没调 Prepare 不是已经又装了一份 raw 提案。那是不变量 356 item 3 余量 / 823。
- 候选已经是 ExecuteTxState。那是不变量 311。
- Prepare 没有确定性要求。那是不变量 338。
- 从提案拿掉 tx 就已经从内存池删掉。那是不变量 355。
