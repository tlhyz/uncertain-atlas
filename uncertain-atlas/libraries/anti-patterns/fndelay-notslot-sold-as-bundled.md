# 反模式：把 FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量）说成已经是槽位 / 已经 finality / 已经 fndelay bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse next_block_delay Deterministic = No not slot ≠ bundled（589）](../../tracks/implementation/worked-example-fndelay-notslot-vs-bundled.md)。

## 错在哪里

把 `FinalizeBlockResponse.next_block_delay` Deterministic = No / non-deterministic field 写成已经是槽位 interchangeable，或已经 ConsensusParams.block 块间隔 interchangeable；把 Deterministic = No 写成已经 finality interchangeable，或已经 +2/3 precommit 决定 interchangeable；把 Deterministic = No 写成已经是 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable，或已经 fndelay bundled interchangeable，或已经和 each node MAY / wallclock / Set to 0 / 480 / 432 / 470 / 52 / 385 / 618 / 619 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay Deterministic = No not slot / not finality / not timeout_commit 正式三事（589 余量），必须分开 not slot、not finality、not fndelay bundled 三件事，不要和 589 / 385 / 480 / 618 / 619 糊成一句。

## 和相邻反模式

- [fndelay-sold-as-slot](fndelay-sold-as-slot.md) 是 589 fndelay bundled 三事专用，不是本页 589 item 1 Deterministic = No 单句边界。
- [finmorepre-notaftercommit-sold-as-bundled](finmorepre-notaftercommit-sold-as-bundled.md) 是 480 finmorepre item 3 after committing not slot，不是本页 589 item 1 Deterministic = No 单句边界。
