# 反模式：把 PrepareProposal When return / use-as-proposal 正式三事卖成 raw proposal bundled / Process 紧跟 Prepare / validValue 跳过 Prepare

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[return / use-as-proposal ≠ bundled](../../tracks/implementation/worked-example-preparewhen-return-vs-bundled.md)。

## 卖法

- 「看见 includes transaction list in return parameters 就已经 raw proposal bundled interchangeable / 已经能改这套就交差 interchangeable。」
- 「看见 returns from the call 就已经 Process 紧跟 Prepare interchangeable / 已经不用再 Process interchangeable。」
- 「看见 uses the possibly modified block as proposal 就已经 validValue 跳过 Prepare interchangeable / 已经 Process 八栏齐 interchangeable。」

## 为什么错

官方把 includes in return、returns from call、uses as proposal 写成三件独立的实现事。把它们卖成 raw proposal bundled、Process 紧跟 Prepare、validValue 跳过 Prepare，会把 return、returns、use-as-proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事，必须分开 includes tx list in return、returns from call、uses modified block as proposal 三个名字，不要把它们卖成 raw proposal bundled / Process 紧跟 Prepare / validValue 跳过 Prepare。

## 和相邻反模式

- [preparewhen-collect-sold-as-bundled](preparewhen-collect-sold-as-bundled.md) 是 PrepareProposal When collect / synchronous / manipulate 三事，不是本页 return / use-as-proposal 单句专用边界。
- [prepareusage-rawmust-sold-as-bundled](prepareusage-rawmust-sold-as-bundled.md) 是 PrepareProposal Usage raw proposal / MUST remove 正式三事，不是本页 When includes in return 单句专用边界。
