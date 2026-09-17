# 模式：把 Info Usage does not have to define lane_priorities not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（497 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage does not have to define lane_priorities not Info 车道 bundled ≠ bundled（497）](../../tracks/implementation/worked-example-infousage-notlaneoptional-vs-bundled.md)。

## 三个名字

1. **does not have to define lane_priorities 不是 Info 车道 bundled：** 看见 The application does not have to define lane_priorities，不是已经 Info 车道 bundled（367）第一件事 interchangeable，不是 367 infolane bundled interchangeable / 497 infousage-persist interchangeable / 665 infousage-notcommitpersist interchangeable。

2. **assign all transactions to one lane 不是 CheckTx empty lane_id default lane：** 看见 In that case, CometBFT will assign all transactions to one lane，不是已经 CheckTx Usage empty lane_id → assigned to default lane interchangeable，不是 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable / 664 infousage-notpriorityzero interchangeable。

3. **optional lane_priorities 不是 CheckTx Priority consensus order：** 看见 does not have to define lane_priorities / assign all transactions to one lane，不是已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable，不是 317 priority consensus interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable。

官方把 Info Usage optional lane_priorities 单句、Info 车道 bundled（367）、CheckTx Usage empty lane_id → default lane（482）、CheckTx Priority 共识顺序（317）写成三个名字。把它们叫成一个「看见 does not have to define lane_priorities 就已经 Info 车道 bundled interchangeable / 就已经 CheckTx empty lane_id default lane interchangeable / 就已经 Priority 共识顺序 interchangeable」，会把 not Info 车道 bundled、not CheckTx empty lane_id default lane、not CheckTx Priority consensus order 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage does not have to define lane_priorities not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（497 余量），先数清问的是 does not have to define 是不是 Info 车道 bundled / 367 / 665 / 667，是不是 assign all transactions to one lane 是不是 CheckTx empty lane_id default lane / 482 / 381 / 389，还是 optional lane_priorities 是不是 CheckTx Priority consensus order / 317 / 663 / 498，再决定要不要同一次发布。497 infousage persist/lane unbundling 在本页 item 2 续。
