# 反模式：把 ProcessProposal candidate state not already committed 正式三事卖成 ProcessProposal 候选执行 bundled / 已经改了已提交状态 / 已经 Process 回了 Accept 就换工作状态

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal candidate state not already committed ≠ bundled](../../tracks/implementation/worked-example-proccand-candidate-notcommitted-vs-bundled.md)。

## 卖法

- 「看见 any resulting state changes must be kept as candidate state / 看见留着 就已经改了已提交状态 interchangeable / 已经 ProcessProposal 候选执行 bundled interchangeable。」
- 「看见 Application should be ready to discard it in case another block is decided 就已经不用再在 Finalize 执行 interchangeable / 已经 candidate 就不需要 Commit interchangeable。」
- 「看见 candidate state 就已经 Process 回了 Accept 就换工作状态 interchangeable / 已经能点名本高度最终 interchangeable。」

## 为什么错

官方把 candidate state not already committed、ready to discard not Finalize apply candidate、candidate not ACCEPT switched working state 写成三件独立的实现事。把它们卖成 ProcessProposal 候选执行 bundled、已经改了已提交状态、已经 Process 回了 Accept 就换工作状态，会把 mutate committed state、Finalize apply candidate、Response ACCEPT 后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal candidate state not already committed 正式三事，必须分开 candidate state not already committed、ready to discard not Finalize apply candidate、candidate not ACCEPT switched working state 三个名字，不要把它们卖成 ProcessProposal 候选执行 bundled / 已经改了已提交状态 / 已经 Process 回了 Accept 就换工作状态。

## 和相邻反模式

- [proccand-sold-as-commit](proccand-sold-as-commit.md) 是 452 bundled 三事专用，不是本页 candidate state not already committed 单句边界。
- [proccand-mayexecute-notcommitted-sold-as-bundled](proccand-mayexecute-notcommitted-sold-as-bundled.md) 是 MAY execute not committed 单句边界，不是本页 candidate must be kept 边界。
- [req9noside-sold-as-commit](req9noside-sold-as-commit.md) 是四门不得改已提交状态 bundled，不是本页 candidate state 边界。
