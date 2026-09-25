# 模式：把这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[填了高度 not already apphash ≠ bundled（371）](../../tracks/implementation/worked-example-queryheight-notapphash-vs-bundled.md)。

## 三个名字

1. **填了高度 不是 already apphash：** 看见填了高度 / 这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态 / 填了 height，不是已经印进本头 AppHash interchangeable / 已经 apphash interchangeable / 已经印进本头 AppHash 交差 interchangeable，不是 371 queryheight bundled interchangeable / queryheight-sold-as-committed interchangeable。

2. **有根 不是 already proof：** 看见有根 / 有应用 Merkle 根 / 根在，不是已经对上 Proof interchangeable / 已经 proof interchangeable / 已经对上 Proof 交差 interchangeable，不是 325 queryproof interchangeable / 860 queryheight-notquerystate interchangeable。

3. **Height-1 不是 already settled：** 看见 Height-1 / 代表 Height-1 提交之后的状态 / Height-1 状态，不是已经是本高度交差 interchangeable / 已经 settled interchangeable / 已经是本高度交差交差 interchangeable，不是 861 queryheight-notfresh interchangeable / 147 apphash interchangeable。

官方把填了高度、不是已经对上 Proof、不是已经是本高度交差写成三个名字。把它们叫成一个「看见填了高度就已经印进本头 AppHash interchangeable / 就已经对上 Proof interchangeable / 就已经是本高度交差 interchangeable」，会把 not already apphash、not already proof、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash not already apphash / not already proof / not already settled 正式三事（371 余量），先数清问的是填了高度 是不是 already apphash / 371 / queryheight-sold-as-committed，是不是有根 是不是 already proof，还是 Height-1 是不是 already settled，再决定要不要同一次发布。371 queryheight-vs-committed bundled unbundling 在本页 item 3 完成。
