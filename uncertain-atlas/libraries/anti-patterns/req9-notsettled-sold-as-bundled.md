# 反模式：把 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量）说成已经交差 / 已经是 Finalize + Commit / 已经能改 s

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Prepare 不得改已提交状态 not already settled ≠ bundled（349）](../../tracks/implementation/worked-example-req9-notsettled-vs-bundled.md)。

## 卖法

把高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>* / 立刻执行了 / Prepare 回了 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable；把立刻执行了 / Prepare 回了 写成已经是 Finalize + Commit interchangeable / 已经 finalize-commit interchangeable / 已经 Finalize 交差 interchangeable；把能改列表 / Prepare 能改交易列表 写成已经能改 *s* interchangeable / 已经 mutate-s interchangeable / 已经改状态交差 interchangeable，或已经和 349 req9noside bundled / req9noside-sold-as-commit interchangeable / 800 req9-notsettled interchangeable。

## 为什么错

官方把 Prepare 不得改已提交状态、不是已经是 Finalize + Commit、不是已经能改 *s* 写成三件独立的实现事。把它们卖成 already settled interchangeable / already finalize-commit interchangeable / already mutate-s interchangeable，会把 not already settled、not already finalize-commit、not already mutate-s 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量），必须分开 not already settled、not already finalize-commit、not already mutate-s 三件事，不要和 349 / 33 / 311 / 801 / 802 糊成一句。

## 和相邻反模式

- [req9noside-sold-as-commit](req9noside-sold-as-commit.md) 是四门无副作用 bundled 全段，不是本页 Prepare 不得改已提交状态 item 1 单句边界。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算（33），不是本页 not already settled 边界。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选不是已经是 ExecuteTxState（311），不是本页 not already mutate-s 边界。
