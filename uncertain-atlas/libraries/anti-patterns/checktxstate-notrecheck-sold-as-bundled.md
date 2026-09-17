# 反模式：把 RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量） 写成已经 已经是新交易 / 已经当 NEW 处理 / 已经交差

**层次**：实现 / RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应**：[`../tracks/implementation/worked-example-checktxstate-notrecheck-vs-bundled.md`](../tracks/implementation/worked-example-checktxstate-notrecheck-vs-bundled.md)。

把 RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量） 写成已经 已经是新交易 / 已经当 NEW 处理 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 RECHECK 正式三事（312 余量），必须分开 not already new-tx、not already unlocked、not already settled 三件事，不要和 312 / 301 / 328 / 968 / 969 糊成一句。

也不是：

- [checktxstate-notsame-sold-as-bundled](checktxstate-notsame-sold-as-bundled.md) 是两边都在改仍不是同一份单句边界（969 item 2），不是本页 RECHECK 仍不是新交易边界。
- 提案收了已经从池里删掉是不变量 301，不是本页 Commit 回了锁仍未放下边界。
