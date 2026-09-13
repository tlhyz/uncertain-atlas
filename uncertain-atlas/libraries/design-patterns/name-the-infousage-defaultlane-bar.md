# 模式：把 Info Usage default_lane in table / priority 0 reserved 正式二事 part 3 说成两个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[default_lane must be in lane_priorities ≠ Info 车道 bundled](../../tracks/implementation/worked-example-infousage-defaultlane-vs-priorityzero.md)。

## 两个名字

1. **default_lane must be in lane_priorities 不是 Info 车道 bundled：** 看见 Methods Info Usage default in table，不是 367 bundled 第二件事 interchangeable。
2. **priority 0 reserved for empty lane_id 不是 Info 车道 bundled：** 看见 priority 0 预留，不是 367 bundled 第三件事 interchangeable。

## 为什么要分开叫

官方把 Info Usage 第 7–8 条、Info Usage part 2（497）、Info 车道 bundled（367）、CheckTx Usage lane_id（482）写成两个名字。把它们叫成一个「看见 Info 回了 default_lane / 优先级 0 就已经选型、已经排了优先」，会把 default in table 约束和 priority 0 预留两条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage default_lane in table / priority 0 reserved 正式二事 part 3，先数清问的是 default_lane must be in lane_priorities 是不是 Info 车道 bundled interchangeable / empty iff interchangeable、priority 0 reserved for empty lane_id 是不是 Info 车道 bundled interchangeable / CheckTx lane_id default lane interchangeable，再决定要不要同一次发布。
