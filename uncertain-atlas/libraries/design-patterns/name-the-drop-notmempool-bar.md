# 模式：把从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[从提案拿掉 tx not already out-of-pool ≠ bundled（355）](../../tracks/implementation/worked-example-drop-notmempool-vs-bundled.md)。

## 三个名字

1. **本块不提 不是 already out-of-pool：** 看见从提案拿掉 tx / 本块不提 / 回包没有它，不是已经从内存池删掉 interchangeable / 已经 out-of-pool interchangeable / 已经出池交差 interchangeable，不是 355 preparedrop bundled interchangeable / preparedrop-sold-as-evicted interchangeable。

2. **拿掉了 不是 already never-propose：** 看见拿掉了 / 本块不提这笔 / 没写进回包，不是已经永远不提 interchangeable / 已经 never-propose interchangeable / 已经永远不提交差 interchangeable，不是 301 proposed-removed interchangeable / 819 add-notmempool interchangeable。

3. **回包没有它 不是 already settled：** 看见回包没有它 / 回包里没这笔 / 没写进 txs，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 820 retarget-nottraceable interchangeable / 33 fourgates interchangeable。

官方把本块不提、不是已经永远不提、不是已经交差写成三个名字。把它们叫成一个「看见本块不提就已经出池 interchangeable / 就已经永远不提 interchangeable / 就已经交差 interchangeable」，会把 not already out-of-pool、not already never-propose、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从提案拿掉 tx 不是已经从内存池删掉 not already out-of-pool / not already never-propose / not already settled 正式三事（355 余量），先数清问的是本块不提 是不是 already out-of-pool / 355 / preparedrop-sold-as-evicted，是不是拿掉了 是不是 already never-propose，还是回包没有它 是不是 already settled，再决定要不要同一次发布。355 preparedrop vs mempool bundled unbundling 在本页 item 1 启动。
