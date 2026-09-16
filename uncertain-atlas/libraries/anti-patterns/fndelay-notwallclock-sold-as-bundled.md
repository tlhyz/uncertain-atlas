# 反模式：把 FinalizeBlockResponse next_block_delay each node MAY / wallclock not app_hash MUST be deterministic / not whole response nondeterministic 正式三事（589 余量）说成已经 app_hash MUST be deterministic / 已经整门非确定 / 已经 fndelay bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse next_block_delay each node MAY / wallclock not app_hash MUST be deterministic ≠ bundled（589）](../../tracks/implementation/worked-example-fndelay-notwallclock-vs-bundled.md)。

## 错在哪里

把 each node MAY provide a different value / depends on local processing / wallclock / NTP 写成已经 app_hash MUST be deterministic interchangeable，或已经和 470 findet / 476 finharddet / 404 finapphash interchangeable；把 MAY / wallclock 写成已经 Finalize 回包整门非确定 interchangeable，或已经 next_block_delay 非确定就代表整门非确定 interchangeable；把 each node MAY / wallclock 写成已经是 FinalizeBlockResponse next_block_delay 非确定正式三事 bundled（589） interchangeable，或已经 fndelay bundled interchangeable，或已经和 Deterministic = No / Set to 0 / 480 / 432 / 617 / 619 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay each node MAY / wallclock not app_hash MUST be deterministic / not whole response nondeterministic 正式三事（589 余量），必须分开 not app_hash MUST be deterministic、not whole response nondeterministic、not fndelay bundled 三件事，不要和 589 / 470 / 476 / 617 / 619 糊成一句。

## 和相邻反模式

- [fndelay-notslot-sold-as-bundled](fndelay-notslot-sold-as-bundled.md) 是 589 fndelay item 1 Deterministic = No，不是本页 each node MAY / wallclock 单句边界。
- [fndelay-sold-as-slot](fndelay-sold-as-slot.md) 是 589 fndelay bundled 三事专用，不是本页 589 item 2 单句边界。
- [finharddet-sold-as-noroot](finharddet-sold-as-noroot.md) 是 app_hash MUST be deterministic（476），不是本页 next_block_delay MAY / wallclock 单句边界。
