# 反模式：把 MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事（299 余量） 写成已经 已经没有上限 / 已经可以随便回 / 已经交差

**层次**：共识 / MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事（299 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应**：[`../tracks/consensus/worked-example-evidreap-notunlim-vs-bundled.md`](../tracks/consensus/worked-example-evidreap-notunlim-vs-bundled.md)。

把 MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事（299 余量） 写成已经 已经没有上限 / 已经可以随便回 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 写成 -1 正式三事（299 余量），必须分开 not already unlimited、not already app-free、not already settled 三件事，不要和 299 / 337 / 46 / 989 / 990 糊成一句。

也不是：

- [evidreap-notsame-sold-as-bundled](evidreap-notsame-sold-as-bundled.md) 是两条上限仍未同一条单句边界（990 item 2），不是本页 -1 仍未没有上限边界。
- -1 就按 100 MB 验就已经没有上限是不变量 337，不是本页整池都给了应用仍不得随便回边界。
