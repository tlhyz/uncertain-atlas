# 反模式：看见 Process 整块执行就当成已经交差 / 看见留着 candidate 就当成已经改了已提交状态 / 看见 read-only 处理就当成已经 mutate committed state

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**例**：[Process MAY 像 Finalize 整块执行 ≠ 已经交差](../../tracks/implementation/worked-example-proccand-vs-execute.md)。

## 塌法

1. 看见 ProcessProposal 里 Application MAY 像处理 FinalizeBlock 那样整块执行 / 看见 immediate execution 跑过了，就当成已经交差，或当成已经是 ExecuteTxState。
2. 看见 any resulting state changes must be kept as candidate state / Application should be ready to discard it in case another block is decided / 看见留着，就当成已经改了上一份已提交状态，或当成已经 Process 回了 Accept 就已经换工作状态。
3. 看见 Application checks/processes the proposed block, which is read-only / 看见处理了，就当成已经改了 *s<sub>p,h-1</sub>*，或当成已经 async 了还能 Reject。

## 为什么会出事

官方写：The Application may fully execute the block as though it was handling `FinalizeBlock`。However, any resulting state changes must be kept as _candidate state_, and the Application should be ready to discard it in case another block is decided。When 也写：The Application checks/processes the proposed block, which is read-only。这不是已经 Finalize + Commit 交差，不是已经改了已提交状态，也不是已经 async 了还能 Reject interchangeable。

## 和相邻反模式

- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是 Prepare/Process 立刻执行出候选那套通用三事 bundled，不是本页这种 ProcessProposal Usage 单独切片。
- [req9noside-sold-as-commit](req9noside-sold-as-commit.md) 是四门不得改已提交状态 bundled，不是本页这种 read-only 处理单独切片。
- [procrespstatus-sold-as-procstatus](procrespstatus-sold-as-procstatus.md) 是 ProcessProposalResponse.status REJECT 就已经当成块非法，不是本页这种 candidate state 不是已经改了已提交状态。
