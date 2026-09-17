# 反模式：把 拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量） 写成已经 已经交差之后拍的 / 已经没有更高高度 / 已经交差

**层次**：实现 / 拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应**：[`../tracks/implementation/worked-example-snapshot-take-notafter-vs-bundled.md`](../tracks/implementation/worked-example-snapshot-take-notafter-vs-bundled.md)。

把 拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量） 写成已经 已经交差之后拍的 / 已经没有更高高度 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拍了这个高度 正式三事（324 余量），必须分开 not already after-commit、not already no-higher、not already settled 三件事，不要和 324 / 38 / 321 / 951 / 952 糊成一句。

也不是：

- [query-proof-notfinal-sold-as-bundled](query-proof-notfinal-sold-as-bundled.md) 是一层根仍不是最终 AppHash 边界（325/949），不是本页拍了仍未交差之后拍边界。
- 只有 AppHash 可信任是不变量 38，不是本页拍了仍可含更高高度边界。
