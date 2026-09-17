# 模式：把 Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled ≠ bundled（498）](../../tracks/implementation/worked-example-infousage-notpriorityzero-vs-bundled.md)。

## 三个名字

1. **priority 0 reserved for empty lane_id 不是 Info 车道 bundled：** 看见 lowest priority is 1 / 0 reserved for empty lane_id in ResponseCheckTx，不是已经 Info 车道 bundled（367）第三件事 interchangeable，不是 367 infolane bundled interchangeable / 497 infousage-persist interchangeable / 498 infousage-defaultlane interchangeable / 663 infousage-notintable interchangeable。

2. **0 reserved for empty lane_id in ResponseCheckTx 不是 CheckTx empty lane_id default lane：** 看见 0 is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`)，不是已经 CheckTx Usage empty lane_id → assigned to default lane interchangeable，不是 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable。

3. **priority 0 reserved 不是 CheckTx Priority consensus order：** 看见 The lowest priority a lane can have is 1 / 0 reserved for empty lane_id，不是已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable，不是 317 priority consensus interchangeable / 494 infousage item 1 app_version interchangeable / 370 info-handshake interchangeable。

官方把 Info Usage priority 0 单句、Info 车道 bundled（367）、CheckTx Usage empty lane_id → default lane（482）、CheckTx Priority 共识顺序（317）写成三个名字。把它们叫成一个「看见 priority 0 reserved 就已经 Info 车道 bundled interchangeable / 就已经 CheckTx empty lane_id default lane interchangeable / 就已经 Priority 共识顺序 interchangeable」，会把 not Info 车道 bundled、not CheckTx empty lane_id default lane、not CheckTx Priority consensus order 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量），先数清问的是 priority 0 reserved 是不是 Info 车道 bundled / 367 / 497 / 663，是不是 0 reserved for empty lane_id 是不是 CheckTx empty lane_id default lane / 482 / 381 / 389，还是 priority 0 reserved 是不是 CheckTx Priority consensus order / 317 / 494，再决定要不要同一次发布。498 infousage default_lane/priority0 unbundling 在本页 item 2 完成。
