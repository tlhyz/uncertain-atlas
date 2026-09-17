# 反模式：把 VerifyVoteExtension Usage hash does not guarantee Process 正式三事卖成 Verify Usage bundled / 已经对该块跑过 Process / 已经是提议者那边也会叫 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[hash does not guarantee Process ≠ bundled](../../tracks/implementation/worked-example-verifyusage-hashproc-vs-bundled.md)。

## 卖法

- 「看见请求里的 hash / 看见指向某块 就已经对该块跑过 Process interchangeable / 已经 Process 过 interchangeable。」
- 「看见有 hash 就已经 Verify Usage bundled interchangeable / 已经验过扩展 interchangeable。」
- 「看见 hash 不保证 Process 就已经是提议者那边也会叫 Process interchangeable / 已经不用再 Process interchangeable。」

## 为什么错

官方把 hash points to a block、does not guarantee exposed via ProcessProposal、hash does not guarantee Process 写成三件独立的实现事。把它们卖成 Verify Usage bundled、已经 Process 过、提议者也会叫 Process，会把有 hash、不保证 Process、不是已经 Process 过三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage hash does not guarantee Process 正式三事，必须分开 hash points to a block、does not guarantee ProcessProposal、hash does not guarantee Process 三个名字，不要把它们卖成 Verify Usage bundled / 已经 Process 过 / 提议者也会叫 Process。

## 和相邻反模式

- [verifyusage-localproc-sold-as-bundled](verifyusage-localproc-sold-as-bundled.md) 是 353 item 2 / 522 边界，不是本页 hash Process 单句边界。
- [verifyusage-emptyext-sold-as-bundled](verifyusage-emptyext-sold-as-bundled.md) 是 353 item 1 / 521 边界，不是本页 hash Process 单句边界。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是 353 bundled 专用；本页是 hash does not guarantee Process 单句边界。
