# 模式：把 Finalize 何时调用三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[+2/3 precommit 同一 id(v) 才决定再调 Finalize ≠ 已经会调 Finalize](../../tracks/implementation/worked-example-finalize-when-vs-decided.md)。

## 三个名字

1. **+2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize：** 看见到了这一高不是已经是 +2/3 prevote 才锁住再调 ExtendVote。
2. **先把 v 落成这一高的决定再同步调 Finalize 不是已经交差：** 看见决定了不是已经落盘应用状态。
3. **应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头：** 看见回了不是已经是本头 AppHash。

## 为什么要分开叫

官方把 +2/3 precommit 同一 `id(v)` 并且收齐块片才决定再调 Finalize、先把决定落盘再同步调用、应用回 AppHash 和各笔输出后引擎再哈希进 ResultHash 写成三件事。把它们叫成一个「看见到了这一高就已经会调 Finalize」，会把 ExtendVote 何时调用、Finalize 落盘禁令和本头 AppHash 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了这一高就已经会调 Finalize」，先数清问的是 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize、先把 v 落成这一高的决定再同步调 Finalize 不是已经交差，还是应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头，再决定要不要同一次发布。
