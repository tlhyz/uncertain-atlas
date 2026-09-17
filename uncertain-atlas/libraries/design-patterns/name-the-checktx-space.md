# 模式：把 CheckTx 回包三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[CheckTx 回包 codespace 是码的命名空间 ≠ 已经是回包码](../../tracks/implementation/worked-example-checktxspace-vs-code.md)。

## 三个名字

1. **CheckTx 回包 codespace 是码的命名空间不是已经是回包码：** 看见写了空间不是已经没进块。
2. **CheckTx 回包 events 是给索引用的类型键值不是已经交差：** 看见回了事件不是已经没进块。
3. **CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道：** 看见填了道不是已经排了优先。

## 为什么要分开叫

官方把 CheckTx 回包 `codespace` 是码的命名空间、`events` 是给索引用的类型键值、`lane_id` 必须在 Info 回包车道范围内写成三件事。把它们叫成一个「看见 CheckTx 回了码空间就已经是回包码」，会把回包码、Finalize 回执和车道一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 CheckTx 回了码空间就已经是回包码」，先数清问的是 CheckTx 回包 codespace 是码的命名空间不是已经是回包码、CheckTx 回包 events 是给索引用的类型键值不是已经交差，还是 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道，再决定要不要同一次发布。
