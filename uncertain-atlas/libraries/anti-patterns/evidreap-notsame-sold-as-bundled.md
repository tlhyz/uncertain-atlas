# 反模式：把 两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量） 写成已经 已经同一条 / 已经扣掉证据之后还收得下 / 已经交差

**层次**：共识 / 两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应**：[`../tracks/consensus/worked-example-evidreap-notsame-vs-bundled.md`](../tracks/consensus/worked-example-evidreap-notsame-vs-bundled.md)。

把 两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量） 写成已经 已经同一条 / 已经扣掉证据之后还收得下 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两条收交易上限 正式三事（299 余量），必须分开 not already same-cap、not already pool-fits、not already settled 三件事，不要和 299 / 63 / 331 / 989 / 991 糊成一句。

也不是：

- [evidreap-notfull-sold-as-bundled](evidreap-notfull-sold-as-bundled.md) 是先装证据仍未装满交易单句边界（989 item 1），不是本页两条上限仍未同一条边界。
- 仓库默认 MaxBytes 已经是活性 SLA 是不变量 63，不是本页内存池收得下仍未扣掉证据之后还收得下边界。
