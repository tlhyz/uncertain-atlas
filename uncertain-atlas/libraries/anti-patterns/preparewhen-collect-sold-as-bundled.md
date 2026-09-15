# 反模式：把 PrepareProposal When collect / synchronous / manipulate 正式三事卖成 raw proposal bundled / 能在返回后再改裁决 / Prepare 改列表 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[collect / synchronous / manipulate ≠ bundled](../../tracks/implementation/worked-example-preparewhen-collect-vs-bundled.md)。

## 卖法

- 「看见 collects txs from mempool in order of priority / creates header 就已经 raw proposal bundled interchangeable / 已经整池可见 interchangeable。」
- 「看见 PrepareProposal call is synchronous 就已经能在返回后再改裁决 interchangeable / 已经 Process 同步 interchangeable。」
- 「看见 Application can manipulate transactions 就已经 Prepare 改列表 bundled interchangeable / 已经从内存池删掉 interchangeable / 已经候选交差 interchangeable。」

## 为什么错

官方把 collect priority、Prepare synchronous call、can manipulate transactions 写成三件独立的实现事。把它们卖成 raw proposal bundled、能在返回后再改裁决、Prepare 改列表 bundled，会把 collect、synchronous、manipulate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When collect / synchronous / manipulate 正式三事，必须分开 collect priority、Prepare synchronous call、can manipulate transactions 三个名字，不要把它们卖成 raw proposal bundled / 能在返回后再改裁决 / Prepare 改列表 bundled。

## 和相邻反模式

- [validvalue-sold-as-prepared](validvalue-sold-as-prepared.md) 是 validValue 跳过 Prepare 三事，不是本页 collect priority 单句专用边界。
- [prepareusage-rawmust-sold-as-bundled](prepareusage-rawmust-sold-as-bundled.md) 是 PrepareProposal Usage raw proposal / MUST remove 正式三事，不是本页 When collect 单句专用边界。
