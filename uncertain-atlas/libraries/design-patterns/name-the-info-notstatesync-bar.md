# 模式：把 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[能回 not already statesync ≠ bundled（370）](../../tracks/implementation/worked-example-info-notstatesync-vs-bundled.md)。

## 三个名字

1. **能回 不是 already statesync：** 看见能回 / Info 用来在启动或恢复时让引擎和应用握手对齐 / 能回 Info，不是已经是快照重放 interchangeable / 已经 statesync interchangeable / 已经是快照重放交差 interchangeable，不是 370 info bundled interchangeable / info-sold-as-handshake interchangeable。

2. **握手了 不是 already querystate：** 看见握手了 / 启动或恢复时用这次握手和应用对齐 / 握过手，不是已经是 QueryState interchangeable / 已经 querystate interchangeable / 已经是 QueryState 交差 interchangeable，不是 314 querystate interchangeable / 858 info-notapphash interchangeable。

3. **对齐了 不是 already settled：** 看见对齐了 / 和应用对齐 / 对齐过，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 859 info-notpersist interchangeable / 33 fourgates interchangeable。

官方把能回、不是已经是 QueryState、不是已经交差写成三个名字。把它们叫成一个「看见能回就已经是快照重放 interchangeable / 就已经是 QueryState interchangeable / 就已经交差 interchangeable」，会把 not already statesync、not already querystate、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量），先数清问的是能回 是不是 already statesync / 370 / info-sold-as-handshake，是不是握手了 是不是 already querystate，还是对齐了 是不是 already settled，再决定要不要同一次发布。370 info-vs-handshake bundled unbundling 在本页 item 1 启动。
