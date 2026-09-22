# 模式：把 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**例**：[Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only-liveness ≠ bundled（348）](../../tracks/implementation/worked-example-req6-notliveness-vs-bundled.md)。

## 三个名字

1. **Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 不是 already only-liveness：** 看见 Extend 或 Verify（或两边）里有确定 bug / 带无效扩展的 Precommit 会被丢掉 / 有确定 bug，不是已经只是活性问题 interchangeable / 已经 only-liveness interchangeable / 已经只伤活性交差 interchangeable，不是 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable。

2. **Precommit 被丢掉 不是 already block-invalid：** 看见 Precommit 被丢掉 / 带无效扩展的 Precommit 会被丢掉 / 算丢掉，不是已经是块非法 interchangeable / 已经 block-invalid interchangeable / 已经块非法交差 interchangeable，不是 34 voteext interchangeable / 341 verifydet interchangeable。

3. **有确定 bug 不是 already nondet：** 看见有确定 bug / 算丢掉 / 确定 bug 让 Precommit 被丢掉，不是已经是 Verify 非确定 bug interchangeable / 已经 nondet interchangeable / 已经非确定交差 interchangeable，不是 797 req6-notany interchangeable / 799 req6-notsafety interchangeable。

官方把确定 bug 丢掉 Precommit、不是已经是块非法、不是已经是非确定 bug写成三个名字。把它们叫成一个「看见丢掉就已经只是活性问题 interchangeable / 就已经是块非法 interchangeable / 就已经是非确定 bug interchangeable」，会把 not already only-liveness、not already block-invalid、not already nondet 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量），先数清问的是 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 是不是 already only-liveness / 348 / req6coherence-sold-as-accept，是不是 Precommit 被丢掉 是不是 already block-invalid，还是有确定 bug 是不是 already nondet，再决定要不要同一次发布。348 req6 vs accept bundled unbundling 在本页 item 2 续。
