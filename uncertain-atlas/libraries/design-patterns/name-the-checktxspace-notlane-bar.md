# 模式：把 CheckTx lane_id not already no-lane / not already prioritized / not already in-block 正式三事（381 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[CheckTx ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notlane-vs-bundled.md)。

## 三个名字

1. **lane_id 不是已经不设道：** 看见填了道，不是已经 367 interchangeable / 787 checktxspace-notlane interchangeable。
2. **看见填了道 不是已经排了优先：** 看见在范围内，不是已经 367 interchangeable。
3. **看见能指道 不是已经进了块：** 看见 CheckTx lane_id，不是已经进了块 interchangeable。

官方把 CheckTx 回包 codespace / events / lane_id 三条核心句拆成三个名字。把它们叫成一个「看见 CheckTx 回了码空间就已经是回包码」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx lane_id 正式三事（381 余量），先数清问的是是不是已经不设道 / 367、是不是已经排了优先、还是看见能指道是不是已经进了块，再决定要不要同一次发布。381 checktxspace vs code bundled unbundling 在本页 item 3 完成。
