# 反模式：把 Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量） 写成已经 已经对上 AppHash / 已经勾了 prove / 已经交差

**层次**：实现 / Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-sheight-notprove-vs-bundled.md`](../tracks/implementation/worked-example-sheight-notprove-vs-bundled.md)。

把 Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量） 写成已经 已经对上 AppHash / 已经勾了 prove / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 可选证明 正式三事（406 余量），必须分开 not already apphash-aligned、not already prove-flagged、not already settled 三件事，不要和 406 / 383 / 1101 / 1106 / 1107 糊成一句。

也不是：

- [sheight-notmeta-sold-as-bundled](sheight-notmeta-sold-as-bundled.md) 是任意元数据仍未全字段对上单句边界（1107 item 2），不是本页可选证明仍未对上 AppHash 边界。
- Query 请求 prove 就已经对上 AppHash 是不变量 383，不是本页有证明仍未勾了 prove 边界。
