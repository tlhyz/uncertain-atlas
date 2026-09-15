# 例：看见 FinalizeBlockResponse app_hash optional Merkle root 不是已经是本头 AppHash / 已经印进本头；看见 included as Header.AppHash in the next block 不是已经写进下一块头；看见 Query proofs anchored in this Merkle root 不是已经对上 AppHash / 已经是按键查

**层次**：实现 / FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「optional Merkle root 不是已经是本头 AppHash / included as Header.AppHash in the next block 不是已经写进下一块头 / Query proofs anchored 不是已经对上 AppHash / 已经是按键查」，不是 Finalize 回包 app_hash 可以空或硬编码 bundled 三事，也不是 Finalize 回包末栏 bundled 三事，也不是本头 AppHash 就已经是本高度交差。不要另写怎样算 Merkle root、怎样回 Query 证明。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.app_hash` optional Merkle root、写进下一块头 `Header.AppHash`、以后 Query 可以拿这份根当锚回证明写成三件独立的实现事，不是「看见回了 app_hash 就已经是本头 AppHash、已经写进下一块头、Query 已经对上 AppHash」一件事：

1. **看见 `FinalizeBlockResponse.app_hash` contains an (optional) Merkle root hash of the application state / 看见 optional Merkle root 不是已经是本头 AppHash，也不是已经印进本头 / 已经交差。**  
   官方 Usage 写：`FinalizeBlockResponse.app_hash` contains an (optional) Merkle root hash of the application state。Response 表也写：`app_hash` is The Merkle root hash of the application state。Deterministic 列是 Yes。看见 optional Merkle root，不是已经本头 `Header.AppHash` 就已经是本高度交差（147）。看见回了根，不是已经印进**本**头。看见 optional，不是已经 may also be empty or hard-coded, but MUST be deterministic（404 / 470）那种空根 / 硬编码 / 必须确定 interchangeable——本页钉 Merkle root 对象，404 / 470 另钉 empty / hard-coded / MUST be deterministic。
2. **看见 `FinalizeBlockResponse.app_hash` is included as the `Header.AppHash` in the next block / 看见会写进下一块头 不是已经写进下一块头，也不是已经本头 AppHash 就已经是本高度交差。**  
   官方 Usage 写：`FinalizeBlockResponse.app_hash` is included as the `Header.AppHash` in the **next** block。When 第 4 步也写：Application calculates and returns the _AppHash_（467）。看见 included in the next block，不是已经写进下一块头——这块刚 Commit，下一块还没造。看见会进下一块头，不是已经本头 AppHash 就已经是本高度交差（147）。看见 next block Header.AppHash，不是已经 FinalizeBlockResponse.app_hash 是应用状态默克尔根 bundled（432）就已经是同一句 interchangeable——432 另钉 Response 表描述 + 末栏 bundled。
3. **看见 Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash / 看见 Query 可以拿这份根当锚 不是已经对上 AppHash，也不是已经是 ProofOp 那种按键查。**  
   官方 Usage 写：Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash。看见能回证明，不是已经对上这一高 AppHash。看见 anchored in this Merkle root，不是已经 Query 可以按键查那种已经是 `ProofOp` 路径（325）。看见能查，不是已经 Finalize 回包 app_hash 可以空或硬-coded bundled（404）里那句 Query 就已经是同一句 interchangeable——404 另钉 empty / hard-coded / Code==0 bundled。

怎样算 Merkle root、怎样写进下一块头、怎样回 Query 证明是规范里的做法，本页不抄。本头 AppHash 就已经是本高度交差（147）是 Header.AppHash 锚上一高度 Finalize 那套另一切片，Finalize 回包 app_hash 可以空或硬编码（404）是 empty / hard-coded / Code==0 bundled 另一切片，Finalize 回包末栏 bundled（432）是 consensus_param_updates / app_hash / next_block_delay 那套另一切片，FinalizeBlock When AppHash tx outputs ResultHash persist（467）是 calculates and returns / ResultHash / persist 那套另一切片，ProofOp.type 就已经是按键查（325）是 Query 证明路径另一切片，本页不抄。

## 官方为什么这样拆

- **optional Merkle root ≠ 已经是本头 AppHash / 已经印进本头：** 官方把 Merkle root 对象和本头 AppHash、本高度交差分开。
- **included as Header.AppHash in the next block ≠ 已经写进下一块头：** 官方把会写进下一块头和已经写进下一块头、本头 AppHash 分开。
- **Query proofs anchored in this Merkle root ≠ 已经对上 AppHash / 已经是按键查：** 官方把 anchored 证明和已经对上 AppHash、ProofOp 按键查分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| optional Merkle root | 不是已经是本头 AppHash | 不是 Finalize 回包 app_hash 可以空或硬编码（404） |
| included as Header.AppHash in the next block | 不是已经写进下一块头 | 不是本头 AppHash 就已经是本高度交差（147） |
| Query proofs anchored in this Merkle root | 不是已经对上 AppHash | 不是 ProofOp.type 就已经是按键查（325） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 app_hash 就已经是本头 AppHash、已经写进下一块头、Query 已经对上 AppHash」，必须分开 optional Merkle root 是不是已经是本头 AppHash / 已经印进本头、included as Header.AppHash in the next block 是不是已经写进下一块头、Query proofs anchored 是不是已经对上 AppHash / 已经是按键查。可以跳过「看见回了 app_hash 就已经是本头 AppHash」。不要另写怎样算 Merkle root、怎样回 Query 证明。

## 本页不抄

- 怎样算 Merkle root、怎样写进下一块头、怎样回 Query 证明。
- Finalize 回包 app_hash 可以空或硬编码 bundled 三事。那是不变量 404。
- Finalize 回包末栏 bundled 三事。那是不变量 432。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- FinalizeBlock When AppHash tx outputs ResultHash persist。那是不变量 467。
- ProofOp.type 就已经是按键查。那是不变量 325。
- FinalizeBlock Usage determinism bundled 三事。那是不变量 470。
