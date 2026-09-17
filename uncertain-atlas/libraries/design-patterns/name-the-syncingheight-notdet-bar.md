# 模式：把 Finalize 回包 events not already must be deterministic / not already settled / not already same order as results 正式三事（382 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[Finalize ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notdet-vs-bundled.md)。

## 三个名字

1. **events 不是已经必须确定：** 看见回了事件，不是已经 342 interchangeable / 784 syncingheight-notdet interchangeable。
2. **看见回了事件 不是已经交差：** 看见标成非确定，不是已经交差 interchangeable。
3. **看见能按类型键值索引 不是已经是结果列表同一顺序：** 看见 Finalize events，不是已经是结果列表同一顺序 interchangeable。

官方把 syncing_to_height / validator_updates 空 / Finalize events 三条核心句拆成三个名字。把它们叫成一个「看见填了同步高度就已经有完整历史」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 events 正式三事（382 余量），先数清问的是是不是已经必须确定 / 342、是不是已经交差、还是看见能按类型键值索引是不是已经是结果列表同一顺序，再决定要不要同一次发布。382 syncingheight vs history bundled unbundling 在本页 item 3 完成。
