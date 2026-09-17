# 反模式：把 写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量） 写成已经 已经刷盘 / 已经防了双签 / 已经交差

**层次**：实现 / 写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应**：[`../tracks/implementation/worked-example-wal-notfsync-vs-bundled.md`](../tracks/implementation/worked-example-wal-notfsync-vs-bundled.md)。

把 写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量） 写成已经 已经刷盘 / 已经防了双签 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写下每条消息 正式三事（298 余量），必须分开 not already fsynced、not already double-sign-safe、not already settled 三件事，不要和 298 / 4 / 307 / 981 / 982 糊成一句。

也不是：

- [abci-conn-notgates-sold-as-bundled](abci-conn-notgates-sold-as-bundled.md) 是一条连接仍不是四门边界（307/979），不是本页写下仍未刷盘边界。
- 锁谓词是不变量 4，不是本页别人的消息仍未按本节点签名刷过边界。
