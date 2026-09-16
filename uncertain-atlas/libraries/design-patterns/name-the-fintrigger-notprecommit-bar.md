# 模式：把 FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts 正式三事（479 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**例**：[FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote ≠ bundled（479）](../../tracks/implementation/worked-example-fintrigger-notprecommit-vs-bundled.md)。

## 三个名字

1. **2f+1 precommit 不是 +2/3 prevote ExtendVote：** 看见 Precommit from 2f+1 voting power precommitting same id(_v_) 不是已经 prevote 锁住 ExtendVote interchangeable，不是 361 extendwhen interchangeable / 361 prevote ExtendVote bundled interchangeable / 438 extwhen flow interchangeable。
2. **2f+1 precommit 不是 without all block parts：** 看见 2f+1 precommit same id(v) 不是已经 partial block 就够 precommit interchangeable，不是 608 notparts interchangeable / 428 finhash interchangeable / 472 Process guarantee interchangeable。
3. **2f+1 precommit 不是 fintrigger bundled：** 看见 Precommit 门槛 不是已经 fintrigger bundled interchangeable，不是 479 item 3 decides block v interchangeable / 362 finwhen interchangeable / 362 +2/3 precommit interchangeable。

## 为什么要分开叫

官方把 Proposal + parts、2f+1 precommit、decides block v 和 only hash、prevote ExtendVote、到了这一高就会调 Finalize 写成三个名字。把它们叫成一个「看见 2f+1 precommit 就已经 prevote ExtendVote、就已经可以没有 all block parts interchangeable、已经 fintrigger bundled interchangeable」，会把 not +2/3 prevote ExtendVote、not without all block parts、not fintrigger bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger 2f+1 precommit not +2/3 prevote ExtendVote / not without all block parts 正式三事（479 余量），先数清问的是 2f+1 precommit 是不是 already +2/3 prevote ExtendVote / 361，是不是 already without all block parts / 608 / 428，还是 2f+1 precommit 是不是 already fintrigger bundled / 479 item 3 / 362，再决定要不要同一次发布。
