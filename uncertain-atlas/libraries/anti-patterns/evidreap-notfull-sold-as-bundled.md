# 反模式：把 先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量） 写成已经 已经装满交易 / 已经执行 / 已经交差

**层次**：共识 / 先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应**：[`../tracks/consensus/worked-example-evidreap-notfull-vs-bundled.md`](../tracks/consensus/worked-example-evidreap-notfull-vs-bundled.md)。

把 先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量） 写成已经 已经装满交易 / 已经执行 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先装证据 正式三事（299 余量），必须分开 not already full-of-txs、not already executed、not already settled 三件事，不要和 299 / 33 / 303 / 990 / 991 糊成一句。

也不是：

- [genesis-notset-sold-as-bundled](genesis-notset-sold-as-bundled.md) 是空名单仍未没有集合边界（303/988），不是本页先装证据仍未装满交易边界。
- 四门已经结算是不变量 33，不是本页证据进了提案仍未执行边界。
