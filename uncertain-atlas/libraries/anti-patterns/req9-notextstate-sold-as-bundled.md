# 反模式：把 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量）说成已经写进已提交状态 / 已经进状态 / 已经是 34

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Extend 和 Verify 不得改已提交状态 not already into-state ≠ bundled（349）](../../tracks/implementation/worked-example-req9-notextstate-vs-bundled.md)。

## 卖法

把高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>* / 签了扩展 / 扩展签了 写成已经写进已提交状态 interchangeable / 已经 into-state interchangeable / 已经进状态交差 interchangeable / 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable；把 Verify 过了 / VerifyVoteExtension 过了 写成已经进状态 interchangeable / 已经 verified-in interchangeable / 已经 Verify 进状态交差 interchangeable；把扩展在 / 扩展写在票上 写成已经是 34 那种本高度状态不得依赖本高度收到的扩展 interchangeable / 已经 ve-dep-34 interchangeable / 已经 34 交差 interchangeable，或已经和 349 req9noside bundled / req9noside-sold-as-commit interchangeable / 802 req9-notextstate interchangeable。

## 为什么错

官方把 Extend 和 Verify 不得改已提交状态、不是已经进状态、不是已经是 34 写成三件独立的实现事。把它们卖成 already into-state interchangeable / already verified-in interchangeable / already ve-dep-34 interchangeable，会把 not already into-state、not already verified-in、not already ve-dep-34 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量），必须分开 not already into-state、not already verified-in、not already ve-dep-34 三件事，不要和 349 / 34 / 311 / 800 / 801 糊成一句。

## 和相邻反模式

- [req9noside-sold-as-commit](req9noside-sold-as-commit.md) 是四门无副作用 bundled 全段，不是本页 Extend 和 Verify 不得改已提交状态 item 3 单句边界。
- [req9-notsettled-sold-as-bundled](req9-notsettled-sold-as-bundled.md) 是 Prepare 不得改已提交状态 not already settled（349 item 1），不是本页 not already into-state 边界。
- [req9-notaccept-sold-as-bundled](req9-notaccept-sold-as-bundled.md) 是 Process 不得改已提交状态 not already accept-mutated（349 item 2），不是本页 not already into-state 边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是本高度状态不得依赖本高度收到的扩展（34），不是本页 not already ve-dep-34 单句边界。
