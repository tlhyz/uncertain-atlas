# 模式：把 implementation MUST be deterministic not Req 11–12 正式三事（470 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[implementation MUST be deterministic not Req 11–12 ≠ bundled（470）](../../tracks/implementation/worked-example-findet-notreq11-vs-bundled.md)。

## 三个名字

1. **implementation MUST be deterministic not Req 11–12 不是 findet bundled：** 看见 Usage 这句不是已经 Req 11–12 interchangeable，不是 470 bundled interchangeable / 342 Req 11–12 interchangeable / 407 finfields not like Prepare interchangeable。
2. **implementation MUST be deterministic not finfields bundled 不是 407 finfields：** 看见 implementation 必须确定不是已经 finfields bundled interchangeable，不是 573 not settled interchangeable / 575 Info not handshake interchangeable / 407 bundled interchangeable。
3. **implementation MUST be deterministic not findet item 1/2 不是 executes txs / app_hash bundled：** 看见 implementation 单句不是已经 findet bundled interchangeable，不是 579 executes txs interchangeable / 580 app_hash interchangeable / 476 empty-hardcoded interchangeable。

## 为什么要分开叫

官方把 implementation MUST be deterministic for state machine replication 写成三个名字。把它们叫成一个「看见 Usage 写了 implementation 必须确定 就已经 Req 11–12 interchangeable / 已经 finfields bundled interchangeable / 已经 findet bundled interchangeable」，会把 not Req 11–12、not finfields bundled、not findet item 1/2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 implementation MUST be deterministic not Req 11–12 正式三事（470 余量），先数清问的是 implementation 是不是 already Req 11–12、是不是 already finfields bundled、是不是 already findet item 1/2 bundled，再决定要不要同一次发布。
