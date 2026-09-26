# 模式：把 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[有下标 not already store ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notstore-vs-bundled.md)。

## 三个名字

1. **有下标 不是 already store：** 看见有下标 / Query 回包 index 是树里这个键的下标 / 有 index 下标，不是已经是按键查 interchangeable / 已经 store interchangeable / 已经是按键查交差 interchangeable，不是 380 queryindex bundled interchangeable / queryindex-sold-as-store interchangeable。

2. **填了下标 不是 already matched：** 看见填了下标 / 填了 index / 下标有值，不是已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable，不是 325 queryprove interchangeable / 377 querypath interchangeable。

3. **有数 不是 already settled：** 看见有数 / 有下标数字 / index 是数，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 371 queryheight interchangeable / 380 queryindex item 2 interchangeable。

官方把有下标、不是已经对上 AppHash、不是已经交差写成三个名字。把它们叫成一个「看见有下标就已经是按键查 interchangeable / 就已经对上 AppHash interchangeable / 就已经交差 interchangeable」，会把 not already store、not already matched、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 index 是树里这个键的下标不是已经是按键查 not already store / not already matched / not already settled 正式三事（380 余量），先数清问的是有下标 是不是 already store / 380 / queryindex-sold-as-store，是不是填了下标 是不是 already matched，还是有数 是不是 already settled，再决定要不要同一次发布。380 queryindex-vs-store bundled unbundling 在本页 item 1 启动。
