# 反模式：把 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量）说成已经交出去 / 已经印进 LastResultsHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Prepare 里产出了事件 not already handed-over ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notfinalize-vs-bundled.md)。

## 卖法

把先跑了 / Prepare 里产出了块事件或交易事件 / 应用 MAY 产出事件 写成已经交出去 interchangeable / 已经 handed-over interchangeable / 已经交给引擎交差 interchangeable / 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable；把有事件 / 产出了块事件或交易事件 写成已经印进 LastResultsHash interchangeable / 已经 results-hash interchangeable / 已经印进 LastResultsHash 交差 interchangeable；把留着 / 必须留到块决定之后 / 还没经 Finalize 交回 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 357 preparevalid bundled / preparevalid-sold-as-checked interchangeable / 826 prepvalid-notfinalize interchangeable。

## 为什么错

官方把先跑了、不是已经印进 LastResultsHash、不是已经交差写成三件独立的实现事。把它们卖成 already handed-over interchangeable / already results-hash interchangeable / already settled interchangeable，会把 not already handed-over、not already results-hash、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 里产出了事件不是已经交给引擎 not already handed-over / not already results-hash / not already settled 正式三事（357 余量），必须分开 not already handed-over、not already results-hash、not already settled 三件事，不要和 357 / 316 / 313 / 824 / 825 糊成一句。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled 全段，不是本页先跑了 item 3 单句边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code / Data 就已经印进本头（316），不是本页 not already handed-over 边界。
- [prepvalid-notreject-sold-as-bundled](prepvalid-notreject-sold-as-bundled.md) 是 Prepare 回包验不过引擎崩溃 not already process-reject（357 item 2），不是本页 not already settled 边界。
