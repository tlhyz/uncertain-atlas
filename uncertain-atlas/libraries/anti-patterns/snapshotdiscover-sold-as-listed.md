# 反模式：看见 ListSnapshots 回了就当成已经有了全部快照 / 看见挑了最高就当成已经收下 / 看见 Offer 被拒就当成已经停

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**例**：[ListSnapshots 回了 ≠ 已经有了全部快照](../../tracks/implementation/worked-example-snapshot-discover-vs-offer.md)。

## 塌法

1. 看见问了邻居 / 看见 ListSnapshots 回了，就当成已经有了全部快照，或当成已经没有上限。
2. 看见挑了最高 / 看见按高度、格式、邻居数排了，就当成已经是应用收下的那份，或当成已经装完。
3. 看见 Offer 被拒 / 看见拒了格式或邻居，就当成已经没有快照，或当成已经停。

## 为什么会出事

官方写：每个节点限 10 份。挑完还要经 OfferSnapshot 交给应用。应用拒了，CometBFT 会继续发现并继续 Offer，直到收下或应用中止。

## 和相邻反模式

- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下 ≠ 已经装完，不是本页这种还没 Offer。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是启动对齐 ≠ 已经是快照重放，不是本页。
