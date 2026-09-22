# 反模式：把 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量）说成已经改了已提交状态 / 已经回滚了已提交状态 / 已经进工作状态

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Process 不得改已提交状态 not already accept-mutated ≠ bundled（349）](../../tracks/implementation/worked-example-req9-notaccept-vs-bundled.md)。

## 卖法

把高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>* / 回了 Accept / Accept 了 写成已经改了已提交状态 interchangeable / 已经 accept-mutated interchangeable / 已经 Accept 改状态交差 interchangeable / 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable；把 Reject 了 / 回了 Reject 写成已经回滚了已提交状态 interchangeable / 已经 reject-rollback interchangeable / 已经 Reject 回滚交差 interchangeable；把跑过了 / Process 跑过了 写成已经进工作状态 interchangeable / 已经 workstate interchangeable / 已经工作状态交差 interchangeable，或已经和 349 req9noside bundled / req9noside-sold-as-commit interchangeable / 801 req9-notaccept interchangeable。

## 为什么错

官方把 Process 不得改已提交状态、不是已经回滚了已提交状态、不是已经进工作状态写成三件独立的实现事。把它们卖成 already accept-mutated interchangeable / already reject-rollback interchangeable / already workstate interchangeable，会把 not already accept-mutated、not already reject-rollback、not already workstate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量），必须分开 not already accept-mutated、not already reject-rollback、not already workstate 三件事，不要和 349 / 311 / 33 / 800 / 802 糊成一句。

## 和相邻反模式

- [req9noside-sold-as-commit](req9noside-sold-as-commit.md) 是四门无副作用 bundled 全段，不是本页 Process 不得改已提交状态 item 2 单句边界。
- [req9-notsettled-sold-as-bundled](req9-notsettled-sold-as-bundled.md) 是 Prepare 不得改已提交状态 not already settled（349 item 1），不是本页 not already accept-mutated 边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选不是已经是 ExecuteTxState（311），不是本页 not already accept-mutated / not already workstate 边界。
