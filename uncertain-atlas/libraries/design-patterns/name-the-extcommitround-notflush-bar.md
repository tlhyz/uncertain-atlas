# 模式：把 Echo 请求 Message not already Flush / not already delivered / not already settled 正式三事（394 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**例**：[Echo ≠ bundled（394）](../../tracks/implementation/worked-example-extcommitround-notflush-vs-bundled.md)。

## 三个名字

1. **Message 不是已经是 Flush：** 看见填了 Message，不是已经 374 interchangeable / 751 extcommitround-notflush interchangeable。
2. **看见填了 Message 不是已经送到：** 看见能回显，不是已经 374 interchangeable。
3. **看见能填 不是已经交差：** 看见 Echo 请求 Message，不是已经交差 interchangeable。

官方把 ExtendedCommitInfo.round / Finalize 请求 next_validators_hash / Echo 请求 Message 三条核心句拆成三个名字。把它们叫成一个「看见填了 ExtendedCommitInfo 轮就已经是 CommitInfo.round」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 请求 Message 正式三事（394 余量），先数清问的是 Message 是不是已经是 Flush / 374、是不是已经送到 / 374、还是看见能填是不是已经交差，再决定要不要同一次发布。394 extcommitround vs commitinfo bundled unbundling 在本页 item 3 完成。
