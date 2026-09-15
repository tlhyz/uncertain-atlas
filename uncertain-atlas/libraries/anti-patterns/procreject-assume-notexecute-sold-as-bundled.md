# 反模式：把 ProcessProposal REJECT consensus assume not can't execute candidate 正式三事卖成 Process REJECT consensus assume bundled / 已经不能整块执行候选 / 已经改了已提交状态

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal REJECT not can't execute candidate ≠ bundled](../../tracks/implementation/worked-example-procreject-assume-notexecute-vs-bundled.md)。

## 卖法

- 「看见 REJECT 共识假设 / 看见 assumes not valid 就已经不能整块执行候选 interchangeable / 已经 Process REJECT consensus assume bundled interchangeable。」
- 「看见 MAY fully execute 就已经改了已提交状态 interchangeable / 已经 ExecuteTxState interchangeable / 已经 Process MAY 整块执行就意味着已经交差 interchangeable。」
- 「看见 candidate state 就已经 Finalize + Commit 交差 interchangeable / 已经 Process 跑过就意味着已经 committed interchangeable。」

## 为什么错

官方把 REJECT not can't execute candidate、candidate state not already committed、REJECT assume not already settled 写成三件独立的实现事。把它们卖成 Process REJECT consensus assume bundled、已经不能整块执行候选、已经改了已提交状态，会把 MAY execute、candidate state、Finalize + Commit 交差三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT consensus assume not can't execute candidate 正式三事，必须分开 REJECT not can't execute candidate、candidate state not already committed、REJECT assume not already settled 三个名字，不要把它们卖成 Process REJECT consensus assume bundled / 已经不能整块执行候选 / 已经改了已提交状态。

## 和相邻反模式

- [procreject-assume-notblockinvalid-sold-as-bundled](procreject-assume-notblockinvalid-sold-as-bundled.md) 是 assumes not valid not block invalid 单句边界，不是本页 REJECT not can't execute candidate 边界。
- [procreject-prevote-notverify-sold-as-bundled](procreject-prevote-notverify-sold-as-bundled.md) 是 prevote nil not Verify whole vote 单句边界，不是本页 candidate 边界。
- [proccand-sold-as-commit](proccand-sold-as-commit.md) 是 Process MAY 整块执行就已经交差，不是本页 REJECT 与 candidate 可并存边界。
