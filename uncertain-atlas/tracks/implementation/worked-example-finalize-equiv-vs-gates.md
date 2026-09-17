# 例：看见 Finalize 等价于 ABCI 1.0 的 BeginBlock / DeliverTx / EndBlock 不是已经是四门已经结算；看见可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没；看见必须回 app_hash / tx_results / validator_updates / consensus_param_updates 不是已经改了集合

**层次**：实现 / Finalize 回包义务。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Finalize 等价于 ABCI 1.0 的 BeginBlock / DeliverTx / EndBlock 不是已经是四门已经结算 / 可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没 / 必须回四列不是已经改了集合」，不是四门已经结算，也不是证据上链就已经罚没。不要另写怎样写 Finalize 回包。

## 官方三件事

规范把 Finalize 收成 ABCI 1.0 那三步、`decided_last_commit` 和 `misbehavior` 可用来定奖惩、执行完必须回四列写成三件独立的实现事，不是「看见收成一门就已经是四门已经结算、已经罚没、已经改了集合」一件事：

1. **看见 Finalize 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门 不是已经是四门已经结算，也不是已经交差。**  
   官方写：这个方法等价于 ABCI 1.0 里 `BeginBlock`、`DeliverTx`、`EndBlock` 那一串调用。看见收成一门，不是已经是 CheckTx / Prepare / Process / Finalize 四门齐了。看见等价，不是已经交差。看见旧三步在，不是已经没有 Prepare / Process。
2. **看见可以用 `decided_last_commit` 和 `misbehavior` 定奖惩 / 看见有上一份 commit 不是已经罚没，也不是已经是本头 LastCommit 就已经是本高 +2/3。**  
   官方写：应用可以用 `FinalizeBlockRequest.decided_last_commit` 和 `FinalizeBlockRequest.misbehavior` 来定验证者的奖惩。看见有这两列，不是已经罚没。看见有上一份 commit，不是已经是本头 LastCommit。看见能定奖惩，不是已经交差。
3. **看见必须回 `app_hash` / `tx_results` / `validator_updates` / `consensus_param_updates` / 看见回了四列 不是已经改了集合，也不是已经交差。**  
   官方写：执行完这块，应用必须给 `FinalizeBlockResponse.app_hash`、`tx_results`、`validator_updates`、`consensus_param_updates` 提供值。看见回了四列，不是已经改了集合。看见有 `validator_updates`，不是已经交差。看见必须回，不是已经印进本头。

怎样写 Finalize 回包、怎样算奖惩、怎样填四列是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **Finalize 等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算：** 官方把收成一门和四门齐了分开。
- **可以用 decided_last_commit 和 misbehavior 定奖惩 ≠ 已经罚没：** 官方把能定奖惩和已经罚没分开。
- **必须回四列 ≠ 已经改了集合：** 官方把必须回和已经改完分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 等价于 ABCI 1.0 那三步 | 不是已经是四门已经结算 | 不是四门已经结算（33） |
| 可以用 decided_last_commit 和 misbehavior 定奖惩 | 不是已经罚没 | 不是证据上链就已经罚没（21） |
| 必须回四列 | 不是已经改了集合 | 不是 InitChain 空名单就已经没有集合（318） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收成一门就已经是四门已经结算、已经罚没、已经改了集合」，必须分开 Finalize 等价于 ABCI 1.0 那三步是不是已经是四门已经结算、可以用 decided_last_commit 和 misbehavior 定奖惩是不是已经罚没、必须回四列是不是已经改了集合。可以跳过「看见收成一门就已经是四门已经结算」。不要另写怎样写 Finalize 回包。

## 本页不抄

- 怎样写 Finalize 回包、怎样算奖惩、怎样填四列。
- 四门已经结算。那是不变量 33。
- 证据上链就已经罚没。那是不变量 21。
- InitChain 空名单就已经没有集合。那是不变量 318。
