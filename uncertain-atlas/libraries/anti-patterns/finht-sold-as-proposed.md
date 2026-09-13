# 反模式：把 FinalizeBlock height/time 对上拟议块头正式三事说成已经验过块头

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Finalize height/time match header ≠ 已经验过块头](../../tracks/implementation/worked-example-finht-vs-header.md)。

## 错在哪里

把 Finalize height and time values match the values from the header of the proposed block 写成已经验过块头，或已经跑过 Process；把 FinalizeBlockRequest.height 是已决块的高度 / time 是已决块的时间戳 写成已经 Usage 那种 match header，或已经是 ProcessProposalRequest.height / time interchangeable；把 Finalize height/time match header 写成已经是 ProcessProposal match interchangeable，或已经知道本头哈希，或已经和 417 / 422 / 454 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock height/time 对上拟议块头正式三事，必须分开 Finalize match header、Request height / time 栏、Finalize vs Process match 三件事，不要和 417 / 422 / 454 / 461 糊成一句。
