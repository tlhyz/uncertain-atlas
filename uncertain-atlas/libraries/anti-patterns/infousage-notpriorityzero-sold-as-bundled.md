# 反模式：把 Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量）说成已经 Info 车道 bundled / 已经 CheckTx empty lane_id default lane / 已经 Priority 共识顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled ≠ bundled（498）](../../tracks/implementation/worked-example-infousage-notpriorityzero-vs-bundled.md)。

## 卖法

把 The lowest priority a lane can have is `1` / The value `0` is reserved for when applications do not assign lanes (empty `lane_id` in `ResponseCheckTx`) 写成已经 Info 车道 bundled（367）第三件事 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第三件事 interchangeable / 497 infousage-persist interchangeable / 498 infousage-defaultlane interchangeable / 663 infousage-notintable interchangeable；把 0 reserved for empty lane_id in ResponseCheckTx 写成已经 CheckTx Usage empty lane_id → assigned to default lane interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable / 已经 assigned to the default lane interchangeable；把 lowest priority is 1 / priority 0 reserved 写成已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable / 317 priority consensus interchangeable / 494 infousage item 1 app_version interchangeable / 已经排了优先 interchangeable / 已经进了块 interchangeable，或已经和 498 infousage-defaultlane bundled / infousage-defaultlane-sold-as-priorityzero interchangeable / 664 infousage-notpriorityzero interchangeable。

## 为什么错

官方把 Info Usage priority 0 预留单句、Info 车道 bundled（367）、CheckTx Usage empty lane_id → default lane（482）、CheckTx Priority 共识顺序（317）写成三件独立的实现事。把它们卖成 Info 车道 bundled interchangeable / CheckTx empty lane_id default lane interchangeable / Priority 共识顺序 interchangeable，会把 not Info 车道 bundled、not CheckTx empty lane_id default lane、not CheckTx Priority consensus order 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage priority 0 reserved for empty lane_id not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（498 余量），必须分开 not Info 车道 bundled、not CheckTx empty lane_id default lane、not CheckTx Priority consensus order 三件事，不要和 498 / 367 / 482 / 381 / 389 / 317 / 663 / 497 糊成一句。

## 和相邻反模式

- [infousage-defaultlane-sold-as-priorityzero](infousage-defaultlane-sold-as-priorityzero.md) 是 498 bundled 专用 default_lane/priority0，不是本页 498 item 2 priority 0 单句边界。
- [infousage-notintable-sold-as-bundled](infousage-notintable-sold-as-bundled.md) 是 498 item 1 default in table 单句边界，不是本页 item 2 priority 0 单句边界。
