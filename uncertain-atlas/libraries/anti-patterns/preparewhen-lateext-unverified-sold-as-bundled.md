# 反模式：把 PrepareProposal When +2/3 late extensions not verified 正式三事卖成迟到扩展 bundled / 已经 Verify 过 / 引擎会再 Verify

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[+2/3 late extensions not verified ≠ bundled](../../tracks/implementation/worked-example-preparewhen-lateext-unverified-vs-bundled.md)。

## 卖法

- 「看见 last_commit 里有扩展 就已经 Verify 过 interchangeable / 已经 Accept interchangeable。」
- 「看见 MAY 用 commit info 扩展改提案 就已经 Verify 过 interchangeable / 已经进了块 interchangeable。」
- 「看见建议按 Verify 同款逻辑再看一遍 就已经是引擎会再 Verify interchangeable / 已经 Req 6 已经测过 interchangeable。」

## 为什么错

官方把 +2/3 commit info extensions not verified、MAY use extensions、suggested validate like Verify 写成三件独立的实现事。把它们卖成迟到扩展 bundled、已经 Verify 过、引擎会再 Verify，会把未 Verify、MAY 使用、建议自验三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When +2/3 late extensions not verified 正式三事，必须分开 +2/3 commit info extensions not verified、MAY use commit info extensions、suggested validate like Verify 三个名字，不要把它们卖成迟到扩展 bundled / 已经 Verify 过 / 引擎会再 Verify。

## 和相邻反模式

- [lateext-sold-as-verified](lateext-sold-as-verified.md) 是 352 bundled 专用；本页是 PrepareProposal When +2/3 not verified 单句边界。
- [verifywhen-latemay-sold-as-bundled](verifywhen-latemay-sold-as-bundled.md) 是 Verify When MAY add without Verify 单句，不是本页 PrepareProposal 侧 not verified 单句边界。
- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是 Verify When 正式流程 bundled，不是本页 suggested validate like Verify 单句边界。
