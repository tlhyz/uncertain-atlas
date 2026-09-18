# 模式：点名 ionce-notcrash 杠

**层次**：实现 / InitChain once-at-genesis not already crash-recall / not already skip-step / not already past-genesis 正式三事（412 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应**：[`../tracks/implementation/worked-example-ionce-notcrash-vs-bundled.md`](../tracks/implementation/worked-example-ionce-notcrash-vs-bundled.md)。

- **once-at-genesis 不是已经是崩溃后再调：** 看见调了一次，不是已经是崩溃后再调 interchangeable / 1091 ionce-notcrash interchangeable。
- **看见调了一次 不是已经能跳步：** 看见调了一次，不是已经能跳步 interchangeable。
- **看见有创世调用 不是已经过了 genesis_time：** 看见有创世调用，不是已经过了 genesis_time interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 once-at-genesis 正式三事（412 余量），先数清问的是是不是已经是崩溃后再调、是不是已经能跳步、还是看见有创世调用是不是已经过了 genesis_time，再决定要不要同一次发布。412 initonce vs crash bundled unbundling 在本页 item 1 启动。
