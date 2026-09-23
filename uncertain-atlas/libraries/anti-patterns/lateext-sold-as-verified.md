# 反模式：看见 +2/3 之后才进来的扩展写进了 commit info 就当成已经 Verify 过 / 看见建议按 Verify 同款逻辑再看一遍就当成已经是引擎会再 Verify / 看见下一高度 round 0 写进 ExtendedCommitInfo 就当成已经又叫了 Verify

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**例**：[+2/3 之后才进来的扩展写进了 commit info ≠ 已经 Verify 过](../../tracks/implementation/worked-example-late-extension-vs-verified.md)。

## 塌法

1. 看见 +2/3 之后才进来的扩展写进了 commit info / 看见 last_commit 里有扩展，就当成已经 Verify 过，或当成已经 Accept。
2. 看见建议按 `VerifyVoteExtension` 同款逻辑再看一遍 / 看见 Prepare 要用这些扩展改提案，就当成已经是引擎会再 Verify，或当成已经是正确进程交出的扩展必须被正确接收者 Verify Accept。
3. 看见下一高度 round 0 收到上一高度 `CommitRound` 的 Precommit / 看见写进 `ExtendedCommitInfo`，就当成已经又叫了 Verify，或当成已经必须再 Verify。

## 为什么会出事

官方写：commit info 里过了最低 +2/3 之后才加进来的扩展没有被 Verify。应用若要用它们改提案，建议按 Verify 同款逻辑再看一遍。下一高度 round 0 收到上一高度 Precommit 时，MAY 写进 `ExtendedCommitInfo` 而不再叫 Verify。

## 和相邻反模式

- [lateext-notverified-sold-as-bundled](lateext-notverified-sold-as-bundled.md) 是 +2/3 之后才进来的扩展写进了 commit info not already verified / not already accept / not already later-verified 正式三事（352 item 1），不是本页 bundled 全段 alone。
- [lateext-notreverify-sold-as-bundled](lateext-notreverify-sold-as-bundled.md) 是建议按 Verify 同款逻辑再看一遍 not already engine-reverify / not already req6-done / not already settled 正式三事（352 item 2），不是本页 bundled 全段 alone。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交就已经是块非法，不是本页这种 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept，不是本页这种建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展，不是本页这种下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify。
