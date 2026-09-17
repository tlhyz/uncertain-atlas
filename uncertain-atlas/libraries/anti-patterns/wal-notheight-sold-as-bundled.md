# 反模式：把 LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量） 写成已经 已经换了高度 / 已经发出另一张承诺 / 已经交差

**层次**：实现 / LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应**：[`../tracks/implementation/worked-example-wal-notheight-vs-bundled.md`](../tracks/implementation/worked-example-wal-notheight-vs-bundled.md)。

把 LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量） 写成已经 已经换了高度 / 已经发出另一张承诺 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LastSignBytes 对上 正式三事（298 余量），必须分开 not already new-height、not already new-commit、not already settled 三件事，不要和 298 / 33 / 310 / 980 / 981 糊成一句。

也不是：

- [wal-notresign-sold-as-bundled](wal-notresign-sold-as-bundled.md) 是回放再签仍未双签单句边界（981 item 2），不是本页对上仍未换高度边界。
- 四门已经结算是不变量 33，不是本页回放走到 precommit 仍未发出另一张承诺边界。
