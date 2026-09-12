# 反模式：看见收到提案和全部块片并且 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 就当成已经会调 ExtendVote / 看见 ExtendVote 调用是同步的就当成已经能在返回之后再改扩展 / 看见应用回了一串字节共识算法不解释就当成已经是同一份扩展

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote ≠ 已经会调 ExtendVote](../../tracks/implementation/worked-example-extend-when-vs-locked.md)。

## 塌法

1. 看见收到提案和全部块片、并且 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote / 看见到了 prevote 步，就当成已经会调 ExtendVote，或当成已经是一轮只能交出一份扩展。
2. 看见 ExtendVote 调用是同步的 / 看见引擎在等回包，就当成已经能在返回之后再改扩展，或当成已经离开关键路径。
3. 看见应用回了一串字节、共识算法不解释 / 看见回了 extension，就当成已经是同一份扩展，或当成已经包进 CanonicalVoteExtension。

## 为什么会出事

官方写：验证者 *p* 处在 prevote 步，收到提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 prevote，才锁住 *v*，再调 `ExtendVote`。这次调用是同步的。应用回一份字节数组，共识算法不解释。

## 和相邻反模式

- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮只能交出一份扩展就已经是每一高度一份，不是本页这种 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能稍后改裁决，不是本页这种 ExtendVote 调用是同步的不是已经能在返回之后再改扩展。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页这种回包字节不被共识算法解释不是已经是同一份扩展。
