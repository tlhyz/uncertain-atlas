# 反模式：把 Info Usage default_lane in table / priority 0 reserved 正式二事 part 3 卖成 Info 车道 bundled interchangeable / 已经选型 / 已经排了优先

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[default_lane must be in lane_priorities ≠ Info 车道 bundled](../../tracks/implementation/worked-example-infousage-defaultlane-vs-priorityzero.md)。

## 卖法

- 「看见 default_lane has to be one of the identifiers defined in lane_priorities / default_lane 必须在 lane_priorities 表里 就已经 Info 车道 bundled（367）第二件事 interchangeable / 已经 empty iff interchangeable / CheckTx lane_id in range interchangeable / 已经选型。」
- 「看见 The lowest priority a lane can have is 1 / 0 is reserved for empty lane_id in ResponseCheckTx / 最低优先级是 1、0 留给不设道 就已经 Info 车道 bundled（367）第三件事 interchangeable / CheckTx lane_id empty → default lane interchangeable / 已经排了优先 / 已经进了块。」

## 为什么错

官方把 Info Usage 第 7–8 条核心句写成两件独立的实现事。把它们卖成 Info 车道 bundled interchangeable / 已经选型 / 已经排了优先，会把 default in table 约束和 priority 0 预留两条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage default_lane in table / priority 0 reserved 正式二事 part 3，必须分开 default_lane must be in lane_priorities、priority 0 reserved for empty lane_id 两个名字，不要把它们卖成 Info 车道 bundled interchangeable / 已经选型 / 已经排了优先。

## 和相邻反模式

- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 Info Usage part 2，不是本页 part 3 专用边界。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是 Info 车道 bundled 三事，不是本页 Methods Info Usage default in table 单句专用边界。
