# 例：看见 Application executes txs deterministically before returning control 不是已经可以像 Prepare 那样；看见 app_hash MUST be deterministic / not function of anything outside params and previous state 不是已经印进本头 / 已经 next_block_delay 非确定就代表整门非确定；看见 implementation MUST be deterministic for state machine replication 不是已经是 Req 11–12 那种只依赖两份 / 已经是 finfields bundled

**层次**：实现 / FinalizeBlock Usage determinism 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Application executes txs deterministically before returning control 不是已经可以像 Prepare 那样 / app_hash MUST be deterministic / not function of anything outside params and previous state 不是已经印进本头 / 已经 next_block_delay 非确定就代表整门非确定 / implementation MUST be deterministic for state machine replication 不是已经是 Req 11–12 那种只依赖两份 / 已经是 finfields bundled」，不是 FinalizeBlock 套用候选 bundled 三事，也不是 Finalize 回包 app_hash 可以空或硬编码 bundled 三事，也不是 FinalizeBlockResponse next_block_delay 非确定正式三事。不要另写怎样写 FinalizeBlock、怎样测确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 executes txs deterministically、app_hash MUST be deterministic、implementation MUST be deterministic for state machine replication 写成三件独立的实现事，不是「看见 Usage 写了必须确定就已经可以像 Prepare 那样、已经印进本头、已经 next_block_delay 非确定就代表整门非确定」一件事：

1. **看见 Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT / 看见确定执行 txs 不是已经可以像 Prepare 那样依赖非确定值，也不是已经套用 candidate 就不需要再在 Finalize 执行。**  
   官方 Usage 写：The Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT。Alternatively, it can apply the candidate state corresponding to the same block previously executed via `PrepareProposal` or `ProcessProposal`。看见 executes txs deterministically，不是已经 Prepare 没有确定性要求（338）那种可以像 Prepare 那样 interchangeable。看见 before returning control，不是已经 Finalize + Commit 那种已经交差。看见 Alternatively apply candidate，不是已经 Process 跑过就不用在 Finalize 再执行（460）就已经是同一句 interchangeable——460 另钉套用候选三事，本页只钉 Usage 确定性三事里的 executes txs deterministically。
2. **看见 `FinalizeBlockResponse.app_hash` may also be empty or hard-coded, but MUST be deterministic — it must not be a function of anything that did not come from the parameters of `FinalizeBlockRequest` and the previous committed state / 看见 app_hash 必须确定 不是已经印进本头，也不是已经 next_block_delay 非确定就代表整门非确定。**  
   官方 Usage 写：`FinalizeBlockResponse.app_hash` may also be empty or hard-coded, but MUST be **deterministic** — it must not be a function of anything that did not come from the parameters of `FinalizeBlockRequest` and the previous committed state。Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash。看见 MUST be deterministic，不是已经本头 AppHash 就已经是本高度交差。看见只依赖请求参数和上一份已提交状态，不是已经像 `next_block_delay` 那样 Deterministic = No（589）就代表 Finalize 回包整门都可以非确定。看见 can return proofs，不是已经 Query 证明已经对上 AppHash（404 bundled 另一切片）。
3. **看见 The implementation of `FinalizeBlock` MUST be deterministic, since it is making the Application's state evolve in the context of state machine replication / 看见 implementation MUST be deterministic for state machine replication 不是已经是 Req 11–12 那种 s_h / T_h 只依赖两份，也不是已经是 finfields bundled 里那句 interchangeable。**  
   官方 Usage 写：The implementation of `FinalizeBlock` MUST be deterministic, since it is making the Application's state evolve in the context of state machine replication。看见 MUST be deterministic，不是已经 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块（342）那种 Req 11–12 就已经是同一句 interchangeable——342 来自 app requirements，本页只钉 abci++_methods Usage 这句。看见 state machine replication，不是已经 Process 对任意块同一裁决（340）。看见 making the Application's state evolve，不是已经 finfields bundled 里「Finalize 含刚决定那块的字段 / Info 用来回应用状态信息」（407）就已经是同一句 interchangeable。

怎样写 FinalizeBlock、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。FinalizeBlock 套用候选（460）是 executes txs / apply candidate / 先前 Prepare Process 执行过那套另一切片，Finalize 回包 app_hash 可以空或硬编码 bundled（404）是 app_hash / Query proofs / tx_results Code==0 那套另一切片，FinalizeBlockResponse next_block_delay 非确定（589）是 next_block_delay 非确定 / wallclock / Commit 后再开下一高那套另一切片，FinalizeBlock 确定性 Req 11–12（342）是 s_h / T_h / 状态机复制那套来自 app requirements 的另一切片，Finalize 字段余量 bundled（407）是 finfields / MUST be deterministic / Info 那套另一切片，本页不抄。

## 官方为什么这样拆

- **executes txs deterministically before returning control ≠ 已经可以像 Prepare 那样 / 已经套用 candidate 就不需要再执行：** 官方把 Finalize 执行确定性要求和 Prepare 可以不确定、套用候选另路分开。
- **app_hash MUST be deterministic / only params + previous state ≠ 已经印进本头 / next_block_delay 非确定就代表整门非确定：** 官方把 app_hash 必须确定和 next_block_delay 明确非确定例外分开。
- **implementation MUST be deterministic for state machine replication ≠ 已经是 Req 11–12 / 已经是 finfields bundled：** 官方把 Usage 这句和 app requirements Req 11–12、finfields bundled 分开写。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| executes txs deterministically before returning control | 不是已经可以像 Prepare 那样 | 不是 FinalizeBlock 套用候选（460） |
| app_hash MUST be deterministic / only params + previous state | 不是已经印进本头 | 不是 next_block_delay 非确定（589） |
| implementation MUST be deterministic for state machine replication | 不是已经是 Req 11–12 | 不是 Finalize 字段余量 bundled（407） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Usage 写了必须确定就已经可以像 Prepare 那样、已经印进本头、已经 next_block_delay 非确定就代表整门非确定」，必须分开 executes txs deterministically 是不是已经可以像 Prepare 那样、app_hash MUST be deterministic 是不是已经印进本头 / 已经 next_block_delay 非确定就代表整门非确定、implementation MUST be deterministic for state machine replication 是不是已经是 Req 11–12 / 已经是 finfields bundled。可以跳过「看见 Usage 写了必须确定就已经可以像 Prepare 那样」。不要另写怎样写 FinalizeBlock。

## 本页不抄

- 怎样写 FinalizeBlock、怎样测确定性、怎样写测试向量。
- FinalizeBlock 套用候选。那是不变量 460。
- Finalize 回包 app_hash 可以空或硬编码 bundled。那是不变量 404。
- FinalizeBlockResponse next_block_delay 非确定。那是不变量 589。
- FinalizeBlock 确定性 Req 11–12。那是不变量 342。
- Finalize 字段余量 bundled。那是不变量 407。
- Prepare 没有确定性要求。那是不变量 338。
