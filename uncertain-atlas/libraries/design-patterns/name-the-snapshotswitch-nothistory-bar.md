# 模式：把切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**例**：[能出块 not already full-history ≠ bundled（323）](../../tracks/implementation/worked-example-snapshotswitch-nothistory-vs-bundled.md)。

## 三个名字

1. **能出块 不是 already full-history：** 看见切进共识 / 能给新高度，不是已经有从创世的完整历史 interchangeable / 已经能给任意旧高度 interchangeable，不是 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable。

2. **和其他节点一样跑 不是 already genesis-replay：** 看见切过去之后一样跑 / 能出块之后，不是已经从创世重放 interchangeable / 已经从创世重放交差 interchangeable，不是 323 snapshotswitch item 2 interchangeable / 726 snapshotswitch-notversion interchangeable。

3. **透明 不是 already no-extension-care：** 看见对应用透明 / 操作透明，不是已经不用管扩展高度 interchangeable / 已经扩展高度交差 interchangeable，不是 323 snapshotswitch item 1 interchangeable / 725 snapshotswitch-notchainid interchangeable。

官方把能出块单句、already full-history、already genesis-replay、already no-extension-care 写成三个名字。把它们叫成一个「看见切进共识就已经有完整历史 interchangeable / 就已经从创世重放 interchangeable / 就已经不用管扩展高度 interchangeable」，会把 not already full-history、not already genesis-replay、not already no-extension-care 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看切进共识不是已经有完整历史 not already full-history / not already genesis-replay / not already no-extension-care 正式三事（323 余量），先数清问的是能出块 是不是 already full-history / 323 / snapshotswitch-sold-as-full-history，是不是和其他节点一样跑 是不是 already genesis-replay，还是透明 是不是 already no-extension-care，再决定要不要同一次发布。323 snapshotswitch vs history bundled unbundling 在本页 item 3 完成。
