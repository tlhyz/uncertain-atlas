# 模式：把 FinalizeBlockResponse next_block_delay Set to 0 not decided / not block interval / not fndelay bundled 正式三事（589 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**例**：[FinalizeBlockResponse next_block_delay Set to 0 not decided ≠ bundled（589）](../../tracks/implementation/worked-example-fndelay-notsetzero-vs-bundled.md)。

## 三个名字

1. **Set to 0 不是已经决定 / finality：** 看见 set to 0 立刻开下一高，不是已经 +2/3 precommit 决定 interchangeable，不是 362 finwhen interchangeable / 610 notdecides interchangeable / 479 fintrigger interchangeable。
2. **Set to 0 不是块间隔 / 槽位：** 看见 set to 0 when all precommits and block processed，不是已经块间隔 interchangeable，不是 385 block interval interchangeable / 613 notaftercommit interchangeable / 593 finh1 interchangeable / 617 notslot interchangeable。
3. **Set to 0 不是 fndelay bundled：** 看见 set to 0，不是已经 fndelay bundled interchangeable，不是 617 notslot interchangeable / 618 notwallclock interchangeable / 589 fndelay item 1 Deterministic = No interchangeable / 589 fndelay item 2 MAY wallclock interchangeable。

## 为什么要分开叫

官方把 Usage 里 Set to 0 when all precommits and block processed、Response 表 Deterministic = No、each node MAY 回不同值 / wallclock 写成三个名字。把它们叫成一个「看见 set to 0 就已经决定 interchangeable、就已经块间隔 interchangeable、就已经 fndelay bundled interchangeable」，会把 not decided、not block interval、not fndelay bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay Set to 0 not decided / not block interval / not fndelay bundled 正式三事（589 余量），先数清问的是 Set to 0 是不是 already 已经决定 / 362 / 610，是不是 already 块间隔 / 385 / 613，还是 Set to 0 是不是 already fndelay bundled / 617 / 618，再决定要不要同一次发布。589 fndelay unbundling 在本页 item 3 完成。
