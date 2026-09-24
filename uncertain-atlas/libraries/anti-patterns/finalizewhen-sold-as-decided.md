# 反模式：看见收到提案和全部块片并且 +2/3 precommit 同一 id(v) 才决定再调 Finalize 就当成已经会调 Finalize / 看见先把 v 落成这一高的决定再同步调 Finalize 就当成已经交差 / 看见应用回了 AppHash 和各笔输出引擎把输出哈希进 ResultHash 就当成已经印进本头

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[+2/3 precommit 同一 id(v) 才决定再调 Finalize ≠ 已经会调 Finalize](../../tracks/implementation/worked-example-finalize-when-vs-decided.md)。

## 塌法

1. 看见收到提案和全部块片、并且 +2/3 precommit 同一 `id(v)` 才决定再调 Finalize / 看见到了这一高，就当成已经会调 Finalize，或当成已经是 +2/3 prevote 才锁住再调 ExtendVote。
2. 看见先把 *v* 落成这一高的决定、再同步调 Finalize / 看见决定了，就当成已经交差，或当成已经落盘应用状态。
3. 看见应用回了 AppHash 和各笔输出、引擎把输出哈希进 ResultHash / 看见回了，就当成已经印进本头，或当成已经是本头 AppHash。

## 为什么会出事

官方写：节点 *p* 处在高度 *h*，收到提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 precommit，才决定 *v*，再调 `FinalizeBlock`。先把 *v* 落成这一高的决定，再同步调用。应用回 AppHash 和各笔输出后，引擎把这些输出哈希进 ResultHash。

## 和相邻反模式

- [finwhen-notwillcall-sold-as-bundled](finwhen-notwillcall-sold-as-bundled.md) 是 +2/3 precommit 才决定再调 not already will-call / not already decided / not already settled 正式三事（362 item 1），不是本页 bundled 全段 alone。
- [finwhen-notpersist-sold-as-bundled](finwhen-notpersist-sold-as-bundled.md) 是落决定再同步调 not already settled / not already app-persist / not already sync-settled 正式三事（362 item 2），不是本页 bundled 全段 alone。
- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote，不是本页这种 +2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 改了就已经落盘，不是本页这种先把 v 落成这一高的决定再同步调 Finalize 不是已经交差。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页这种应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头。
