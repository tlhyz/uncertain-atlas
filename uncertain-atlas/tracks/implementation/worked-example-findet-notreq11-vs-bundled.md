# 例：看见 implementation MUST be deterministic for state machine replication is not already Req 11–12 / s_h T_h interchangeable / not findet bundled（470） interchangeable / not finfields bundled interchangeable

**层次**：实现 / implementation MUST be deterministic not Req 11–12 正式三事（470 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「implementation MUST be deterministic not Req 11–12 / not findet bundled（470） interchangeable / not finfields bundled interchangeable」，不是 FinalizeBlock Usage determinism 正式三事（470），也不是 Finalize 实现必须确定 not like Prepare（407 finfields item 2 余量）。不要另写怎样测确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 The implementation of `FinalizeBlock` MUST be deterministic, since it is making the Application's state evolve in the context of state machine replication 和「已经是 Req 11–12 / finfields bundled interchangeable / findet bundled interchangeable」分开写成三件独立的实现事，不是「看见 Usage 写了 implementation 必须确定 就已经 Req 11–12 interchangeable、已经 finfields bundled interchangeable、已经 findet bundled interchangeable」一件事：

1. **看见 The implementation of `FinalizeBlock` MUST be deterministic, since it is making the Application's state evolve in the context of state machine replication / 看见 implementation MUST be deterministic is not already Req 11–12 / s_h and T_h only depend on previous state and decided block interchangeable / 看见必须确定 is not already FinalizeBlock 算出的状态必须只依赖上一份状态和决定块 bundled（342 余量） interchangeable / 已经 Req 11–12 interchangeable / 已经可以依赖其它值 interchangeable，也不是已经 FinalizeBlock Usage determinism 正式三事 bundled（470） interchangeable / 已经 findet bundled interchangeable / 已经 app_hash MUST be deterministic interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（407 余量） interchangeable / 已经 state machine replication interchangeable / 已经 executes txs deterministically interchangeable，也不是已经 Process 对任意块同一裁决 bundled（340 余量） interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable / 已经 candidate state interchangeable，也不是已经 executes txs deterministically not like Prepare bundled（579 余量） interchangeable / 已经 like Prepare interchangeable / 已经 apply candidate interchangeable。**  
   官方 Usage 写 implementation MUST be deterministic for state machine replication。看见 MUST be deterministic，不是已经 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块（342） interchangeable——342 来自 app requirements Req 11–12，本页钉 Methods Usage implementation 单句。看见 state machine replication，不是已经 Process 对任意块同一裁决（340） interchangeable——340 钉 Process 裁决，本页钉 470 item 3 边界。看见 making the Application's state evolve，不是已经 Finalize 实现必须确定 not like Prepare（407 余量） interchangeable——574 钉 407 item 2 角度，本页钉 findet item 3 单句。
2. **看见 implementation MUST be deterministic for state machine replication is not already finfields bundled interchangeable / 看见必须确定 is not already Finalize 字段余量 bundled（407） interchangeable / 已经 finfields bundled interchangeable / 已经 Info 用来回应用状态信息 interchangeable，也不是已经 Finalize 含刚决定那块的字段 not already settled bundled（573 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable，也不是已经 Info 用来回应用状态信息 not handshake bundled（575 余量） interchangeable / 已经握手对齐 interchangeable / 已经快照重放 interchangeable，也不是已经 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事（586） interchangeable / 已经收成一门 interchangeable / 已经四门已经结算 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable，也不是已经 app_hash MUST be deterministic not 印进本头 bundled（580 余量） interchangeable / 已经 next_block_delay nondet interchangeable / 已经印进本头 interchangeable。**  
   官方把 Usage 这句 implementation must be deterministic 和 finfields bundled 里 MUST be deterministic / Info 回应用状态信息分开——470 bundled 常与 407 混成「看见 Usage 写了必须确定 就已经 finfields bundled interchangeable」，本页钉 implementation not finfields bundled 单句。看见 state machine replication，不是已经 Finalize 含刚决定那块的字段 not settled（573 余量） interchangeable——573 钉 item 1 not settled，本页钉 470 item 3 边界。看见 MUST be deterministic，不是已经 Info not handshake（575 余量） interchangeable——575 钉 407 item 3，本页钉 implementation 单句。
3. **看见 implementation MUST be deterministic is not already executes txs deterministically / app_hash MUST be deterministic bundled / findet item 1/2 interchangeable / 看见必须确定 is not already executes txs deterministically not like Prepare bundled（579 余量） interchangeable / 已经 like Prepare interchangeable / 已经 apply candidate interchangeable，也不是已经 app_hash MUST be deterministic not 印进本头 bundled（580 余量） interchangeable / 已经 next_block_delay nondet interchangeable / 已经印进本头 interchangeable，也不是已经 FinalizeBlockResponse app_hash empty / hard-coded bundled（476 余量） interchangeable / 已经 may be empty interchangeable / 已经 may be hard-coded interchangeable，也不是已经 Finalize 实现必须确定 not findet bundled bundled（407 第二件事 / 407 余量） interchangeable / 已经 findet bundled interchangeable / 已经 Req 11–12 interchangeable，也不是已经 FinalizeBlock must provide values bundled（477 余量） interchangeable / 已经 Process 跑过就不用再回 tx_results interchangeable / 已经空更新就没有 must provide 义务 interchangeable。**  
   官方把 implementation MUST be deterministic 和 executes txs / app_hash 那两句 bundled 分开——470 bundled 三事常被写成「看见 Usage 写了必须确定 就已经 findet bundled interchangeable」，本页钉 implementation not findet item 1/2 单句。看见 implementation must be deterministic，不是已经 executes txs not like Prepare（579 余量） interchangeable——579 钉 executes txs 单句，本页钉 implementation 边界。看见 MUST be deterministic，不是已经 app_hash not 印进本头（580 余量） interchangeable——580 钉 app_hash 单句，本页钉 470 item 3 第三件事。

怎样写 FinalizeBlock、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。executes txs not like Prepare（579 余量）、app_hash not 印进本头（580 余量）、Finalize 实现必须确定 not like Prepare（407 余量）、FinalizeBlock Usage determinism 正式三事（470）是另外那套，本页不抄。

## 官方为什么这样拆

- **implementation MUST be deterministic not Req 11–12 ≠ findet bundled interchangeable：** 官方把 Methods Usage 这句和 app requirements Req 11–12 分开。
- **implementation MUST be deterministic not finfields bundled ≠ 407 finfields interchangeable：** 官方把 implementation 必须确定和 finfields bundled 分开。
- **implementation MUST be deterministic not findet item 1/2 ≠ executes txs / app_hash bundled interchangeable：** 官方把 implementation 单句和 findet 其它两件事分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| implementation MUST be deterministic | 不是 already Req 11–12 | 不是 FinalizeBlock 确定性 Req 11–12（342） |
| implementation MUST be deterministic | 不是 already finfields bundled | 不是 Finalize 字段余量 bundled（407） |
| implementation MUST be deterministic | 不是 already findet item 1/2 | 不是 executes txs / app_hash slices（579/580） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 implementation MUST be deterministic not Req 11–12 正式三事（470 余量），必须分开 implementation 是不是 already Req 11–12 interchangeable / 342 Req 11–12 interchangeable / 470 findet interchangeable、implementation 是不是 already finfields bundled interchangeable / 573 not settled interchangeable / 575 Info not handshake interchangeable、implementation 是不是 already findet item 1/2 interchangeable / 579 executes txs interchangeable / 580 app_hash interchangeable。可以跳过「看见 Usage 写了 implementation 必须确定 就已经 Req 11–12 interchangeable」。不要另写怎样测确定性。

## 本页不抄

- 怎样写 FinalizeBlock、怎样测确定性、怎样写测试向量。
- executes txs not like Prepare。那是不变量 579（470 item 1 余量）。
- app_hash not 印进本头。那是不变量 580（470 item 2 余量）。
- Finalize 实现必须确定 not like Prepare。那是不变量 407 finfields item 2 余量。
- FinalizeBlock Usage determinism 正式三事。那是不变量 470。
