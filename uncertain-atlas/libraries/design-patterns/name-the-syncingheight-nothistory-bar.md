# 模式：把 syncing_to_height not already full history / not already snapshot replay / not already settled 正式三事（382 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[syncing_to_height ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-nothistory-vs-bundled.md)。

## 三个名字

1. **syncing_to_height 不是已经有完整历史：** 看见填了目标，不是已经 323 interchangeable / 782 syncingheight-nothistory interchangeable。
2. **看见填了目标 不是已经是快照重放：** 看见在同步，不是已经是快照重放 interchangeable。
3. **看见等于本高 不是已经交差：** 看见 syncing_to_height，不是已经交差 interchangeable。

官方把 syncing_to_height / validator_updates 空 / Finalize events 三条核心句拆成三个名字。把它们叫成一个「看见填了同步高度就已经有完整历史」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 正式三事（382 余量），先数清问的是是不是已经有完整历史 / 323、是不是已经是快照重放、还是看见等于本高是不是已经交差，再决定要不要同一次发布。382 syncingheight vs history bundled unbundling 在本页 item 1 启动。
