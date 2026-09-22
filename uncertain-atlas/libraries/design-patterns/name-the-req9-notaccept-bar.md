# 模式：把 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 9 [*all*, no-side-effects]。  
**例**：[Process 不得改已提交状态 not already accept-mutated ≠ bundled（349）](../../tracks/implementation/worked-example-req9-notaccept-vs-bundled.md)。

## 三个名字

1. **Process 不得改已提交状态 不是 already accept-mutated：** 看见高度 *h* 的 `ProcessProposal` 不得改 *s<sub>p,h-1</sub>* / 回了 Accept / Accept 了，不是已经改了已提交状态 interchangeable / 已经 accept-mutated interchangeable / 已经 Accept 改状态交差 interchangeable，不是 349 req9noside bundled interchangeable / req9noside-sold-as-commit interchangeable。

2. **Reject 了 不是 already reject-rollback：** 看见 Reject 了 / 回了 Reject / 拒了提案，不是已经回滚了已提交状态 interchangeable / 已经 reject-rollback interchangeable / 已经 Reject 回滚交差 interchangeable，不是 33 fourgates interchangeable / 311 candidate interchangeable。

3. **跑过了 不是 already workstate：** 看见跑过了 / Process 跑过了 / 处理过提案，不是已经进工作状态 interchangeable / 已经 workstate interchangeable / 已经工作状态交差 interchangeable，不是 800 req9-notsettled interchangeable / 802 req9-notextstate interchangeable。

官方把 Process 不得改已提交状态、不是已经回滚了已提交状态、不是已经进工作状态写成三个名字。把它们叫成一个「看见 Accept 了就已经改了 interchangeable / 就已经回滚了 interchangeable / 就已经进工作状态 interchangeable」，会把 not already accept-mutated、not already reject-rollback、not already workstate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 不得改已提交状态不是已经 Accept 就已经改了 not already accept-mutated / not already reject-rollback / not already workstate 正式三事（349 余量），先数清问的是 Process 不得改已提交状态 是不是 already accept-mutated / 349 / req9noside-sold-as-commit，是不是 Reject 了 是不是 already reject-rollback，还是跑过了 是不是 already workstate，再决定要不要同一次发布。349 req9 vs commit bundled unbundling 在本页 item 2 续。
