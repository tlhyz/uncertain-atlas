# 模式：把 FinalizeBlock When trigger Proposal + all block parts not only hash / Process ran 正式三事（479 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**例**：[FinalizeBlock When trigger Proposal + all block parts not only hash ≠ bundled（479）](../../tracks/implementation/worked-example-fintrigger-notparts-vs-bundled.md)。

## 三个名字

1. **Proposal + all block parts 不是 only hash：** 看见 Proposal message with block _v_ and all its block parts 不是已经 hash 栏对上 interchangeable，不是 428 finhash interchangeable / partial block interchangeable。
2. **Proposal + all block parts 不是 Process 跑过：** 看见 Proposal + all block parts 不是已经 ProcessProposal 跑过 interchangeable，不是 472 Process guarantee interchangeable / 452 candidate interchangeable / 354 processwhen synchronous interchangeable。
3. **Proposal + all block parts 不是 fintrigger bundled：** 看见 Proposal + all block parts 不是已经 fintrigger bundled interchangeable，不是 479 item 2 2f+1 precommit interchangeable / 479 item 3 decides block v interchangeable / 362 finwhen interchangeable / 361 prevote ExtendVote interchangeable。

## 为什么要分开叫

官方把 Proposal + parts、2f+1 precommit、decides block v 和 only hash、Process 跑过、到了这一高就会调 Finalize 写成三个名字。把它们叫成一个「看见 Proposal + parts 就已经 only hash、已经 Process 跑过 interchangeable、已经 fintrigger bundled interchangeable」，会把 not only hash、not Process ran、not fintrigger bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When trigger Proposal + all block parts not only hash / Process ran 正式三事（479 余量），先数清问的是 Proposal + all block parts 是不是 already only hash / 428，是不是 already Process 跑过 / 472 / 452，还是 Proposal + all block parts 是不是 already fintrigger bundled / 479 item 2 / 479 item 3 / 362，再决定要不要同一次发布。
