# 例：看见 app_hash MUST be deterministic / only params + previous state is not already 印进本头 / not findet bundled（470） interchangeable / not next_block_delay nondet interchangeable

**层次**：实现 / app_hash MUST be deterministic not 印进本头 正式三事（470 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「app_hash MUST be deterministic not 印进本头 / not findet bundled（470） interchangeable / not next_block_delay nondet interchangeable」，不是 FinalizeBlock Usage determinism 正式三事（470），也不是 FinalizeBlockResponse app_hash empty / hard-coded（476）。不要另写怎样测确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.app_hash` MUST be deterministic — it must not be a function of anything that did not come from the parameters of `FinalizeBlockRequest` and the previous committed state 和「已经印进本头 / findet bundled interchangeable / next_block_delay 非确定就代表整门非确定 interchangeable」分开写成三件独立的实现事，不是「看见 app_hash 必须确定 就已经印进本头 interchangeable、已经 next_block_delay 非确定 interchangeable、已经 findet bundled interchangeable」一件事：

1. **看见 `FinalizeBlockResponse.app_hash` may also be empty or hard-coded, but MUST be deterministic / 看见 app_hash MUST be deterministic is not already 印进本头 / 本头 AppHash 交差 interchangeable / 看见 MUST be deterministic is not already FinalizeBlock Usage determinism 正式三事 bundled（470） interchangeable / 已经 findet bundled interchangeable / 已经 executes txs deterministically interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic bundled（476 余量） interchangeable / 已经 may be empty interchangeable / 已经 may be hard-coded interchangeable / 已经 MUST be deterministic interchangeable，也不是已经 FinalizeBlockResponse app_hash Merkle root / next block Header.AppHash bundled（475 余量） interchangeable / 已经 optional Merkle root interchangeable / 已经 included in next block interchangeable / 已经 Query anchored interchangeable，也不是已经本头 AppHash 就已经是本高度交差 bundled（147 余量） interchangeable / 已经印进本头 interchangeable / 已经交差 interchangeable，也不是已经 Finalize 改了就已经落盘 bundled（335 余量） interchangeable / 已经 Code/Data 印进本头 interchangeable / 已经 Finalize + Commit interchangeable。**  
   官方 Usage 写 app_hash MUST be deterministic。Later calls to `Query` can return proofs about the application state anchored in this Merkle root hash。看见 MUST be deterministic，不是已经本头 AppHash 就已经是本高度交差——470 bundled 第二件事常被写成「看见 app_hash 必须确定 就已经印进本头」，本页钉 app_hash not 印进本头 单句。看见 can return proofs，不是已经 optional Merkle root / Query anchored（475 余量） interchangeable——475 钉 Merkle root 对象，本页钉 470 item 2 边界。看见 app_hash，不是已经 empty / hard-coded / MUST be deterministic（476 余量） interchangeable——476 钉 may be empty / may be hard-coded 三事，本页钉 findet app_hash 单句。
2. **看见 app_hash MUST be deterministic is not already only params + previous committed state not next_block_delay nondet interchangeable / 看见必须确定 is not already FinalizeBlockResponse.next_block_delay 非确定正式三事 bundled（469 余量） interchangeable / 已经 wallclock interchangeable / 已经 Commit 后再开下一高 interchangeable / 已经 Deterministic = No interchangeable，也不是已经 FinalizeBlock Usage determinism 正式三事 bundled（470） interchangeable / 已经 findet bundled interchangeable / 已经 implementation MUST be deterministic interchangeable，也不是已经 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块 bundled（342 余量） interchangeable / 已经 Req 11–12 interchangeable / 已经 s_h and T_h interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（407 余量） interchangeable / 已经 state machine replication interchangeable / 已经 executes txs deterministically interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded bundled（476 第三件事 / 476 余量） interchangeable / 已经 next_block_delay 非确定就代表整门非确定 interchangeable / 已经印进本头 interchangeable。**  
   官方把 app_hash MUST be deterministic 和 `next_block_delay` Deterministic = No 分开——470 bundled 常与 469 混成「看见 next_block_delay 非确定 就已经 Finalize 回包整门都可以非确定 interchangeable」，本页钉 app_hash not next_block_delay nondet 单句。看见 only params + previous state，不是已经 Req 11–12（342 余量） interchangeable——342 来自 app requirements，本页钉 Methods Usage app_hash 单句。看见 MUST be deterministic，不是已经 implementation must be deterministic（581 余量） interchangeable——581 钉 item 3 边界，本页钉 item 2 单句。
3. **看见 app_hash MUST be deterministic is not already executes txs deterministically bundled / findet item 1 interchangeable / 看见 app_hash 必须确定 is not already executes txs deterministically not like Prepare bundled（579 余量） interchangeable / 已经 like Prepare interchangeable / 已经 apply candidate interchangeable，也不是已经 executes txs deterministically not already committed bundled（576 余量） interchangeable / 已经交差 interchangeable / 已经 before returning control interchangeable，也不是已经 implementation MUST be deterministic not Req 11–12 bundled（581 余量） interchangeable / 已经 finfields bundled interchangeable / 已经 state machine replication interchangeable，也不是已经 Finalize 回包 app_hash 可以空或硬编码 bundled（404 余量） interchangeable / 已经 Query proofs interchangeable / 已经 Code==0 interchangeable，也不是已经 FinalizeBlock must provide values bundled（477 余量） interchangeable / 已经 Process 跑过就不用再回 tx_results interchangeable / 已经空更新就没有 must provide 义务 interchangeable。**  
   官方把 app_hash MUST be deterministic 和 executes txs deterministically / implementation MUST be deterministic 分开——470 bundled 三事常被写成「看见 Usage 写了必须确定 就已经 findet bundled interchangeable」，本页钉 app_hash not findet item 1/3 单句。看见 app_hash 必须确定，不是已经 executes txs not like Prepare（579 余量） interchangeable——579 钉 executes txs 单句，本页钉 app_hash 边界。看见 MUST be deterministic，不是已经 implementation not Req 11–12（581 余量） interchangeable——581 钉 item 3 边界，本页钉 470 item 2 第三件事。

怎样写 FinalizeBlock、怎样测确定性、怎样挑空根是规范里的做法，本页不抄。executes txs not like Prepare（579 余量）、implementation not Req 11–12（581 余量）、FinalizeBlock Usage determinism 正式三事（470）是另外那套，本页不抄。

## 官方为什么这样拆

- **app_hash MUST be deterministic not 印进本头 ≠ findet bundled interchangeable：** 官方把 app_hash 必须确定和本头 AppHash 交差分开。
- **app_hash not next_block_delay nondet ≠ 469 next_block_delay 非确定 interchangeable：** 官方把 app_hash 必须确定和 next_block_delay 明确非确定例外分开。
- **app_hash not findet item 1/3 ≠ executes txs / implementation bundled interchangeable：** 官方把 app_hash 单句和 findet 其它两件事分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| app_hash MUST be deterministic | 不是 already 印进本头 | 不是本头 AppHash 交差（147） |
| app_hash MUST be deterministic | 不是 already next_block_delay nondet | 不是 next_block_delay 非确定（469） |
| app_hash MUST be deterministic | 不是 already findet item 1/3 | 不是 executes txs not like Prepare（579） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash MUST be deterministic not 印进本头 正式三事（470 余量），必须分开 app_hash 是不是 already 印进本头 interchangeable / 470 findet interchangeable / 475 Merkle root interchangeable、app_hash 是不是 already next_block_delay nondet interchangeable / 469 next_block_delay interchangeable / 342 Req 11–12 interchangeable、app_hash 是不是 already findet item 1/3 interchangeable / 579 executes txs interchangeable / 581 implementation interchangeable。可以跳过「看见 app_hash 必须确定 就已经印进本头 interchangeable」。不要另写怎样测确定性。

## 本页不抄

- 怎样写 FinalizeBlock、怎样测确定性、怎样挑空根。
- executes txs not like Prepare。那是不变量 579（470 item 1 余量）。
- implementation not Req 11–12。那是不变量 581（470 item 3 余量）。
- app_hash empty / hard-coded / MUST be deterministic 三事。那是不变量 476。
- FinalizeBlock Usage determinism 正式三事。那是不变量 470。
