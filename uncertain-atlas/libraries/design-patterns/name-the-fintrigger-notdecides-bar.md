# 模式：把 FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs 正式三事（479 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**例**：[FinalizeBlock When trigger decides block v not at height h will Finalize ≠ bundled（479）](../../tracks/implementation/worked-example-fintrigger-notdecides-vs-bundled.md)。

## 三个名字

1. **decides block v 不是 at height h will Finalize：** 看见 then decides block _v_ 不是已经处在高度 _h_ 就会调 Finalize interchangeable，不是 362 finwhen interchangeable / 362 +2/3 precommit interchangeable / 606 notoutputs interchangeable / 607 notsync interchangeable。
2. **decides block v 不是 persist outputs / 交差：** 看见 decides block v 不是已经 persist decision interchangeable，不是 478 finpersist interchangeable / 605 notpersist interchangeable / 587 finreturn interchangeable / 33 four gates interchangeable。
3. **decides block v 不是 fintrigger bundled：** 看见 then decides block _v_ 不是已经 fintrigger bundled interchangeable，不是 608 notparts interchangeable / 609 notprecommit interchangeable / 611 finwhenparts interchangeable。

## 为什么要分开叫

官方把 Proposal + parts、2f+1 precommit、decides block v 和 only hash、prevote ExtendVote、到了这一高就会调 Finalize 写成三个名字。把它们叫成一个「看见 decides block v 就已经到了这一高就会调 Finalize、已经 persist outputs interchangeable、已经 fintrigger bundled interchangeable」，会把 not at height h will Finalize、not persist outputs、not fintrigger bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger decides block v not at height h will Finalize / not persist outputs 正式三事（479 余量），先数清问的是 decides block v 是不是 already at height h will Finalize / 362，是不是 already persist outputs / 478 / 605 / 587，还是 decides block v 是不是 already fintrigger bundled / 608 / 609，再决定要不要同一次发布。
