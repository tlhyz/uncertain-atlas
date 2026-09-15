# 例：看见 must provide app_hash / tx_results / validator_updates / consensus_param_updates 不是已经改了集合 / 已经交差；看见 as a result of executing the block 不是已经 Process / Prepare candidate 就不需要再在 Finalize 执行；看见提供了值 不是已经 apply candidate 就不需要回 tx_results / 已经空更新就没有义务

**层次**：实现 / FinalizeBlock must provide values as a result of executing the block 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「must provide 四列不是已经改了集合 / as a result of executing the block 不是已经 candidate 就不需要执行 / 提供了值不是已经空更新就没有义务」，不是 FinalizeBlock 空更新保持当前值 bundled 三事，不是 Finalize 套用候选 bundled 三事，也不是 Finalize 回包义务 bundled 三事。不要另写怎样编回包四列。

## 官方三件事

规范把 The Application must provide values for `FinalizeBlockResponse.app_hash`, `FinalizeBlockResponse.tx_results`, `FinalizeBlockResponse.validator_updates`, and `FinalizeBlockResponse.consensus_param_updates` **as a result of executing the block** 写成三件独立的实现事，不是「看见 must provide 就已经改了集合、已经 Process 跑过就不用再执行、已经空着就没有义务」一件事：

1. **看见 must provide values for app_hash / tx_results / validator_updates / consensus_param_updates / 看见必须回四列 不是已经改了集合，也不是已经 Finalize + Commit 那种已经交差。**  
   官方 Usage 写：The Application must provide values for `FinalizeBlockResponse.app_hash`, `FinalizeBlockResponse.tx_results`, `FinalizeBlockResponse.validator_updates`, and `FinalizeBlockResponse.consensus_param_updates` as a result of executing the block。看见 must provide，不是已经 `validator_updates` 非空那种已经改了集合 interchangeable。看见回了四列，不是已经 H+1 换人（459）就已经生效。看见提供了值，不是已经 Finalize + Commit 那种已经交差——本页钉 must provide 义务，458 另钉 empty keep current。
2. **看见 as a result of executing the block / 看见是执行这块的结果 不是已经 Process / Prepare candidate 就不需要再在 Finalize 执行，也不是已经 apply candidate state 就不需要执行 txs。**  
   官方把 as a result of executing the block 和 Alternatively apply candidate state（460）配成：must provide 的值来自执行这块，或来自套用同一块先前 Prepare / Process 跑出的 candidate——但 apply candidate 不是已经不用再提供 tx_results / app_hash interchangeable。看见 as a result of executing，不是已经 Process 回了 Accept（347）就已经是同一句 interchangeable。看见 executing the block，不是已经 Application executes block _v_ When 第 3 步（466）就已经是同一句 interchangeable——466 钉 When executes block v，本页钉 Usage must provide as a result of executing。
3. **看见提供了值 / 看见 tx_results 等来自执行结果 不是已经空更新就没有 must provide 义务，也不是已经 CheckTx 过了就不需要 Finalize 再回 tx_results。**  
   官方写 must provide values，和 The values for validator_updates or consensus_param_updates may be empty … CometBFT will keep the current values 是两句——空更新是 keep current values，不是没有 must provide 义务。看见提供了 tx_results，不是已经 CheckTx 弱过滤器（339）那种过了池门就已经验完 interchangeable。看见 must provide tx_results，不是已经 Code == 0 only if fully valid（464）那种只钉 Code 语义 interchangeable——464 另钉 Code==0 完全合法三事。

怎样编回包四列、怎样在 Finalize 套用 candidate、怎样写空更新是规范里的做法，本页不抄。FinalizeBlock 空更新保持当前值（458）是 must provide + validator_updates 空 + consensus_param_updates 空 keep current 那套另一切片，Finalize 套用候选（460）是 execute txs / apply candidate / previously executed 那套另一切片，Finalize 回包义务 bundled（363）是 can use decided_last_commit 定奖惩 / 必须回四列 / 等价 ABCI 1.0 那套另一切片，FinalizeBlock When Application executes block v（466）是 executes block v / persist decision / apply candidate 那套另一切片，本页不抄。

## 官方为什么这样拆

- **must provide 四列 ≠ 已经改了集合 / 已经交差：** 官方把 must provide 义务和 validator set 已经更新、Finalize + Commit 交差分开。
- **as a result of executing the block ≠ 已经 Process / Prepare candidate 就不需要再执行：** 官方把 must provide 来自执行这块和 apply candidate 另路分开。
- **提供了值 ≠ 已经空更新就没有义务 / 已经 CheckTx 过了：** 官方把 must provide tx_results 和 empty keep current、CheckTx 弱过滤器分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| must provide 四列 | 不是已经改了集合 | 不是 FinalizeBlock 空更新 keep current（458） |
| as a result of executing the block | 不是已经 candidate 就不需要执行 | 不是 Finalize 套用候选（460） |
| 提供了 tx_results 等 | 不是已经 CheckTx 过了 | 不是 tx_results Code==0 完全合法（464） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 must provide 就已经改了集合、已经 Process 跑过就不用再执行、已经空着就没有义务」，必须分开 must provide 四列是不是已经改了集合、as a result of executing the block 是不是已经 candidate 就不需要执行、提供了值是不是已经空更新就没有义务 / 已经 CheckTx 过了。可以跳过「看见 must provide 就已经改了集合」。不要另写怎样编回包四列。

## 本页不抄

- 怎样编回包四列、怎样在 Finalize 套用 candidate、怎样写空更新。
- FinalizeBlock 空更新保持当前值。那是不变量 458。
- Finalize 套用候选。那是不变量 460。
- Finalize 回包义务 bundled。那是不变量 363。
- FinalizeBlock When Application executes block v。那是不变量 466。
- FinalizeBlock tx_results Code==0 完全合法。那是不变量 464。
