# 模式：把 app_hash MUST be deterministic not 印进本头 正式三事（470 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[app_hash MUST be deterministic not 印进本头 ≠ bundled（470）](../../tracks/implementation/worked-example-findet-notapphash-vs-bundled.md)。

## 三个名字

1. **app_hash MUST be deterministic not 印进本头 不是 findet bundled：** 看见 app_hash 必须确定不是已经本头 AppHash 交差，不是 470 bundled interchangeable / 476 empty-hardcoded interchangeable / 475 Merkle root interchangeable。
2. **app_hash not next_block_delay nondet 不是 469 next_block_delay 非确定：** 看见 only params + previous state 不是已经 next_block_delay 非确定就代表整门非确定，不是 469 next_block_delay interchangeable / 342 Req 11–12 interchangeable。
3. **app_hash not findet item 1/3 不是 executes txs / implementation bundled：** 看见 app_hash 单句不是已经 findet bundled interchangeable，不是 579 executes txs interchangeable / 581 implementation interchangeable / 404 finresp bundled interchangeable。

## 为什么要分开叫

官方把 app_hash MUST be deterministic 写成三个名字。把它们叫成一个「看见 app_hash 必须确定 就已经印进本头 interchangeable / 已经 next_block_delay 非确定 interchangeable / 已经 findet bundled interchangeable」，会把 not 印进本头、not next_block_delay nondet、not findet item 1/3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash MUST be deterministic not 印进本头 正式三事（470 余量），先数清问的是 app_hash 是不是 already 印进本头、是不是 already next_block_delay nondet、是不是 already findet item 1/3 bundled，再决定要不要同一次发布。
