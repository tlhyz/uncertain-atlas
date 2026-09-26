# 模式：把 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[填了道 not already unset ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notunset-vs-bundled.md)。

## 三个名字

1. **填了道 不是 already unset：** 看见填了道 / CheckTx 的 lane_id 必须在 Info 回包车道范围内 / 填了 lane_id，不是已经不设道 interchangeable / 已经 unset interchangeable / 已经不设道交差 interchangeable，不是 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable。

2. **在范围内 不是 already priority：** 看见在范围内 / 落在 Info 车道范围内 / 道在范围内，不是已经排了优先 interchangeable / 已经 priority interchangeable / 已经排了优先交差 interchangeable，不是 367 lane-priority interchangeable / 890 checktxspace-notcode interchangeable。

3. **能指道 不是 already included：** 看见能指道 / 能指 lane_id / 有车道指派，不是已经进了块 interchangeable / 已经 included interchangeable / 已经进了块交差 interchangeable，不是 891 checktxspace-notsettled interchangeable / 373 checktxopt interchangeable。

官方把填了道、不是已经排了优先、不是已经进了块写成三个名字。把它们叫成一个「看见填了道就已经不设道 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」，会把 not already unset、not already priority、not already included 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量），先数清问的是填了道 是不是 already unset / 381 / checktxspace-sold-as-code，是不是在范围内 是不是 already priority，还是能指道 是不是 already included，再决定要不要同一次发布。381 checktxspace-vs-code bundled unbundling 在本页 item 3 完成。
