# 模式：把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[把 t1 改成 t2 not already t1-lookup ≠ bundled（355）](../../tracks/implementation/worked-example-retarget-nottraceable-vs-bundled.md)。

## 三个名字

1. **t1 没进块 不是 already t1-lookup：** 看见把 t1 改成 t2 / t1 没进块 / t1 没进已提交块，不是已经还能按 t1 查到 interchangeable / 已经 t1-lookup interchangeable / 已经按 t1 查到交差 interchangeable，不是 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable。

2. **t2 进了块 不是 already origin-known：** 看见 t2 进了块 / t2 在已提交块里 / 改成了 t2，不是已经有人知道 t2 来自 t1 interchangeable / 已经 origin-known interchangeable / 已经来源已知交差 interchangeable，不是 33 fourgates interchangeable / 819 add-notmempool interchangeable。

3. **改了 不是 already settled：** 看见改了 / 拿掉再加 / 改了列表，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 818 drop-notmempool interchangeable / 301 proposed-removed interchangeable。

官方把 t1 没进块、不是已经有人知道来源、不是已经交差写成三个名字。把它们叫成一个「看见 t1 没进块就已经还能按 t1 查到 interchangeable / 就已经有人知道来源 interchangeable / 就已经交差 interchangeable」，会把 not already t1-lookup、not already origin-known、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把 t1 改成 t2 不是已经还能按 t1 查到 not already t1-lookup / not already origin-known / not already settled 正式三事（355 余量），先数清问的是 t1 没进块 是不是 already t1-lookup / 355 / preparedrop-sold-as-evicted，是不是 t2 进了块 是不是 already origin-known，还是改了 是不是 already settled，再决定要不要同一次发布。355 preparedrop vs mempool bundled unbundling 在本页 item 3 完成。
