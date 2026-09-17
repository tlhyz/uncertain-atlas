# 反模式：看见 Finalize 等价于 ABCI 1.0 的 BeginBlock / DeliverTx / EndBlock 就当成已经是四门已经结算 / 看见可以用 decided_last_commit 和 misbehavior 定奖惩就当成已经罚没 / 看见必须回 app_hash / tx_results / validator_updates / consensus_param_updates 就当成已经改了集合

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize 等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finalize-equiv-vs-gates.md)。

## 塌法

1. 看见 Finalize 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` / 看见收成一门，就当成已经是四门已经结算，或当成已经交差。
2. 看见可以用 `decided_last_commit` 和 `misbehavior` 定奖惩 / 看见有上一份 commit，就当成已经罚没，或当成已经是本头 LastCommit 就已经是本高 +2/3。
3. 看见必须回 `app_hash` / `tx_results` / `validator_updates` / `consensus_param_updates` / 看见回了四列，就当成已经改了集合，或当成已经交差。

## 为什么会出事

官方写：这个方法等价于 ABCI 1.0 里 `BeginBlock`、`DeliverTx`、`EndBlock` 那一串调用。应用可以用 `decided_last_commit` 和 `misbehavior` 来定验证者的奖惩。执行完这块，必须给 `app_hash`、`tx_results`、`validator_updates`、`consensus_param_updates` 提供值。

## 和相邻反模式

- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种 Finalize 等价于 ABCI 1.0 那三步不是已经是四门已经结算。
- [evidence-equals-slash](evidence-equals-slash.md) 是证据上链就已经罚没，不是本页这种可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空名单就已经没有集合，不是本页这种必须回四列不是已经改了集合。
