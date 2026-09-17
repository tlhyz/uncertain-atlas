# 模式：把 ListSnapshots 空请求三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**例**：[ListSnapshots 请求是空请求、向应用要一份快照清单 ≠ 已经齐](../../tracks/implementation/worked-example-listsnapempty-vs-discovery.md)。

## 三个名字

1. **ListSnapshots 请求是空请求、向应用要一份快照清单不是已经齐：** 看见填了空请求不是已经问了邻居。
2. **ListSnapshots 回包 snapshots 是本地状态快照清单不是已经是同一份：** 看见回了清单不是已经装完。
3. **ListSnapshots 用来在 state sync 时发现邻居上有哪些快照不是已经在拉块：** 看见用来发现不是已经齐。

## 为什么要分开叫

官方把 ListSnapshots 请求是空请求、向应用要一份快照清单、回包 `snapshots` 是本地状态快照清单、Usage 是在 state sync 时发现邻居上有哪些快照写成三件事。把它们叫成一个「看见填了 ListSnapshots 空请求就已经齐」，会把问了邻居就已经齐、全字段对上就已经装完和拉块一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ListSnapshots 空请求就已经齐」，先数清问的是 ListSnapshots 请求是空请求、向应用要一份快照清单不是已经齐、ListSnapshots 回包 snapshots 是本地状态快照清单不是已经是同一份，还是 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照不是已经在拉块，再决定要不要同一次发布。
