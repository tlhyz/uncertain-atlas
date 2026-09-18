# 模式：把 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[Commit 里等 broadcast_tx not already can proceed ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notbroadcast-vs-bundled.md)。

## 三个名字

1. **能调广播 不是 already can proceed：** 看见 Commit 里调了 broadcast_tx / 发了 `/broadcast_tx_sync` 或 `/broadcast_tx`，不是已经能往下走 interchangeable / 已经能继续 interchangeable，不是 310 commitlock bundled interchangeable / 689 commitlock-notrpcsafe interchangeable / 690 commitlock-notunlocked interchangeable。

2. **等回执 不是 already settled：** 看见 waits for the response / 等 broadcast 回了再往下，不是已经交差 interchangeable / 已经 Finalize + Commit interchangeable，不是 33 four gates interchangeable / 403 finafter interchangeable。

3. **同步内存池调用 不是 already allowed sync mempool in Commit：** 看见 Synchronous mempool-related calls / 在 Commit 顺序逻辑里调广播，不是已经允许写进 Commit 顺序逻辑 interchangeable / 已经可以在 Commit 里等锁 interchangeable，不是 310 commitlock item 1 interchangeable / 301 proposed-removed interchangeable。

官方把能调广播单句、already can proceed、already settled、already allowed sync mempool in Commit 写成三个名字。把它们叫成一个「看见能调广播 就已经能往下走 interchangeable / 就已经交差 interchangeable / 就已经允许 interchangeable」，会把 not already can proceed、not already settled、not already allowed sync mempool in Commit 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量），先数清问的是能调广播 是不是 already can proceed / 310 / 689，是不是等回执 是不是 already settled，还是同步内存池调用 是不是 already allowed，再决定要不要同一次发布。310 commitlock vs RPC bundled unbundling 在本页 item 3 完成。
