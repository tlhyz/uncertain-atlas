# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量）卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经提议者 Process 过就代表全网都 Process 过 / 已经本节点 Process 过

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed ≠ bundled（472）](../../tracks/implementation/worked-example-finproc-notproposer-vs-bundled.md)。

## 卖法

- 「看见 at least one non-byzantine validator / 看见至少一名非拜占庭 就已经提议者 Process 过就代表全网都 Process 过 interchangeable。」
- 「看见 at least one 就已经本节点刚 Process 过就代表每个验证者都 Process 过 interchangeable / 已经 local 路径 interchangeable。」
- 「看见 at least one 就已经 Process 通常紧跟 Prepare / 列表对得上 interchangeable / 已经不用再 Process interchangeable。」

## 为什么错

官方把 at least one non-byzantine validator has run `ProcessProposal` on that block、提议者 Process 路径、本节点 Process 路径、Prepare/Process 列表对得上 写成三件独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经提议者 Process 过就代表全网都 Process 过、已经本节点 Process 过，会把 not proposer means everyone、not local node means every validator、not list matches means guarantee 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量），必须分开 at least one not proposer means everyone Processed、at least one not local node means every validator Processed、at least one not list matches means guarantee satisfied 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经提议者 Process 过就代表全网都 Process 过 / 已经本节点 Process 过。

## 和相邻反模式

- [finproc-sold-as-allvalidators](finproc-sold-as-allvalidators.md) 是 472 bundled 三事专用，不是本页 at least one not proposer 单句边界。
- [finproc-notallvalidators-sold-as-bundled](finproc-notallvalidators-sold-as-bundled.md) 是 570 When calling not every validator 余量，不是本页 at least one not proposer 单句边界。
