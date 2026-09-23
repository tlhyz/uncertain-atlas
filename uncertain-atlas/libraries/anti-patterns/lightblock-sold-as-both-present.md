# 反模式：lightblock-sold-as-both-present

**层次**：实现 / LightBlock 绑定。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) LightBlock / SignedHeader。  
**例**：[LightBlock 有 SignedHeader ≠ 已经有头](../../tracks/implementation/worked-example-lightblock-vs-binding.md)。

## 病症

把「`LightBlock` 里两件都在、都不为 nil」写成已经拿到一份同一高度的可验对象，或把有 `SignedHeader` 写成已经有能验的头（忘了它还要 `Commit`），或把绑定额降成「两边都填了」而漏掉 `SignedHeader.ValidatorsHash == ValidatorSet.Hash()` 那句相等。

## 为什么错

规范把 `LightBlock` 写成「把验证所需的两个数据结构合起来」，并要求两者都不得为 nil 且各自合规；但连接这两者的条件只有**一句哈希相等**：`SignedHeader.ValidatorsHash == ValidatorSet.Hash()`。两件都在、都非 nil，仍可能是两个不同高度的碎片。缺了那句相等，这份结构就没有证明力。

## 正确写法

分开三句：LightBlock 有 SignedHeader 不是已经有头；两件都在不是已经是同一高；绑定的那一句是哈希相等不是已经非 nil 就够。

## 边界

不是 [validatorset-hash-sold-as-whole-set](validatorset-hash-sold-as-whole-set.md)（那是 `ValidatorSet.Hash()` 的覆盖面，不变量 444），不是 [lastcommit-sold-as-this-block](lastcommit-sold-as-this-block.md)（那是本头 `LastCommit` 不是本高已 +2/3，不变量 148），不是 NextValidatorsHash 的 H+1 延迟（不变量 35）。

## 本页不抄

- 怎样构造 `LightBlock`、怎样算集合哈希、怎样切 `Header`/`Commit`。
- 怎样写利用步骤。
