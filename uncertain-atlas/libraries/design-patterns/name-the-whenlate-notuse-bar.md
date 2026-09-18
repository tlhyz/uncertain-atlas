# 模式：点名 whenlate-notuse 杠

**层次**：实现 / LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事（519 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**对应**：[`../tracks/implementation/worked-example-whenlate-notuse-vs-bundled.md`](../tracks/implementation/worked-example-whenlate-notuse-vs-bundled.md)。

- **MAY 用 commit info 里的扩展改提案 不是已经 Verify 过：看见MAY 用 commit info 里的扩展改提案，不是已经 Verify 过 interchangeable / 1320 whenlate-notuse interchangeable。**
- **未 Verify 前提下 MAY 使用 不是已经 ExtendedCommitInfo 就已经进了块：看见未 Verify 前提下 MAY 使用，不是已经 ExtendedCommitInfo 就已经进了块 interchangeable / 1320 whenlate-notuse interchangeable。**
- **MAY 用 commit info 里的扩展改提案 不是已经 Prepare 改列表 bundled：看见MAY 用 commit info 里的扩展改提案，不是已经 Prepare 改列表 bundled interchangeable / 1320 whenlate-notuse interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When +2/3 late extensions not verified 正式三事（519 余量），必须分开 not already 352-bundled、not already verified、not already engine-re-Verify 三件事。
