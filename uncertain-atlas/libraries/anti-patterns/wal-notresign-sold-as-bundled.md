# 反模式：把 回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量） 写成已经 已经双签 / 已经发出新票 / 已经交差

**层次**：实现 / 回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应**：[`../tracks/implementation/worked-example-wal-notresign-vs-bundled.md`](../tracks/implementation/worked-example-wal-notresign-vs-bundled.md)。

把 回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量） 写成已经 已经双签 / 已经发出新票 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回放时再签 正式三事（298 余量），必须分开 not already double-signed、not already new-vote、not already settled 三件事，不要和 298 / 5 / 307 / 980 / 982 糊成一句。

也不是：

- [wal-notfsync-sold-as-bundled](wal-notfsync-sold-as-bundled.md) 是写下仍未刷盘单句边界（980 item 1），不是本页回放再签仍未双签边界。
- 半写已经原子是不变量 5，不是本页回放仍未发出新票边界。
