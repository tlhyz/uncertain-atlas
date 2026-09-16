# 模式：把 FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage `next_block_delay`。  
**例**：[FinalizeBlockResponse next_block_delay Deterministic = No not slot ≠ bundled（589）](../../tracks/implementation/worked-example-fndelay-notslot-vs-bundled.md)。

## 三个名字

1. **next_block_delay Deterministic = No 不是槽位：** 看见 non-deterministic field 不是已经槽位 interchangeable，不是 385 block interval interchangeable / 593 finh1 slot interchangeable / 52 post-commit nondet interchangeable。
2. **next_block_delay Deterministic = No 不是 finality：** 看见 Deterministic = No 不是已经 finality interchangeable，不是 362 finwhen interchangeable / 362 +2/3 precommit interchangeable / 610 notdecides interchangeable / 619 notsetzero interchangeable。
3. **next_block_delay Deterministic = No 不是 fndelay bundled：** 看见 Deterministic = No 不是已经 fndelay bundled interchangeable，不是 618 notwallclock interchangeable / 619 notsetzero interchangeable / 589 fndelay item 2 MAY wallclock interchangeable / 589 fndelay item 3 set to 0 interchangeable。

## 为什么要分开叫

官方把 Response 表 **Deterministic = No**、Usage 里 each node MAY 回不同值 / wallclock、Set to 0 when all precommits and block processed 写成三个名字。把它们叫成一个「看见 Deterministic = No 就已经槽位 interchangeable、就已经 finality interchangeable、就已经 timeout_commit interchangeable」，会把 not slot、not finality、not fndelay bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量），先数清问的是 Deterministic = No 是不是 already 槽位 / 385 / 593，是不是 already finality / 362 / 619，还是 Deterministic = No 是不是 already fndelay bundled / 618 / 619 / 611，再决定要不要同一次发布。
