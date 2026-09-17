# 模式：把 CheckTx 回包 codespace not already response code / not already not-in-block / not already settled 正式三事（381 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[CheckTx ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notcode-vs-bundled.md)。

## 三个名字

1. **codespace 不是已经是回包码：** 看见写了空间，不是已经 373 interchangeable / 785 checktxspace-notcode interchangeable。
2. **看见写了空间 不是已经没进块：** 看见有命名空间，不是已经没进块 interchangeable。
3. **看见能回 不是已经交差：** 看见 CheckTx codespace，不是已经交差 interchangeable。

官方把 CheckTx 回包 codespace / events / lane_id 三条核心句拆成三个名字。把它们叫成一个「看见 CheckTx 回了码空间就已经是回包码」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 codespace 正式三事（381 余量），先数清问的是是不是已经是回包码 / 373、是不是已经没进块、还是看见能回是不是已经交差，再决定要不要同一次发布。381 checktxspace vs code bundled unbundling 在本页 item 1 启动。
