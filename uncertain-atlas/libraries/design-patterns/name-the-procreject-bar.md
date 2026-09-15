# 模式：把 ProcessProposal REJECT 共识假设正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**例**：[REJECT 时共识假设收到的提案不合法 ≠ 已经当成块非法](../../tracks/implementation/worked-example-procreject-vs-assume.md)。

## 三个名字

1. **REJECT → consensus assumes not valid 不是已经当成块非法 / 已经永久标成非法块：** 看见假设不合法不是已经块非法。
2. **REJECT → prevote nil 不是已经 VerifyVoteExtension REJECT 拒整张票：** 看见验证者 prevote nil 不是已经 Verify 拒 Precommit。
3. **REJECT 共识假设不是已经不能整块执行候选 / 已经交差：** 看见 assumes not valid 不是已经 Process 跑过就意味着已经改了已提交状态。

## 为什么要分开叫

官方把 ProcessProposal REJECT 共识假设写成三个名字。把它们叫成一个「看见 Process 回了 REJECT 就已经当成块非法」，会把 assumes not valid、prevote nil 和整块执行候选一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 回了 REJECT 就已经当成块非法」，先数清问的是 REJECT 时共识假设收到的提案不合法是不是已经当成块非法、验证者 prevote nil 是不是已经 VerifyVoteExtension REJECT，还是 REJECT 共识假设是不是已经不能整块执行候选，再决定要不要同一次发布。
