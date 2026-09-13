# 反模式：看见 Process 回了 REJECT 就当成已经当成块非法 / 看见 prevote nil 就当成已经 Verify 拒整张票 / 看见 assumes not valid 就当成已经不能整块执行候选

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**例**：[REJECT 时共识假设收到的提案不合法 ≠ 已经当成块非法](../../tracks/implementation/worked-example-procreject-vs-assume.md)。

## 塌法

1. 看见 `ProcessProposalResponse.status` 是 `REJECT` 时共识假设收到的提案不合法 / 看见 consensus assumes the proposal received is not valid，就当成已经当成块非法，或当成已经永久标成非法块。
2. 看见验证者会 prevote nil / 看见 When 里 `REJECT`: _p_ prevotes `nil`，就当成已经 VerifyVoteExtension REJECT 拒整张票，或当成已经 Process 回包栏 bundled 三事 interchangeable。
3. 看见 REJECT 共识假设 / 看见 assumes not valid，就当成已经不能整块执行候选，或当成已经 Process MAY 整块执行就意味着已经交差。

## 为什么会出事

官方写：If `ProcessProposalResponse.status` is `REJECT`, consensus assumes the proposal received is not valid。When 也写：If _p_ is a validator and the returned value is `REJECT`: _p_ prevotes `nil`。Usage 也写：The Application MAY fully execute the block (immediate execution)。However, any resulting state changes must be kept as _candidate state_。这不是已经当成块非法，不是已经 Verify 拒整张票 interchangeable，也不是已经不能整块执行候选。

## 和相邻反模式

- [procrespstatus-sold-as-procstatus](procrespstatus-sold-as-procstatus.md) 是 Process 回包栏 bundled，不是本页这种 REJECT 共识假设单独切片。
- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus 枚举就已经是 prevote nil，不是本页这种 consensus assumes not valid 不是已经当成块非法。
- [proccand-sold-as-commit](proccand-sold-as-commit.md) 是 Process 整块执行就已经交差，不是本页这种 REJECT 不是已经不能整块执行候选。
