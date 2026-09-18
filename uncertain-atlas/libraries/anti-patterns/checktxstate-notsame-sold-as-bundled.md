# 反模式：把同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量）说成已经同一份 / 已经合并 / 已经共用一份工作状态

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[同时在改 not already same state ≠ bundled（312）](../../tracks/implementation/worked-example-checktxstate-notsame-vs-bundled.md)。

## 卖法

把 CheckTxState 和 ExecuteTxState 同时在改 / 两边都在改 / may be updated concurrently 写成已经同一份状态 interchangeable / 已经 same state interchangeable / 已经一份状态 interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable；把共识和内存池两条连接都在说话 / 消息可以并发 写成已经合并 interchangeable / 已经 merged interchangeable；把都叫 CheckTx / Finalize / 两边都在处理交易相关调用 写成已经共用一份工作状态 interchangeable / 已经 shared working state interchangeable，或已经和 312 checktxstate bundled / checktxstate-sold-as-execute interchangeable / 696 checktxstate-notsame interchangeable。

## 为什么错

官方把同时更新单句、already same state、already merged、already shared working state 写成三件独立的实现事。把它们卖成 already same state interchangeable / already merged interchangeable / already shared working state interchangeable，会把 not already same state、not already merged、not already shared working state 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量），必须分开 not already same state、not already merged、not already shared working state 三件事，不要和 312 / 33 / 695 / 697 / 311 / 310 糊成一句。

## 和相邻反模式

- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState bundled 全段，不是本页同时在改 item 2 单句边界。
- [checktxstate-notexecute-sold-as-bundled](checktxstate-notexecute-sold-as-bundled.md) 是 CheckTx 过了 item 1，不是本页两边都在改 ≠ 已经同一份边界。
- [conn-sold-as-gates](conn-sold-as-gates.md) 是一条连接 ≠ 已经是四门（307），不是本页两条连接并发 ≠ 已经合并边界。
