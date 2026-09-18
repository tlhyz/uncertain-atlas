# 模式：点名 eviuse-nottwo 杠

**层次**：实现 / ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事（447 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage 句。  
**对应**：[`../tracks/implementation/worked-example-eviuse-nottwo-vs-bundled.md`](../tracks/implementation/worked-example-eviuse-nottwo-vs-bundled.md)。

- **两份签都在且没 non_rp 就签空切片不是已经只有一份签 不是已经只有一份签：看见两份签都在且没 non_rp 就签空切片不是已经只有一份签，不是已经只有一份签 interchangeable / 1367 eviuse-nottwo interchangeable。**
- **two signatures present and empty-slice if no non_rp is not already one signature 不是已经没 non_rp 就没有第二份签：看见two signatures present and empty-slice if no non_rp is not already one signature，不是已经没 non_rp 就没有第二份签 interchangeable / 1367 eviuse-nottwo interchangeable。**
- **两份签都在且没 non_rp 就签空切片不是已经只有一份签 不是已经 optional 就跳过 Verify：看见两份签都在且没 non_rp 就签空切片不是已经只有一份签，不是已经 optional 就跳过 Verify interchangeable / 1367 eviuse-nottwo interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（447 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
