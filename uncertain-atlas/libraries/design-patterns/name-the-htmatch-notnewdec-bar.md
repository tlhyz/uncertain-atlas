# 模式：把头字段对上余量 Finalize height/time match header not already newly decided fields 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[头字段对上余量 Finalize height/time match header not already newly decided fields ≠ bundled](../../tracks/implementation/worked-example-htmatch-notnewdec-vs-bundled.md)。

## 三个名字

1. **Finalize height/time match header not already newly decided block fields 不是头字段对上余量 bundled：** 看见 Finalize 对上了不是已经是刚决定那块的字段，不是 417 bundled interchangeable / 407 Contains newly decided interchangeable / 555 not settled interchangeable。
2. **Finalize height/time match header not already know hash 不是 428 Finalize hash：** 看见 Usage match 不是已经知道本头哈希，不是 417 bundled interchangeable / 428 Finalize hash interchangeable / 311 Prepare no header hash interchangeable。
3. **Finalize height/time match header not already four gates settled 不是 407 four gates settled：** 看见对上了不是已经四门已经结算，不是 417 bundled interchangeable / 407 finfields interchangeable / 363 fill all fields interchangeable。

## 为什么要分开叫

官方把头字段对上余量 Finalize height/time match header not already newly decided fields 写成三个名字。把它们叫成一个「看见 Finalize 对上了 就已经是刚决定那块的字段 / 已经知道本头哈希」，会把 Finalize match vs newly decided fields、Finalize match vs know hash、Finalize match vs four gates settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 Finalize height/time match header not already newly decided fields 正式三事，先数清问的是 Finalize match 是不是 already newly decided block fields、Finalize match 是不是 already know hash、Finalize match 是不是 already four gates settled，再决定要不要同一次发布。
