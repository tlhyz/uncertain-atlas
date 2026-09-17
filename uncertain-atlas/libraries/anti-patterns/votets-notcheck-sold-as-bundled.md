# 反模式：把 带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量） 写成已经 已经验过 / 已经执行 / 票上的时间已经有要求

**层次**：共识 / 带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应**：[`../tracks/consensus/worked-example-votets-notcheck-vs-bundled.md`](../tracks/consensus/worked-example-votets-notcheck-vs-bundled.md)。

把 带了 Timestamp not already checked / not already enforced / not already required 正式三事（304 余量） 写成已经 已经验过 / 已经执行 / 票上的时间已经有要求，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看带了 Timestamp 正式三事（304 余量），必须分开 not already checked、not already enforced、not already required 三件事，不要和 304 / 40 / 302 / 999 / 1000 糊成一句。

也不是：

- [roundset-notscale-sold-as-bundled](roundset-notscale-sold-as-bundled.md) 是缩放仍未按人头轮边界（302/997），不是本页时间戳仍未验过边界。
- 块时间必须点名算法是不变量 40，不是本页单调期望仍未执行边界。
