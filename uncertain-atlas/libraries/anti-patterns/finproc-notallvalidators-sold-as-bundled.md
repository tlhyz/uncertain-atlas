# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee not already every validator 正式三事（472 余量）卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经每个验证者都跑过 Process / 已经 Application executes block v

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not already every validator ≠ bundled（472）](../../tracks/implementation/worked-example-finproc-notallvalidators-vs-bundled.md)。

## 卖法

- 「看见 When calling FinalizeBlock / consensus algorithm guarantees 就已经每个验证者都跑过 Process interchangeable。」
- 「看见 When calling 就已经 Application executes block v / persist decision interchangeable / 已经把块落成这一高的决定 interchangeable。」
- 「看见 When calling 就已经 +2/3 precommit same id(v) 会 Finalize interchangeable / 已经 When 里收到带上头的 Proposal 会先验块头 interchangeable。」

## 为什么错

官方把 When calling `FinalizeBlock` with a block / consensus algorithm guarantees、Application executes block _v_ / persist decision、+2/3 precommit 会调 Finalize 写成三件独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经每个验证者都跑过 Process、已经 Application executes block v，会把 not every validator、not executes block v、not +2/3 precommit already Finalize 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not already every validator 正式三事（472 余量），必须分开 When calling not every validator、When calling not executes block v、When calling not +2/3 precommit already Finalize 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经每个验证者都跑过 Process / 已经 Application executes block v。

## 和相邻反模式

- [finproc-sold-as-allvalidators](finproc-sold-as-allvalidators.md) 是 472 bundled 三事专用，不是本页 When calling not every validator 单句边界。
- [finexec-sold-as-decided](finexec-sold-as-decided.md) 是 466 executes block v 三事，不是本页 When calling not executes block v 单句边界。
