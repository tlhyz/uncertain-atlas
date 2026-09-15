# 模式：把 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[optional Merkle root ≠ 已经是本头 AppHash](../../tracks/implementation/worked-example-finmerkle-vs-nextheader.md)。

## 三个名字

1. **optional Merkle root 不是已经是本头 AppHash：** 看见 Merkle root 不是已经印进本头 / 已经交差 interchangeable。
2. **included as Header.AppHash in the next block 不是已经写进下一块头：** 看见会写进下一块头不是已经本头 AppHash 就已经是本高度交差 interchangeable。
3. **Query proofs anchored in this Merkle root 不是已经对上 AppHash：** 看见 Query 可以拿这份根当锚不是已经是 ProofOp 按键查 interchangeable。

## 为什么要分开叫

官方把 optional Merkle root、next block Header.AppHash、Query proofs anchored 写成三个名字。把它们叫成一个「看见回了 app_hash 就已经是本头 AppHash、已经写进下一块头、Query 已经对上 AppHash」，会把 Merkle root 对象、下一块头写入时机和 Query 证明锚三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「FinalizeBlockResponse.app_hash」，先数清问的是 optional Merkle root 是不是已经是本头 AppHash / 已经印进本头、included as Header.AppHash in the next block 是不是已经写进下一块头，还是 Query proofs anchored 是不是已经对上 AppHash / 已经是按键查，再决定要不要同一次发布。
