# 模式：把 ExtendVote When call / synchronous 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 2。  
**例**：[call / synchronous ≠ bundled](../../tracks/implementation/worked-example-extwhen-call-vs-bundled.md)。

## 三个名字

1. **calls ExtendVote with v 不是 lock values bundled：** 看见 calls ExtendVote with v in ExtendVoteRequest，不是 507 step 1 lock values interchangeable。
2. **synchronous ExtendVote call 不是 ExtendVote 何时调用 bundled：** 看见 The call is synchronous，不是 361 门槛+同步+回包 bundled interchangeable。
3. **step 2 before return extension 不是 ExtendVote When 正式流程 bundled：** 看见 step 2 after lock values before return bytes，不是 438 填 CanonicalVoteExtension / 广播 Precommit interchangeable。

## 为什么要分开叫

官方把 calls ExtendVote with v、synchronous call、step 2 before return extension、lock values bundled（507）、ExtendVote 何时调用 bundled（361）、ExtendVote When 正式流程 bundled（438）写成三个名字。把它们叫成一个「看见设了 lock values 就已经会调 ExtendVote interchangeable、已经能在返回之后再改扩展 interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」，会把 call with v、sync、step 2 顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When call / synchronous 正式三事，先数清问的是 calls ExtendVote with v 是不是 lock values bundled interchangeable、The call is synchronous 是不是 ExtendVote 何时调用 bundled interchangeable、step 2 before return extension 是不是 ExtendVote When 正式流程 bundled interchangeable，再决定要不要同一次发布。
