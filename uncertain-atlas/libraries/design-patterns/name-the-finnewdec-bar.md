# 模式：把 FinalizeBlock Contains newly decided block fields 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Contains newly decided block fields ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finnewdec-vs-proposed.md)。

## 三个名字

1. **Contains the fields of the newly decided block 不是已经是四门已经结算：** 看见含刚决定那块的字段不是已经跑过 Process / 已经交差 interchangeable。
2. **newly decided block 不是 proposed block：** 看见刚决定那块不是已经 ProcessProposal 含执行所需全部信息 interchangeable。
3. **fields of the newly decided block 不是 height/time match header 就代表对象已经分清：** 看见刚决定那块的字段不是已经 match header / fill all fields even if passed interchangeable。

## 为什么要分开叫

官方把 Contains the fields of the newly decided block、newly decided block 对象、fields of the newly decided block 和 proposed / match header 的边界写成三个名字。把它们叫成一个「看见填了 Finalize 含刚决定那块的字段就已经是四门已经结算」，会把刚决定那块的字段、拟议块执行信息和 height/time match header 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Contains the fields of the newly decided block」，先数清问的是含刚决定那块的字段是不是已经是四门已经结算、newly decided block 是不是 proposed block / ProcessProposal 含执行所需全部信息，还是 fields of the newly decided block 是不是已经 height/time match header 就代表对象已经分清，再决定要不要同一次发布。
