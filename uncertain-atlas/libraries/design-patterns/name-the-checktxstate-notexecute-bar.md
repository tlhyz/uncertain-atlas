# 模式：把 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[CheckTx 过了 not already checked against ExecuteTxState ≠ bundled（312）](../../tracks/implementation/worked-example-checktxstate-notexecute-vs-bundled.md)。

## 三个名字

1. **CheckTx 过了 不是 already checked against ExecuteTxState：** 看见没报错 / 按 CheckTxState 顺序验过，不是已经按 ExecuteTxState 验过 interchangeable / 已经按工作状态验 interchangeable，不是 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable。

2. **进了池 不是 already checked against to-be-executed state：** 看见 Accepted into the mempool / CometBFT 开始 gossip，不是已经按将要执行的那份状态验过 interchangeable / 已经按决定块那份验 interchangeable，不是 312 checktxstate item 2 interchangeable / 696 checktxstate-notsame interchangeable。

3. **重置了 不是 already same as ExecuteTxState after reset：** 看见 Commit 结束时 CheckTxState 重置成最新已提交，不是已经和 ExecuteTxState 同一份 interchangeable / 已经两份合并 interchangeable，不是 312 checktxstate item 3 interchangeable / 697 checktxstate-notrecheck interchangeable。

官方把 CheckTx 过了单句、already checked against ExecuteTxState、already checked against to-be-executed state、already same as ExecuteTxState after reset 写成三个名字。把它们叫成一个「看见过了 就已经按工作状态验 interchangeable / 就已经按将要执行的那份验 interchangeable / 就已经同一份 interchangeable」，会把 not already checked against ExecuteTxState、not already checked against to-be-executed state、not already same as ExecuteTxState after reset 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量），先数清问的是 CheckTx 过了 是不是 already checked against ExecuteTxState / 312 / 33，是不是进了池 是不是 already checked against to-be-executed state，还是重置了 是不是 already same as ExecuteTxState after reset，再决定要不要同一次发布。312 checktxstate vs execute bundled unbundling 在本页 item 1 完成。
