# 模式：把 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**例**：[Prepare 不得改已提交状态 not already settled ≠ bundled（349）](../../tracks/implementation/worked-example-req9-notsettled-vs-bundled.md)。

## 三个名字

1. **Prepare 不得改已提交状态 不是 already settled：** 看见高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>* / 立刻执行了 / Prepare 回了，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable。

2. **立刻执行了 不是 already finalize-commit：** 看见立刻执行了 / Prepare 回了 / 能立刻执行，不是已经是 Finalize + Commit interchangeable / 已经 finalize-commit interchangeable / 已经 Finalize 交差 interchangeable，不是 33 fourgates interchangeable / 311 candidate interchangeable。

3. **能改列表 不是 already mutate-s：** 看见能改列表 / Prepare 能改交易列表 / 回了列表，不是已经能改 *s* interchangeable / 已经 mutate-s interchangeable / 已经改状态交差 interchangeable，不是 801 req9-notaccept interchangeable / 802 req9-notextstate interchangeable。

官方把 Prepare 不得改已提交状态、不是已经是 Finalize + Commit、不是已经能改 *s* 写成三个名字。把它们叫成一个「看见立刻执行了就已经交差 interchangeable / 就已经是 Finalize + Commit interchangeable / 就已经能改 *s* interchangeable」，会把 not already settled、not already finalize-commit、not already mutate-s 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 不得改已提交状态不是已经立刻执行就已经交差 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 余量），先数清问的是 Prepare 不得改已提交状态 是不是 already settled / 349 / req9noside-sold-as-commit，是不是立刻执行了 是不是 already finalize-commit，还是能改列表 是不是 already mutate-s，再决定要不要同一次发布。349 req9 vs commit bundled unbundling 在本页 item 1 启动。
