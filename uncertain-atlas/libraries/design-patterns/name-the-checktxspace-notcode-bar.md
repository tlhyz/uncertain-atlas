# 模式：把 CheckTx 回包 codespace 是码的命名空间不是已经是回包码 not already code / not already excluded / not already settled 正式三事（381 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[写了空间 not already code ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notcode-vs-bundled.md)。

## 三个名字

1. **写了空间 不是 already code：** 看见写了空间 / CheckTx 回包 codespace 是码的命名空间 / 写了 codespace，不是已经是回包码 interchangeable / 已经 code interchangeable / 已经是回包码交差 interchangeable，不是 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable。

2. **有命名空间 不是 already excluded：** 看见有命名空间 / 有 codespace 命名空间 / 有空间名，不是已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable，不是 373 checktxopt interchangeable / 316 txresults interchangeable。

3. **能回 不是 already settled：** 看见能回 / 能回 codespace / 有 codespace 回包，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 381 checktxspace item 2 interchangeable / 367 lane-priority interchangeable。

官方把写了空间、不是已经没进块、不是已经交差写成三个名字。把它们叫成一个「看见写了空间就已经是回包码 interchangeable / 就已经没进块 interchangeable / 就已经交差 interchangeable」，会把 not already code、not already excluded、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 codespace 是码的命名空间不是已经是回包码 not already code / not already excluded / not already settled 正式三事（381 余量），先数清问的是写了空间 是不是 already code / 381 / checktxspace-sold-as-code，是不是有命名空间 是不是 already excluded，还是能回 是不是 already settled，再决定要不要同一次发布。381 checktxspace-vs-code bundled unbundling 在本页 item 1 启动。
