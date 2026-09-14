# 例：看见 Finalize 实现必须确定 / implementation MUST be deterministic for state machine replication is not already like Prepare / not finfields bundled（407） interchangeable / not findet bundled（470） interchangeable

**层次**：实现 / Finalize 实现必须确定 not like Prepare 正式三事（407 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 实现必须确定 not like Prepare / not finfields bundled（407） interchangeable / not findet bundled（470） interchangeable」，不是 Finalize 字段余量 bundled（407），也不是 FinalizeBlock Usage determinism 正式三事（470），也不是 Prepare 没有确定性要求（338）。不要另写怎样写 Finalize 确定性。

## 官方三件事

规范把 FinalizeBlock Usage 里 `The implementation of FinalizeBlock MUST be deterministic, since it is making the Application's state evolve in the context of state machine replication` 和「已经可以像 Prepare 那样 / 已经是 Req 11–12 / 已经是 finfields bundled interchangeable」分开写成三件独立的实现事，不是「看见 Usage 写了必须确定就已经可以像 Prepare 那样 interchangeable、已经 Req 11–12 interchangeable、已经 finfields bundled interchangeable」一件事：

1. **看见 Finalize 实现必须确定、因为它在状态机复制里推进应用状态 / 看见 implementation MUST be deterministic for state machine replication is not already like Prepare / 看见必须确定 is not already Prepare 没有确定性要求 / 可以依赖非确定值 interchangeable / 看见在复制里推进 is not already Finalize 字段余量 bundled（407） interchangeable / 已经像 Prepare 那样 interchangeable / 已经 Prepare 没有确定性要求 interchangeable，也不是已经 Prepare 没有确定性要求 bundled（338 余量） interchangeable / 已经 ExtendVote 没有确定性要求 interchangeable / 已经两边 raw 一样 interchangeable，也不是已经 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块 bundled（342 余量） interchangeable / 已经 Req 11–12 interchangeable / 已经可以依赖其它值 interchangeable，也不是已经 FinalizeBlock Usage determinism 正式三事 bundled（470 余量） interchangeable / 已经 executes txs deterministically interchangeable / 已经 app_hash MUST be deterministic interchangeable，也不是已经 Finalize 含刚决定那块的字段 not already settled bundled（573 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable。**  
   官方 Usage 写：`FinalizeBlock` 的实现必须确定，因为它在状态机复制的上下文里推进应用状态。看见 MUST be deterministic，不是已经 Prepare 没有确定性要求（338） interchangeable——338 钉 Prepare 可以不确定，本页钉 407 item 2 not like Prepare 单句。看见在复制里推进，不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块（342） interchangeable——342 来自 app requirements Req 11–12，本页钉 Methods Usage 这句。看见必须确定，不是已经 finfields bundled（407） interchangeable——407 bundled 第二件事常被写成「看见必须确定就已经可以像 Prepare 那样」，本页钉 implementation must be deterministic 单句。
2. **看见 implementation MUST be deterministic for state machine replication is not already Req 11–12 / s_h and T_h only depend on previous state and decided block interchangeable / 看见必须确定 is not already FinalizeBlock Usage determinism 正式三事 bundled（470 余量） interchangeable / 已经 executes txs deterministically interchangeable / 已经 app_hash MUST be deterministic interchangeable / 已经 findet bundled interchangeable，也不是已经 Application executes txs deterministically before returning control bundled（470 第一件事） interchangeable / 已经套用 candidate 就不需要再执行 interchangeable / 已经像 Prepare 那样 interchangeable，也不是已经 app_hash MUST be deterministic / only params + previous state bundled（470 第二件事） interchangeable / 已经印进本头 interchangeable / 已经 next_block_delay 非确定就代表整门非确定 interchangeable，也不是已经 FinalizeBlockResponse.next_block_delay 非确定正式三事 bundled（469 余量） interchangeable / 已经 wallclock interchangeable / 已经 Commit 后再开下一高 interchangeable。**  
   官方把 Usage 这句 implementation must be deterministic 和 executes txs / app_hash 那三句 bundled 分开——470 bundled 常与 407 混成「看见 Usage 写了必须确定就已经是 Req 11–12 / findet bundled interchangeable」，本页钉 implementation must be deterministic not findet bundled 单句。看见 state machine replication，不是已经 executes txs deterministically（470 第一件事） interchangeable——470 钉 executes txs 单句，本页钉 407 item 2 边界。看见 MUST be deterministic，不是已经 app_hash MUST be deterministic（470 第二件事） interchangeable——470 钉 app_hash 只依赖两份，本页钉 implementation 单句。看见 implementation must be deterministic，不是已经 next_block_delay 非确定（469 余量） interchangeable——469 钉回包例外，本页钉 Usage implementation 单句。
3. **看见 implementation MUST be deterministic for state machine replication is not already finfields bundled item 1 four gates settled / Info handshake interchangeable / 看见必须确定 is not already Finalize 含刚决定那块的字段 not already settled bundled（573 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable，也不是已经 Finalize 字段余量 not Info handshake bundled（407 第三件事 / 575 余量） interchangeable / 已经握手对齐 interchangeable / 已经快照重放 interchangeable，也不是已经 Finalize 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock bundled（465 余量） interchangeable / 已经收成一门 interchangeable / 已经四门已经结算 interchangeable，也不是已经 CometBFT fill up all fields even if Prepare/Process passed bundled（363 余量） interchangeable / 已经又填一遍 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable。**  
   官方把 Finalize 实现必须确定 和含刚决定那块的字段 / Info 回应用状态信息 bundled 分开——407 bundled 三事常被写成「看见填了 Finalize 字段余量就已经必须确定 interchangeable」，本页钉 implementation must be deterministic not finfields bundled item 1/3 单句。看见 MUST be deterministic，不是已经 Finalize 含刚决定那块的字段 not already settled（573 余量） interchangeable——573 钉 item 1 not settled，本页钉 item 2 deterministic。看见在复制里推进，不是已经 Info 用来回应用状态信息（407 item 3 / 575 余量） interchangeable——575 钉 Info not handshake，本页钉 implementation must be deterministic 单句。

怎样写 Finalize 确定性、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。Finalize 字段余量 bundled item 1 not settled（573 余量）、Info not handshake（575 余量）、FinalizeBlock Usage determinism 正式三事（470）是另外那套，本页不抄。

## 官方为什么这样拆

- **implementation MUST be deterministic for state machine replication ≠ like Prepare interchangeable：** 官方把 Finalize 必须确定和 Prepare 可以不确定分开。
- **implementation MUST be deterministic ≠ findet bundled / Req 11–12 interchangeable：** 官方把 Usage 这句和 executes txs / app_hash 三句 bundled 分开。
- **implementation MUST be deterministic ≠ finfields bundled item 1/3 interchangeable：** 官方把实现必须确定和含刚决定那块的字段 / Info 回应用状态信息 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| implementation MUST be deterministic | 不是 already like Prepare | 不是 Prepare 没有确定性要求（338） |
| implementation MUST be deterministic | 不是 already findet bundled | 不是 FinalizeBlock Usage determinism（470） |
| implementation MUST be deterministic | 不是 already finfields bundled item 1/3 | 不是 Finalize 含刚决定那块的字段 not settled（573） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 实现必须确定 not like Prepare 正式三事（407 余量），必须分开 implementation must be deterministic 是不是 already like Prepare interchangeable / 407 bundled interchangeable / 338 Prepare nondet interchangeable、implementation must be deterministic 是不是 already findet bundled interchangeable / 470 executes txs interchangeable / 342 Req 11–12 interchangeable、implementation must be deterministic 是不是 already finfields bundled item 1/3 interchangeable / 573 not settled interchangeable / 575 Info not handshake interchangeable。可以跳过「看见 Usage 写了必须确定就已经可以像 Prepare 那样 interchangeable」。不要另写怎样写 Finalize 确定性。

## 本页不抄

- 怎样写 Finalize 确定性、怎样测确定性、怎样写测试向量。
- Finalize 含刚决定那块的字段 not already settled。那是不变量 573（407 item 1 余量）。
- Info not handshake aligned。那是不变量 575（407 item 3 余量）。
- FinalizeBlock Usage determinism 正式三事。那是不变量 470。
- FinalizeBlockResponse next_block_delay 非确定。那是不变量 469。
