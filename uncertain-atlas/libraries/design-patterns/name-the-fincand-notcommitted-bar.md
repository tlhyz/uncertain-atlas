# 模式：把 executes txs deterministically not already committed 正式三事（460 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[executes txs deterministically not already committed ≠ bundled（460）](../../tracks/implementation/worked-example-fincand-notcommitted-vs-bundled.md)。

## 三个名字

1. **executes txs deterministically not already committed 不是 fincand bundled：** 看见 before returning control 不是已经交差，不是 460 bundled interchangeable / 470 findet interchangeable / 452 candidate interchangeable。
2. **executes txs deterministically not like Prepare 不是 Prepare nondet：** 看见 deterministically 不是已经可以像 Prepare 那样，不是 338 Prepare nondet interchangeable / 407 finfields interchangeable。
3. **executes txs deterministically not apply candidate / previously executed 不是 fincand item 2/3：** 看见 execute txs 路不是已经套用 candidate 就不需要再执行，不是 572 has run not apply candidate interchangeable / 577 apply candidate interchangeable / 578 not no re-execute interchangeable。

## 为什么要分开叫

官方把 executes txs deterministically before returning control 写成三个名字。把它们叫成一个「看见确定执行 txs 就已经交差 interchangeable / 已经像 Prepare 那样 interchangeable / 已经 fincand bundled interchangeable」，会把 not committed、not like Prepare、not apply candidate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 executes txs deterministically not already committed 正式三事（460 余量），先数清问的是 executes txs 是不是 already committed、是不是 already like Prepare、是不是 already apply candidate / previously executed，再决定要不要同一次发布。
