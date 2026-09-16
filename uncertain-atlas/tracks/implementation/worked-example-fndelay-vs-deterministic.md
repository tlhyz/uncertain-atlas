# 例：看见 `FinalizeBlockResponse.next_block_delay` is a non-deterministic field / Deterministic = No 不是已经是槽位 / 已经 finality / 已经是本地 timeout_commit；看见 each node MAY provide a different value / depends on local processing / wallclock / NTP 不是已经 app_hash MUST be deterministic / 已经整门非确定；看见 Set to 0 when all precommits and block processed 不是已经决定 / 已经 finality / 已经块间隔

**层次**：实现 / FinalizeBlockResponse next_block_delay 非确定正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage `next_block_delay`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。mempool 只在 CheckTx 弱过滤器那页已有边界时对照，本页不另写 mempool 正文。本页是「next_block_delay Deterministic = No 不是已经是槽位 / finality / timeout_commit、each node MAY 回不同值 / depends on local processing 不是已经 app_hash MUST be deterministic / 整门非确定、Set to 0 when all precommits and block processed 不是已经决定 / finality / 块间隔」，不是 processing time / more precommits / after committing 三事，不是 Finalize 回包末栏 bundled，也不是共识层 ADR 精读。不要另写怎样填 next_block_delay、怎样抄规范 1s。

## 官方三件事

规范把 `FinalizeBlockResponse.next_block_delay` Response 表 **Deterministic = No**、Usage 里 each node MAY 回不同值 / depends on local processing / wallclock、Set to 0 when all precommits and block processed 写成三件独立的实现事，不是「看见回了 next_block_delay 就已经是槽位 / 已经 finality / 已经是 timeout_commit、各节点可以不同就代表整门非确定、set to 0 就已经决定」一件事：

1. **看见 `FinalizeBlockResponse.next_block_delay` is a non-deterministic field / Response 表 Deterministic = No / 看见非确定 不是已经是槽位，也不是已经 finality，也不是已经是本地 `timeout_commit` interchangeable。**  
   官方 Response 表写：`next_block_delay` 列 **Deterministic = No**。Usage 写：`FinalizeBlockResponse.next_block_delay` is a **non-deterministic field**。看见 Deterministic = No，不是已经 post-commit 等待必须标非确定性（52）那种高层不变量 interchangeable——52 是产品门禁，本页钉 Response / Usage 对象边界。看见 non-deterministic field，不是已经 `ConsensusParams.block` 块间隔（385） interchangeable。看见 replaces Previously `timeout_commit`，不是已经 includes processing time / more precommits（480）就已经是同一句 interchangeable。
2. **看见 each node MAY provide a different value / depends on how long processing is taking at the local node / reasonable to use real wallclock time / synchronized clocks (NTP) / 看见各节点可以回不同值 不是已经 app_hash MUST be deterministic，也不是已经 next_block_delay 非确定就代表 Finalize 回包整门非确定。**  
   官方 Usage 写：This means that each node MAY provide a different value, which is supposed to depend on how long processing is taking at the local node。It's reasonable to use real --wallclock-- time and mandate for the nodes to have synchronized clocks (NTP, or other; PBTS also requires this)。看见 MAY 回不同值，不是已经 `app_hash` / `tx_results` / `validator_updates` / `consensus_param_updates` 那些 Deterministic = Yes 列 interchangeable。看见 depends on local processing，不是已经 FinalizeBlock Usage determinism bundled（470）那种 executes txs / app_hash / implementation MUST be deterministic 就代表整门非确定 interchangeable。看见 wallclock / NTP，不是已经 PBTS 槽位（40） interchangeable。
3. **看见 Set to 0 if you want a proposer to make progress as soon as it has all the precommits and the block has been processed by the application / 看见 set to 0 立刻开下一高 不是已经决定 / 已经 finality，也不是已经块间隔 / 槽位。**  
   官方 Usage 写：Set to 0 if you want a proposer to make progress as soon as it has all the precommits and the block has been processed by the application。看见 set to 0，不是已经 +2/3 precommit 决定就已经 finality interchangeable。看见 all precommits and block processed，不是已经 When trigger 2f+1 precommit（479）就已经是同一句 interchangeable——479 钉 When 触发，本页钉 Usage set to 0 语义。看见 progress as soon as，不是已经 ADR 恒定出块间隔 / 槽位那种已经块间隔 interchangeable——共识层 [`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md) 另钉 ADR / 发布线，本页不抄。

怎样填 next_block_delay、怎样从 timeout_commit 迁移、怎样配 NTP 是规范里的做法，本页不抄。processing time / more precommits / after committing（480）是 includes processing time / despite 2/3+ / set to 0 vs 1s 常量那套另一切片，Finalize 回包末栏 bundled（432）是 consensus_param_updates / app_hash / next_block_delay 三栏那套另一切片，FinalizeBlock Usage determinism bundled（470）是 executes txs / app_hash MUST be deterministic / implementation MUST be deterministic 那套另一切片，post-commit 等待必须标非确定性（52）是高层产品门禁那套另一切片，共识层 next_block_delay 精读是 ADR / 不是槽位 / 不是所有发布线都有那套另一切片，本页不抄。

## 官方为什么这样拆

- **next_block_delay Deterministic = No ≠ 已经是槽位 / finality / timeout_commit interchangeable：** 官方把 Response 表非确定列和槽位、最终性、配置项 timeout_commit 分开。
- **each node MAY 回不同值 / wallclock ≠ app_hash MUST be deterministic / 整门非确定：** 官方把 next_block_delay 非确定例外和其它 Deterministic = Yes 列分开。
- **Set to 0 when all precommits and block processed ≠ 已经决定 / finality / 块间隔：** 官方把 set to 0 语义和决定、最终性、块间隔分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| next_block_delay Deterministic = No | 不是已经是槽位 / finality | 不是 post-commit 非确定（52） |
| each node MAY / wallclock / NTP | 不是 app_hash MUST be deterministic | 不是 FinalizeBlock Usage determinism（470） |
| Set to 0 when all precommits and block processed | 不是已经决定 / finality | 不是 processing time / more precommits（480） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 next_block_delay 就已经是槽位 / 已经 finality、各节点可以不同就代表整门非确定、set to 0 就已经决定」，必须分开 next_block_delay Deterministic = No 是不是已经是槽位 / finality / timeout_commit、each node MAY / wallclock 是不是已经 app_hash MUST be deterministic / 整门非确定、Set to 0 when all precommits and block processed 是不是已经决定 / finality / 块间隔。可以跳过「看见非确定就已经是槽位」。不要另写怎样填 next_block_delay。不要把规范 Set to constant 1s 抄进不确定。

## 本页不抄

- 怎样填 next_block_delay、怎样从 timeout_commit 迁移、怎样配 NTP。
- processing time / more precommits / after committing 三事。那是不变量 480。
- Finalize 回包末栏 bundled 三事。那是不变量 432。
- FinalizeBlock Usage determinism bundled 三事。那是不变量 470。
- post-commit 等待必须标非确定性。那是不变量 52。
- 共识层 next_block_delay 精读（ADR / 发布线 / 不是槽位）。那是 [`../consensus/worked-example-next-block-delay.md`](../consensus/worked-example-next-block-delay.md)。
