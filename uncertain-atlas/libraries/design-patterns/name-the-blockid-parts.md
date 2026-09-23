# 模式：把 BlockID 两个根说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) BlockID / PartSetHeader。  
**例**：[BlockID.Hash 是头字段的默克尔根 ≠ 已经是整块的根](../../tracks/implementation/worked-example-blockid-vs-roots.md)。

## 三个名字

1. **BlockID.Hash 是头字段的默克尔根不是已经是整块的根：** 官方写明 `MerkleRoot(header)`，长度必须 32。
2. **PartSetHeader 是整块的根不是已经是头：** 官方写明它是 `MerkleRoot(MakeParts(block))`，用于共识期间安全流言。
3. **PartSetHeader.Total 是片数不是已经收到那些片：** 校验要求必须大于 0。

## 为什么要分开叫

官方在 `BlockID` 一节明写它含「**两个不同的默克尔根**」。把它们叫成一个「看见一个根对上就已经是同一块」，会把头字段的根、整块的根和片数一起吞掉，也会把「两块是不是同一块」这个判断降成「某一个根是不是相等」。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见一个根对上就已经是同一块」，先数清问的是 BlockID.Hash 是头字段的默克尔根不是已经是整块的根、PartSetHeader 是整块的根不是已经是头，还是两块的 BlockID 有一个根对上不是已经是同一块，再决定要不要同一次发布。
