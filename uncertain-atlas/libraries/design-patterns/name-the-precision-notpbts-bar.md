# 模式：把填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**例**：[填了两个 not already pbts-enabled ≠ bundled（336）](../../tracks/implementation/worked-example-precision-notpbts-vs-bundled.md)。

## 三个名字

1. **填了两个 不是 already pbts-enabled：** 看见填了两个 / Precision 和 MessageDelay 都填了 / 两把尺都在，不是已经启用 PBTS interchangeable / 已经到了 PbtsEnableHeight 交差 interchangeable，不是 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable。

2. **写了用于 PBTS 不是 already switched：** 看见这两个参数用于 PBTS / 写了用于 PBTS / 参数写给 PBTS，不是已经切到 PBTS interchangeable / 已经切过去交差 interchangeable，不是 330 veheight interchangeable / 336 precision item 1 interchangeable。

3. **参数在 不是 already cannot-off：** 看见参数在 / 同步参数还在 / 两把尺还在表里，不是已经不能关 interchangeable / 已经永远开着交差 interchangeable，不是 330 veheight interchangeable / 336 precision item 3 interchangeable。

官方把填了两个单句、already pbts-enabled、already switched、already cannot-off 写成三个名字。把它们叫成一个「看见填了两个就已经启用 PBTS interchangeable / 就已经切到 PBTS interchangeable / 就已经不能关 interchangeable」，会把 not already pbts-enabled、not already switched、not already cannot-off 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了两个不是已经启用 PBTS not already pbts-enabled / not already switched / not already cannot-off 正式三事（336 余量），先数清问的是填了两个 是不是 already pbts-enabled / 336 / precision-sold-as-msgdelay，是不是写了用于 PBTS 是不是 already switched，还是参数在 是不是 already cannot-off，再决定要不要同一次发布。336 precision vs msgdelay bundled unbundling 在本页 item 2 续。
