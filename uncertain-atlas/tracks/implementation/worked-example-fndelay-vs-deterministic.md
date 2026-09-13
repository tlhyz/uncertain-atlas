# 例：看见 FinalizeBlockResponse.next_block_delay 标成非确定 / each node MAY 回不同值 不是已经 Finalize 必须确定；看见 depends on local wallclock processing / NTP 不是已经是本地 timeout_commit；看见 Commit 后再开下一高 / set to 0 立刻开下一高 不是已经是槽位 / 已经最终

**层次**：实现 / FinalizeBlockResponse next_block_delay 非确定正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.next_block_delay 标成非确定 / each node MAY 回不同值 不是已经 Finalize 必须确定 / FinalizeBlockResponse.next_block_delay 依赖本机处理耗时 / wallclock / NTP 不是已经是本地 timeout_commit / ConsensusParams.block 块间隔 / FinalizeBlockResponse.next_block_delay 是 Commit 后再开下一高的等待 / set to 0 立刻开下一高 不是已经是槽位 / 已经最终」，不是 Finalize 回包末栏 bundled 三事，也不是 post-commit 等待已经标成非确定性那种高层不变量，也不是 Finalize 算出的状态必须只依赖上一份状态和决定块那种必须确定。不要另写怎样填 next_block_delay、怎样配 NTP、怎样抄规范里的 1s 常量。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.next_block_delay` 的非确定语义、本机 wallclock 依赖、Commit 后再开下一高的等待写成三件独立的实现事，不是「看见回了 next_block_delay 就已经必须确定、已经是本地 timeout_commit、已经是槽位 / 已经最终」一件事：

1. **看见 `FinalizeBlockResponse.next_block_delay` 标成非确定 / each node MAY provide a different value / 看见各节点可以回不同值 不是已经 Finalize 必须确定，也不是已经像 `app_hash` / `tx_results` 那样 Deterministic = Yes。**  
   官方 Response 表写：`next_block_delay` 的 Deterministic 列是 No。Usage 也写：`FinalizeBlockResponse.next_block_delay` is a non-deterministic field。This means that each node MAY provide a different value。看见标成非确定，不是已经 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块（342）那种必须确定 interchangeable。看见 MAY 回不同值，不是已经像 `app_hash` 那样必须确定。看见是 Finalize 回包字段，不是已经 Process 必须只依赖请求和上一份状态（340）就已经是同一句 interchangeable。
2. **看见 depends on how long processing is taking at the local node / reasonable to use real wallclock time / NTP / 看见依赖本机处理耗时 不是已经是本地 `timeout_commit`，也不是已经是 `ConsensusParams.block` 块间隔。**  
   官方 Usage 写：which is supposed to depend on how long processing is taking at the local node。It's reasonable to use real --wallclock-- time and mandate for the nodes to have synchronized clocks (NTP, or other; PBTS also requires this) for the variable delay to work properly。看见 wallclock / NTP，不是已经本地配置里的 `timeout_commit` interchangeable。看见本机处理耗时，不是已经 Finalize 回包末栏 bundled 里「是这块 Commit 后再开下一高的等待不是已经是本地 timeout_commit」（432）就已经是同一句 interchangeable——本页只钉 Usage 非确定三事，不 bundled consensus_param_updates / app_hash。看见可变延迟，不是已经 `ConsensusParams.block` 限制块大小和块间隔（385）那种已经是块间隔。
3. **看见 Commit 后再开下一高 / how long CometBFT waits after committing a block, before starting the next height / set to 0 if you want a proposer to make progress as soon as it has all the precommits / 看见 set to 0 立刻开下一高 不是已经是槽位，也不是已经最终，也不是已经把规范里的 1s 常量抄进不确定。**  
   官方 Usage 写：how long CometBFT waits after committing a block, before starting the next height。This includes the time the application and CometBFT take for processing the committed block。In CometBFT terms, this interval gives the proposer a chance to receive some more precommits, even though it already has the required 2/3+。Set to 0 if you want a proposer to make progress as soon as it has all the precommits and the block has been processed by the application。Previously `timeout_commit` in CometBFT config。**Set to constant 1s to preserve the old (v0.34 - v1.0) behavior**。看见 Commit 后再等，不是已经 post-commit 等待已经标成非确定性（52）那种高层不变量 interchangeable——52 不拆 wallclock / timeout_commit / set to 0 三事。看见能填 0，不是已经槽位或已经最终。看见 replaces timeout_commit，不是已经把规范示例秒数抄进不确定。

怎样填 next_block_delay、怎样配 NTP、怎样从 timeout_commit 迁移是规范里的做法，本页不抄。Finalize 回包末栏 bundled（432）是 consensus_param_updates / app_hash / next_block_delay 三栏那套另一切片，post-commit 等待已经标成非确定性（52）是高层不变量那套另一切片，FinalizeBlock 确定性（342）是 s_h / T_h 必须确定那套另一切片，共识层 next_block_delay 精读（[`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md)）是 ADR / 发布线 / 不是槽位那套另一切片，本页不抄。

## 官方为什么这样拆

- **next_block_delay 非确定 / each node MAY 回不同值 ≠ 已经 Finalize 必须确定 / 已经像 app_hash 那样必须确定：** 官方把唯一明确的非确定 Finalize 回包字段和 Requirement 11–12 那种必须确定分开。
- **depends on local wallclock / NTP ≠ 已经是本地 timeout_commit / ConsensusParams.block 块间隔：** 官方把应用回的可变等待和配置里的 timeout_commit、共识参数块间隔分开。
- **Commit 后再开下一高 / set to 0 立刻开下一高 ≠ 已经是槽位 / 已经最终：** 官方把 post-commit 等待和槽位、最终性、规范示例 1s 常量分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| next_block_delay 非确定 / each node MAY 回不同值 | 不是已经 Finalize 必须确定 | 不是 Finalize 算出的状态必须只依赖上一份状态和决定块（342） |
| depends on local wallclock / NTP | 不是已经是本地 timeout_commit | 不是 Finalize 回包末栏 bundled（432） |
| Commit 后再开下一高 / set to 0 | 不是已经是槽位 / 已经最终 | 不是 post-commit 等待已经标成非确定性（52） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 next_block_delay 就已经必须确定、已经是本地 timeout_commit、已经是槽位 / 已经最终」，必须分开 next_block_delay 标成非确定 / each node MAY 回不同值是不是已经 Finalize 必须确定、depends on local wallclock / NTP是不是已经是本地 timeout_commit / ConsensusParams.block 块间隔、Commit 后再开下一高 / set to 0是不是已经是槽位 / 已经最终。可以跳过「看见回了 next_block_delay 就已经必须确定」。不要另写怎样填 next_block_delay。不要把规范里的 1s 常量抄进不确定。

## 本页不抄

- 怎样填 next_block_delay、怎样配 NTP、怎样从 timeout_commit 迁移。
- Finalize 回包末栏 bundled 三事。那是不变量 432。
- post-commit 等待已经标成非确定性。那是不变量 52。
- FinalizeBlock 算出的状态必须只依赖上一份状态和决定块。那是不变量 342。
- 共识层 next_block_delay 精读（ADR / 发布线 / 不是槽位）。那是 [`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md)。
