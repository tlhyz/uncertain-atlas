# 模式：把空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[空对空 not already algo ≠ bundled（367）](../../tracks/implementation/worked-example-lane-notalgo-vs-bundled.md)。

## 三个名字

1. **空对空 不是 already algo：** 看见空对空 / `lane_priorities` 空当且仅当 `default_lane` 空 / 空表对空默认，不是已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，不是 367 lane bundled interchangeable / lane-sold-as-priority interchangeable。

2. **默认道在表里 不是 already prioritized：** 看见默认道在表里 / `default_lane` 必须是 `lane_priorities` 里定义过的一个标识 / 默认道是表里标识，不是已经排了优先 interchangeable / 已经 prioritized interchangeable / 已经排了优先交差 interchangeable，不是 317 checktx-priority interchangeable / 848 lane-notpriority interchangeable。

3. **对上了 不是 already in-block：** 看见对上了 / 空对空且默认道在表里 / 约束对上，不是已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable，不是 850 lane-notinblock interchangeable / 301 proposed interchangeable。

官方把空对空、不是已经排了优先、不是已经进了块写成三个名字。把它们叫成一个「看见空对空就已经选型 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」，会把 not already algo、not already prioritized、not already in-block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量），先数清问的是空对空 是不是 already algo / 367 / lane-sold-as-priority，是不是默认道在表里 是不是 already prioritized，还是对上了 是不是 already in-block，再决定要不要同一次发布。367 lane-vs-priority bundled unbundling 在本页 item 2 续。
