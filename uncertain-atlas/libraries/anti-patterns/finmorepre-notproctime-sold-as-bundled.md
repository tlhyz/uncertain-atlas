# 反模式：把 FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / wallclock 正式三事（480 余量）说成已经 timeout_commit / 已经 wallclock 非确定 / 已经 finmorepre bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse next_block_delay includes processing time not timeout_commit ≠ bundled（480）](../../tracks/implementation/worked-example-finmorepre-notproctime-vs-bundled.md)。

## 错在哪里

把 This includes the time the application and CometBFT take for processing the committed block 写成已经本地 timeout_commit interchangeable，或已经 Previously timeout_commit in CometBFT config interchangeable；把 includes processing time 写成已经 depends on local wallclock / NTP 非确定 interchangeable，或已经 next_block_delay Deterministic = No interchangeable；把 includes processing time 写成已经是 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事 bundled（480） interchangeable，或已经 finmorepre bundled interchangeable，或已经和 more precommits despite 2/3+ / after committing before next height / 589 fndelay / 432 finrespend / 362 +2/3 precommit interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay includes processing time not timeout_commit / wallclock 正式三事（480 余量），必须分开 not timeout_commit、not wallclock 非确定、not finmorepre bundled 三件事，不要和 480 / 589 / 432 / 47 糊成一句。

## 和相邻反模式

- [fndelay-sold-as-slot](../../libraries/anti-patterns/fndelay-sold-as-slot.md) 是 589 next_block_delay 非确定 bundled 专用，不是本页 480 item 1 单句边界。
- [finmorepre-sold-as-timeout](finmorepre-sold-as-timeout.md) 是 480 finmorepre bundled 三事专用，不是本页 includes processing time 单句边界。
