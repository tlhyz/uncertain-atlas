# 模式：把 FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / wallclock 正式三事（480 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**例**：[FinalizeBlockResponse next_block_delay includes processing time not timeout_commit ≠ bundled（480）](../../tracks/implementation/worked-example-finmorepre-notproctime-vs-bundled.md)。

## 三个名字

1. **includes processing time 不是 timeout_commit：** 看见 This includes the time the application and CometBFT take for processing the committed block 不是已经 Previously timeout_commit in CometBFT config interchangeable，不是 47 timeout_commit interchangeable / 432 finrespend interchangeable / 385 block interval interchangeable。
2. **includes processing time 不是 wallclock 非确定：** 看见 includes processing time 不是已经 depends on local wallclock / NTP 非确定 interchangeable，不是 589 fndelay interchangeable / 589 Deterministic = No interchangeable / 470 findet interchangeable / 476 finharddet interchangeable。
3. **includes processing time 不是 finmorepre bundled：** 看见 includes processing time 不是已经 finmorepre bundled interchangeable，不是 480 item 2 more precommits interchangeable / 480 item 3 after committing interchangeable / 362 +2/3 precommit interchangeable / 479 fintrigger interchangeable。

## 为什么要分开叫

官方把 includes processing time、more precommits despite 2/3+、after committing before next height 和 timeout_commit、wallclock 非确定、槽位 / 1s 常量 写成三个名字。把它们叫成一个「看见 includes processing time 就已经 timeout_commit、就已经 wallclock 非确定 interchangeable、就已经 finmorepre bundled interchangeable」，会把 not timeout_commit、not wallclock 非确定、not finmorepre bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / wallclock 正式三事（480 余量），先数清问的是 includes processing time 是不是 already timeout_commit / 47 / 432，是不是 already wallclock 非确定 / 589 / 470，还是 includes processing time 是不是 already finmorepre bundled / 480 item 2 / 480 item 3，再决定要不要同一次发布。
