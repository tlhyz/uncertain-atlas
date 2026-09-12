# 模式：把 ExtendVote 何时调用三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote ≠ 已经会调 ExtendVote](../../tracks/implementation/worked-example-extend-when-vs-locked.md)。

## 三个名字

1. **+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote：** 看见到了 prevote 步不是已经是一轮只能交出一份扩展。
2. **ExtendVote 调用是同步的不是已经能在返回之后再改扩展：** 看见引擎在等回包不是已经离开关键路径。
3. **回包字节不被共识算法解释不是已经是同一份扩展：** 看见回了 extension 不是已经包进 CanonicalVoteExtension。

## 为什么要分开叫

官方把 +2/3 prevote 同一 `id(v)` 并且收齐块片才锁住再调 ExtendVote、这次调用是同步的、回包字节不被共识算法解释写成三件事。把它们叫成一个「看见到了 prevote 步就已经会调 ExtendVote」，会把一轮一份扩展、Process 同步和两份扩展两份签一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了 prevote 步就已经会调 ExtendVote」，先数清问的是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote、ExtendVote 调用是同步的不是已经能在返回之后再改扩展，还是回包字节不被共识算法解释不是已经是同一份扩展，再决定要不要同一次发布。
