# 模式：把 Finalize 回包义务三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize 等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finalize-equiv-vs-gates.md)。

## 三个名字

1. **Finalize 等价于 ABCI 1.0 那三步不是已经是四门已经结算：** 看见收成一门不是已经交差。
2. **可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没：** 看见有上一份 commit 不是已经是本头 LastCommit。
3. **必须回四列不是已经改了集合：** 看见回了 validator_updates 不是已经交差。

## 为什么要分开叫

官方把 Finalize 收成 ABCI 1.0 那三步、`decided_last_commit` 和 `misbehavior` 可用来定奖惩、执行完必须回四列写成三件事。把它们叫成一个「看见收成一门就已经是四门已经结算」，会把四门、证据上链和集合更新一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收成一门就已经是四门已经结算」，先数清问的是 Finalize 等价于 ABCI 1.0 那三步不是已经是四门已经结算、可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没，还是必须回四列不是已经改了集合，再决定要不要同一次发布。
