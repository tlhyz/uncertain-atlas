# 模式：把 ProcessProposal Process match header not Finalize newly decided fields 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[ProcessProposal Process match header not Finalize newly decided fields ≠ bundled](../../tracks/implementation/worked-example-procht-notfinht-vs-bundled.md)。

## 三个名字

1. **Process match header not Finalize newly decided fields 不是 ProcessProposal height/time 对上拟议块头 bundled：** 看见 Process 这边 match 不是已经是 FinalizeBlockRequest 字段，不是 454 bundled interchangeable / 461 newly decided interchangeable / 548 Contains all information interchangeable。
2. **Process match header not Finalize height/time match 不是 462 Finalize match：** 看见 Process match 不是已经 Finalize height/time match interchangeable，不是 454 bundled interchangeable / 462 Finalize match interchangeable / 428 Finalize hash interchangeable。
3. **Process match header not fill all fields again 不是 363 fill all fields：** 看见 Process match 不是已经又填一遍 newly decided block 字段，不是 454 bundled interchangeable / 363 fill all fields interchangeable / 461 newly decided interchangeable。

## 为什么要分开叫

官方把 ProcessProposal Process match header not Finalize newly decided fields 写成三个名字。把它们叫成一个「看见 Process match header 就已经是 Finalize 字段 interchangeable」，会把 Process Usage match、Finalize height/time match 和 Finalize 又填字段三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Process match header not Finalize newly decided fields 正式三事，先数清问的是 Process match header 是不是 FinalizeBlockRequest newly decided fields、Process match header 是不是 Finalize height/time match interchangeable、Process match header 是不是 fill all fields again，再决定要不要同一次发布。
