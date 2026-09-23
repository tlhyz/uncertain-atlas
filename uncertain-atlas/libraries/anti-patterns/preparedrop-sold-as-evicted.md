# 反模式：看见从提案拿掉 tx 就当成已经从内存池删掉 / 看见往提案加了一笔新的就当成已经进了内存池 / 看见把 t1 改成 t2 就当成已经还能按 t1 查到

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[从提案拿掉 tx ≠ 已经从内存池删掉](../../tracks/implementation/worked-example-prepare-drop-vs-mempool.md)。

## 塌法

1. 看见从提案拿掉 tx / 看见本块不提，就当成已经从内存池删掉，或当成已经永远不提。
2. 看见往提案加了一笔新的 / 看见回包里有它，就当成已经进了内存池，或当成已经过了 CheckTx。
3. 看见把 t1 改成 t2 / 看见 t1 没进块，就当成已经还能按 t1 查到，或当成已经有人知道 t2 来自 t1。

## 为什么会出事

官方写：不写进 `PrepareProposalResponse.txs` 不会把它从内存池删掉，只是推迟。往回包加一笔新的，引擎不会把它加进内存池。拿掉再加可能丢掉可追踪性；除非应用自己记，没有组件知道 t2 来自 t1。

## 和相邻反模式

- [drop-notmempool-sold-as-bundled](drop-notmempool-sold-as-bundled.md) 是从提案拿掉 tx not already out-of-pool / not already never-propose / not already settled 正式三事（355 item 1），不是本页 bundled 全段 alone。
- [add-notmempool-sold-as-bundled](add-notmempool-sold-as-bundled.md) 是往提案加了一笔新的 not already in-pool / not already checktx / not already settled 正式三事（355 item 2），不是本页 bundled 全段 alone。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了就已经从池里删掉，不是本页这种从提案拿掉 tx 不是已经从内存池删掉。
- [preparereturn-sold-as-trimmed](preparereturn-sold-as-trimmed.md) 是整池可见就已经只能看见装得进一块的子集，不是本页这种往提案加了一笔新的不是已经进了内存池。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种把 t1 改成 t2 不是已经还能按 t1 查到。
