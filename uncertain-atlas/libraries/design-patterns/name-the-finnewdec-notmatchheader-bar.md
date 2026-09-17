# 模式：把 FinalizeBlock Contains newly decided block fields not match header 正式三事（474 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock Contains newly decided block fields not match header ≠ bundled（474）](../../tracks/implementation/worked-example-finnewdec-notmatchheader-vs-bundled.md)。

## 三个名字

1. **fields of the newly decided block not match header means objects separated 不是 FinalizeBlock Contains newly decided block fields bundled：** 看见刚决定那块的字段不是已经 height/time match header 就代表对象已经分清，不是 474 bundled interchangeable / 462 match header interchangeable / 555 Finalize match not ProcessProposal match interchangeable。
2. **fields of the newly decided block not fill all fields means newly decided/proposed interchangeable 不是 473 fill all fields：** 看见 fields of the newly decided block 不是 fill up all fields even if passed 就代表 newly decided 和 proposed interchangeable，不是 474 bundled interchangeable / 473 fill all fields interchangeable / 558 decided/proposed interchangeable。
3. **fields of the newly decided block not decided/proposed commit columns interchangeable 不是 422 decided vs proposed：** 看见 fields of the newly decided block 不是 decided_last_commit 和 proposed_last_commit 就可以混用，不是 474 bundled interchangeable / 422 decided vs proposed interchangeable / 422 decided not proposed interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock Contains newly decided block fields not match header 写成三个名字。把它们叫成一个「看见 fields of the newly decided block 就已经 height/time 对上了就代表对象已经分清 / fill all fields interchangeable / decided/proposed 单栏 interchangeable」，会把 fields not match header、fields not fill all fields、fields not decided/proposed commit columns 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Contains newly decided block fields not match header 正式三事（474 余量），先数清问的是 fields of the newly decided block 是不是 match header 就代表对象已经分清、fields of the newly decided block 是不是 fill all fields 就代表 newly decided/proposed interchangeable、fields of the newly decided block 是不是 decided/proposed commit columns interchangeable，再决定要不要同一次发布。
