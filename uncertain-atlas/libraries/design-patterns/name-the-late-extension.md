# 模式：把 +2/3 之后才进来的扩展三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**例**：[+2/3 之后才进来的扩展写进了 commit info ≠ 已经 Verify 过](../../tracks/implementation/worked-example-late-extension-vs-verified.md)。

## 三个名字

1. **+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过：** 看见 last_commit 里有扩展不是已经 Accept。
2. **建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify：** 看见 Prepare 要用这些扩展不是已经过了 Req 6。
3. **下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify：** 看见规范允许写入不是已经必须再叫。

## 为什么要分开叫

官方把 +2/3 之后才进来的扩展未经 Verify、Prepare 要用时建议再看、下一高度可以不叫 Verify 写成三件事。把它们叫成一个「看见 last_commit 里有扩展就已经 Verify 过」，会把拒收整张预提交、Req 6 必须 Accept 和到了 H 才 Prepare 带扩展一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 last_commit 里有扩展就已经 Verify 过」，先数清问的是 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过、建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify，还是下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify，再决定要不要同一次发布。
