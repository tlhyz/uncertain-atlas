# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量）卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经是提议者那边也会叫 Process / 已经 351 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed ≠ bundled（472）](../../tracks/implementation/worked-example-finwhen-notproposer-vs-bundled.md)。

## 卖法

- 「看见 guarantees at least one non-byzantine validator has run ProcessProposal 就已经 proposer means everyone Processed interchangeable / 已经 FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable。」
- 「看见 at least one 就已经 Process 也会在提议者那边叫 interchangeable / 351 Process also on proposer interchangeable。」
- 「看见 guarantees at least one 就已经 at least one not proposer interchangeable / 582 not proposer interchangeable。」

## 为什么错

官方把 at least one guarantee、proposer means everyone Processed、Process 也会在提议者那边叫、360 item 1 not proposer 单句 写成独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经是提议者那边也会叫 Process、已经 351 bundled，会把 not proposer means everyone Processed、not 351 proposer path、not 582 not proposer 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量），必须分开 not proposer means everyone Processed、not Process 也会在提议者那边叫、not 582 not proposer 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经是提议者那边也会叫 Process / 已经 351 bundled。

## 和相邻反模式

- [finwhen-sold-as-bundled](finwhen-sold-as-bundled.md) 是 472 bundled 三事专用，不是本页 When calling guarantee not proposer means everyone Processed 单句边界。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 351 专用，不是本页 472 item 2 单句边界。
- [finprocgua-notallproc-sold-as-bundled](finprocgua-notallproc-sold-as-bundled.md) 是 582 / 360 item 1 专用，不是本页 472 item 2 单句边界。
