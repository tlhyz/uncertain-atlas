# 模式：把 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**例**：[Extend 和 Verify 不得改已提交状态 not already into-state ≠ bundled（349）](../../tracks/implementation/worked-example-req9-notextstate-vs-bundled.md)。

## 三个名字

1. **Extend 和 Verify 不得改已提交状态 不是 already into-state：** 看见高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>* / 签了扩展 / 扩展签了，不是已经写进已提交状态 interchangeable / 已经 into-state interchangeable / 已经进状态交差 interchangeable，不是 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable。

2. **Verify 过了 不是 already verified-in：** 看见 Verify 过了 / VerifyVoteExtension 过了 / 扩展验过了，不是已经进状态 interchangeable / 已经 verified-in interchangeable / 已经 Verify 进状态交差 interchangeable，不是 34 voteext interchangeable / 311 candidate interchangeable。

3. **扩展在 不是 already ve-dep-34：** 看见扩展在 / 扩展写在票上 / 本高度有扩展，不是已经是 34 那种本高度状态不得依赖本高度收到的扩展 interchangeable / 已经 ve-dep-34 interchangeable / 已经 34 交差 interchangeable，不是 800 req9-notsettled interchangeable / 801 req9-notaccept interchangeable。

官方把 Extend 和 Verify 不得改已提交状态、不是已经进状态、不是已经是 34 写成三个名字。把它们叫成一个「看见签了扩展就已经进状态 interchangeable / 就已经进状态 interchangeable / 就已经是 34 interchangeable」，会把 not already into-state、not already verified-in、not already ve-dep-34 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 余量），先数清问的是 Extend 和 Verify 不得改已提交状态 是不是 already into-state / 349 / req9noside-sold-as-commit，是不是 Verify 过了 是不是 already verified-in，还是扩展在 是不是 already ve-dep-34，再决定要不要同一次发布。349 req9 vs commit bundled unbundling 在本页 item 3 完成。
