# 模式：点名 querystate-notlive 杠

**层次**：实现 / 上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应**：[`../tracks/implementation/worked-example-querystate-notlive-vs-bundled.md`](../tracks/implementation/worked-example-querystate-notlive-vs-bundled.md)。

- **上次 Commit 不是已经跟上正在跑的块：** 看见上次 Commit，不是已经含本轮还没交差的执行 interchangeable / 963 querystate-notlive interchangeable。
- **看见能读 不是已经是 CheckTxState：** 看见能读，不是已经是 CheckTxState interchangeable。
- **看见只读 不是已经交差：** 看见只读，不是已经和正在改的 ExecuteTxState 同步 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看上次 Commit 正式三事（314 余量），先数清问的是是不是已经跟上正在跑的块、是不是已经是 CheckTxState、还是看见只读是不是已经交差，再决定要不要同一次发布。314 querystate vs execute bundled unbundling 在本页 item 2 续。
