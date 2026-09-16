# 例：看见 `FinalizeBlockResponse.app_hash` may also be hard-coded / 看见可以硬编码 is not already 必须真是 Merkle root interchangeable / 写死就不算 AppHash interchangeable / 已经交差 interchangeable；不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476） interchangeable / 已经 finharddet bundled interchangeable

**层次**：实现 / FinalizeBlockResponse app_hash may be hard-coded not Merkle root / not settled / not finharddet bundled 正式三事（476 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse app_hash may be hard-coded not Merkle root / not settled / not finharddet bundled 正式三事（476 余量）/ not 621 nothardcoded interchangeable / not 475 finmerkle interchangeable / not 404 finapphash interchangeable / not 147 apphash vs this block interchangeable / not 620 notempty interchangeable / not 622 notnondet interchangeable」，不是 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476），也不是 optional Merkle root bundled（475），也不是 Finalize 回包余量 bundled（404）。不要另写怎样挑空根、怎样写死常量、怎样测确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 `FinalizeBlockResponse.app_hash` may also be hard-coded 和「已经是必须真是 Merkle root interchangeable / 已经是已经交差 interchangeable / 已经是 finharddet bundled interchangeable」分开写成三件独立的实现事，不是「看见 may be hard-coded 就已经必须真是 Merkle root、就已经交差、就已经 finharddet bundled interchangeable」一件事：

1. **看见 `FinalizeBlockResponse.app_hash` may also be hard-coded / 看见可以硬编码 is not already 必须真是 Merkle root interchangeable / Response 表 Merkle root hash of application state interchangeable / optional Merkle root contains optional Merkle root hash interchangeable / 475 finmerkle interchangeable / 392 initchain apphash interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476） interchangeable / 621 nothardcoded interchangeable / 476 finharddet interchangeable / 404 finapphash interchangeable / 470 findet not apphash interchangeable，也不是已经 FinalizeBlockResponse app_hash optional Merkle root bundled（475 余量） interchangeable / 475 finmerkle interchangeable / 404 finapphash interchangeable / 614 notheader interchangeable / 432 finrespend interchangeable，也不是已经 Finalize 回包 app_hash 可以空或硬编码 bundled（404 余量） interchangeable / 404 finapphash interchangeable / 404 item 1 empty hardcoded interchangeable / 404 item 2 Query proofs interchangeable / 404 item 3 Code==0 interchangeable，也不是已经 InitChain 回包 app_hash 是起步应用哈希 bundled（392 余量） interchangeable / 392 initchain apphash interchangeable / 147 apphash vs this block interchangeable / 335 finpersist interchangeable。**  
   官方 Usage 写：`FinalizeBlockResponse.app_hash` may also be empty **or hard-coded**, but MUST be **deterministic**。Response 表也写：`app_hash` is The Merkle root hash of the application state；Deterministic 列是 Yes。看见 may be hard-coded，不是已经必须算出真实 Merkle root 才合法 interchangeable——476 bundled 第二件事常被写成「看见 may be hard-coded 就已经必须真是 Merkle root interchangeable」，本页从 476 item 2 侧钉 not Merkle root 单句。看见可以硬编码，不是已经 optional Merkle root contains optional Merkle root hash（475） interchangeable——475 另钉 optional Merkle root / next block Header / Query anchored，本页钉 476 item 2 第二件事。看见 hard-coded，不是已经 Finalize 回包余量 bundled（404） interchangeable——404 钉 empty / hard-coded + Query proofs + Code==0，本页钉 may be hard-coded 单句。
2. **看见 `FinalizeBlockResponse.app_hash` may also be hard-coded / 看见可以硬编码 is not already 已经交差 interchangeable / 已经印进本头 interchangeable / 147 apphash vs this block interchangeable / 33 four gates interchangeable / 601 notsettled interchangeable / 362 finwhen interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476） interchangeable / 621 nothardcoded interchangeable / 476 finharddet interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable，也不是已经 本头 AppHash ≠ 本高度交易已经交差 bundled（147 余量） interchangeable / 147 apphash vs this block interchangeable / 614 notheader interchangeable / 404 finapphash interchangeable / 475 finmerkle interchangeable，也不是已经 Application calculates and returns AppHash not printed in this header bundled（614 余量） interchangeable / 614 notheader interchangeable / 587 finreturn item 1 interchangeable / 470 findet not apphash interchangeable / 581 findet not replication interchangeable，也不是已经 FinalizeBlock When persist decision not 已经交差 bundled（605 余量） interchangeable / 605 notpersist interchangeable / 478 finpersist interchangeable / 616 notpersist interchangeable / 606 notoutputs interchangeable。**  
   官方把 may be hard-coded 和已经交差 / 印进本头分开——476 item 2 常与 147 混成「看见 may be hard-coded 就已经交差 interchangeable」，本页钉 not settled 单句。看见可以硬编码，不是已经本头 AppHash 就代表本高度交易已经交差（147） interchangeable——147 钉本头 AppHash vs 本高度交差，本页钉 476 item 2 第二件事。看见 hard-coded，不是已经 Application returns AppHash 印进本头（614） interchangeable——614 另钉 not printed in this header / not this header AppHash，本页钉 not settled 单句。
3. **看见 `FinalizeBlockResponse.app_hash` may also be hard-coded / 看见可以硬编码 is not already finharddet bundled（476） interchangeable / 已经 may be empty interchangeable / 已经 MUST be deterministic interchangeable / 476 finharddet item 1 interchangeable / 476 finharddet item 3 interchangeable / 620 notempty interchangeable / 622 notnondet interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476） interchangeable / 621 nothardcoded interchangeable / 620 notempty interchangeable / 622 notnondet interchangeable / 404 finapphash interchangeable / 470 findet interchangeable，也不是已经 `FinalizeBlockResponse.app_hash` may also be empty not no state root bundled（476 item 1 余量 / 620） interchangeable / 620 notempty interchangeable / 404 finapphash interchangeable / 475 finmerkle interchangeable / 392 initchain apphash interchangeable，也不是已经 MUST be deterministic not next_block_delay nondet bundled（476 item 3 余量 / 622） interchangeable / 622 notnondet interchangeable / 589 fndelay interchangeable / 618 notwallclock interchangeable / 470 findet not apphash interchangeable / 580 findet not apphash interchangeable，也不是已经 FinalizeBlock Usage determinism bundled（470 余量） interchangeable / 470 findet interchangeable / 579 findet notlikeprepare interchangeable / 581 findet not replication interchangeable。**  
   官方把 476 finharddet bundled 三事里的 may be hard-coded 和 may be empty / MUST be deterministic 分开——476 bundled 常与 item 1 / item 3 混成「看见 may be hard-coded 就已经 finharddet bundled interchangeable」，本页钉 476 item 2 第三件事。看见 hard-coded，不是已经 may be empty（476 item 1 余量 / 620） interchangeable——620 另钉 not no state root / not settled / not finharddet bundled，本页钉 item 2 单句。看见 can be hard-coded，不是已经 MUST be deterministic（476 item 3 余量 / 622） interchangeable——622 另钉 not next_block_delay nondet / not 印进本头，本页钉 not finharddet bundled 单句。

怎样挑空根、怎样写死常量、怎样测确定性是规范里的做法，本页不抄。FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled（476）、may be empty not no state root（476 item 1 余量 / 620）、MUST be deterministic not next_block_delay nondet（476 item 3 余量 / 622）、Finalize 回包余量 bundled（404）、optional Merkle root bundled（475）、FinalizeBlock Usage determinism bundled（470）、next_block_delay 非确定（589）是另外那套，本页不抄。

## 官方为什么这样拆

- **may be hard-coded not Merkle root ≠ 475 finmerkle / 404 finapphash interchangeable：** 官方把可以硬编码和 optional Merkle root / Response 表 Merkle root 分开。
- **may be hard-coded not settled ≠ 147 apphash vs this block / 614 notheader interchangeable：** 官方把 476 item 2 和已经交差 / 印进本头分开。
- **may be hard-coded not finharddet bundled ≠ 620 notempty / 622 notnondet interchangeable：** 官方把 476 item 2 和 item 1 / item 3 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| may be hard-coded | 不是 already 必须真是 Merkle root | 不是 optional Merkle root bundled（475） |
| may be hard-coded | 不是 already 已经交差 | 不是 apphash vs this block（147） |
| may be hard-coded | 不是 already finharddet bundled | 不是 may be empty（476 item 1 / 620） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash may be hard-coded not Merkle root / not settled / not finharddet bundled 正式三事（476 余量），必须分开 may be hard-coded 是不是 already 必须真是 Merkle root interchangeable / 475 finmerkle interchangeable / 404 finapphash interchangeable / 392 initchain apphash interchangeable、may be hard-coded 是不是 already 已经交差 interchangeable / 147 apphash vs this block interchangeable / 614 notheader interchangeable / 335 finpersist interchangeable、may be hard-coded 是不是 already finharddet bundled interchangeable / 620 notempty interchangeable / 622 notnondet interchangeable / 470 findet interchangeable。可以跳过「看见 may be hard-coded 就已经必须真是 Merkle root interchangeable」。不要另写怎样写死常量。

## 本页不抄

- 怎样挑空根、怎样写死常量、怎样测确定性。
- FinalizeBlockResponse app_hash empty / hard-coded / MUST be deterministic 正式三事 bundled。那是不变量 476。
- may be empty not no state root。那是不变量 476 item 1 余量 / 620。
- MUST be deterministic not next_block_delay nondet。那是不变量 476 item 3 余量 / 622。
- Finalize 回包余量 bundled。那是不变量 404。
- optional Merkle root bundled。那是不变量 475。
- FinalizeBlock Usage determinism bundled。那是不变量 470。
- next_block_delay 非确定。那是不变量 589。
- 本头 AppHash vs 本高度交差。那是不变量 147。
