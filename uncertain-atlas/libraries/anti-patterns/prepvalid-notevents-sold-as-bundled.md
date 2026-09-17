# 反模式：把 Prepare 回包校验 events not handed / not LastResultsHash / not Finalize events 正式三事（357 余量） 说成已经交给引擎 / 已经印进 LastResultsHash / 已经 Finalize events 交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[events ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notevents-vs-bundled.md)。

## 卖法

把 Prepare 回包校验这句写成已经已经交给引擎 / 已经印进 LastResultsHash / 已经 Finalize events 交差 interchangeable，或已经和 357 prepare-valid-vs-checked bundled / prepvalid-notevents-sold-as-bundled interchangeable。

## 为什么错

官方把 Prepare 回包校验三条核心句写成三件独立的实现事。把它们卖成已经交给引擎 / 已经印进 LastResultsHash / 已经 Finalize events 交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 events 正式三事（357 余量），必须分开 not handed、not LastResultsHash、not Finalize events 三件事，不要和 357 / 316 / 431 / 451 / 716 / 717 糊成一句。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled（357），不是本页 item 3 单句边界。
- [prepvalid-notcrash-sold-as-bundled](prepvalid-notcrash-sold-as-bundled.md) 是 crash 单句边界（717 item 2），不是本页 events 边界。
