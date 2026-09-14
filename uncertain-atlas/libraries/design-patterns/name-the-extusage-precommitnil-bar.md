# 模式：把 ExtendVote Usage precommit nil will not call ExtendVote 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / When precommit nil 句。  
**例**：[precommit nil will not call ExtendVote ≠ bundled](../../tracks/implementation/worked-example-extusage-precommitnil-vs-bundled.md)。

## 三个名字

1. **only attached to non-nil Precommit 不是 already will call：** 看见 vote_extension only on non-nil，不是 437 bundled interchangeable / 350 only on non-nil at Req 6 interchangeable / 438 ExtendVote When interchangeable。
2. **precommit nil will not call ExtendVote 不是 ExtendVote Usage bundled：** 看见 will not call on nil，不是 437 bundled interchangeable / 525 0-length still calls interchangeable / 361 +2/3 prevote nil ExtendVote interchangeable。
3. **nil vote no CanonicalVoteExtension 不是 already has extension：** 看见 nil vote no extension，不是 510 fill CanonicalVoteExtension interchangeable / 438 construct/broadcast interchangeable / 525 chose empty interchangeable。

## 为什么要分开叫

官方把 only on non-nil Precommit、precommit nil will not call、nil vote no CanonicalVoteExtension、ExtendVote Usage bundled（437）、0-length still calls（525）、ExtendVote When（438）写成三个名字。把它们叫成一个「看见 precommit nil 就已经会调 ExtendVote interchangeable、已经不会叫 interchangeable」，会把 attachment 条件、nil 路径不调、nil 票无 extension 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage precommit nil will not call ExtendVote 正式三事，先数清问的是 only on non-nil 是不是 already will call、precommit nil will not call 是不是 ExtendVote Usage bundled、nil vote no CanonicalVoteExtension 是不是 already has extension，再决定要不要同一次发布。
