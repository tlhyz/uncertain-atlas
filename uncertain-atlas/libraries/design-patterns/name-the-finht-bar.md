# 模式：把 FinalizeBlock height/time 对上拟议块头正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[Finalize height/time match header ≠ 已经验过块头](../../tracks/implementation/worked-example-finht-vs-header.md)。

## 三个名字

1. **Finalize height/time match header 不是已经验过块头：** 看见 Finalize 对上了不是已经跑过 Process。
2. **Request height / time 栏不是已经 Usage 那种 match header：** 看见已决块高度/时间戳栏不是已经 ProcessProposalRequest.height / time interchangeable。
3. **Finalize match header 不是已经是 ProcessProposal match interchangeable：** 看见 Finalize 对上了不是已经知道本头哈希。

## 为什么要分开叫

官方把 Finalize 的 height / time match、Request 表上 height / time 栏描述、Finalize 和 Process 各自的 match 语句写成三个名字。把它们叫成一个「看见 Finalize 填了 height/time 就已经验过块头」，会把 Finalize match、Request 栏语义和 Process match 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Finalize 填了 height/time 就已经验过块头」，先数清问的是 Finalize height/time match header 是不是已经验过块头、Request height / time 栏是不是已经 Usage 那种 match header，还是 Finalize match header 是不是已经是 ProcessProposal height/time match interchangeable，再决定要不要同一次发布。
