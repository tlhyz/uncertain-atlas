# 模式：把 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**例**：[ACCEPT keep or REJECT discard ≠ bundled](../../tracks/implementation/worked-example-verifywhen-keepdiscard-vs-bundled.md)。

## 三个名字

1. **ACCEPT keep vote and extension 不是 Verify When 正式流程 bundled：** 看见 keep in internal structures，不是 435 bundled interchangeable / 已经写进 last_commit interchangeable。
2. **populate ExtendedCommitInfo in h+1 Prepare 不是已经进了块：** 看见 h+1 Prepare 用途，不是 352 迟到扩展已经 Verify 过 interchangeable / 441 Notes 票序 bundled interchangeable。
3. **REJECT discard Precommit 不是 step 1 discard bundled：** 看见 REJECT deem invalid and discard，不是 514 discard interchangeable / 433 status 回包 bundled interchangeable。

## 为什么要分开叫

官方把 ACCEPT keep、h+1 Prepare populate、REJECT discard、Verify When 正式流程 bundled（435）、step 3 return（516）、迟到扩展 MAY（352）写成三个名字。把它们叫成一个「看见 ACCEPT 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」，会把 keep、用途、discard 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事，先数清问的是 ACCEPT keep 是不是 Verify When 正式流程 bundled interchangeable、populate ExtendedCommitInfo in h+1 Prepare 是不是已经写进 last_commit interchangeable、REJECT discard 是不是 step 1 discard bundled interchangeable，再决定要不要同一次发布。
