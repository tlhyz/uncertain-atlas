# 反模式：把 同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量） 写成已经 已经换成应用刚回的那套 / 本高度各轮已经用上 / 集合已经变了

**层次**：共识 / 同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应**：[`../tracks/consensus/worked-example-roundset-notset-vs-bundled.md`](../tracks/consensus/worked-example-roundset-notset-vs-bundled.md)。

把 同一高度换轮 not already new-set / not already this-height / not already applied 正式三事（302 余量） 写成已经 已经换成应用刚回的那套 / 本高度各轮已经用上 / 集合已经变了，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度换轮 正式三事（302 余量），必须分开 not already new-set、not already this-height、not already applied 三件事，不要和 302 / 35 / 301 / 996 / 997 糊成一句。

也不是：

- [proposed-notforever-sold-as-bundled](proposed-notforever-sold-as-bundled.md) 是 CheckTx 绿仍未永远有效边界（301/994），不是本页换轮仍未换集合边界。
- H 的更新已经在 H+1 计票是不变量 35，不是本页应用回了更新仍未本高度各轮用上边界。
