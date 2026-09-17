# 反模式：把 拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量） 写成已经 已经能接着装 / 已经同一份 / 已经交差

**层次**：实现 / 拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应**：[`../tracks/implementation/worked-example-snapshot-restore-notresume-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-restore-notresume-vs-bundled.md)。

把 拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量） 写成已经 已经能接着装 / 已经同一份 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拉失败换一份 正式三事（321 余量），必须分开 not already resumable、not already same-snapshot、not already settled 三件事，不要和 321 / 320 / 322 / 959 / 960 糊成一句。

也不是：

- [snapshot-restore-notchunk-sold-as-bundled](snapshot-restore-notchunk-sold-as-bundled.md) 是一块 chunk 仍未齐单句边界（960 item 2），不是本页换一份仍不能接着装边界。
- 崩溃三步已经 Commit 是不变量 320，不是本页能重试仍不是同一份边界。
