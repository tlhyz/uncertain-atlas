# 例：看见定期 Flush 是为了让异步请求真发出去 is not already four gates interchangeable / not already received interchangeable / not already settled interchangeable

**层次**：实现 / 定期 Flush not already four gates / not already received / not already settled 正式三事（374 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「定期 Flush not already four gates / not already received / not already settled 正式三事（374 余量）/ not 804 flush-notgates interchangeable / not 374 flush-vs-sent bundled interchangeable」，不是 Flush bundled（374），也不是一条连接就已经是四门（307），也不是 Usage periodically async 就已经发出去（493/672），也不是 Echo Usage 就已经是测实现（492/674）。不要另写怎样写 Flush。

## 官方三件事

1. **看见定期 Flush 是为了让异步请求真发出去 / 看见定期在冲 / 这份定期 is not already 已经是四门 interchangeable / 307 abci-conn interchangeable，也不是已经 Flush bundled（374） interchangeable / 804 flush-notgates interchangeable / 803 flush-notdelivered interchangeable / 374 flush item 1 冲队列 interchangeable，也不是已经定期 Flush not already four gates / not already received / not already settled 正式三事 bundled（374 item 2 余量） interchangeable / 374 flush item 2 interchangeable。**  
   官方写：客户端实现会定期叫 Flush，好让异步请求真的发出去。看见定期在冲，不是已经是四门 interchangeable——本页从 374 item 2 侧钉 not already four gates 单句。374 flush vs sent bundled unbundling 在本页 item 2 续。

2. **看见定期在冲 / 看见发出去了 / 这份定期 is not already 已经收到 interchangeable / 307 abci-conn interchangeable，也不是已经 Flush bundled（374） interchangeable / 804 flush-notgates interchangeable / 374 flush item 3 立刻 interchangeable / 805 flush-notproceed interchangeable，也不是已经 Usage periodically async 就已经发出去 interchangeable / 493 flushusage / 672 flushusage-notperiodicasync interchangeable，也不是已经 Echo Usage 就已经是测实现 interchangeable / 492 echousage / 674 echousage-notflush interchangeable。**  
   官方把发出去了和已经收到分开——374 bundled 第二件事常与 307 / 493 / 492 混成「看见定期在冲就已经是四门或已经交差 interchangeable」，本页钉 not already received 单句。

3. **看见定期在冲 / 看见异步 / 这份定期 is not already 已经交差 interchangeable，也不是已经 Flush bundled（374） interchangeable / 804 flush-notgates interchangeable / 803 flush-notdelivered interchangeable。**  
   官方把异步和已经交差分开。看见异步，不是已经交差 interchangeable。374 flush vs sent bundled unbundling 在本页 item 2 续。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。

## 官方为什么这样拆

- **定期 Flush not already four gates ≠ 307 interchangeable：** 官方把定期冲异步请求和一条连接已经是四门分开。
- **看见发出去了 not already received ≠ 已经收到 interchangeable：** 官方把发出去了和已经收到分开。
- **看见异步 not already settled ≠ 已经交差 interchangeable：** 官方把异步和已经交差分开；374 flush vs sent bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 定期 Flush 是为了让异步请求真发出去 | 不是已经是四门（307） | 不是冲队列（803/374 item 1） |
| 看见定期在冲 | 不是已经收到 | 不是 Usage periodically async（493/672） |
| 看见异步 | 不是已经交差 | 不是 Echo Usage 测实现（492/674） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看定期 Flush not already four gates / not already received / not already settled 正式三事（374 余量），必须分开是不是已经是四门 interchangeable / 307、是不是已经收到、是不是已经交差。可以跳过「看见定期在冲就已经是四门」。不要另写怎样写 Flush。374 flush vs sent bundled unbundling 在本页 item 2 续；续 [`worked-example-flush-notproceed-vs-bundled.md`](worked-example-flush-notproceed-vs-bundled.md)（不变量 805 item 3）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush bundled。那是不变量 374。
- 冲队列。那是不变量 374 item 1 余量 / 803。
- 一条连接就已经是四门。那是不变量 307。
- Usage periodically async 就已经发出去。那是不变量 493 / 672。
