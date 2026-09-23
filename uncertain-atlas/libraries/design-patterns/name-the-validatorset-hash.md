# 模式：把集合哈希覆盖面三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) ValidatorSet。  
**例**：[ValidatorSet.Hash() 是叶子根 ≠ 已经是整套集合](../../tracks/implementation/worked-example-validatorset-hash-vs-whole-set.md)。

## 三个名字

1. **ValidatorSet.Hash() 是 SimpleValidator 叶子的默克尔根不是已经是整套集合：** 看见根对上不是已经覆盖每个字段。
2. **叶子只编码 pub_key 与 voting_power 不是已经是完整验证者：** 看见权与钥不是已经含地址。
3. **不含地址与提议者优先不是已经不需要交叉核对：** 看见对上不是已经含日程。

## 为什么要分开叫

官方明写 `ValidatorSet.Hash()` 的叶子只是 `pub_key` 与 `voting_power` 的编码，**地址与提议者优先不在里面**。把三者叫成一个「看见集合哈希对上就已经是同一套验证者」，会把根的覆盖面、叶子内容、以及那个缺口一起吞掉 —— 而那个缺口正是不变量 56 那条状态同步事故的设计根源。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见集合哈希对上就已经是同一套验证者」，先数清问的是 ValidatorSet.Hash() 是叶子根不是已经是整套集合、叶子只编码 pub_key 与 voting_power 不是已经是完整验证者，还是不含地址与提议者优先不是已经不需要交叉核对，再决定要不要同一次发布。
