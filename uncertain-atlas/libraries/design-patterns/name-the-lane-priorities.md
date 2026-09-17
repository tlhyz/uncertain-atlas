# 模式：把 Info 车道三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[没定义 lane_priorities ≠ 已经排了优先](../../tracks/implementation/worked-example-lane-vs-priority.md)。

## 三个名字

1. **没定义 lane_priorities 不是已经排了优先：** 看见并成一条道不是已经是 CheckTx 的 Priority。
2. **空表对空默认不是已经选型：** 看见默认道在表里不是已经排了优先。
3. **优先级 0 留给不设道不是已经进了块：** 看见空 lane_id 不是已经从池里删掉。

## 为什么要分开叫

官方把应用可以不定义车道、空表必须对空默认、优先级 0 留给不设道写成三件事。把它们叫成一个「看见 Info 回了车道就已经排了优先」，会把 CheckTx 优先、CheckTxState 和内存池交接一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Info 回了车道就已经排了优先」，先数清问的是没定义 lane_priorities 不是已经排了优先、空表对空默认不是已经选型，还是优先级 0 留给不设道不是已经进了块，再决定要不要同一次发布。
