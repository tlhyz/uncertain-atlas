# 模式：把 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事（377 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[写了 /store not already engine ≠ bundled（377）](../../tracks/implementation/worked-example-querypath-notengine-vs-bundled.md)。

## 三个名字

1. **写了 /store 不是 already engine：** 看见写了 /store / path 按 URI 路径解释、/store 必须按键查 / 写了 /store 路径，不是已经是引擎在用 interchangeable / 已经 engine interchangeable / 已经是引擎在用交差 interchangeable，不是 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable。

2. **能带路径 不是 already filter：** 看见能带路径 / path 能带路径 / 带了路径，不是已经是过滤 interchangeable / 已经 filter interchangeable / 已经是过滤交差 interchangeable，不是 326 peerfilter interchangeable / 878 querypath-notheight interchangeable。

3. **键在 data 不是 already settled：** 看见键在 data / 键应当写在 data 里 / 键写在 data，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 329 query replicated interchangeable / 377 querypath item 3 interchangeable。

官方把写了 /store、不是已经是过滤、不是已经交差写成三个名字。把它们叫成一个「看见写了 /store 就已经是引擎在用 interchangeable / 就已经是过滤 interchangeable / 就已经交差 interchangeable」，会把 not already engine、not already filter、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用 not already engine / not already filter / not already settled 正式三事（377 余量），先数清问的是写了 /store 是不是 already engine / 377 / querypath-sold-as-store，是不是能带路径 是不是 already filter，还是键在 data 是不是 already settled，再决定要不要同一次发布。377 querypath-vs-store bundled unbundling 在本页 item 2 续。
