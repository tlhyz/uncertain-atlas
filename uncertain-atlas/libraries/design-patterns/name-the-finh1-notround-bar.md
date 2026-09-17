# 模式：把 FinalizeBlock When round 0 not same round / not next_block_delay / not timeout_commit / not finh1 bundled 正式三事（593 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 11。  
**例**：[FinalizeBlock When round 0 not same round ≠ bundled（593）](../../tracks/implementation/worked-example-finh1-notround-vs-bundled.md)。

## 三个名字

1. **round 0 不是继续同一 round：** 看见 round 0 / starts consensus for height h+1, round 0，不是已经继续同一 round _r_ interchangeable，不是 302 same height round change interchangeable / 35 round change interchangeable / 640 finunlock-notcommitlock interchangeable / 634 notrecheck interchangeable。
2. **round 0 不是 next_block_delay 槽位：** 看见 round 0，不是已经 `FinalizeBlockResponse.next_block_delay` 槽位 interchangeable，不是 589 fndelay interchangeable / 617 notslot interchangeable / 385 block interval interchangeable / 613 notaftercommit interchangeable / 619 notsetzero interchangeable。
3. **round 0 不是 timeout_commit / finh1 bundled：** 看见 round 0，不是已经 processing time / more precommits / `timeout_commit` interchangeable，不是 480 finmorepre interchangeable / 611 notproctime interchangeable / 612 notmorepre interchangeable / 47 timeout_commit interchangeable / 641 finh1-notsettled interchangeable / 643 finh1-notafterunlock interchangeable。

## 为什么要分开叫

官方把 When 第 11 步 round 0、同高换轮 / next_block_delay / timeout_commit、593 finh1 bundled 三事 写成三个名字。把它们叫成一个「看见 round 0 就已经继续同一 round interchangeable、就已经 next_block_delay interchangeable、就已经 timeout_commit interchangeable」，会把 not same round、not next_block_delay、not timeout_commit / not finh1 bundled / not 641 / not 643 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When round 0 not same round / not next_block_delay / not timeout_commit / not finh1 bundled 正式三事（593 余量），先数清问的是 round 0 是不是 already same round / 302 / 640 / 634，是不是 already next_block_delay / 589 / 617 / 385 / 613，还是 round 0 是不是 already timeout_commit / 480 / 611 / 612 / 641 / 643，再决定要不要同一次发布。593 finh1 unbundling 在本页 item 2 续。
