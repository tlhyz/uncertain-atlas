# 模式：点名 snapshot-restore-notresume 杠

**层次**：实现 / 拉失败换一份 not already resumable / not already same-snapshot / not already settled 正式三事（321 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**对应**：[`../tracks/implementation/worked-example-snapshot-restore-notresume-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-restore-notresume-vs-bundled.md)。

- **拉失败换一份 不是已经能接着装：** 看见换了一份，不是已经能接着上次 interchangeable / 961 snapshot-restore-notresume interchangeable。
- **看见能重试 不是已经同一份：** 看见能重试，不是已经同一份 interchangeable。
- **看见失败了 不是已经交差：** 看见失败了，不是已经装过的还能用 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拉失败换一份 正式三事（321 余量），先数清问的是是不是已经能接着装、是不是已经同一份、还是看见失败了是不是已经交差，再决定要不要同一次发布。321 snapshot-restore vs offer bundled unbundling 在本页 item 3 完成。
