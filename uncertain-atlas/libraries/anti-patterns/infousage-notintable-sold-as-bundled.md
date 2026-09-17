# 反模式：把 Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量）说成已经 Info 车道 bundled / 已经 empty iff / 已经 CheckTx lane_id in range

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled ≠ bundled（498）](../../tracks/implementation/worked-example-infousage-notintable-vs-bundled.md)。

## 错在哪里

把 `default_lane` has to be one of the identifiers defined in `lane_priorities` 写成已经 Info 车道 bundled（367）第二件事 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第二件事 interchangeable / 497 infousage-persist interchangeable / 498 infousage-defaultlane interchangeable；把 default_lane 必须在表里 写成已经 lane_priorities empty iff default_lane empty interchangeable / 497 infousage-persist item 3 empty iff interchangeable / 367 infolane bundled interchangeable / 494 infousage item 1 app_version interchangeable；把 default_lane 必须是 lane_priorities 里定义过的一个标识 写成已经 CheckTx Usage lane_id in ResponseInfo range interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable / 317 priority consensus interchangeable / 664 infousage-notpriorityzero interchangeable，或已经和 498 infousage-defaultlane bundled / infousage-defaultlane-sold-as-priorityzero interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage default_lane has to be one of identifiers defined in lane_priorities not Info 车道 bundled / not empty iff / not CheckTx lane_id in range 正式三事（498 余量），必须分开 not Info 车道 bundled、not empty iff、not CheckTx lane_id in range 三件事，不要和 498 / 367 / 497 / 482 / 381 / 389 / 317 / 664 糊成一句。

## 和相邻反模式

- [infousage-defaultlane-sold-as-priorityzero](infousage-defaultlane-sold-as-priorityzero.md) 是 498 bundled 专用 default_lane/priority0，不是本页 498 item 1 default in table 单句边界。
- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 497 专用 last_block persist / empty iff，不是本页 not empty iff 单句边界。
- [chktxlane-sold-as-default](chktxlane-sold-as-default.md) 是 482 专用 CheckTx lane_id empty → default lane，不是本页 not CheckTx lane_id in range 单句边界。
