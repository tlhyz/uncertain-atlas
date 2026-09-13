# 模式：把 ProcessProposal height/time 对上拟议块头正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[Process height/time match header ≠ 已经验过块头](../../tracks/implementation/worked-example-procht-vs-header.md)。

## 三个名字

1. **Process height/time match header 不是已经验过块头 / 已经跑过 Process：** 看见对上了不是已经 When 里先验块头。
2. **Request height / time 栏不是已经 Usage 那种对上了：** 看见填了 height / time 不是已经 match the values from the header。
3. **Process match header 不是已经是 FinalizeBlockRequest 刚决定那块的字段：** 看见 Process 这边 match 不是已经 Finalize height/time match interchangeable。

## 为什么要分开叫

官方把 ProcessProposal height/time 对上拟议块头写成三个名字。把它们叫成一个「看见 Process 填了 height/time 就已经验过块头」，会把 Usage match、Request 栏描述和 Finalize 字段一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 填了 height/time 就已经验过块头」，先数清问的是 Process height/time match header 是不是已经验过块头、Request height / time 栏是不是已经 Usage 那种对上了，还是 Process match header 是不是已经是 FinalizeBlockRequest 刚决定那块的字段，再决定要不要同一次发布。
