# 模式：把 VerifyVoteExtension When late-arriving MAY add without Verify 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When late-arriving MAY 段。  
**例**：[late-arriving MAY add without Verify ≠ bundled](../../tracks/implementation/worked-example-verifywhen-latemay-vs-bundled.md)。

## 三个名字

1. **MAY add without Verify 不是迟到扩展 bundled：** 看见 MAY add to ExtendedCommitInfo without calling VerifyVoteExtension，不是 352 bundled interchangeable / 已经 Verify 过 interchangeable / 已经又叫了 Verify interchangeable。
2. **round 0 h-1 CommitRound 不是正常 When round r height h：** 看见 round 0 height h 收到上一高度 Precommit，不是 515 正常 When 前提 interchangeable / 435 Verify When 正式流程 interchangeable。
3. **without calling VerifyVoteExtension 不是已经 Verify 过：** 看见 without calling Verify，不是 352 建议再看 interchangeable / 515 step 2 call interchangeable / 已经 Accept interchangeable。

## 为什么要分开叫

官方把 MAY add without Verify、round 0 h-1 CommitRound 前提、without calling VerifyVoteExtension、迟到扩展 bundled（352）、正常 Verify When steps（514–517）写成三个名字。把它们叫成一个「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经又叫了 Verify interchangeable」，会把 MAY 路径、前提、不调 Verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When late-arriving MAY add without Verify 正式三事，先数清问的是 MAY add without Verify 是不是迟到扩展 bundled interchangeable、round 0 h-1 CommitRound 是不是正常 When round r height h interchangeable、without calling VerifyVoteExtension 是不是已经 Verify 过 interchangeable，再决定要不要同一次发布。
