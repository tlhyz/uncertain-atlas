# 反模式：把 一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量） 写成已经 已经齐 / 已经封禁 / 已经交差

**层次**：实现 / 一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应**：[`../tracks/implementation/worked-example-snapshot-restore-notchunk-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-restore-notchunk-vs-bundled.md)。

把 一块 chunk 收下 not already complete / not already banned / not already settled 正式三事（321 余量） 写成已经 已经齐 / 已经封禁 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一块 chunk 收下 正式三事（321 余量），必须分开 not already complete、not already banned、not already settled 三件事，不要和 321 / 314 / 323 / 959 / 961 糊成一句。

也不是：

- [snapshot-restore-notdone-sold-as-bundled](snapshot-restore-notdone-sold-as-bundled.md) 是 Offer 收下仍未装完单句边界（959 item 1），不是本页一块 chunk 仍未齐边界。
- 启动对齐已经是快照重放是不变量 314，不是本页回了再拉仍未封禁边界。
