# 模式：把 ListSnapshots Usage discover / Snapshot type 正式二事说成两个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots Usage。  
**例**：[discover on peers during state sync ≠ ListSnapshots 空请求 bundled](../../tracks/implementation/worked-example-listsnapusage-discover-vs-bundled.md)。

## 两个名字

1. **discover on peers during state sync 不是 ListSnapshots 空请求 bundled：** 看见 Methods ListSnapshots Usage discover，不是 395 空请求 bundled interchangeable。
2. **See Snapshot data type for details 不是 Snapshot 类型 bundled：** 看见 Usage 交叉引用 Snapshot 类型，不是 368 five fields bundled interchangeable。

## 为什么要分开叫

官方把 ListSnapshots Usage discover 单句、ListSnapshots 空请求 bundled（395）、Snapshot 类型 bundled（368）写成两个名字。把它们叫成一个「看见 ListSnapshots Usage 了就已经空请求 bundled interchangeable、已经 five fields 对上 interchangeable」，会把 discover on peers、See Snapshot data type 两条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage discover / Snapshot type 正式二事，先数清问的是 discover on peers during state sync 是不是 ListSnapshots 空请求 bundled interchangeable / 已经本地清单 / 已经问了邻居就齐、See Snapshot data type for details 是不是 Snapshot 类型 bundled interchangeable / 已经 five fields 对上 / 已经装完，再决定要不要同一次发布。
