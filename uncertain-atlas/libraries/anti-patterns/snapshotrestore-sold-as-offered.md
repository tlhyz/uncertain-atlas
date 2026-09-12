# 反模式：看见 OfferSnapshot 收下了就当成已经装完 / 看见一块 chunk 收下了就当成已经齐 / 看见拉失败换一份就当成已经能接着装

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**例**：[Offer 收下 ≠ 已经装完](../../tracks/implementation/worked-example-snapshot-restore-vs-offer.md)。

## 塌法

1. 看见 OfferSnapshot 收下了 / 看见选了这份快照，就当成已经装完，或当成已经有了全部块。
2. 看见 ApplySnapshotChunk 收下了一块 / 看见回了再拉，就当成已经齐，或当成已经交差。
3. 看见拉一块失败 / 看见换了一份快照，就当成已经能接着装，或当成已经同一份。

## 为什么会出事

官方写：Offer 收下之后才按顺序装 chunk。应用可以回再拉、封禁或拒快照。一段时间拉不到一块会拒这份再换一份；能不能重新开始装由应用决定。

## 和相邻反模式

- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是启动对齐 ≠ 已经是快照重放，不是本页这种 Offer 收下还没装。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是块进 store ≠ 已经 Commit，不是本页。
