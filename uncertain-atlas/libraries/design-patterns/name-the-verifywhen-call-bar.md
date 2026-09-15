# 模式：把 VerifyVoteExtension When call VerifyVoteExtension 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**例**：[call VerifyVoteExtension ≠ bundled](../../tracks/implementation/worked-example-verifywhen-call-vs-bundled.md)。

## 三个名字

1. **calls VerifyVoteExtension 不是 Verify When 正式流程 bundled：** 看见 Else CometBFT calls VerifyVoteExtension，不是 435 bundled interchangeable / 已经验过扩展 interchangeable / 已经 Accept interchangeable。
2. **received from q≠p 不是不对 local process 调用 bundled：** 看见收到他人 Precommit 后 call，不是 353 Usage 本地票也 Verify interchangeable / 352 迟到扩展已经 Verify 过 interchangeable。
3. **step 2 before status return 不是已经 Accept：** 看见 step 2 before Application returns ACCEPT/REJECT，不是 435 step 3–4 interchangeable / 433 status 回包 interchangeable / 已经写进 last_commit interchangeable。

## 为什么要分开叫

官方把 calls VerifyVoteExtension、received from q≠p、step 2 before return、Verify When 正式流程 bundled（435）、step 1 discard（514）、Verify 回包 status（433）写成三个名字。把它们叫成一个「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable、已经 Accept interchangeable」，会把 call、收到侧前提、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事，先数清问的是 calls VerifyVoteExtension 是不是 Verify When 正式流程 bundled interchangeable、received from q≠p 是不是不对 local process 调用 bundled interchangeable、step 2 before status return 是不是已经 Accept interchangeable，再决定要不要同一次发布。
