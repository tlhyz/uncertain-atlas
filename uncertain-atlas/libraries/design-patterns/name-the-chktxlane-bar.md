# 模式：把 CheckTx Usage lane_id 正式二事说成两个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[empty lane_id ≠ priority 0 留给不设道](../../tracks/implementation/worked-example-chktxlane-vs-default.md)。

## 两个名字

1. **empty lane_id → assigned to default lane 不是 priority 0 留给不设道 / 已经从池里删掉：** 看见空回包 lane_id 会放进默认道，不是 Info 侧 priority 0 不设道 interchangeable。
2. **lane_id in ResponseInfo range 不是 Info 表选型 / CheckTx 回包栏 interchangeable：** 看见 Usage 要求必须在 Info 定义范围内，不是已经 Info 回了车道表就算交差 interchangeable。

## 为什么要分开叫

官方把 CheckTx Usage 里空 lane_id 分配默认道、非空 lane_id 必须在 Info 范围内和 Info 车道配置、CheckTx Response 字段 bundled 写成两个名字。把它们叫成一个「看见 CheckTx 回了 lane_id 就已经排了优先」，会把引擎分配默认道、Info 配置、Response 字段 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage lane_id，先数清问的是 empty lane_id 是不是 assigned to default lane 而不是 priority 0 不设道，还是 lane_id in ResponseInfo range 是不是 Info 表选型 / CheckTx 回包栏 interchangeable，再决定要不要同一次发布。
