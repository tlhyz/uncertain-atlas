# 模式：把 FinalizeBlockResponse next_block_delay after committing before next height not slot / not final / not finmorepre bundled 正式三事（480 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**例**：[FinalizeBlockResponse next_block_delay after committing before next height not slot ≠ bundled（480）](../../tracks/implementation/worked-example-finmorepre-notaftercommit-vs-bundled.md)。

## 三个名字

1. **after committing before next height 不是 slot：** 看见 how long CometBFT waits after committing a block, before starting the next height 不是已经 ConsensusParams.block 块间隔 interchangeable，不是 385 block interval interchangeable / 593 finh1 slot interchangeable / 52 post-commit nondet interchangeable / 589 next_block_delay slot interchangeable。
2. **after committing / set to 0 不是 final / decided：** 看见 Set to 0 if you want progress as soon as it has all the precommits and the block has been processed 不是已经决定 interchangeable，不是 362 finwhen interchangeable / 362 +2/3 precommit interchangeable / 610 notdecides interchangeable / 589 set to 0 interchangeable / 33 four gates interchangeable。
3. **after committing before next height 不是 finmorepre bundled：** 看见 after committing before next height 不是已经 finmorepre bundled interchangeable，不是 611 notproctime interchangeable / 612 notmorepre interchangeable / 480 item 1 includes processing time interchangeable / 480 item 2 more precommits interchangeable / Set to constant 1s interchangeable。

## 为什么要分开叫

官方把 includes processing time、more precommits despite 2/3+、after committing before next height 和 timeout_commit、已经决定 / 479 fintrigger、槽位 / 1s 常量 写成三个名字。把它们叫成一个「看见 after committing 就已经槽位、就已经 final interchangeable、就已经 finmorepre bundled interchangeable」，会把 not slot、not final、not finmorepre bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay after committing before next height not slot / not final / not finmorepre bundled 正式三事（480 余量），先数清问的是 after committing 是不是 already slot / 385 / 593，是不是 set to 0 是不是 already final / 362 / 589，还是 after committing 是不是 already finmorepre bundled / 611 / 612 / 1s constant，再决定要不要同一次发布。
