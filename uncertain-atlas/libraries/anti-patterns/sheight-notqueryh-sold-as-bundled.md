# 反模式：把 Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量） 写成已经 已经是 Query 高度 / 已经装完 / 已经交差

**层次**：实现 / Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-sheight-notqueryh-vs-bundled.md`](../tracks/implementation/worked-example-sheight-notqueryh-vs-bundled.md)。

把 Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量） 写成已经 已经是 Query 高度 / 已经装完 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Snapshot.height 正式三事（406 余量），必须分开 not already Query-height、not already loaded、not already settled 三件事，不要和 406 / 371 / 321 / 1107 / 1108 糊成一句。

也不是：

- [cguard-notproof-sold-as-bundled](cguard-notproof-sold-as-bundled.md) 是自描述 type 仍未是 ProofOp 类型边界（405/1105），不是本页拍快照高度仍未是 Query 高度边界。
- 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash 是不变量 371，不是本页写成 Commit 之后仍未装完边界。
