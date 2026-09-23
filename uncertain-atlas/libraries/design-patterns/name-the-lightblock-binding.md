# 模式：把 LightBlock 绑定三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) LightBlock / SignedHeader。  
**例**：[LightBlock 有 SignedHeader ≠ 已经有头](../../tracks/implementation/worked-example-lightblock-vs-binding.md)。

## 三个名字

1. **LightBlock 有 SignedHeader 不是已经有头：** `SignedHeader` 是头**加上**用来证明它的 `Commit`，两者各自都要合规。
2. **两件都在不是已经是同一高：** `SignedHeader` 与 `ValidatorSet` 都不得为 nil，但「都在」不等于「绑上」。
3. **绑定是 `SignedHeader.ValidatorsHash == ValidatorSet.Hash()` 不是已经非 nil 就够：** 官方明写由集合哈希连接。

## 为什么要分开叫

官方把 `LightBlock` 写成「把验证所需的两个数据结构合起来」，并给出连接条件那**一句哈希相等**。把它们叫成一个「看见两件都在就已经是一份可验对象」，会把头与 `Commit` 的分工、高度归属、以及真正的绑定额一起吞掉 —— 而绑定额正是这份结构存在的理由。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见两件都在就已经是同一高的一份可验对象」，先数清问的是 LightBlock 有 SignedHeader 不是已经有头、两件都在不是已经是同一高，还是绑定的那一句是哈希相等不是已经非 nil 就够，再决定要不要同一次发布。
