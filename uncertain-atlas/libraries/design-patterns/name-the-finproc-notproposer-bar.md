# 模式：把 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed ≠ bundled（472）](../../tracks/implementation/worked-example-finproc-notproposer-vs-bundled.md)。

## 三个名字

1. **at least one not proposer means everyone Processed 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 at least one non-byzantine 不是已经提议者 Process 过就代表全网都 Process 过，不是 472 bundled interchangeable / 351 Process also on proposer interchangeable / 570 When calling interchangeable。
2. **at least one not local node means every validator Processed 不是 VerifyVoteExtension local path：** 看见 at least one 不是已经本节点刚 Process 过就代表每个验证者都 Process 过，不是 472 bundled interchangeable / 457 VVE local interchangeable / 351 proposer path interchangeable。
3. **at least one not list matches means guarantee satisfied 不是 Process follows Prepare：** 看见 at least one 不是已经列表对得上就代表 guarantee 已满足，不是 472 bundled interchangeable / 351 Process follows Prepare interchangeable / 506 Prepare return interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 写成三个名字。把它们叫成一个「看见至少一名就已经提议者 Process 过 interchangeable / 已经本节点 Process 过 interchangeable / 已经列表对得上 interchangeable」，会把 not proposer means everyone、not local node means every validator、not list matches means guarantee 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量），先数清问的是 at least one 是不是 already proposer Process means everyone Processed、at least one 是不是 already local node just Processed means every validator、at least one 是不是 already list matches means guarantee satisfied，再决定要不要同一次发布。
