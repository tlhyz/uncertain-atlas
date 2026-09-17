# 模式：把 FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided / not 479 fintrigger 正式三事（480 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**例**：[FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided ≠ bundled（480）](../../tracks/implementation/worked-example-finmorepre-notmorepre-vs-bundled.md)。

## 三个名字

1. **more precommits despite 2/3+ 不是 decided / final：** 看见 gives the proposer a chance to receive some more precommits despite 2/3+ 不是已经 has required 2/3+ 就已经决定 interchangeable，不是 362 finwhen interchangeable / 362 +2/3 precommit interchangeable / 610 notdecides interchangeable。
2. **more precommits despite 2/3+ 不是 479 fintrigger：** 看见 more precommits 不是已经 When trigger 2f+1 precommit interchangeable，不是 609 notprecommit interchangeable / 608 notparts interchangeable / 479 fintrigger item 2 interchangeable / 479 fintrigger item 3 interchangeable。
3. **more precommits despite 2/3+ 不是 finmorepre bundled：** 看见 more precommits 不是已经 finmorepre bundled interchangeable，不是 611 notproctime interchangeable / 613 notaftercommit interchangeable / 480 item 1 includes processing time interchangeable / 480 item 3 after committing interchangeable。

## 为什么要分开叫

官方把 includes processing time、more precommits despite 2/3+、after committing before next height 和 timeout_commit、已经决定 / 479 fintrigger、槽位 / 1s 常量 写成三个名字。把它们叫成一个「看见 more precommits despite 2/3+ 就已经决定、就已经 479 fintrigger interchangeable、已经 finmorepre bundled interchangeable」，会把 not decided、not 479 fintrigger、not finmorepre bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay more precommits despite 2/3+ not decided / not 479 fintrigger 正式三事（480 余量），先数清问的是 more precommits 是不是 already decided / 362，是不是 already 479 fintrigger / 609 / 608，还是 more precommits 是不是 already finmorepre bundled / 611 / 613，再决定要不要同一次发布。
