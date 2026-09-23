# 反模式：paramsdocs-sold-as-one-table

**层次**：实现 / 共识参数跨文档。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) 与 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) 的 ConsensusParams。  
**例**：[ConsensusParams.version 有这一栏 ≠ 已经知道看的是哪一份](../../tracks/implementation/worked-example-consensusparams-vs-docs.md)。

## 病症

把「`ConsensusParams` 的字段号对上了」写成两个实现/两个版本已经在按同一个对象对齐，或把一份官方文档的字段表当成唯一依据（并因此把 `ABCIParams` 或 `FeatureParams` 当成同一个字段 5），或把「字段名变了」（`app_version` → `app`）当成「字段换了对象」。

## 为什么错

CometBFT 现行两份官方文档对同一个 `ConsensusParams` 给出**不同的内嵌类型表**：`abci++_methods.md` 有字段 5 `abci`（`ABCIParams`，并注明自 v1.0 起弃用），`data_structures.md` 字段 5 空档、字段 7 为 `feature`（`FeatureParams`）。号相同不等于类型相同。反过来，`VersionParams.app` 只是**改过名**（0.34 里叫 `app_version`），名字变了不等于对象变了。两种坑不能混。

## 正确写法

分开三句：ConsensusParams.version 有这一栏不是已经知道看的是哪一份；字段号 5 相同不是已经是同一个内嵌类型；spec 内部写法不齐不是已经能挑一份照做。实现里点名依据哪一份、哪一版。

## 边界

不是 [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md)（那是回了参数不是已经在本高生效，不变量 319），不是 `ConsensusParams.abci` 是 ABCI 相关参数（不变量 386），不是 `ConsensusParams.version` 是 ABCI 应用版本（不变量 385），不是 `app_version` 进每块头（不变量 370）。

## 本页不抄

- 怎样编 `ConsensusParams`、怎样处理字段 5 与 7。
- 怎样写利用步骤。
