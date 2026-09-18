# 模式：点名 vwkeep-notkeep 杠

**层次**：实现 / VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事（517 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应**：[`../tracks/implementation/worked-example-vwkeep-notkeep-vs-bundled.md`](../tracks/implementation/worked-example-vwkeep-notkeep-vs-bundled.md)。

- **ACCEPT 会把票和扩展留在内部结构 不是已经 Verify When 正式流程 bundled：看见ACCEPT 会把票和扩展留在内部结构，不是已经 Verify When 正式流程 bundled interchangeable / 1334 vwkeep-notkeep interchangeable。**
- **keep vote and extension 不是已经写进 last_commit：看见keep vote and extension，不是已经写进 last_commit interchangeable / 1334 vwkeep-notkeep interchangeable。**
- **ACCEPT 会把票和扩展留在内部结构 不是已经 +2/3 之后才进来的扩展写进了 commit info：看见ACCEPT 会把票和扩展留在内部结构，不是已经 +2/3 之后才进来的扩展写进了 commit info interchangeable / 1334 vwkeep-notkeep interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事（517 余量），必须分开 not already Verify-When-bundled、not already last_commit、not already step-1-discard 三件事。
