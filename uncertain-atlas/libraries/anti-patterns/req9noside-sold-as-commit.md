# 反模式：看见 Prepare 不得改已提交状态就当成已经立刻执行就已经交差 / 看见 Process 不得改已提交状态就当成已经 Accept 就已经改了 / 看见 Extend 和 Verify 不得改已提交状态就当成已经签了扩展就已经进状态

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**例**：[Prepare 不得改已提交状态 ≠ 已经立刻执行就已经交差](../../tracks/implementation/worked-example-req9-noside-vs-commit.md)。

## 塌法

1. 看见高度 *h* 的 `PrepareProposal` 不得改 *s<sub>p,h-1</sub>* / 看见立刻执行了，就当成已经交差，或当成已经是 Finalize + Commit。
2. 看见高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>* / 看见回了 Accept，就当成已经改了已提交状态，或当成已经是候选已经是 ExecuteTxState。
3. 看见高度 *h* 的 `ExtendVote` 和 `VerifyVoteExtension` 不得改 *s<sub>p,h-1</sub>* / 看见签了扩展，就当成已经进状态，或当成已经是 *s<sub>h</sub>* 不依赖本高度 *e*。

## 为什么会出事

官方写：正确进程在高度 *h* 叫 `PrepareProposal`、`ProcessProposal`、`ExtendVote` 和 `VerifyVoteExtension`，都不得改上一份已提交状态 *s<sub>p,h-1</sub>*。

## 和相邻反模式

- [req9-notsettled-sold-as-bundled](req9-notsettled-sold-as-bundled.md) 是 Prepare 不得改已提交状态 not already settled / not already finalize-commit / not already mutate-s 正式三事（349 item 1），不是本页 bundled 全段 alone。
- [req9-notaccept-sold-as-bundled](req9-notaccept-sold-as-bundled.md) 是 Process 不得改已提交状态 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 item 2），不是本页 bundled 全段 alone。
- [req9-notextstate-sold-as-bundled](req9-notextstate-sold-as-bundled.md) 是 Extend 和 Verify 不得改已提交状态 not already into-state / not already verified-in / not already ve-dep-34 正式三事（349 item 3），不是本页 bundled 全段 alone。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种 Prepare 不得改已提交状态不是已经立刻执行就已经交差。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选不是已经是 ExecuteTxState，不是本页这种 Process 不得改已提交状态不是已经 Accept 就已经改了。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是本高度状态不得依赖本高度收到的扩展，不是本页这种 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态。
