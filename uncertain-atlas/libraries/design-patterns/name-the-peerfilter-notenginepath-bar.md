# 模式：把有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**例**：[有 /store not already all-paths-used ≠ bundled（326）](../../tracks/implementation/worked-example-peerfilter-notenginepath-vs-bundled.md)。

## 三个名字

1. **规范写了三条路径 不是 already all-paths-used：** 看见规范写了三条路径 / 有 `/p2p`、`/store`、`/app` / 高层路径表，不是已经三条都在用 interchangeable / 已经引擎三条都开交差 interchangeable，不是 326 peerfilter bundled interchangeable / 33 four gates interchangeable / peerfilter-sold-as-connected interchangeable。

2. **有 /store 不是 already is-filter：** 看见有 /store / 有 `/app` / 路径名在表里，不是已经是过滤 interchangeable / 已经邻居过滤交差 interchangeable，不是 50 banlist interchangeable / 326 peerfilter item 1 interchangeable。

3. **能带数据 不是 already filter-has-data：** 看见能带数据 / Query 还可以另带数据 / 路径外还能带数据，不是已经两道过滤带了数据 interchangeable / 已经 addr/id 过滤带数据交差 interchangeable，不是 305 initpeer interchangeable / 326 peerfilter item 2 interchangeable。

官方把规范写了三条路径单句、already all-paths-used、already is-filter、already filter-has-data 写成三个名字。把它们叫成一个「看见有 /store 路径就已经是引擎在用 interchangeable / 就已经是过滤 interchangeable / 就已经过滤带了数据 interchangeable」，会把 not already all-paths-used、not already is-filter、not already filter-has-data 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看有 /store 路径不是已经是引擎在用 not already all-paths-used / not already is-filter / not already filter-has-data 正式三事（326 余量），先数清问的是规范写了三条路径 是不是 already all-paths-used / 326 / peerfilter-sold-as-connected，是不是有 /store 是不是 already is-filter，还是能带数据 是不是 already filter-has-data，再决定要不要同一次发布。326 peerfilter vs query bundled unbundling 在本页 item 3 完成。
