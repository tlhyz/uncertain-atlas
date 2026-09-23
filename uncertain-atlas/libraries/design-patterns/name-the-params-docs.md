# 模式：把共识参数跨文档三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（规范现状）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) 与 [Core Data Structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md) 的 ConsensusParams。  
**例**：[ConsensusParams.version 有这一栏 ≠ 已经知道看的是哪一份](../../tracks/implementation/worked-example-consensusparams-vs-docs.md)。

## 三个名字

1. **ConsensusParams.version 有这一栏不是已经知道看的是哪一份：** 两份官方文档都列了它。
2. **字段号 5 相同不是已经是同一个内嵌类型：** 一份写 `abci`（`ABCIParams`，已弃用），一份字段 5 空着、字段 7 写 `feature`（`FeatureParams`）。
3. **spec 内部写法不齐不是已经能挑一份照做：** 两份都是官方，必须点名出处与版本。

## 为什么要分开叫

同一个类型名、同一段字段号，在两个官方文档里内嵌了不同的类型表。把它们叫成一个「看见字段号对上就已经是同一个对象」，会在跨实现或跨版本对齐时把两套定义糊成一套 —— 而 `ABCIParams` 那份还带着「自 v1.0 起已弃用」这句话。

**另一种坑，别混：** `VersionParams.app` 在 CometBFT 0.34 里叫 `app_version`。那是**同义不同名（跨版本）**，与本页的**同名不同义（跨文档）**是两回事。

## 产品

**建议（产品，不是事实）**：实现里若处理 `ConsensusParams`，必须**点名依据哪一份文档、哪一版**，不要自己补折中定义。产品文案若说「共识参数已对齐」，先数清问的是 ConsensusParams.version 有这一栏不是已经知道看的是哪一份、字段号 5 相同不是已经是同一个内嵌类型，还是 spec 内部写法不齐不是已经能挑一份照做。
