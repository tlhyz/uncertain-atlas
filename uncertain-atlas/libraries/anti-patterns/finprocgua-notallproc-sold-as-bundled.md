# 反模式：把 at least one non-byzantine ran Process not every validator 正式三事（360 余量）卖成 Finalize 时的 Process 保证 bundled / 已经每个验证者都跑过 Process / 已经是提议者那边也会叫 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[at least one non-byzantine ran Process not every validator ≠ bundled（360）](../../tracks/implementation/worked-example-finprocgua-notallproc-vs-bundled.md)。

## 卖法

- 「看见 at least one non-byzantine validator has run ProcessProposal 就已经 every validator has run ProcessProposal interchangeable / 已经 Finalize 时的 Process 保证 bundled interchangeable。」
- 「看见 guarantees at least one 就已经 Process 也会在提议者那边叫 interchangeable / 已经提议者 Process 过就代表全网都 Process 过 interchangeable。」
- 「看见要 Finalize 了有共识保证 就已经 Application executes block v / persist decision interchangeable / 已经 When calling ProcessProposal guarantee bundled interchangeable。」

## 为什么错

官方把 at least one non-byzantine validator has run ProcessProposal、every validator ran Process、proposer also Process 写成独立的实现事。把它们卖成 Finalize 时的 Process 保证 bundled、已经每个验证者都跑过 Process、已经是提议者那边也会叫 Process，会把 not every validator、not proposer means everyone Processed、not executes block v 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 at least one non-byzantine ran Process not every validator 正式三事（360 余量），必须分开 not every validator、not proposer means everyone Processed、not executes block v 三个名字，不要把它们卖成 Finalize 时的 Process 保证 bundled / 已经每个验证者都跑过 Process / 已经是提议者那边也会叫 Process。

## 和相邻反模式

- [finalize-sold-as-processed](finalize-sold-as-processed.md) 是 360 bundled 三事专用，不是本页 at least one not every validator 单句边界。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 351 专用，不是本页 360 item 1 余量边界。
