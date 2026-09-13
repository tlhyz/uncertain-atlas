# 反模式：把 FinalizeBlockResponse next_block_delay 非确定正式三事说成已经 Finalize 必须确定

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[next_block_delay 非确定 ≠ 已经 Finalize 必须确定](../../tracks/implementation/worked-example-fndelay-vs-deterministic.md)。

## 错在哪里

把 `FinalizeBlockResponse.next_block_delay` 标成非确定 / each node MAY provide a different value 写成已经 Finalize 必须确定，或已经像 `app_hash` / `tx_results` 那样 Deterministic = Yes；把 depends on how long processing is taking at the local node / wallclock / NTP 写成已经是本地 `timeout_commit`，或已经是 `ConsensusParams.block` 块间隔；把 Commit 后再开下一高 / set to 0 立刻开下一高 写成已经是槽位，或已经最终，或已经和 432 / 52 / 342 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay 非确定正式三事，必须分开 next_block_delay 非确定、wallclock 依赖、Commit 后再开下一高三件事，不要和 432 / 52 / 342 糊成一句。不要把规范里的 1s 常量抄进不确定。
