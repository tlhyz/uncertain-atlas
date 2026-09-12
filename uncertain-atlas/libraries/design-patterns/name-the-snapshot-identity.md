# 模式：把 Snapshot 类型三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**例**：[快照全字段（含 Metadata）对上 ≠ 已经装完](../../tracks/implementation/worked-example-snapshot-vs-identical.md)。

## 三个名字

1. **全字段（含 Metadata）对上不是已经装完：** 看见能拉 chunk 不是已经齐。
2. **引擎不解释 format / hash 不是已经轻验 AppHash：** 看见比过了不是已经从创世重放。
3. **空快照也至少 1 块不是已经齐：** 看见网上有 4 MB 上限不是已经是共识常数。

## 为什么要分开叫

官方把快照全字段相等才算同一份、引擎不解释 format / hash、空快照也至少 1 块且网上报文有上限写成三件事。把它们叫成一个「看见快照对上就已经装完」，会把装回、发现和从创世重放一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见快照对上就已经装完」，先数清问的是全字段（含 Metadata）对上不是已经装完、引擎不解释 format / hash 不是已经轻验 AppHash，还是空快照也至少 1 块不是已经齐，再决定要不要同一次发布。
