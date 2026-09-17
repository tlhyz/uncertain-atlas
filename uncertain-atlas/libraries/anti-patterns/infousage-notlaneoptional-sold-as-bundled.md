# 反模式：把 Info Usage does not have to define lane_priorities not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（497 余量）说成已经 Info 车道 bundled / 已经 CheckTx empty lane_id default lane / 已经 Priority 共识顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage does not have to define lane_priorities not Info 车道 bundled ≠ bundled（497）](../../tracks/implementation/worked-example-infousage-notlaneoptional-vs-bundled.md)。

## 卖法

把 The application does not have to define `lane_priorities` 写成已经 Info 车道 bundled（367）第一件事 interchangeable / 367 infolane bundled interchangeable / 已经 Info 车道 bundled 第一件事 interchangeable / 497 infousage-persist interchangeable / 665 infousage-notcommitpersist interchangeable；把 In that case, CometBFT will assign all transactions to one lane 写成已经 CheckTx Usage empty lane_id → assigned to default lane interchangeable / 482 chktxlane interchangeable / 381 chktxlane-range interchangeable / 389 info-lane-fields interchangeable / 664 infousage-notpriorityzero interchangeable / 已经 assigned to the default lane interchangeable；把 optional lane_priorities / assign all transactions to one lane 写成已经 CheckTx 的 Priority 就已经是共识顺序 interchangeable / 317 priority consensus interchangeable / 663 infousage-notintable interchangeable / 498 infousage-defaultlane interchangeable / 已经排了优先 interchangeable / 已经进了块 interchangeable，或已经和 497 infousage-persist bundled / infousage-persist-sold-as-committed interchangeable / 666 infousage-notlaneoptional interchangeable。

## 为什么错

官方把 Info Usage optional lane_priorities 单句、Info 车道 bundled（367）、CheckTx Usage empty lane_id → default lane（482）、CheckTx Priority 共识顺序（317）写成三件独立的实现事。把它们卖成 Info 车道 bundled interchangeable / CheckTx empty lane_id default lane interchangeable / Priority 共识顺序 interchangeable，会把 not Info 车道 bundled、not CheckTx empty lane_id default lane、not CheckTx Priority consensus order 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage does not have to define lane_priorities not Info 车道 bundled / not CheckTx empty lane_id default lane / not CheckTx Priority consensus order 正式三事（497 余量），必须分开 not Info 车道 bundled、not CheckTx empty lane_id default lane、not CheckTx Priority consensus order 三件事，不要和 497 / 367 / 482 / 381 / 389 / 317 / 665 / 667 / 663 / 664 / 498 糊成一句。

## 和相邻反模式

- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 497 bundled 专用 last_block/lane 三事，不是本页 497 item 2 optional lane_priorities 单句边界。
- [infousage-notcommitpersist-sold-as-bundled](infousage-notcommitpersist-sold-as-bundled.md) 是 497 item 1 last_block persist 单句边界，不是本页 item 2 optional lane_priorities 单句边界。
