# 反模式：看见 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希就当成已经跑过 Process / 看见 ExtendVoteRequest.height 是拟议块高度（用来对一下）就当成已经对上了拟议块 / 看见 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳就当成已经验过票上时间

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**例**：[ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希 ≠ 已经跑过 Process](../../tracks/implementation/worked-example-extreqhash-vs-process.md)。

## 塌法

1. 看见 `ExtendVoteRequest.hash` 是扩展要指的那份拟议块头哈希 / 看见填了 hash，就当成已经跑过 Process，或当成已经交差。
2. 看见 `ExtendVoteRequest.height` 是拟议块高度（用来对一下） / 看见填了 height，就当成已经对上了拟议块，或当成已经会调 ExtendVote。
3. 看见 `ExtendVoteRequest.time` 是扩展要指的那份拟议块时间戳 / 看见填了 time，就当成已经验过票上时间，或当成已经交差。

## 为什么会出事

官方写：`hash` 是扩展要指的那份拟议块的头哈希。`height` 是拟议块高度，用来对一下。`time` 是扩展要指的那份拟议块的时间戳。看见填了栏，不是已经对该块跑过 Process，也不是请求内容已经对应拟议块，也不是票上时间已经验过。

## 和相邻反模式

- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是请求里的 hash 不是已经对该块跑过 Process，不是本页这种 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希不是已经跑过 Process。
- [extreq-sold-as-precommit](extreq-sold-as-precommit.md) 是请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote，不是本页这种 ExtendVoteRequest.height 是拟议块高度（用来对一下）不是已经对上了拟议块。
- [timestamp-sold-as-checked](timestamp-sold-as-checked.md) 是票上 Timestamp 就已经验过，不是本页这种 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳不是已经验过票上时间。
