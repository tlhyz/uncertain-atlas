# 模式：把 ExtendVote 请求栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**例**：[ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希 ≠ 已经跑过 Process](../../tracks/implementation/worked-example-extreqhash-vs-process.md)。

## 三个名字

1. **ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希不是已经跑过 Process：** 看见填了 hash 不是已经交差。
2. **ExtendVoteRequest.height 是拟议块高度（用来对一下）不是已经对上了拟议块：** 看见填了 height 不是已经会调 ExtendVote。
3. **ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳不是已经验过票上时间：** 看见填了 time 不是已经交差。

## 为什么要分开叫

官方把 `hash` 是扩展要指的那份拟议块头哈希、`height` 是拟议块高度（用来对一下）、`time` 是扩展要指的那份拟议块时间戳写成三件事。把它们叫成一个「看见填了 ExtendVote 请求栏就已经跑过 Process」，会把已经跑过 Process、已经对上了拟议块和已经验过票上时间一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求栏就已经跑过 Process」，先数清问的是 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希不是已经跑过 Process、ExtendVoteRequest.height 是拟议块高度（用来对一下）不是已经对上了拟议块，还是 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳不是已经验过票上时间，再决定要不要同一次发布。
