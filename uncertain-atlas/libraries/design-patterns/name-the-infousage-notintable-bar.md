# 模式：把 Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled ≠ bundled（498）](../../tracks/implementation/worked-example-infousage-notintable-vs-bundled.md)。

## 三个名字

1. **default_lane has to be one of identifiers defined in lane_priorities 不是 Info 车道 bundled：** 看见 has to be one of the identifiers defined in lane_priorities，不是已经 Info 车道 bundled（367）第二件事 interchangeable，不是 367 infolane bundled interchangeable / 497 infousage-persist interchangeable / 498 infousage-defaultlane interchangeable。
2. **default_lane has to be one of identifiers defined in lane_priorities 不是 empty iff：** 看见 default_lane 必须在表里，不是已经 lane_priorities empty iff default_lane empty interchangeable，不是 497 infousage-persist interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 367 infolane bundled interchangeable。
3. **default_lane has to be one of identifiers defined in lane_priorities 不是 CheckTx lane_id in range：** 看见 default_lane 必须是 lane_priorities 里定义过的一个标识，不是已经 CheckTx Usage lane_id in ResponseInfo range interchangeable，不是 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable / 317 priority consensus interchangeable。

## 为什么要分开叫

官方把 Info Usage default in table 单句、Info 车道 bundled（367）、Info Usage part 2 empty iff（497）、CheckTx Usage lane_id in range（482）写成三个名字。把它们叫成一个「看见 default_lane in table 就已经 Info 车道 bundled interchangeable / 就已经 empty iff interchangeable / 就已经 CheckTx lane_id in range interchangeable」，会把 not Info 车道 bundled、not empty iff、not CheckTx lane_id in range 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量），先数清问的是 default_lane in table 是不是 Info 车道 bundled / 367 / 497，是不是 has to be one of identifiers 是不是 empty iff / 497 item 3，还是 default_lane 是不是 CheckTx lane_id in range / 482 / 381 / 389，再决定要不要同一次发布。498 infousage default_lane/priority0 unbundling 在本页 item 1 启动。
