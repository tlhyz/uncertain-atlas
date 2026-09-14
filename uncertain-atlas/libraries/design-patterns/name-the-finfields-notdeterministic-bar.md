# 模式：把 Finalize 实现必须确定 not like Prepare 正式三事（407 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Finalize 实现必须确定 not like Prepare ≠ bundled（407）](../../tracks/implementation/worked-example-finfields-notdeterministic-vs-bundled.md)。

## 三个名字

1. **implementation MUST be deterministic for state machine replication 不是 like Prepare：** 看见必须确定不是已经可以像 Prepare 那样依赖非确定值，不是 407 bundled interchangeable / 338 Prepare nondet interchangeable / 342 Req 11–12 interchangeable。
2. **implementation MUST be deterministic 不是 findet bundled：** 看见 Usage 这句不是 executes txs / app_hash MUST be deterministic bundled interchangeable，不是 470 findet bundled interchangeable / 469 next_block_delay interchangeable。
3. **implementation MUST be deterministic 不是 finfields bundled item 1/3：** 看见必须确定不是已经四门已经结算 / Info 握手 interchangeable，不是 573 not settled interchangeable / 575 Info not handshake interchangeable / 407 bundled interchangeable。

## 为什么要分开叫

官方把 Finalize 实现必须确定写成三个名字。把它们叫成一个「看见 Usage 写了必须确定就已经可以像 Prepare 那样 interchangeable / 已经 findet bundled interchangeable / 已经 finfields bundled interchangeable」，会把 not like Prepare、not findet bundled、not finfields item 1/3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 实现必须确定 not like Prepare 正式三事（407 余量），先数清问的是 implementation must be deterministic 是不是 already like Prepare、是不是 already findet bundled、是不是 already finfields bundled item 1/3，再决定要不要同一次发布。
