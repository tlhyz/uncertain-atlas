# 反模式：把 ProcessProposal MAY fully execute not already committed 正式三事卖成 ProcessProposal 候选执行 bundled / 已经交差 / 已经是 ExecuteTxState

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal MAY fully execute not already committed ≠ bundled](../../tracks/implementation/worked-example-proccand-mayexecute-notcommitted-vs-bundled.md)。

## 卖法

- 「看见 ProcessProposal 里 Application MAY 像 Finalize 整块执行 / 看见 immediate execution 跑过了 就已经交差 interchangeable / 已经 ProcessProposal 候选执行 bundled interchangeable。」
- 「看见像 Finalize 那样跑 就已经 ExecuteTxState interchangeable / 已经 Prepare/Process 立刻执行出候选 interchangeable。」
- 「看见 Process 回了 ACCEPT 就已经能点名本高度最终 interchangeable / 已经 Process 回了 Accept 就已经换工作状态 interchangeable。」

## 为什么错

官方把 MAY fully execute not already committed、MAY execute not ExecuteTxState、MAY execute not ACCEPT already final 写成三件独立的实现事。把它们卖成 ProcessProposal 候选执行 bundled、已经交差、已经是 ExecuteTxState，会把 Finalize + Commit 交差、ExecuteTxState、Response ACCEPT 后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal MAY fully execute not already committed 正式三事，必须分开 MAY fully execute not already committed、MAY execute not ExecuteTxState、MAY execute not ACCEPT already final 三个名字，不要把它们卖成 ProcessProposal 候选执行 bundled / 已经交差 / 已经是 ExecuteTxState。

## 和相邻反模式

- [proccand-sold-as-commit](proccand-sold-as-commit.md) 是 452 bundled 三事专用，不是本页 MAY fully execute not already committed 单句边界。
- [procreject-assume-notexecute-sold-as-bundled](procreject-assume-notexecute-sold-as-bundled.md) 是 REJECT 与 candidate 可并存边界，不是本页 MAY execute not committed 边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是 Prepare/Process 候选 bundled，不是本页 Process Usage MAY execute 单句边界。
