# 模式：把 CheckTx Usage assigned to default lane not default_lane identifier / not Priority consensus order / not Check passed is in proposal 正式三事（482 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[assigned ≠ bundled（482）](../../tracks/implementation/worked-example-chktxlane-notassigned-vs-bundled.md)。

## 三个名字

1. **assigned to default lane 不是 default_lane 标识写进回包：** 看见放进默认道，不是已经写了标识 interchangeable / 705 chktxlane-notassigned interchangeable。
2. **看见放进默认道 不是 Priority 就已经是共识顺序：** 看见 assigned，不是已经 317 interchangeable。
3. **看见 Usage 这句 不是 Check 通过就是已进提案：** 看见 assigned 单句，不是已经 33 interchangeable。

官方把 CheckTx Usage lane_id 三条核心句拆成三个名字。把它们叫成一个「看见 CheckTx 回了 lane_id 就已经排了优先」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage assigned to default lane 正式三事（482 余量），先数清问的是 assigned 是不是回包写了 default_lane 标识、是不是 Priority 就已经是共识顺序 / 317、还是看见 Usage 是不是 Check 通过就是已进提案 / 33，再决定要不要同一次发布。482 chktxlane vs default bundled unbundling 在本页 item 2 续。
