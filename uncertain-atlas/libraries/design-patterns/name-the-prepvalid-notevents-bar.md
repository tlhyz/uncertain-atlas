# 模式：把 Prepare 回包校验 events not handed / not LastResultsHash / not Finalize events 正式三事（357 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[events ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notevents-vs-bundled.md)。

## 三个名字

1. **events 不是已经交给引擎：** 看见先跑了，不是已经交出去 interchangeable / 718 prepvalid-notevents interchangeable。
2. **看见有事件 不是已经印进 LastResultsHash：** 看见有事件，不是已经 316 interchangeable。
3. **看见先跑了 不是 Finalize events：** 看见 Prepare 先产出，不是已经 431 / 451 interchangeable。

官方把 Prepare 回包校验三条核心句拆成三个名字。把它们叫成一个「看见回了提案就已经验过重复」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 events 正式三事（357 余量），先数清问的是先产出是不是已经交给引擎、是不是已经印进 LastResultsHash / 316、还是看见先跑了是不是 431 / 451，再决定要不要同一次发布。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。
