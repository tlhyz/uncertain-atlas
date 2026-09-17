# 反模式：把 PrepareProposal Usage no checks / crash / nondet 正式三事卖成已经验过重复 / Process REJECT / 必须确定

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[no checks / crash / nondet ≠ bundled](../../tracks/implementation/worked-example-prepareusage-nochecks-vs-bundled.md)。

## 卖法

- 「看见 CometBFT does NOT provide additional validity checks / 看见回了 Prepare 回包就已经验过重复 interchangeable / 已经有应用级重放保护 interchangeable。」
- 「看见 fails to validate PrepareProposalResponse / 引擎崩溃就已经 Process REJECT interchangeable / 已经 prevote nil interchangeable。」
- 「看见 PrepareProposal MAY be non-deterministic 就已经必须确定 interchangeable / 已经和 Process MUST deterministic interchangeable。」

## 为什么错

官方把 no additional validity checks、crash on invalid response、MAY be non-deterministic 写成三件独立的实现事。把它们卖成已经验过重复、Process REJECT、必须确定，会把 no checks、crash、MAY nondet 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage no checks / crash / nondet 正式三事，必须分开 no checks、crash、MAY nondet 三个名字，不要把它们卖成已经验过重复 / Process REJECT / 必须确定。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled 三事，不是本页 no checks 单句专用边界。
- [prepareusage-rawmust-sold-as-bundled](prepareusage-rawmust-sold-as-bundled.md) 是 PrepareProposal Usage raw proposal / MUST remove 正式三事，不是本页 no checks / crash / nondet。
