# 模式：把 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[Commit wait broadcast_tx not already can proceed ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notbroadcast-vs-bundled.md)。

## 三个名字

1. **能调广播 不是 already can proceed：** 看见 Commit 里调了 broadcast_tx / 发了 `/broadcast_tx_sync`，不是已经能往下走 interchangeable / 已经能继续 interchangeable，不是 310 commitlock bundled interchangeable / 301 proposed-removed interchangeable。

2. **等回执 不是 receipt already settled：** 看见等 broadcast_tx 回执再往下走 / 同步等回执，不是已经交差 interchangeable / 已经 settled interchangeable，不是 33 four gates interchangeable / 403 finafter interchangeable / 310 commitlock item 2 interchangeable / 690 commitlock-notunlocked interchangeable。

3. **同步内存池调用 不是 sync call already allowed：** 看见把 broadcast_tx 写进 Commit 顺序逻辑 / Commit 期间要拿内存池锁，不是已经允许写进 Commit 顺序逻辑 interchangeable / 已经能在 Commit 里等锁 interchangeable，不是 690 commitlock-notunlocked interchangeable / 588 finlock interchangeable。

官方把 Commit 里等广播单句、already can proceed、receipt already settled、sync call already allowed 写成三个名字。把它们叫成一个「看见能调广播 就已经能往下走 interchangeable / 就已经交差 interchangeable / 就已经允许写进顺序逻辑 interchangeable」，会把 not already can proceed、not receipt already settled、not sync call already allowed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量），先数清问的是能调广播 是不是 already can proceed / 310 / 301，是不是等回执 是不是 receipt already settled，还是同步内存池调用 是不是 sync call already allowed，再决定要不要同一次发布。310 commitlock vs RPC bundled unbundling 在本页 item 3 完成。
