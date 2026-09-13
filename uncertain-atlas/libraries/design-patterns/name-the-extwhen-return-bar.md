# 模式：把 ExtendVote When return extension 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 3。  
**例**：[return extension ≠ bundled](../../tracks/implementation/worked-example-extwhen-return-vs-bundled.md)。

## 三个名字

1. **returns ExtendVoteResponse.extension 不是 ExtendVote When 正式流程 bundled：** 看见 Application returns extension bytes，不是 438 填 CanonicalVoteExtension / 广播 Precommit interchangeable。
2. **not interpreted by consensus 不是已经是同一份扩展：** 看见 which is not interpreted by the consensus algorithm，不是 361 return+不解释 bundled interchangeable。
3. **step 3 before CanonicalVoteExtension 不是 ExtendVote 何时调用 bundled：** 看见 step 3 after synchronous call before fill CanonicalVoteExtension，不是 361 门槛 bundled interchangeable。

## 为什么要分开叫

官方把 returns extension、not interpreted by consensus、step 3 before CanonicalVoteExtension、ExtendVote 何时调用 bundled（361）、ExtendVote When 正式流程 bundled（438）、vote_extension 会包进包装（358）写成三个名字。把它们叫成一个「看见调了 ExtendVote 就已经是同一份扩展 interchangeable、已经包进 CanonicalVoteExtension interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」，会把 return、不解释、step 3 顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When return extension 正式三事，先数清问的是 returns ExtendVoteResponse.extension 是不是 ExtendVote When 正式流程 bundled interchangeable、not interpreted by consensus 是不是已经是同一份扩展 interchangeable、step 3 before CanonicalVoteExtension 是不是 ExtendVote 何时调用 bundled interchangeable，再决定要不要同一次发布。
