# 模式：把 validator_updates 空 not already no set / not already changed set / not already InitChain empty list 正式三事（382 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[validator_updates ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notnoset-vs-bundled.md)。

## 三个名字

1. **空着 不是已经没有集合：** 看见空着，不是已经 318 interchangeable / 783 syncingheight-notnoset interchangeable。
2. **看见空着 不是已经改了集合：** 看见没回人，不是已经改了集合 interchangeable。
3. **看见能空 不是已经是 InitChain 那种空名单：** 看见 validator_updates 空，不是已经 318 interchangeable。

官方把 syncing_to_height / validator_updates 空 / Finalize events 三条核心句拆成三个名字。把它们叫成一个「看见填了同步高度就已经有完整历史」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 空 正式三事（382 余量），先数清问的是是不是已经没有集合 / 318、是不是已经改了集合、还是看见能空是不是已经是 InitChain 那种空名单，再决定要不要同一次发布。382 syncingheight vs history bundled unbundling 在本页 item 2 续。
