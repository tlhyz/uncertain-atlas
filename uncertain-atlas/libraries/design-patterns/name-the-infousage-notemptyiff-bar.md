# 模式：把 Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled ≠ bundled（497）](../../tracks/implementation/worked-example-infousage-notemptyiff-vs-bundled.md)。

## 三个名字

1. **lane_priorities empty iff default_lane empty 不是 Info 车道 bundled：** 看见 `lane_priorities` is empty if and only if `default_lane` is empty，不是已经 Info 车道 bundled（367）第二件事 interchangeable，不是 367 infolane bundled interchangeable / 497 infousage-persist interchangeable / 666 infousage-notlaneoptional interchangeable / 665 infousage-notcommitpersist interchangeable。

2. **empty if and only if 不是 default_lane in table：** 看见 lane_priorities 空当且仅当 default_lane 空，不是已经 default_lane has to be one of identifiers defined in lane_priorities interchangeable，不是 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable / 389 info-lane-fields interchangeable / 664 infousage-notpriorityzero interchangeable。

3. **空对空 不是 CheckTx lane_id in range：** 看见 empty iff 规则，不是已经 CheckTx Usage lane_id in ResponseInfo range interchangeable，不是 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 317 priority consensus interchangeable / 663 infousage-notintable interchangeable。

官方把 Info Usage empty iff 单句、Info 车道 bundled（367）、default_lane in table（663/498）、CheckTx Usage lane_id in range（482）写成三个名字。把它们叫成一个「看见 lane_priorities empty iff default_lane empty 就已经 Info 车道 bundled interchangeable / 就已经 default in table interchangeable / 就已经 CheckTx lane_id in range interchangeable」，会把 not Info 车道 bundled、not default_lane in table、not CheckTx lane_id in range 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量），先数清问的是 empty iff 是不是 Info 车道 bundled / 367 / 666 / 665，是不是 empty if and only if 是不是 default in table / 663 / 498 / 389，还是空对空 是不是 CheckTx lane_id in range / 482 / 381 / 664，再决定要不要同一次发布。497 infousage persist/lane unbundling 在本页 item 3 完成。
