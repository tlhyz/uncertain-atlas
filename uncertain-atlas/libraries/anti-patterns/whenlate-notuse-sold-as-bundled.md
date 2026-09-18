# 反模式：把 LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事（519 余量） 写成已经 已经 Verify 过 / 已经 ExtendedCommitInfo 就已经进了块 / 已经 Prepare 改列表 bundled

**层次**：实现 / LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事（519 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**对应**：[`../tracks/implementation/worked-example-whenlate-notuse-vs-bundled.md`](../tracks/implementation/worked-example-whenlate-notuse-vs-bundled.md)。

把 LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事（519 余量） 写成已经 已经 Verify 过 / 已经 ExtendedCommitInfo 就已经进了块 / 已经 Prepare 改列表 bundled，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When +2/3 late extensions not verified 正式三事（519 余量），必须分开 not already 352-bundled、not already verified、not already engine-re-Verify 三件事，不要和 519 / 355 / 330 / 1319 / 1321 糊成一句。

也不是：

- [whenlate-notver-sold-as-bundled](whenlate-notver-sold-as-bundled.md) 是 notver 单句边界（1319），不是本页边界。
- [whenlate-notsug-sold-as-bundled](whenlate-notsug-sold-as-bundled.md) 是 notsug 单句边界（1321），不是本页边界。
- [sugval-notreverify-sold-as-bundled](sugval-notreverify-sold-as-bundled.md) 是 SuggestValidate 不是引擎再 Verify 仍未是已经 Verify 过边界（520/1318），不是本页 +2/3 未 Verify 边界。
