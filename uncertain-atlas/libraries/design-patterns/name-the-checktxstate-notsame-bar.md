# 模式：把同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[同时在改 not already same state ≠ bundled（312）](../../tracks/implementation/worked-example-checktxstate-notsame-vs-bundled.md)。

## 三个名字

1. **两边都在改 不是 already same state：** 看见 CheckTxState 和 ExecuteTxState 同时在改 / may be updated concurrently，不是已经同一份状态 interchangeable / 已经一份状态 interchangeable，不是 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable。

2. **两条连接并发 不是 already merged：** 看见共识和内存池两条连接都在说话 / 消息可以并发，不是已经合并 interchangeable / 已经并成一份 interchangeable，不是 312 checktxstate item 1 interchangeable / 695 checktxstate-notexecute interchangeable。

3. **都叫 CheckTx / Finalize 不是 already shared working state：** 看见两边都在处理交易相关调用 / 共识和内存池都在动，不是已经共用一份工作状态 interchangeable / 已经共用 ExecuteTxState interchangeable，不是 312 checktxstate item 3 interchangeable / 697 checktxstate-notrecheck interchangeable / 311 candidate interchangeable。

官方把同时更新单句、already same state、already merged、already shared working state 写成三个名字。把它们叫成一个「看见同时在改 就已经同一份 interchangeable / 就已经合并 interchangeable / 就已经共用一份 interchangeable」，会把 not already same state、not already merged、not already shared working state 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量），先数清问的是两边都在改 是不是 already same state / 312 / 33，是不是两条连接并发 是不是 already merged，还是都叫 CheckTx / Finalize 是不是 already shared working state，再决定要不要同一次发布。312 checktxstate vs execute bundled unbundling 在本页 item 2 完成。
