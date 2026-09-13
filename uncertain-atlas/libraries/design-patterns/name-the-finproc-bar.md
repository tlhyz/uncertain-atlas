# 模式：把 FinalizeBlock When calling ProcessProposal guarantee 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[When calling FinalizeBlock guarantee ≠ 已经每个验证者都跑过 Process](../../tracks/implementation/worked-example-finproc-vs-allvalidators.md)。

## 三个名字

1. **When calling FinalizeBlock / consensus algorithm guarantees 不是已经每个验证者都跑过 Process：** 看见 guarantee 不是已经 executes block v / persist decision interchangeable。
2. **at least one non-byzantine validator 不是已经提议者 Process 过就代表全网都 Process 过：** 看见至少一名不是已经 Process 也会在提议者那边叫 interchangeable。
3. **has run ProcessProposal on that block 不是已经套用 candidate 就不需要 guarantee：** 看见 ran ProcessProposal 不是已经 previously executed / apply candidate interchangeable。

## 为什么要分开叫

官方把 When calling FinalizeBlock、at least one non-byzantine validator、has run ProcessProposal on that block 写成三个名字。把它们叫成一个「看见要 Finalize 了就已经每个验证者都跑过 Process、已经提议者 Process 过就代表全网都 Process 过、已经套用 candidate 就不需要 Process 保证」，会把 guarantee 范围、至少一名和 ran ProcessProposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见要 Finalize 了」，先数清问的是 When calling FinalizeBlock / consensus guarantees 是不是已经每个验证者都跑过 Process、at least one non-byzantine 是不是已经提议者 Process 过就代表全网都 Process 过，还是 has run ProcessProposal on that block 是不是已经套用 candidate 就不需要 guarantee，再决定要不要同一次发布。
