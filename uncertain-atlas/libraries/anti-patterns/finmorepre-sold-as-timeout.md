# 反模式：把 FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事卖成已经是 timeout_commit / 已经有 2/3+ 就不需要 delay

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[includes processing time ≠ 已经是 timeout_commit](../../tracks/implementation/worked-example-finmorepre-vs-timeout.md)。

## 卖法

- 「看见 includes processing time 就已经是本地 timeout_commit / 配置项 interchangeable。」
- 「看见已经有 required 2/3+ precommit，就不需要 next_block_delay / 已经决定 / 已经最终。」
- 「看见 after committing before next height 就已经是槽位 / 已经最终 / 已经把规范 1s 抄进不确定。」

## 为什么错

官方把 includes processing time、more precommits despite 2/3+、after committing before next height 写成三件独立的实现事。把它们卖成已经是 timeout_commit、已经有 2/3+ 就不需要 delay、已经是槽位，会把 processing time、more precommits、Commit 后再等 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_block_delay Usage 里的 processing time / more precommits / after committing，必须分开 includes processing time、more precommits despite 2/3+、after committing before next height 三个名字，不要把它们卖成已经是 timeout_commit / 已经有 2/3+ 就不需要 delay。

## 和相邻反模式

- [fndelay-sold-as-slot](../../libraries/anti-patterns/fndelay-sold-as-slot.md) 是把 delay 卖成槽位 / 已经最终，不是本页 processing time 三事。
- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，不是本页 more precommits despite 2/3+。
- [finrespend-sold-as-params](../../libraries/anti-patterns/finrespend-sold-as-params.md) 是 consensus_param_updates，不是本页 next_block_delay processing time。
