# 反模式：把 结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量） 写成已经 已经同一顺序 / 已经按送来的顺序 / 引擎已经替你排好

**层次**：实现 / 结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应**：[`../tracks/implementation/worked-example-exectx-notorder-vs-bundled.md`](../tracks/implementation/worked-example-exectx-notorder-vs-bundled.md)。

把 结果列表 not already same-order / not already same-count / not already engine-sorted 正式三事（316 余量） 写成已经 已经同一顺序 / 已经按送来的顺序 / 引擎已经替你排好，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看结果列表 正式三事（316 余量），必须分开 not already same-order、not already same-count、not already engine-sorted 三件事，不要和 316 / 33 / 309 / 1014 / 1015 糊成一句。

也不是：

- [sendq-notsame-sold-as-bundled](sendq-notsame-sold-as-bundled.md) 是 TrySend 仍未和 Send 同一把尺边界（309/1012），不是本页结果列表仍未同一顺序边界。
- 四门已经结算是不变量 33，不是本页条数一样仍未按送来的顺序边界。
