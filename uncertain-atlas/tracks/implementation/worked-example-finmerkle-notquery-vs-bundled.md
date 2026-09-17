# 例：看见 Later calls to `Query` can return proofs anchored in this Merkle root / 看见 Query 可以拿这份根当锚 is not already 已经对上 AppHash interchangeable / 这一高 AppHash interchangeable / 已经能查 interchangeable；不是已经 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable / 已经 finmerkle bundled interchangeable

**层次**：实现 / FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量）/ not 625 notquery interchangeable / not 325 proofop interchangeable / not 404 finapphash interchangeable / not 371 queryheight interchangeable / not 623 notthisheader interchangeable / not 624 notnextheader interchangeable」，不是 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475），也不是 optional Merkle root not this header AppHash（475 item 1 余量 / 623），也不是 included as Header.AppHash in the next block not already written（475 item 2 余量 / 624）。不要另写怎样算 Merkle root、怎样写进下一块头、怎样回 Query 证明。

## 官方三件事

规范把 FinalizeBlock Usage 里 Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash 和「已经是已经对上 AppHash interchangeable / 已经是 ProofOp 按键查 interchangeable / 已经是 finmerkle bundled interchangeable」分开写成三件独立的实现事，不是「看见 Query 可以拿这份根当锚 就已经对上 AppHash、就已经是按键查、就已经 finmerkle bundled interchangeable」一件事：

1. **看见 Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash / 看见 Query 可以拿这份根当锚 / Query proofs anchored is not already 已经对上 AppHash interchangeable / 这一高 AppHash interchangeable / 147 apphash vs this block interchangeable / 371 queryheight interchangeable / 404 finapphash interchangeable，也不是已经 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable / 625 notquery interchangeable / 475 finmerkle interchangeable / 623 notthisheader interchangeable / 624 notnextheader interchangeable / 432 finrespend interchangeable，也不是已经 optional Merkle root not this header AppHash bundled（475 item 1 余量 / 623） interchangeable / 623 notthisheader interchangeable / 404 finapphash interchangeable / 392 initchain apphash interchangeable / 476 finharddet interchangeable，也不是已经 included as Header.AppHash in the next block not already written bundled（475 item 2 余量 / 624） interchangeable / 624 notnextheader interchangeable / 147 apphash vs this block interchangeable / 614 notheader interchangeable / 432 finrespend interchangeable，也不是已经 Finalize 回包 app_hash 可以空或硬编码 bundled（404 余量） interchangeable / 404 finapphash interchangeable / 404 item 2 Query proofs interchangeable / 404 item 1 empty hardcoded interchangeable / 404 item 3 Code==0 interchangeable。**  
   官方 Usage 写：Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash。看见 Query proofs anchored，不是已经对上这一高 AppHash interchangeable——475 bundled 第三件事常被写成「看见 Query 可以拿这份根当锚 就已经对上 AppHash interchangeable」，本页从 475 item 3 侧钉 not matched AppHash 单句。看见能回证明，不是已经 Query 可以按键查那种已经是 `ProofOp` 路径（325） interchangeable——325 另钉 ProofOp.type 按键查，本页钉 anchored 单句。看见 anchored in this Merkle root，不是已经 Finalize 回包余量 bundled（404）里那句 Query 就已经是同一句 interchangeable——404 另钉 empty / hard-coded + Query proofs + Code==0 bundled，本页钉 Query anchored 单句。
2. **看见 Query proofs anchored in this Merkle root / 看见 Query 可以拿这份根当锚 is not already ProofOp 按键查 interchangeable / 已经是按键查 interchangeable / 325 proofop interchangeable / 371 queryheight interchangeable / 325 proofop type interchangeable，也不是已经 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable / 625 notquery interchangeable / 475 finmerkle interchangeable / 325 proofop interchangeable / 371 queryheight interchangeable / 487 queryusage interchangeable，也不是已经 Query 可以对当前或过去高度查 bundled（371 余量） interchangeable / 371 queryheight interchangeable / 325 proofop interchangeable / 404 finapphash item 2 Query proofs interchangeable / 147 apphash vs this block interchangeable，也不是已经 ProofOp.type 就已经是按键查 bundled（325 余量） interchangeable / 325 proofop interchangeable / 371 queryheight interchangeable / 404 finapphash interchangeable / 487 queryusage interchangeable，也不是已经 optional Merkle root not this header AppHash bundled（623 余量） interchangeable / 623 notthisheader interchangeable / 404 finapphash interchangeable / 475 finmerkle item 1 interchangeable / 392 initchain apphash interchangeable。**  
   官方把 Query proofs anchored 和 ProofOp 按键查 / Query height 分开——475 item 3 常与 325 混成「看见 Query 可以拿这份根当锚 就已经是按键查 interchangeable」，本页钉 not ProofOp key lookup 单句。看见 anchored in this Merkle root，不是已经 ProofOp.type 就已经是按键查（325） interchangeable——325 钉 ProofOp 路径对象，本页钉 475 item 3 第二件事。看见能查，不是已经 Query 可以对当前或过去高度查（371） interchangeable——371 另钉 height 默认 0 / committed state，本页钉 not ProofOp key lookup 单句。
3. **看见 Query proofs anchored in this Merkle root / 看见 Query 可以拿这份根当锚 is not already finmerkle bundled（475） interchangeable / 已经 optional Merkle root interchangeable / 已经 included as Header.AppHash in the next block interchangeable / 475 finmerkle item 1 interchangeable / 475 finmerkle item 2 interchangeable / 623 notthisheader interchangeable / 624 notnextheader interchangeable，也不是已经 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475） interchangeable / 625 notquery interchangeable / 623 notthisheader interchangeable / 624 notnextheader interchangeable / 404 finapphash interchangeable / 432 finrespend interchangeable，也不是已经 optional Merkle root not this header AppHash bundled（475 item 1 余量 / 623） interchangeable / 623 notthisheader interchangeable / 404 finapphash interchangeable / 475 finmerkle item 1 interchangeable / 392 initchain apphash interchangeable，也不是已经 included as Header.AppHash in the next block not already written bundled（475 item 2 余量 / 624） interchangeable / 624 notnextheader interchangeable / 147 apphash vs this block interchangeable / 432 finrespend interchangeable / 614 notheader interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476 余量） interchangeable / 620 notempty interchangeable / 621 nothardcoded interchangeable / 622 notnondet interchangeable。**  
   官方把 475 finmerkle bundled 三事里的 Query proofs anchored 和 optional Merkle root / included in next block 分开——475 bundled 常与 item 1 / item 2 混成「看见 Query 可以拿这份根当锚 就已经 finmerkle bundled interchangeable」，本页钉 475 item 3 第三件事。看见 Query anchored，不是已经 optional Merkle root（475 item 1 余量 / 623） interchangeable——623 另钉 not this header AppHash / not settled，本页钉 item 3 单句。看见 proofs anchored，不是已经 included as Header.AppHash in the next block（475 item 2 余量 / 624） interchangeable——624 另钉 not already written / not this header AppHash，本页钉 not finmerkle bundled 单句。

怎样算 Merkle root、怎样写进下一块头、怎样回 Query 证明是规范里的做法，本页不抄。FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled（475）、optional Merkle root not this header AppHash（475 item 1 余量 / 623）、included as Header.AppHash in the next block not already written（475 item 2 余量 / 624）、Finalize 回包余量 bundled（404）、ProofOp.type 就已经是按键查（325）、Query 可以对当前或过去高度查（371）是另外那套，本页不抄。

## 官方为什么这样拆

- **Query proofs anchored not matched AppHash ≠ 404 finapphash / 147 apphash vs this block interchangeable：** 官方把 anchored 证明和已经对上 AppHash / Finalize 回包余量 Query 分开。
- **Query proofs anchored not ProofOp key lookup ≠ 325 proofop / 371 queryheight interchangeable：** 官方把 475 item 3 和 ProofOp 路径 / Query height 分开。
- **Query proofs anchored not finmerkle bundled ≠ 623 notthisheader / 624 notnextheader interchangeable：** 官方把 475 item 3 和 item 1 / item 2 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query proofs anchored | 不是 already 对上 AppHash | 不是 finapphash bundled（404） |
| Query proofs anchored | 不是 already ProofOp 按键查 | 不是 proofop bundled（325） |
| Query proofs anchored | 不是 already finmerkle bundled | 不是 optional Merkle root（475 item 1 / 623） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse Query proofs anchored in this Merkle root not matched AppHash / not ProofOp key lookup / not finmerkle bundled 正式三事（475 余量），必须分开 Query proofs anchored 是不是 already 对上 AppHash interchangeable / 404 finapphash interchangeable / 147 apphash vs this block interchangeable / 371 queryheight interchangeable、Query proofs anchored 是不是 already ProofOp 按键查 interchangeable / 325 proofop interchangeable / 487 queryusage interchangeable、Query proofs anchored 是不是 already finmerkle bundled interchangeable / 623 notthisheader interchangeable / 624 notnextheader interchangeable / 432 finrespend interchangeable。可以跳过「看见 Query 可以拿这份根当锚 就已经对上 AppHash interchangeable」。不要另写怎样回 Query 证明。

## 本页不抄

- 怎样算 Merkle root、怎样写进下一块头、怎样回 Query 证明。
- FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash / Query proofs anchored 正式三事 bundled。那是不变量 475。
- optional Merkle root not this header AppHash。那是不变量 475 item 1 余量 / 623。
- included as Header.AppHash in the next block not already written。那是不变量 475 item 2 余量 / 624。
- Finalize 回包余量 bundled。那是不变量 404。
- ProofOp.type 就已经是按键查。那是不变量 325。
- Query 可以对当前或过去高度查。那是不变量 371。
- 本头 AppHash vs 本高度交差。那是不变量 147。
