# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee not every validator 正式三事（472 余量）卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经每个验证者都跑过 Process / 已经 360 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not every validator ≠ bundled（472）](../../tracks/implementation/worked-example-finwhen-notallproc-vs-bundled.md)。

## 卖法

- 「看见 When calling FinalizeBlock / guarantees at least one non-byzantine validator has run ProcessProposal 就已经 every validator has run ProcessProposal interchangeable / 已经 FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable。」
- 「看见 When calling guarantee 就已经 Finalize 时的 Process 保证 bundled interchangeable / 360 bundled interchangeable。」
- 「看见 guarantees at least one 就已经 at least one non-byzantine ran Process not every validator interchangeable / 582 not every validator interchangeable。」

## 为什么错

官方把 When calling guarantee、every validator ran Process、Finalize 时的 Process 保证 bundled、360 item 1 at least one 单句 写成独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经每个验证者都跑过 Process、已经 360 bundled，会把 not every validator、not 360 bundled、not 582 not every validator 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not every validator 正式三事（472 余量），必须分开 not every validator、not Finalize 时的 Process 保证 bundled、not 582 not every validator 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经每个验证者都跑过 Process / 已经 360 bundled。

## 和相邻反模式

- [finwhen-sold-as-bundled](finwhen-sold-as-bundled.md) 是 472 bundled 三事专用，不是本页 When calling guarantee not every validator 单句边界。
- [finprocgua-notallproc-sold-as-bundled](finprocgua-notallproc-sold-as-bundled.md) 是 582 / 360 item 1 专用，不是本页 472 item 1 单句边界。
