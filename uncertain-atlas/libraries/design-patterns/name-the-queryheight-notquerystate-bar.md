# 模式：把 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[能查 not already querystate ≠ bundled（371）](../../tracks/implementation/worked-example-queryheight-notquerystate-vs-bundled.md)。

## 三个名字

1. **能查 不是 already querystate：** 看见能查 / Query 可以对当前或过去高度查 / 能查高度，不是已经是 QueryState interchangeable / 已经 querystate interchangeable / 已经是 QueryState 交差 interchangeable，不是 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable。

2. **填了高度 不是 already replicated：** 看见填了高度 / 填了当前或过去高度 / 有高度参数，不是已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制到各节点交差 interchangeable，不是 329 query-replicated interchangeable / 861 queryheight-notfresh interchangeable。

3. **能回 不是 already settled：** 看见能回 / 能回 Query / 回得了，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 862 queryheight-notapphash interchangeable / 33 fourgates interchangeable。

官方把能查、不是已经复制到各节点、不是已经交差写成三个名字。把它们叫成一个「看见能查就已经是 QueryState interchangeable / 就已经复制到各节点 interchangeable / 就已经交差 interchangeable」，会把 not already querystate、not already replicated、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 可以对当前或过去高度查不是已经是 QueryState not already querystate / not already replicated / not already settled 正式三事（371 余量），先数清问的是能查 是不是 already querystate / 371 / queryheight-sold-as-committed，是不是填了高度 是不是 already replicated，还是能回 是不是 already settled，再决定要不要同一次发布。371 queryheight-vs-committed bundled unbundling 在本页 item 1 启动。
