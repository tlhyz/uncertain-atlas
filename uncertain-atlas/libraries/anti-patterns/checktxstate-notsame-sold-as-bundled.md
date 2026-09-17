# 反模式：把 同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量） 写成已经 已经同一份 / 已经合并 / 已经交差

**层次**：实现 / 同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应**：[`../tracks/implementation/worked-example-checktxstate-notsame-vs-bundled.md`](../tracks/implementation/worked-example-checktxstate-notsame-vs-bundled.md)。

把 同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量） 写成已经 已经同一份 / 已经合并 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同时在改 正式三事（312 余量），必须分开 not already same-state、not already merged、not already settled 三件事，不要和 312 / 310 / 314 / 968 / 970 糊成一句。

也不是：

- [checktxstate-notexec-sold-as-bundled](checktxstate-notexec-sold-as-bundled.md) 是过了仍未按 ExecuteTxState 验单句边界（968 item 1），不是本页两边都在改仍不是同一份边界。
- 默认锁已经 RPC 安全是不变量 310，不是本页并发仍未合并边界。
