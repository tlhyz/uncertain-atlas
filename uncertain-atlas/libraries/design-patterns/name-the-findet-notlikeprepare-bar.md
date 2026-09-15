# 模式：把 executes txs deterministically not like Prepare 正式三事（470 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[executes txs deterministically not like Prepare ≠ bundled（470）](../../tracks/implementation/worked-example-findet-notlikeprepare-vs-bundled.md)。

## 三个名字

1. **executes txs deterministically not like Prepare 不是 findet bundled：** 看见 deterministically 不是已经 Prepare 没有确定性要求 interchangeable，不是 470 bundled interchangeable / 338 Prepare nondet interchangeable / 407 finfields interchangeable。
2. **executes txs deterministically not apply candidate / previously executed 不是 fincand item 2/3：** 看见 execute txs 路不是已经套用 candidate 就不需要再执行，不是 577 apply candidate interchangeable / 578 not no re-execute interchangeable / 572 has run not apply candidate interchangeable。
3. **executes txs deterministically not committed 不是 576 / 460 committed：** 看见 before returning control 不是已经交差 interchangeable，不是 576 not committed interchangeable / 460 fincand interchangeable / 335 Finalize 改了就已经落盘 interchangeable。

## 为什么要分开叫

官方把 executes txs deterministically before returning control 写成三个名字。把它们叫成一个「看见 Usage 写了 deterministically 就已经可以像 Prepare 那样 interchangeable / 已经套用 candidate interchangeable / 已经 findet bundled interchangeable」，会把 not like Prepare、not apply candidate、not committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 executes txs deterministically not like Prepare 正式三事（470 余量），先数清问的是 executes txs 是不是 already like Prepare、是不是 already apply candidate / previously executed、是不是 already committed，再决定要不要同一次发布。
