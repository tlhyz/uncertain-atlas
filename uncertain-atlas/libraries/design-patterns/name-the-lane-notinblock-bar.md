# 模式：把优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[写了 0 not already in-block ≠ bundled（367）](../../tracks/implementation/worked-example-lane-notinblock-vs-bundled.md)。

## 三个名字

1. **写了 0 不是 already in-block：** 看见写了 0 / 最低优先级是 1、0 留给应用不设道 / 预留 0，不是已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable，不是 367 lane bundled interchangeable / lane-sold-as-priority interchangeable。

2. **空 lane_id 不是 already removed：** 看见空 `lane_id` / 对应 `ResponseCheckTx` 里空的 `lane_id` / 不设道空 id，不是已经从池里删掉 interchangeable / 已经 removed interchangeable / 已经从池里删掉交差 interchangeable，不是 301 proposed interchangeable / 848 lane-notpriority interchangeable。

3. **有优先级 不是 already consensus-order：** 看见有优先级 / 最低是 1、有道就有优先级 / 写了优先级，不是已经是共识顺序 interchangeable / 已经 consensus-order interchangeable / 已经是共识顺序交差 interchangeable，不是 849 lane-notalgo interchangeable / 317 checktx-priority interchangeable。

官方把写了 0、不是已经从池里删掉、不是已经是共识顺序写成三个名字。把它们叫成一个「看见写了 0 就已经进了块 interchangeable / 就已经从池里删掉 interchangeable / 就已经是共识顺序 interchangeable」，会把 not already in-block、not already removed、not already consensus-order 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量），先数清问的是写了 0 是不是 already in-block / 367 / lane-sold-as-priority，是不是空 lane_id 是不是 already removed，还是有优先级 是不是 already consensus-order，再决定要不要同一次发布。367 lane-vs-priority bundled unbundling 在本页 item 3 完成。
