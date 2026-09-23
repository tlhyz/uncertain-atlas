# 反模式：partindex-sold-as-whole

**层次**：实现 / 片下标。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) Part。  
**例**：[Part.index 是这片的下标 ≠ 已经有整叠](../../tracks/implementation/worked-example-partindex-vs-whole.md)。

## 病症

把 `Part.index` 在位写成已经有整叠、已经齐，或把校验 `Must be >= 0` 写成已经有序、已经落在总片数范围内，或照抄 `Part` 表的校验栏与说明栏（「Must be of length 32」「MerkleRoot of a serialized block」）当成 `bytes` / `proof` 的规则。

## 为什么错

官方给 `Part` 的定义是「块的一片」，`index` 的校验只有 `Must be >= 0` —— 一条**下限**，既不是范围上界也不是顺序保证。而 `Part` 表的校验栏与说明栏本身有复制粘贴错位：`bytes`（bytes 类型）与 `proof`（`[Proof]` **结构**类型）都被写成「Must be of length 32 / MerkleRoot of a serialized block」——那两条语义按下文属于 `PartSetHeader`。「32 字节」对 `Proof` 结构根本不成立。

## 正确写法

分开三句：Part.index 是这片的下标不是已经有整叠；写成 ≥ 0 不是已经有序；Part 表的校验栏不是已经是本对象的校验。实现以下文 `PartSetHeader` 的定义为准，不照抄该表。

## 边界

不是 [part-index-sold-as-proof-index](part-index-sold-as-proof-index.md)（那是外层下标必须与证明下标同一对象，不变量 59），不是带内部长度的结构必须先验再传（不变量 60），不是部分下载对象必须一次终结（不变量 37），不是 `PartSetHeader` 是整块的根（不变量 442）。

## 本页不抄

- 怎样切片、怎样算片根、怎样流言。
- 怎样写利用步骤。
