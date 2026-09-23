# 反模式：blockid-sold-as-one-root

**层次**：实现 / BlockID 双根。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) BlockID / PartSetHeader。  
**例**：[BlockID.Hash 是头字段的默克尔根 ≠ 已经是整块的根](../../tracks/implementation/worked-example-blockid-vs-roots.md)。

## 病症

把 `BlockID.Hash` 当成整块的根，或把 `PartSetHeader` 当成头哈希，或写成两块的 `BlockID` 只要有一个根对上就已经是同一块、已经是同一种承诺。

## 为什么错

规范在 `BlockID` 一节明写它含**两个不同的默克尔根**：`Hash` 是头里全部字段的根（`MerkleRoot(header)`），`PartSetHeader` 是完整序列化块切片后的根（`MerkleRoot(MakeParts(block))`），并带片数 `Total`。它们覆盖的对象不同。判断两块是不是同一块，要看这两个根，不是看其中一个。

## 正确写法

分开三句：BlockID.Hash 是头字段的默克尔根不是已经是整块的根；PartSetHeader 是整块的根不是已经是头；两块的 BlockID 有一个根对上不是已经是同一块。

## 边界

不是 [two-votes-sold-as-slash](two-votes-sold-as-slash.md)（那是同一对上不同 `BlockID` 就已经构成双签证据，不变量 21），不是 [part-index-sold-as-proof-index](part-index-sold-as-proof-index.md)（那是 `Part.Index` 与 `Proof.Index` 必须同一对象，不变量 59）。

## 本页不抄

- 怎样算 `BlockID`、怎样切片、怎样流言。
- 怎样写利用步骤。
