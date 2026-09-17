# 反模式：看见同一高度换轮就当成已经换了集合 / 看见新验证者加进来就当成已经能跳到队头 / 看见优先级差被缩放就当成已经按人头轮

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md)。  
**例**：[同一高度换轮 ≠ 已经换了集合](../../tracks/consensus/worked-example-round-vs-set.md)。

## 塌法

1. 看见同一高度换轮 / 看见还用同一套验证者，就当成已经换成应用刚回的那套。
2. 看见新验证者加进来 / 看见初始优先级被往后放，就当成已经能靠退出再加入跳到队头。
3. 看见优先级差被缩放 / 看见范围被压住，就当成已经按人头轮，或当成已经没有优先级。
4. 看见应用回了更新，就当成本高度各轮已经用上。
5. 看见下一轮换了人，就当成集合已经变了。

## 为什么会出事

官方写：同一高度各轮用同一套验证者。集合更新是高度之间的事。新加入的初始优先级被往后放，为的是防止退出再加入往前跳。优先级差会被压住，不是已经按人头轮。

## 和相邻反模式

- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了 ≠ 已经从池里删掉，不是本页这种集合。
- [state-sold-as-block](state-sold-as-block.md) 是本地 State ≠ 已经进了块，不是本页。
