# 例：看见 FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动不是已经在块 H 生效；看见 FinalizeBlockResponse.app_hash 是应用状态默克尔根不是已经写进下一块头的 AppHash；看见 FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待不是已经是本地 timeout_commit

**层次**：实现 / Finalize 回包末栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动不是已经在块 H 生效 / FinalizeBlockResponse.app_hash 是应用状态默克尔根不是已经写进下一块头的 AppHash / FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待不是已经是本地 timeout_commit」，不是 H 的更新已经在 H+1 计票那种已经在 H+1 换人，也不是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头，也不是 post-commit 等待已经标成非确定性就不能写进 ConsensusParams。不要另写怎样写 Finalize 回包末栏。

## 官方三件事

规范把 FinalizeBlock Response 表上 `consensus_param_updates` 是对 gas、大小和其它共识相关参数的改动、`app_hash` 是应用状态默克尔根、`next_block_delay` 是这块 Commit 后再开下一高的等待写成三件独立的实现事，不是「看见回了 Finalize 回包末栏就已经在块 H 生效、已经写进下一块头、已经是本地 timeout_commit」一件事：

1. **看见 `FinalizeBlockResponse.consensus_param_updates` 是对 gas、大小和其它共识相关参数的改动 / 看见回了 consensus_param_updates 不是已经在块 H 生效，也不是已经是只填一个字段就只改这一项。**  
   官方写：`consensus_param_updates` 是 Changes to gas, size, and other consensus-related parameters。Deterministic 列是 Yes。Usage 也写：块 H 返回的 `consensus_param_updates` 用于块 H+1 的共识参数。空着时，CometBFT 保持当前值。看见回了改动，不是已经在块 H 就用新 MaxBytes / MaxGas 验这块。看见能指 H+1，不是已经高度 H 的 validator_updates 已经在 H+1 计票那种已经在 H+1 换人。看见有 ConsensusParams，不是已经只填 `Block.MaxBytes` 其它 `Block` 字段就保持原值那种只改这一项。
2. **看见 `FinalizeBlockResponse.app_hash` 是应用状态默克尔根 / 看见回了 app_hash 不是已经写进下一块头的 AppHash，也不是已经是本头 AppHash。**  
   官方写：`app_hash` 是 The Merkle root hash of the application state。Deterministic 列是 Yes。Usage 也写：`FinalizeBlockResponse.app_hash` 会作为下一块头的 `Header.AppHash`。可以空或硬编码，但必须确定。看见回了根，不是已经写进下一块头——这块刚 Commit，下一块还没造。看见有默克尔根，不是已经本头 AppHash 就已经是本高度交差那种已经是本头 AppHash。看见必须确定，不是已经 Finalize 回包 events 标成非确定那种只是索引。
3. **看见 `FinalizeBlockResponse.next_block_delay` 是这块 Commit 后再开下一高的等待 / 看见回了 next_block_delay 不是已经是本地 timeout_commit，也不是已经是 ConsensusParams.block 块间隔。**  
   官方写：`next_block_delay` 是 Delay between the time when this block is committed and the next height is started。Deterministic 列是 No。Usage 也写：以前 CometBFT 配置里的 `timeout_commit`；设成 0 可以让提议者一收齐 precommit 且应用处理完就立刻开下一高。这是非确定字段，各节点可以回不同值。看见回了等待，不是已经本地 `timeout_commit` 就已经是全网同一份配置。看见能指 post-commit 等待，不是已经 `ConsensusParams.block` 限制块大小和块间隔那种已经是块间隔。看见标成非确定，不是已经像 `app_hash` 那样必须确定。

怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay 是规范里的做法，本页不抄。只改一个字段就只改这一项是不变量 319，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动 ≠ 已经在块 H 生效：** 官方把 H→H+1 的参数线和块 H 的执行分开。
- **FinalizeBlockResponse.app_hash 是应用状态默克尔根 ≠ 已经写进下一块头的 AppHash：** 官方把下一块头 AppHash 和本头 AppHash、本高度交差分开。
- **FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待 ≠ 已经是本地 timeout_commit：** 官方把应用回的 post-commit 等待和配置里的 timeout_commit、ConsensusParams.block 间隔分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动 | 不是已经在块 H 生效 | 不是只改一个字段就只改这一项（319） |
| FinalizeBlockResponse.app_hash 是应用状态默克尔根 | 不是已经写进下一块头的 AppHash | 不是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头（404） |
| FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待 | 不是已经是本地 timeout_commit | 不是 post-commit 等待已经标成非确定性（52） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 回包末栏就已经在块 H 生效、已经写进下一块头、已经是本地 timeout_commit」，必须分开 FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动是不是已经在块 H 生效、FinalizeBlockResponse.app_hash 是应用状态默克尔根是不是已经写进下一块头的 AppHash、FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待是不是已经是本地 timeout_commit。可以跳过「看见回了 Finalize 回包末栏就已经在块 H 生效」。不要另写怎样写 Finalize 回包末栏。

## 本页不抄

- 怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay。
- 只改一个字段就只改这一项。那是不变量 319。
- Finalize 回包 app_hash 可以空或硬编码就已经印进本头。那是不变量 404。
- post-commit 等待已经标成非确定性。那是不变量 52。
