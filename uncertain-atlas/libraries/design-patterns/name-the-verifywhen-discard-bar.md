# 模式：把 VerifyVoteExtension When discard invalid extension 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**例**：[discard invalid extension ≠ bundled](../../tracks/implementation/worked-example-verifywhen-discard-vs-bundled.md)。

## 三个名字

1. **discards invalid Precommit 不是 Verify When 正式流程 bundled：** 看见 discards Precommit without valid signature extension，不是 435 bundled interchangeable / 已经带有效签就会调 Verify interchangeable。
2. **0-length with valid signature 不是空扩展仍会调 Verify bundled：** 看见 0-length valid with valid signature，不是 353 跳过 Verify interchangeable / 0 长就不合法 interchangeable。
3. **step 1 before VerifyVoteExtension call 不是已经验过扩展：** 看见 step 1 before call，不是 435 ACCEPT/REJECT interchangeable / 已经写进 last_commit interchangeable。

## 为什么要分开叫

官方把 discards invalid、0-length validity、step 1 before call、Verify When 正式流程 bundled（435）、空扩展仍会调 Verify（353）写成三个名字。把它们叫成一个「看见收到 Precommit 就已经跳过 Verify interchangeable、已经验过扩展 interchangeable」，会把 discard、0 长有效性、顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事，先数清问的是 discards invalid 是不是 Verify When 正式流程 bundled interchangeable、0-length with valid signature 是不是空扩展仍会调 Verify bundled interchangeable、step 1 before call 是不是已经验过扩展 interchangeable，再决定要不要同一次发布。
