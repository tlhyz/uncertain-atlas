# 反模式：把 FinalizeBlockResponse next_block_delay Set to 0 not decided / not block interval / not fndelay bundled 正式三事（589 余量）说成已经决定 / 已经块间隔 / 已经 fndelay bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse next_block_delay Set to 0 not decided ≠ bundled（589）](../../tracks/implementation/worked-example-fndelay-notsetzero-vs-bundled.md)。

## 错在哪里

把 Set to 0 if you want a proposer to make progress as soon as it has all the precommits and the block has been processed by the application 写成已经决定 interchangeable，或已经 finality interchangeable；把 set to 0 写成已经块间隔 interchangeable，或已经槽位 interchangeable，或已经把规范 Set to constant 1s 抄进不确定；把 Set to 0 when all precommits and block processed 写成已经是 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable，或已经 fndelay bundled interchangeable，或已经和 Deterministic = No / each node MAY / wallclock / 480 / 432 / 617 / 618 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay Set to 0 not decided / not block interval / not fndelay bundled 正式三事（589 余量），必须分开 not decided、not block interval、not fndelay bundled 三件事，不要和 589 / 362 / 385 / 613 / 617 / 618 糊成一句。589 fndelay unbundling 在本页 item 3 完成。

## 和相邻反模式

- [fndelay-notslot-sold-as-bundled](fndelay-notslot-sold-as-bundled.md) 是 589 fndelay item 1 Deterministic = No，不是本页 Set to 0 单句边界。
- [fndelay-notwallclock-sold-as-bundled](fndelay-notwallclock-sold-as-bundled.md) 是 589 fndelay item 2 each node MAY / wallclock，不是本页 Set to 0 单句边界。
- [fndelay-sold-as-slot](fndelay-sold-as-slot.md) 是 589 fndelay bundled 三事专用，不是本页 589 item 3 单句边界。
- [finmorepre-notaftercommit-sold-as-bundled](finmorepre-notaftercommit-sold-as-bundled.md) 是 480 finmorepre item 3 after committing not slot，不是本页 589 item 3 Set to 0 单句边界。
