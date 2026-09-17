# 反模式：把 CheckTx Usage lane_id 正式二事卖成 priority 0 不设道 / Info 表选型 / 已经排了优先

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[empty lane_id ≠ priority 0 留给不设道](../../tracks/implementation/worked-example-chktxlane-vs-default.md)。

## 卖法

- 「看见 `lane_id` 是空字符串 / 看见应用没设道就已经是 Info 侧 priority 0 不设道 / 已经从池里删掉。」
- 「看见 assigned to the default lane / 看见放进默认道就已经是 `default_lane` 标识 / 已经排了优先 / 已经进了块。」
- 「看见 `lane_id` 必须在 ResponseInfo 范围内 / 看见填了道就已经在 Info 表选型 / 已经 CheckTx 回包栏交差。」

## 为什么错

官方把 empty lane_id → assigned to default lane、lane_id in ResponseInfo range 写成两件独立的实现事。把它们卖成 Info 侧 priority 0 不设道、Info 表选型、已经排了优先，会把 CheckTx Usage 侧引擎分配、Info 配置、Response 字段 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage lane_id，必须分开 empty lane_id → default lane、lane_id in ResponseInfo range 两个名字，不要把它们卖成 priority 0 不设道 / Info 表选型 / 已经排了优先。

## 和相邻反模式

- [lane-sold-as-priority](../../libraries/anti-patterns/lane-sold-as-priority.md) 是 Info 车道就已经排了优先，不是本页 CheckTx Usage assigned to default lane。
- [checktxresponse-sold-as-exec](../../libraries/anti-patterns/checktxresponse-sold-as-exec.md) 是 CheckTx 回包就已经 ExecuteTxState，不是本页 lane_id in range。
