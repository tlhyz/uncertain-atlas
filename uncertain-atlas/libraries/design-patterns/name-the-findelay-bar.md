# 模式：把 FinalizeBlockResponse next_block_delay 非确定正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[next_block_delay 非确定 ≠ 已经 Finalize 必须确定](../../tracks/implementation/worked-example-fndelay-vs-deterministic.md)。

## 三个名字

1. **next_block_delay 非确定 / each node MAY 回不同值 不是已经 Finalize 必须确定：** 看见 Deterministic = No 不是已经像 app_hash 那样必须确定。
2. **depends on local wallclock / NTP 不是已经是本地 timeout_commit：** 看见本机处理耗时不是已经配置里的 timeout_commit interchangeable。
3. **Commit 后再开下一高 / set to 0 不是已经是槽位 / 已经最终：** 看见 post-commit 等待不是已经槽位或已经最终。

## 为什么要分开叫

官方把 next_block_delay 的非确定语义、wallclock 依赖、Commit 后再开下一高写成三个名字。把它们叫成一个「看见回了 next_block_delay 就已经必须确定、已经是 timeout_commit、已经是槽位」，会把非确定例外、配置迁移和最终性三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 next_block_delay 就已经必须确定」，先数清问的是 next_block_delay 是不是已经 Finalize 必须确定、depends on wallclock 是不是已经是 timeout_commit，还是 Commit 后再开下一高是不是已经是槽位 / 已经最终，再决定要不要同一次发布。
