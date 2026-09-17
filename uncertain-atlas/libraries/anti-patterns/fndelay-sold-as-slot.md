# 反模式：把 FinalizeBlockResponse next_block_delay 非确定正式三事说成已经是槽位 / finality

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[next_block_delay Deterministic = No ≠ 已经是槽位](../../tracks/implementation/worked-example-fndelay-vs-deterministic.md)。

## 错在哪里

把 `FinalizeBlockResponse.next_block_delay` Deterministic = No / non-deterministic field 写成已经是槽位，或已经 finality，或已经是本地 `timeout_commit` interchangeable；把 each node MAY provide a different value / depends on local processing / wallclock / NTP 写成已经 app_hash MUST be deterministic，或已经 next_block_delay 非确定就代表 Finalize 回包整门非确定；把 Set to 0 when all precommits and block processed 写成已经决定 / 已经 finality，或已经块间隔 / 槽位，或已经和 480 / 432 / 470 / 52 / 385 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay 非确定正式三事，必须分开 next_block_delay Deterministic = No、each node MAY / wallclock、Set to 0 when all precommits and block processed 三件事，不要和 480 / 432 / 470 / 52 / 385 糊成一句。
