# 模式：把 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields not decided/proposed interchangeable ≠ bundled](../../tracks/implementation/worked-example-finnewfields-notdecprop-vs-bundled.md)。

## 三个名字

1. **fill all fields not decided/proposed interchangeable 不是 FinalizeBlock 含刚决定那块字段 bundled：** 看见又填一遍不是已经 decided 和 proposed 就可以混用，不是 461 bundled interchangeable / 422 decided vs proposed interchangeable / 473 fill all fields interchangeable。
2. **fill all fields not newly decided/proposed interchangeable 不是 359 Prepare 同一套字段：** 看见 even if passed 不是已经 newly decided 和 proposed interchangeable，不是 461 bundled interchangeable / 359 Prepare 同一套 interchangeable / 557 not ProcessProposal full info interchangeable。
3. **fill all fields not ran Process means don't need Finalize 不是 360 Process guarantee：** 看见引擎填齐不是已经跑过 Process 就不需要 Finalize，不是 461 bundled interchangeable / 360 Process guarantee interchangeable / 473 not need Finalize interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock fill all fields not decided/proposed interchangeable 写成三个名字。把它们叫成一个「看见又填一遍就已经 decided 和 proposed 就可以混用」，会把 decided vs proposed 语义、newly decided vs proposed 对象、fill all fields vs Process 跑过 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not decided/proposed interchangeable 正式三事，先数清问的是 fill all fields 是不是 decided/proposed interchangeable、fill all fields 是不是 newly decided/proposed interchangeable、fill all fields 是不是 ran Process means don't need Finalize，再决定要不要同一次发布。
