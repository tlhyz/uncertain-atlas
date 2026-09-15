# 反模式：把 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事卖成已经印进本头

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[optional Merkle root ≠ 已经是本头 AppHash](../../tracks/implementation/worked-example-finmerkle-vs-nextheader.md)。

## 卖法

- 「看见 Finalize 回了 app_hash 就已经是本头 AppHash / 已经印进本头。」
- 「看见 Usage 写了 included as Header.AppHash in the next block 就已经写进下一块头。」
- 「看见 Query 可以拿这份根当锚，就已经对上 AppHash / 已经是按键查。」

## 为什么错

官方把 optional Merkle root、included as Header.AppHash in the next block、Query proofs anchored in this Merkle root hash 写成三件独立的实现事。把它们卖成已经印进本头、已经写进下一块头、Query 已经对上 AppHash，会把 Merkle root 对象、下一块头写入时机和 Query 证明锚三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回的 app_hash，必须分开 optional Merkle root、included as Header.AppHash in the next block、Query proofs anchored 三个名字，不要把它们卖成已经印进本头。

## 和相邻反模式

- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头，不是本页这种 optional Merkle root / next block Header.AppHash / Query anchored 三事。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页这种 included as Header.AppHash in the next block 不是已经写进下一块头。
- [proofop-sold-as-key](proofop-sold-as-key.md) 是 ProofOp.type 就已经是按键查，不是本页这种 Query proofs anchored 不是已经对上 AppHash。
