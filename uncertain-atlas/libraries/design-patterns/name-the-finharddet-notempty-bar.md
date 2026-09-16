# 模式：把 FinalizeBlockResponse app_hash may be empty not no state root / not settled / not finharddet bundled 正式三事（476 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlockResponse app_hash may be empty not no state root ≠ bundled（476）](../../tracks/implementation/worked-example-finharddet-notempty-vs-bundled.md)。

## 三个名字

1. **may be empty 不是没有状态根：** 看见可以空，不是已经没回根就代表没有应用状态 interchangeable，不是 404 finapphash interchangeable / 475 finmerkle interchangeable / 392 initchain apphash interchangeable。
2. **may be empty 不是已经交差：** 看见 may be empty，不是已经交差 interchangeable，不是 147 apphash vs this block interchangeable / 614 notheader interchangeable / 33 four gates interchangeable。
3. **may be empty 不是 finharddet bundled：** 看见 may be empty，不是已经 finharddet bundled interchangeable，不是 621 nothardcoded interchangeable / 622 notnondet interchangeable / 476 finharddet item 2 hard-coded interchangeable / 476 finharddet item 3 MUST be deterministic interchangeable。

## 为什么要分开叫

官方把 Usage 里 may be empty、may be hard-coded、MUST be deterministic 写成三个名字。把它们叫成一个「看见 may be empty 就已经没有状态 interchangeable、就已经交差 interchangeable、就已经 finharddet bundled interchangeable」，会把 not no state root、not settled、not finharddet bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse app_hash may be empty not no state root / not settled / not finharddet bundled 正式三事（476 余量），先数清问的是 may be empty 是不是 already 没有状态根 / 404 / 475，是不是 already 已经交差 / 147 / 614，还是 may be empty 是不是 already finharddet bundled / 621 / 622，再决定要不要同一次发布。
