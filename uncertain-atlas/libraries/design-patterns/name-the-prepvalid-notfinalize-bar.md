# 模式：把 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[Prepare 里产出了事件 not already handed-over ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notfinalize-vs-bundled.md)。

## 三个名字

1. **先跑了 不是 already handed-over：** 看见先跑了 / Prepare 里产出了块事件或交易事件 / 应用 MAY 产出事件，不是已经交出去 interchangeable / 已经 handed-over interchangeable / 已经交给引擎交差 interchangeable，不是 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable。

2. **有事件 不是 already results-hash：** 看见有事件 / 产出了块事件或交易事件 / 先产出了，不是已经印进 LastResultsHash interchangeable / 已经 results-hash interchangeable / 已经印进 LastResultsHash 交差 interchangeable，不是 316 exectxresult interchangeable / 824 prepvalid-notdedup interchangeable。

3. **留着 不是 already settled：** 看见留着 / 必须留到块决定之后 / 还没经 Finalize 交回，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 825 prepvalid-notreject interchangeable / 33 fourgates interchangeable。

官方把先跑了、不是已经印进 LastResultsHash、不是已经交差写成三个名字。把它们叫成一个「看见先跑了就已经交出去 interchangeable / 就已经印进 LastResultsHash interchangeable / 就已经交差 interchangeable」，会把 not already handed-over、not already results-hash、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量），先数清问的是先跑了 是不是 already handed-over / 357 / preparevalid-sold-as-checked，是不是有事件 是不是 already results-hash，还是留着 是不是 already settled，再决定要不要同一次发布。357 prepare-valid vs checked bundled unbundling 在本页 item 3 完成。
