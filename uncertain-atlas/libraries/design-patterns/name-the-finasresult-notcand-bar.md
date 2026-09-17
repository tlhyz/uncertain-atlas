# 模式：把 FinalizeBlock must provide values as a result of executing the block not candidate / Process already ran 正式三事（477 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[as a result of executing the block not candidate ≠ bundled（477）](../../tracks/implementation/worked-example-finasresult-notcand-vs-bundled.md)。

## 三个名字

1. **as a result of executing not Process already ran 不是 finasresult bundled：** 看见 executing the block 不是已经 Process / Prepare candidate 就不需要再在 Finalize 执行 interchangeable，不是 477 finasresult interchangeable / 574 notcand interchangeable / 351 Process also on proposer interchangeable。
2. **as a result of executing not apply candidate 不是 fincand bundled：** 看见 must provide as a result of executing 不是已经 apply candidate state 就不需要执行 txs interchangeable，不是 460 fincand interchangeable / 584 apply candidate interchangeable / 578 not no re-execute interchangeable。
3. **as a result of executing not candidate 不是 466 executes block v / not settled：** 看见 executing the block 不是已经 Application executes block _v_ interchangeable，不是 466 executes block v interchangeable / 594 not settled interchangeable / 477 item 3 finempty interchangeable。

## 为什么要分开叫

官方把 must provide values as a result of executing the block 和 Process already ran / apply candidate / finasresult bundled 写成三个名字。把它们叫成一个「看见 as a result of executing 就已经 Process 跑过就不用再执行 / 已经 apply candidate interchangeable / 已经 477 finasresult bundled interchangeable」，会把 not Process already ran、not apply candidate、not 466 / 351 / 594 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock must provide values as a result of executing the block not candidate / Process already ran 正式三事（477 余量），先数清问的是 as a result of executing 是不是 already Process already ran / no need to execute、是不是 already apply candidate / ExecuteTxState、还是 as a result of executing 是不是 already 466 executes block v / 594 not settled / 477 item 3 empty keep current，再决定要不要同一次发布。
