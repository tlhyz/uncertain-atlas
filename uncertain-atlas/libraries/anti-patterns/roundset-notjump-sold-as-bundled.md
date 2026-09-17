# 反模式：把 新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量） 写成已经 已经能跳到队头 / 已经洗掉队尾 / 已经公平当过一轮

**层次**：共识 / 新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Proposer Selection Procedure](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-selection.md) proposer selection / same-height set。  
**对应**：[`../tracks/consensus/worked-example-roundset-notjump-vs-bundled.md`](../tracks/consensus/worked-example-roundset-notjump-vs-bundled.md)。

把 新加入 not already jump / not already washed / not already fair-round 正式三事（302 余量） 写成已经 已经能跳到队头 / 已经洗掉队尾 / 已经公平当过一轮，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看新加入 正式三事（302 余量），必须分开 not already jump、not already washed、not already fair-round 三件事，不要和 302 / 56 / 303 / 995 / 997 糊成一句。

也不是：

- [roundset-notset-sold-as-bundled](roundset-notset-sold-as-bundled.md) 是换轮仍未换集合单句边界（995 item 1），不是本页新加入仍未能跳队头边界。
- 轻验集合已经对齐提议者字段是不变量 56，不是本页退出再加入仍未洗掉队尾边界。
