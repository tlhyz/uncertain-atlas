# 例：看见 FinalizeBlockResponse app_hash may be empty 不是已经没有状态根 / 已经交差；看见 may be hard-coded 不是已经必须真是 Merkle root；看见 MUST be deterministic / only params + previous committed state 不是已经 next_block_delay 非确定就代表整门非确定 / 已经印进本头

**层次**：实现 / FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「may be empty 不是已经没有状态根 / may be hard-coded 不是已经必须真是 Merkle root / MUST be deterministic 不是已经 next_block_delay 非确定就代表整门非确定 / 已经印进本头」，不是 Finalize 回包余量 bundled 三事，不是 FinalizeBlock Usage determinism bundled 三事，也不是 optional Merkle root / next block Header.AppHash / Query anchored 三事。不要另写怎样挑空根、怎样写死常量、怎样测确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.app_hash` may also be empty or hard-coded, but MUST be deterministic — it must not be a function of anything that did not come from the parameters of `FinalizeBlockRequest` and the previous committed state 写成三件独立的实现事，不是「看见回了空根或硬编码就已经没有状态、已经必须真是 Merkle root、已经 next_block_delay 非确定就代表整门非确定」一件事：

1. **看见 `FinalizeBlockResponse.app_hash` may also be empty / 看见可以空 不是已经没有状态根，也不是已经交差 / 已经印进本头。**  
   官方 Usage 写：`FinalizeBlockResponse.app_hash` may also be empty or hard-coded, but MUST be **deterministic**。Response 表也写：`app_hash` is The Merkle root hash of the application state；Deterministic 列是 Yes。看见 may be empty，不是已经没回根就代表没有应用状态。看见回了空根，不是已经本头 `Header.AppHash` 就已经是本高度交差（147）。看见可以空，不是已经 optional Merkle root（475）那种必须真是默克尔根 interchangeable——475 另钉 optional Merkle root / next block Header / Query anchored。
2. **看见 `FinalizeBlockResponse.app_hash` may also be hard-coded / 看见可以硬编码 不是已经必须真是 Merkle root，也不是已经写死就不算 AppHash。**  
   官方写：may also be empty **or hard-coded**, but MUST be deterministic。看见 hard-coded，不是已经必须算出真实 Merkle root 才合法。看见写死常量，不是已经 optional Merkle root contains an (optional) Merkle root hash（475）那种必须真是默克尔根 interchangeable。看见可以硬编码，不是已经 InitChain 回包 app_hash 是起步应用哈希（392）那种已经是本头 AppHash interchangeable。
3. **看见 MUST be deterministic / must not be a function of anything that did not come from the parameters of `FinalizeBlockRequest` and the previous committed state / 看见必须确定 不是已经 next_block_delay 非确定就代表 Finalize 回包整门都可以非确定，也不是已经印进本头。**  
   官方写：MUST be **deterministic** — it must not be a function of anything that did not come from the parameters of `FinalizeBlockRequest` and the previous committed state。看见 MUST be deterministic，不是已经像 `next_block_delay` 那样 Deterministic = No（589）就代表 Finalize 回包整门都可以非确定 interchangeable。看见只依赖请求参数和上一份已提交状态，不是已经 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块（342）那种 Req 11–12 就已经是同一句 interchangeable——342 钉 s_h / T_h 只依赖两份，本页钉 app_hash 空 / 硬编码 / MUST be deterministic 三事。看见必须确定，不是已经印进本头。

怎样挑空根、怎样写死常量、怎样测确定性是规范里的做法，本页不抄。Finalize 回包余量 bundled（404）是 empty / hard-coded + Query proofs + Code==0 那套另一切片，FinalizeBlock Usage determinism bundled（470）是 executes txs deterministically + app_hash MUST be deterministic + implementation MUST be deterministic 那套另一切片，optional Merkle root / next block Header / Query anchored（475）是 contains optional Merkle root / included as Header.AppHash in next block / Query anchored 那套另一切片，next_block_delay 非确定（589）是 wallclock / timeout_commit / set to 0 那套另一切片，本页不抄。

## 官方为什么这样拆

- **may be empty ≠ 已经没有状态根 / 已经交差：** 官方把可以空和没有状态、已经交差分开。
- **may be hard-coded ≠ 必须真是 Merkle root：** 官方把可以硬编码和 optional Merkle root 对象分开。
- **MUST be deterministic / only params + previous committed state ≠ next_block_delay 非确定就代表整门非确定 / 已经印进本头：** 官方把 app_hash 必须确定和 next_block_delay 非确定、本头 AppHash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| may be empty | 不是已经没有状态根 | 不是 Finalize 回包余量 bundled（404） |
| may be hard-coded | 不是必须真是 Merkle root | 不是 optional Merkle root / next block Header（475） |
| MUST be deterministic / only params + previous state | 不是 next_block_delay 非确定就代表整门非确定 | 不是 FinalizeBlock Usage determinism bundled（470） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了空根或硬编码就已经没有状态、已经必须真是 Merkle root、已经 next_block_delay 非确定就代表整门非确定」，必须分开 may be empty 是不是已经没有状态根 / 已经交差、may be hard-coded 是不是必须真是 Merkle root、MUST be deterministic 是不是已经 next_block_delay 非确定就代表整门非确定 / 已经印进本头。可以跳过「看见回了空根就已经没有状态」。不要另写怎样挑空根、怎样写死常量。

## 本页不抄

- 怎样挑空根、怎样写死常量、怎样测确定性。
- Finalize 回包余量 bundled 三事。那是不变量 404。
- FinalizeBlock Usage determinism bundled 三事。那是不变量 470。
- optional Merkle root / next block Header.AppHash / Query anchored。那是不变量 475。
- next_block_delay 非确定。那是不变量 589。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
