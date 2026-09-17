# 模式：把 CheckTx Usage lane_id in ResponseInfo range not Info table selection / not in-table means prioritized / not CheckTx response field bundled 正式三事（482 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[lane_id ≠ bundled（482）](../../tracks/implementation/worked-example-chktxlane-notrange-vs-bundled.md)。

## 三个名字

1. **lane_id in range 不是 Info 表选型交差：** 看见必须在范围内，不是已经 367 interchangeable / 706 chktxlane-notrange interchangeable。
2. **看见必须在范围内 不是填了就排了优先：** 看见 in range，不是已经排了优先 interchangeable。
3. **看见 Usage 这句 不是 CheckTx 回包栏 bundled：** 看见 in range 单句，不是已经 381 interchangeable。

官方把 CheckTx Usage lane_id 三条核心句拆成三个名字。把它们叫成一个「看见 CheckTx 回了 lane_id 就已经排了优先」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage lane_id in range 正式三事（482 余量），先数清问的是 in range 是不是 Info 表选型 / 367、是不是填了就排了优先、还是看见 Usage 是不是 CheckTx 回包栏 bundled / 381，再决定要不要同一次发布。482 chktxlane vs default bundled unbundling 在本页 item 3 完成。
