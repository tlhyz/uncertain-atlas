# 反模式：把 SuggestValidate same-manner not already step-2-call / not already Verify-When / not already MUST-det 正式三事（520 余量） 写成已经 已经 Verify When step 2 call bundled / 已经 CometBFT 会叫 / 已经 VerifyVoteExtension MUST be deterministic

**层次**：实现 / SuggestValidate same-manner not already step-2-call / not already Verify-When / not already MUST-det 正式三事（520 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**对应**：[`../tracks/implementation/worked-example-sugval-notcall-vs-bundled.md`](../tracks/implementation/worked-example-sugval-notcall-vs-bundled.md)。

把 SuggestValidate same-manner not already step-2-call / not already Verify-When / not already MUST-det 正式三事（520 余量） 写成已经 已经 Verify When step 2 call bundled / 已经 CometBFT 会叫 / 已经 VerifyVoteExtension MUST be deterministic，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When suggested validate like Verify 正式三事（520 余量），必须分开 not already must-Accept、not already step-2-call、not already engine-re-Verify 三件事，不要和 520 / 515 / 435 / 1316 / 1318 糊成一句。

也不是：

- [sugval-notmust-sold-as-bundled](sugval-notmust-sold-as-bundled.md) 是 notmust 单句边界（1316），不是本页边界。
- [sugval-notreverify-sold-as-bundled](sugval-notreverify-sold-as-bundled.md) 是 notreverify 单句边界（1318），不是本页边界。
- [whenret-notuse-sold-as-bundled](whenret-notuse-sold-as-bundled.md) 是 PrepareWhenRet 用改过的块当提案仍未是 validValue 跳过边界（506/1315），不是本页建议自验边界。
