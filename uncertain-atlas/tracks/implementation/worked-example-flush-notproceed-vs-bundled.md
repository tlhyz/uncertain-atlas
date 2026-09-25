# 例：看见立刻叫了 / 看见回包回来 / 看见同步了 is not already already proceed interchangeable / already commit interchangeable / already unlocked interchangeable

**层次**：实现 / 立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量）/ not 871 flush-notproceed interchangeable / not 374 flush bundled interchangeable」，不是 flush bundled（374），也不是 Flush 要把客户端排队的消息冲到服务端不是已经送到（869 item 1 余量）或定期 Flush 是为了让异步请求真发出去不是已经是四门（870 item 2 余量）。不要另写怎样写 Flush。

## 官方三件事

规范把 Methods 里立刻 Flush 是为了做成同步请求、回包回来才算这次同步 和「已经是立刻叫了就已经能往下走 interchangeable / 已经是回包回来就已经 Commit interchangeable / 已经是同步了就已经解锁 interchangeable / 已经是 flush bundled interchangeable」分开写成三件独立的实现事，不是「看见立刻叫了就已经能往下走 interchangeable / 就已经 Commit interchangeable / 就已经解锁 interchangeable」一件事：

1. **看见立刻叫了 / 看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步 / 看见立刻叫了 Flush is not already 已经能往下走 interchangeable / 已经 proceed interchangeable / 已经能往下走交差 interchangeable / 374 flush bundled interchangeable / 310 commit-lock interchangeable / flush-sold-as-sent interchangeable，也不是已经 flush bundled（374） interchangeable / 871 flush-notproceed interchangeable / 374 flush item 3 interchangeable，也不是已经立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事 bundled（374 item 3 余量） interchangeable / 374 flush item 3 interchangeable，也不是已经叫了就已经送到（869） interchangeable / 已经定期就已经是四门（870） interchangeable / 307 abci-conn interchangeable，也不是已经 Commit 里等广播就已经能往下走（310） interchangeable。**  
   官方写：立刻叫 Flush 是为了做成同步请求；Flush 回包回来，这次同步才算完。看见立刻叫了，不是已经能往下走。看见立刻叫了，不是已经 proceed interchangeable——374 钉 bundled 三事，本页从 item 3 侧钉 not already proceed 单句。看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步，不是已经 flush bundled（374） interchangeable——374 钉 bundled，本页钉 item 3 第一件事。看见立刻叫了，不是已经叫了就已经送到（869） interchangeable——869 另钉 item 1。看见立刻叫了，不是已经定期就已经是四门（870） interchangeable——870 另钉 item 2。374 flush-vs-sent bundled unbundling 在本页 item 3 完成。

2. **看见回包回来 / 看见 Flush 回包回来 / 看见回包在 is not already 已经 Commit interchangeable / 已经 commit interchangeable / 已经 Commit 交差 interchangeable / 374 flush bundled interchangeable / 310 commit-lock interchangeable，也不是已经 flush bundled（374） interchangeable / 871 flush-notproceed interchangeable / 374 flush item 1 叫了 interchangeable / 374 flush item 2 定期 interchangeable，也不是已经立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事 bundled（374 item 3 余量） interchangeable / 374 flush item 3 interchangeable，也不是已经能往下走（本页第一件事） interchangeable。**  
   官方写：看见回包回来，不是已经 Commit。看见 Flush 回包回来，不是已经 commit interchangeable——本页钉 not already commit 单句。看见回包在，不是已经能往下走（本页第一件事） interchangeable——三件事分开钉。374 flush-vs-sent bundled unbundling 在本页 item 3 完成。

3. **看见同步了 / 看见这次同步算完 / 看见同步完了 is not already 已经解锁 interchangeable / 已经 unlocked interchangeable / 已经解锁交差 interchangeable / 374 flush bundled interchangeable / 310 commit-lock interchangeable，也不是已经 flush bundled（374） interchangeable / 871 flush-notproceed interchangeable / 374 flush item 1 / 374 flush item 2，也不是已经立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事 bundled（374 item 3 余量） interchangeable / 374 flush item 3 interchangeable，也不是已经能往下走（本页第一件事） interchangeable / 已经 Commit（本页第二件事） interchangeable。**  
   官方写：看见同步了，不是已经解锁。看见这次同步算完，不是已经 unlocked interchangeable——本页钉 not already unlocked 单句。看见同步完了，不是已经 Commit（本页第二件事） interchangeable——三件事分开钉。374 flush-vs-sent bundled unbundling 在本页 item 3 完成。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。flush bundled（374）、Flush 要把客户端排队的消息冲到服务端不是已经送到（374 item 1 余量 / 869）、定期 Flush 是为了让异步请求真发出去不是已经是四门（374 item 2 余量 / 870）、HasChannel 就已经入队（309）、一条连接就已经是四门（307）、Commit 里等广播就已经能往下走（310）是另外那套，本页不抄。

## 官方为什么这样拆

- **立刻叫了 not already proceed ≠ 374 / 310 interchangeable：** 官方把立刻同步和已经能往下走分开。
- **回包回来 not already commit ≠ 已经 Commit interchangeable：** 官方把回包回来和已经 Commit 分开。
- **同步了 not already unlocked ≠ 已经解锁 interchangeable：** 官方把同步完了和已经解锁分开；374 flush-vs-sent bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻叫了 | 不是 already proceed | 不是 Commit 里等广播就已经能往下走 alone（310） |
| 回包回来 | 不是 already commit | 不是叫了 already sent alone（869） |
| 同步了 | 不是 already unlocked | 不是定期 already fourgates alone（870） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量），必须分开立刻叫了 是不是 already proceed interchangeable / 374 flush bundled interchangeable / flush-sold-as-sent interchangeable、回包回来 是不是 already commit interchangeable、同步了 是不是 already unlocked interchangeable。可以跳过「看见立刻叫了就已经能往下走 interchangeable / 就已经 Commit interchangeable / 就已经解锁 interchangeable」。不要另写怎样写 Flush。374 flush-vs-sent bundled unbundling 在本页 item 3 完成（869 + 870 + 871）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- flush bundled。那是不变量 374。
- Flush 要把客户端排队的消息冲到服务端不是已经送到。那是不变量 374 item 1 余量 / 869。
- 定期 Flush 是为了让异步请求真发出去不是已经是四门。那是不变量 374 item 2 余量 / 870。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
