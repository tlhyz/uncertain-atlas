# 例：看见应用必须回 app_hash / tx_results / validator_updates / consensus_param_updates 不是已经改了集合；看见 validator_updates 空则引擎保持当前集合不是已经没有集合；看见 consensus_param_updates 空则引擎保持当前参数不是已经清掉参数

**层次**：实现 / FinalizeBlock 空更新保持当前值正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「必须回四列不是已经改了集合 / validator_updates 空则保持当前集合不是已经没有集合 / consensus_param_updates 空则保持当前参数不是已经清掉参数」，不是 Finalize 同步高度 bundled 三事，也不是 InitChain / Finalize 没回 ConsensusParams 那套，也不是 H 的参数更新已经在 H+1 生效。不要另写怎样写空更新。

## 官方三件事

规范把必须回四列、validator_updates 空则保持当前集合、consensus_param_updates 空则保持当前参数写成三件独立的实现事，不是「看见 Finalize 回了空更新就已经没有集合、已经清掉参数、已经改了集合」一件事：

1. **看见应用必须给 `FinalizeBlockResponse.app_hash`、`tx_results`、`validator_updates`、`consensus_param_updates` 提供值 / 看见回了四列 不是已经改了集合，也不是已经交差。**  
   官方写：The Application must provide values for `FinalizeBlockResponse.app_hash`, `FinalizeBlockResponse.tx_results`, `FinalizeBlockResponse.validator_updates`, and `FinalizeBlockResponse.consensus_param_updates` as a result of executing the block。看见必须回四列，不是已经 `validator_updates` 非空那种已经改了集合。看见提供了值，不是已经 Finalize + Commit 那种已经交差。看见有 `validator_updates` 栏，不是已经 H+1 换人（35）就已经生效。
2. **看见 `FinalizeBlockResponse.validator_updates` 可以空 / 看见空着 不是已经没有集合，也不是已经 InitChain 空名单那种没有验证者。**  
   官方写：The values for `FinalizeBlockResponse.validator_updates`, or `FinalizeBlockResponse.consensus_param_updates` may be empty. In this case, CometBFT will keep the current values。看见 validator_updates 空，不是已经没有集合。看见保持当前值，不是已经 power 0 删掉不在集合里的人（318）就已经是同一句 interchangeable。看见没回人，不是已经改了集合。
3. **看见 `FinalizeBlockResponse.consensus_param_updates` 可以空 / 看见空着 不是已经清掉参数，也不是已经只填一个字段就只改这一项。**  
   官方 Usage 同句写：may be empty … CometBFT will keep the current values。看见 consensus_param_updates 空，不是已经 Finalize 没回 ConsensusParams 那种 nil 就什么也不做（319）就已经是同一句 interchangeable。看见保持当前值，不是已经 H 的参数更新已经在 H+1 生效（333）就已经改了。看见空着，不是已经只改 Block.MaxBytes 其余字段保持原值那种已经只改这一项。

怎样写空更新、怎样编 ValidatorUpdate、怎样编 ConsensusParams 是规范里的做法，本页不抄。Finalize 回包义务（363）是必须回四列 / decided_last_commit 定奖惩 / 等价 ABCI 1.0 那套另一切片，Finalize 同步高度（382）是 syncing_to_height / 空更新 / events 非确定 bundled 另一切片，InitChain 空名单（318）和 Finalize 没回 ConsensusParams（319）是创世和 nil 语义另一切片，本页不抄。

## 官方为什么这样拆

- **必须回四列 ≠ 已经改了集合：** 官方把 must provide values 和 validator set 已经更新分开。
- **validator_updates 空则保持当前集合 ≠ 已经没有集合：** 官方把 Finalize 空更新和 InitChain 空名单分开。
- **consensus_param_updates 空则保持当前参数 ≠ 已经清掉参数：** 官方把 keep current values 和 nil 什么也不做 / 只改一项分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须回四列 | 不是已经改了集合 | 不是必须回四列就已经交差（363） |
| validator_updates 空 | 不是已经没有集合 | 不是 InitChain 空名单就已经没有集合（318） |
| consensus_param_updates 空 | 不是已经清掉参数 | 不是 Finalize 没回 ConsensusParams 就什么也不做（319） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 回了空更新就已经没有集合、已经清掉参数、已经改了集合」，必须分开必须回 app_hash / tx_results / validator_updates / consensus_param_updates 是不是已经改了集合、validator_updates 空是不是已经没有集合、consensus_param_updates 空是不是已经清掉参数。可以跳过「看见回了空更新就已经没有集合」。不要另写怎样写空更新。

## 本页不抄

- 怎样写空更新、怎样编 ValidatorUpdate、怎样编 ConsensusParams。
- Finalize 回包义务。那是不变量 363。
- Finalize 同步高度 bundled。那是不变量 382。
- InitChain 空名单 / Finalize 没回 ConsensusParams。那是不变量 318 / 319。
- H 的参数更新已经在 H+1 生效。那是不变量 333 / 35。
