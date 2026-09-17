# 例：看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步 is not already can proceed interchangeable / not already Commit interchangeable / not already unlocked interchangeable

**层次**：实现 / 立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事（374 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事（374 余量）/ not 805 flush-notproceed interchangeable / not 374 flush-vs-sent bundled interchangeable」，不是 Flush bundled（374），也不是 Commit 里等广播就已经能往下走（310），也不是 Usage immediately sync 就已经回包（493/673），也不是 Commit 空请求 Echo 就已经是测（399/733）。不要另写怎样写 Flush。

## 官方三件事

1. **看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步 / 看见立刻叫了 / 这份立刻 is not already 已经能往下走 interchangeable / 310 commitlock interchangeable，也不是已经 Flush bundled（374） interchangeable / 805 flush-notproceed interchangeable / 803 flush-notdelivered interchangeable / 374 flush item 1 冲队列 interchangeable，也不是已经立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事 bundled（374 item 3 余量） interchangeable / 374 flush item 3 interchangeable。**  
   官方写：立刻叫 Flush 是为了做成同步请求；Flush 回包回来，这次同步才算完。看见立刻叫了，不是已经能往下走 interchangeable——本页从 374 item 3 侧钉 not already can proceed 单句。374 flush vs sent bundled unbundling 在本页 item 3 完成。

2. **看见立刻叫了 / 看见回包回来 / 这份立刻 is not already 已经 Commit interchangeable / 310 commitlock interchangeable，也不是已经 Flush bundled（374） interchangeable / 805 flush-notproceed interchangeable / 374 flush item 2 定期 interchangeable / 804 flush-notgates interchangeable，也不是已经 Usage immediately sync 就已经回包 interchangeable / 493 flushusage / 673 flushusage-notimmediatesync interchangeable，也不是已经 Commit 空请求 Echo 就已经是测 interchangeable / 399 commitnoparam / 733 commitnoparam-notflush interchangeable。**  
   官方把回包回来和已经 Commit 分开——374 bundled 第三件事常与 310 / 493 / 399 混成「看见立刻叫了就已经能往下走或已经 Commit interchangeable」，本页钉 not already Commit 单句。

3. **看见立刻叫了 / 看见同步了 / 这份立刻 is not already 已经解锁 interchangeable，也不是已经 Flush bundled（374） interchangeable / 805 flush-notproceed interchangeable / 803 flush-notdelivered interchangeable。**  
   官方把同步了和已经解锁分开。看见同步了，不是已经解锁 interchangeable。374 flush vs sent bundled unbundling 在本页 item 3 完成。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。

## 官方为什么这样拆

- **立刻 Flush not already can proceed ≠ 310 interchangeable：** 官方把立刻同步和已经能往下走分开。
- **看见回包回来 not already Commit ≠ 已经 Commit interchangeable：** 官方把回包回来和已经 Commit 分开。
- **看见同步了 not already unlocked ≠ 已经解锁 interchangeable：** 官方把同步了和已经解锁分开；374 flush vs sent bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 立刻 Flush 是为了做成同步请求、回包回来才算这次同步 | 不是已经能往下走（310） | 不是冲队列（803/374 item 1） |
| 看见立刻叫了 | 不是已经 Commit | 不是 Usage immediately sync（493/673） |
| 看见同步了 | 不是已经解锁 | 不是 Commit 空请求 Echo（399/733） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事（374 余量），必须分开是不是已经能往下走 interchangeable / 310、是不是已经 Commit、是不是已经解锁。可以跳过「看见立刻叫了就已经能往下走」。不要另写怎样写 Flush。374 flush vs sent bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush bundled。那是不变量 374。
- 冲队列。那是不变量 374 item 1 余量 / 803。
- Commit 里等广播就已经能往下走。那是不变量 310。
- Usage immediately sync 就已经回包。那是不变量 493 / 673。
