# 模式：把 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[填了 data not already height ≠ bundled（377）](../../tracks/implementation/worked-example-querypath-notheight-vs-bundled.md)。

## 三个名字

1. **填了 data 不是 already height：** 看见填了 data / data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 / 填了 data 字段，不是已经是 Query 高度 interchangeable / 已经 height interchangeable / 已经是 Query 高度交差 interchangeable，不是 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable。

2. **能代替 path 不是 already fresh：** 看见能代替 path / data 可以代替 path / 代替 path，不是已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable，不是 371 queryheight interchangeable / 377 querypath item 2 interchangeable。

3. **有字节 不是 already settled：** 看见有字节 / data 有字节 / 填了字节，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 329 query replicated interchangeable / 377 querypath item 3 interchangeable。

官方把填了 data、不是已经新鲜、不是已经交差写成三个名字。把它们叫成一个「看见填了 data 就已经是 Query 高度 interchangeable / 就已经新鲜 interchangeable / 就已经交差 interchangeable」，会把 not already height、not already fresh、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量），先数清问的是填了 data 是不是 already height / 377 / querypath-sold-as-store，是不是能代替 path 是不是 already fresh，还是有字节 是不是 already settled，再决定要不要同一次发布。377 querypath-vs-store bundled unbundling 在本页 item 1 启动。
