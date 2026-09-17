# 反模式：把 Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量）说成已经 Info 车道 bundled / 已经 default in table / 已经 CheckTx lane_id in range

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled ≠ bundled（497）](../../tracks/implementation/worked-example-infousage-notemptyiff-vs-bundled.md)。

## 卖法

把 `lane_priorities` is empty if and only if `default_lane` is empty 写成已经 Info 车道 bundled（367）第二件事 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第二件事 interchangeable / 497 infousage-persist interchangeable / 666 infousage-notlaneoptional interchangeable / 665 infousage-notcommitpersist interchangeable；把 empty if and only if / lane_priorities 空当且仅当 default_lane 空 写成已经 default_lane has to be one of identifiers defined in lane_priorities interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable / 389 info-lane-fields interchangeable / 664 infousage-notpriorityzero interchangeable / 已经 default in table interchangeable / 已经选型 interchangeable；把空对空 写成已经 CheckTx Usage lane_id in ResponseInfo range interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 317 priority consensus interchangeable / 已经 priority 0 不设道 interchangeable，或已经和 497 infousage-persist bundled / infousage-persist-sold-as-committed interchangeable / 667 infousage-notemptyiff interchangeable。

## 为什么错

官方把 Info Usage empty iff 单句、Info 车道 bundled（367）、default_lane in table（663/498）、CheckTx Usage lane_id in range（482）写成三件独立的实现事。把它们卖成 Info 车道 bundled interchangeable / default in table interchangeable / CheckTx lane_id in range interchangeable，会把 not Info 车道 bundled、not default_lane in table、not CheckTx lane_id in range 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage lane_priorities empty iff default_lane empty not Info 车道 bundled / not default_lane in table / not CheckTx lane_id in range 正式三事（497 余量），必须分开 not Info 车道 bundled、not default_lane in table、not CheckTx lane_id in range 三件事，不要和 497 / 367 / 663 / 498 / 482 / 381 / 666 / 665 / 664 糊成一句。

## 和相邻反模式

- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 497 bundled 专用 last_block/lane 三事，不是本页 497 item 3 empty iff 单句边界。
- [infousage-notlaneoptional-sold-as-bundled](infousage-notlaneoptional-sold-as-bundled.md) 是 497 item 2 optional lane_priorities 单句边界，不是本页 item 3 empty iff 单句边界。
