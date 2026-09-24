# 反模式：看见快照全字段（含 Metadata）对上就当成已经装完 / 看见引擎不解释 format / hash 就当成已经轻验 AppHash / 看见空快照也至少 1 块就当成已经齐

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**例**：[快照全字段（含 Metadata）对上 ≠ 已经装完](../../tracks/implementation/worked-example-snapshot-vs-identical.md)。

## 塌法

1. 看见快照全字段（含 `Metadata`）对上才算同一份、同一份才能从各节点拉 chunk / 看见对上了，就当成已经装完，或当成已经交差。
2. 看见 `format` 是应用自己的版本、引擎不解释 `format` / `hash`、只比较 `hash` / 看见有哈希，就当成已经轻验 AppHash，或当成已经从创世重放。
3. 看见空快照也至少 1 块、网上一份快照报文最多 4 MB / 看见有块数，就当成已经齐，或当成已经是共识常数。

## 为什么会出事

官方写：一份快照只有全部字段都相等（包括 `Metadata`）才算各节点同一份。同一份才能从各节点拉 chunk。`format` 是应用自己的快照格式，CometBFT 不解释。`hash` 只比较、不解释。`chunks` 至少是 1，哪怕是空快照。网上一份快照报文最多 4 MB。

## 和相邻反模式

- [snapident-notrestored-sold-as-bundled](snapident-notrestored-sold-as-bundled.md) 是快照全字段含 Metadata 对上 not already restored / not already settled / not already complete 正式三事（368 item 1），不是本页 bundled 全段 alone。
- [snapident-notapphash-sold-as-bundled](snapident-notapphash-sold-as-bundled.md) 是引擎不解释 format / hash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 item 2），不是本页 bundled 全段 alone。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完，不是本页这种全字段（含 Metadata）对上不是已经装完。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了就已经齐，不是本页这种引擎不解释 format / hash 不是已经轻验 AppHash。
- [statesync-sold-as-genesis](statesync-sold-as-genesis.md) 是应用快照就已经从创世重放，不是本页这种空快照也至少 1 块不是已经齐。
