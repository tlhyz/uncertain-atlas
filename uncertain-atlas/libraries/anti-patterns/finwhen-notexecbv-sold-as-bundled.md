# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision 正式三事（472 余量）卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经 persist decision / 已经 Application executes block v

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision ≠ bundled（472）](../../tracks/implementation/worked-example-finwhen-notexecbv-vs-bundled.md)。

## 卖法

- 「看见 When calling FinalizeBlock / guarantees at least one non-byzantine validator has run ProcessProposal 就已经 persist decision interchangeable / 已经 FinalizeBlock When calling ProcessProposal guarantee bundled interchangeable。」
- 「看见 at least one 就已经 Application executes block v interchangeable / 466 executes block v interchangeable。」
- 「看见 guarantees at least one 就已经 at least one not executes block v interchangeable / 582 not executes block v interchangeable。」

## 为什么错

官方把 at least one guarantee、When 第 3 步 Application executes block _v_ / persist decision、466 When 流程 executes block _v_、360 item 1 not executes block v 单句 写成独立的实现事。把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled、已经 persist decision、已经 Application executes block v，会把 not executes block v / persist decision、not 466 bundled、not 582 not executes block v 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision 正式三事（472 余量），必须分开 not executes block v / persist decision、not Application executes block v bundled、not 582 not executes block v 三个名字，不要把它们卖成 FinalizeBlock When calling ProcessProposal guarantee bundled / 已经 persist decision / 已经 Application executes block v。

## 和相邻反模式

- [finwhen-sold-as-bundled](finwhen-sold-as-bundled.md) 是 472 bundled 三事专用，不是本页 When calling guarantee not executes block v 单句边界。
- [finalizewhen-sold-as-decided](finalizewhen-sold-as-decided.md) 是 362 / 466 When 流程专用，不是本页 472 item 3 单句边界。
- [finprocgua-notallproc-sold-as-bundled](finprocgua-notallproc-sold-as-bundled.md) 是 582 / 360 item 1 专用，不是本页 472 item 3 单句边界。
