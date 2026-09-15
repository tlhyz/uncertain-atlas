# 例：看见 includes processing time for committed block 不是已经是本地 timeout_commit；看见 more precommits despite 2/3+ 不是已经决定 / 已经最终；看见 after committing before next height / set to 0 when processed 不是已经是槽位 / 已经 1s 常量

**层次**：实现 / FinalizeBlockResponse next_block_delay processing time / more precommits 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage `next_block_delay`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「includes processing time 不是已经是 timeout_commit、more precommits despite 2/3+ 不是已经决定 / 已经最终、after committing before next height 不是已经是槽位 / 已经 1s 常量」，不是 next_block_delay 非确定 / wallclock / set to 0 三事，不是 Finalize 回包末栏 bundled 三事，也不是 post-commit 等待已经标成非确定性那种高层不变量。不要另写怎样填 next_block_delay、怎样抄规范 1s。

## 官方三件事

规范把 `FinalizeBlockResponse.next_block_delay` Usage 里 processing time、more precommits、after committing before next height 写成三件独立的实现事，不是「看见回了 next_block_delay 就已经是 timeout_commit、已经有 2/3+ 就不需要再等、已经是槽位 / 已经最终」一件事：

1. **看见 This includes the time the application and CometBFT take for processing the committed block / 看见包含应用和 CometBFT 处理已提交块的时间 不是已经是本地 `timeout_commit` interchangeable，也不是已经是 depends on local wallclock / NTP 那种非确定三事（469）就已经是同一句 interchangeable。**  
   官方 Usage 写：how long CometBFT waits after committing a block, before starting the next height。**This includes the time the application and CometBFT take for processing the committed block**。看见 includes processing time，不是已经 Previously `timeout_commit` in CometBFT config 那种可以整段替换成配置项 interchangeable。看见包含应用处理时间，不是已经 like `next_block_delay` Deterministic = No（469 第 1 件事）就已经是同一句 interchangeable——469 钉非确定 / each node MAY 回不同值，本页钉 delay 语义里的 processing time。
2. **看见 In CometBFT terms, this interval gives the proposer a chance to receive some more precommits, even though it already has the required 2/3+ / 看见给提议者多收 precommit 的机会 不是已经 has required 2/3+ 就已经决定 / 已经最终，也不是已经 When trigger 2f+1 precommit（479）就已经是同一句 interchangeable。**  
   官方写：In CometBFT terms, this interval gives the proposer a chance to receive some more precommits, even though it already has the required 2/3+。看见 more precommits，不是已经 +2/3 precommit 同一 id(v) 才决定再调 Finalize（362）那种已经决定 interchangeable。看见 despite 2/3+，不是已经 has all the precommits 就不需要 delay interchangeable——官方另写 set to 0 when all precommits and block processed，本页钉 more precommits 语义，469 另钉 set to 0 三事。
3. **看见 how long CometBFT waits after committing a block, before starting the next height / Set to 0 if you want progress as soon as it has all the precommits and the block has been processed / 看见 Commit 后再开下一高 / set to 0 立刻开下一高 不是已经是槽位，也不是已经最终，也不是已经把规范 Set to constant 1s 抄进不确定。**  
   官方写：how long CometBFT waits after committing a block, before starting the next height。Set to 0 if you want a proposer to make progress as soon as it has all the precommits and the block has been processed by the application。**Set to constant 1s to preserve the old (v0.34 - v1.0) behavior**。看见 after committing before next height，不是已经 `ConsensusParams.block` 块间隔（385） interchangeable。看见 set to 0，不是已经槽位或已经最终。看见 replaces timeout_commit，不是已经把 1s 示例常量抄进不确定。

怎样填 next_block_delay、怎样配 NTP、怎样从 timeout_commit 迁移是规范里的做法，本页不抄。next_block_delay 非确定 / wallclock / set to 0（469）是 Deterministic = No / depends on local node / set to 0 vs slot 那套另一切片，Finalize 回包末栏 bundled（432）是 consensus_param_updates / app_hash / next_block_delay 三栏那套另一切片，post-commit 等待已经标成非确定性（52）是高层不变量那套另一切片，共识层 next_block_delay 精读（[`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md)）是 ADR / 发布线 / 不是槽位那套另一切片，本页不抄。

## 官方为什么这样拆

- **includes processing time ≠ 已经是 timeout_commit / wallclock 非确定 interchangeable：** 官方把 delay 包含的处理时间和配置项 timeout_commit、非确定 wallclock 分开。
- **more precommits despite 2/3+ ≠ 已经决定 / 已经最终：** 官方把 post-commit 等多收 precommit 的机会和已有 2/3+ 决定、最终性分开。
- **after committing before next height / set to 0 ≠ 已经是槽位 / 已经 1s 常量：** 官方把 Commit 后再开下一高的等待和槽位、最终性、规范示例秒数分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| includes processing time | 不是已经是 timeout_commit | 不是 next_block_delay 非确定（469） |
| more precommits despite 2/3+ | 不是已经决定 / 已经最终 | 不是 When trigger 2f+1（479） |
| after committing / set to 0 | 不是已经是槽位 / 1s 常量 | 不是 post-commit 非确定（52） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 next_block_delay 就已经是 timeout_commit、已经有 2/3+ 就不需要再等、已经是槽位」，必须分开 includes processing time 是不是已经是 timeout_commit、more precommits despite 2/3+ 是不是已经决定 / 已经最终、after committing before next height 是不是已经是槽位 / 已经 1s 常量。可以跳过「已经有 2/3+ 就不需要 delay」。不要另写怎样填 next_block_delay。不要把规范 1s 抄进不确定。

## 本页不抄

- 怎样填 next_block_delay、怎样配 NTP、怎样从 timeout_commit 迁移。
- next_block_delay 非确定 / wallclock / set to 0 三事。那是不变量 469。
- Finalize 回包末栏 bundled 三事。那是不变量 432。
- post-commit 等待已经标成非确定性。那是不变量 52。
- 共识层 next_block_delay 精读（ADR / 发布线 / 不是槽位）。那是 [`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md)。
