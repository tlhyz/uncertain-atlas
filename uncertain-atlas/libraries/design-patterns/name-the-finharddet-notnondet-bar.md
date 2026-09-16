# 模式：把 FinalizeBlockResponse MUST be deterministic not next_block_delay nondet / not 印进本头 / not finharddet bundled 正式三事（476 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlockResponse MUST be deterministic not next_block_delay nondet ≠ bundled（476）](../../tracks/implementation/worked-example-finharddet-notnondet-vs-bundled.md)。

## 三个名字

1. **MUST be deterministic 不是 next_block_delay 非确定：** 看见禁止非确定源，不是已经 next_block_delay 非确定就代表整包 finharddet 失败 interchangeable，不是 589 fndelay interchangeable / 618 notwallclock interchangeable / 611 notproctime interchangeable / 470 findet bundled interchangeable。
2. **MUST be deterministic 不是已经 settled：** 看见 MUST be deterministic，不是已经 settled interchangeable，不是 147 apphash vs this block interchangeable / 614 notheader interchangeable / 580 findet not apphash interchangeable / 601 notsettled interchangeable。
3. **MUST be deterministic 不是 finharddet bundled：** 看见 MUST be deterministic，不是已经 finharddet bundled interchangeable，不是 620 notempty interchangeable / 621 nothardcoded interchangeable / 476 finharddet item 1 empty interchangeable / 476 finharddet item 2 hard-coded interchangeable。

## 为什么要分开叫

官方把 Usage 里 may be empty、may be hard-coded、MUST be deterministic 写成三个名字。把它们叫成一个「看见 MUST be deterministic 就已经 next_block_delay 非确定 interchangeable、就已经 settled interchangeable、就已经 finharddet bundled interchangeable」，会把 not next_block_delay nondet、not 印进本头、not finharddet bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse MUST be deterministic not next_block_delay nondet / not 印进本头 / not finharddet bundled 正式三事（476 余量），先数清问的是 MUST be deterministic 是不是 already next_block_delay 非确定 / 589 / 618，是不是 already settled / 147 / 580，还是 MUST be deterministic 是不是 already finharddet bundled / 620 / 621，再决定要不要同一次发布。
