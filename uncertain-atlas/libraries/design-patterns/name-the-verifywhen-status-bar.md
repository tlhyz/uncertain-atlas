# 模式：把 VerifyVoteExtension When return status 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**例**：[return status ≠ bundled](../../tracks/implementation/worked-example-verifywhen-status-vs-bundled.md)。

## 三个名字

1. **Application returns ACCEPT/REJECT 不是 Verify When 正式流程 bundled：** 看见 returns status via VerifyVoteExtensionResponse.status，不是 435 bundled interchangeable / 已经 Accept interchangeable / 已经 REJECT 丢掉 Precommit interchangeable。
2. **step 3 after call VerifyVoteExtension 不是 step 2 call bundled：** 看见 step 3 after call，不是 515 call interchangeable / 514 discard interchangeable / 353 跳过 Verify interchangeable。
3. **step 3 before keep/discard 不是已经写进 last_commit：** 看见 step 3 before step 4，不是 435 ACCEPT/REJECT post-effects interchangeable / 352 迟到扩展已经 Verify 过 interchangeable。

## 为什么要分开叫

官方把 Application returns status、step 3 after call、step 3 before keep/discard、Verify When 正式流程 bundled（435）、step 2 call（515）、Verify 回包栏（433）写成三个名字。把它们叫成一个「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable、已经 REJECT 丢掉 Precommit interchangeable」，会把 return、顺序、后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事，先数清问的是 Application returns ACCEPT/REJECT 是不是 Verify When 正式流程 bundled interchangeable、step 3 after call 是不是 step 2 call bundled interchangeable、step 3 before keep/discard 是不是已经写进 last_commit interchangeable，再决定要不要同一次发布。
