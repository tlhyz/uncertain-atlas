# 模式：把 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[RECHECK not already new transaction ≠ bundled（312）](../../tracks/implementation/worked-example-checktxstate-notrecheck-vs-bundled.md)。

## 三个名字

1. **又跑了 不是 already new transaction：** 看见 Commit 之后又跑了 CheckTx / 对本地池里剩下的再验，不是已经是一笔新交易 interchangeable / 已经是 NEW interchangeable，不是 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable。

2. **Type 是 RECHECK 不是 already treated as NEW：** 看见 Type 在 / CheckTxRequest.Type 标明再验，不是已经当 NEW 处理 interchangeable / 已经 CHECK_TX_TYPE_NEW interchangeable，不是 312 checktxstate item 1 interchangeable / 695 checktxstate-notexecute interchangeable。

3. **Commit 回了 不是 already unlocked：** 看见 Commit 返回 / 应用 Commit 绿了，不是已经放下锁 interchangeable / 已经内存池锁已经放开 interchangeable，不是 310 commitlock interchangeable / 690 commitlock-notunlocked interchangeable / 696 checktxstate-notsame interchangeable。

官方把再验单句、already new transaction、already treated as NEW、already unlocked 写成三个名字。把它们叫成一个「看见又跑了 就已经是新交易 interchangeable / 就已经当 NEW 处理 interchangeable / 就已经解锁 interchangeable」，会把 not already new transaction、not already treated as NEW、not already unlocked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量），先数清问的是又跑了 是不是 already new transaction / 312 / 33，是不是 Type 是 RECHECK 是不是 already treated as NEW，还是 Commit 回了 是不是 already unlocked，再决定要不要同一次发布。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。
