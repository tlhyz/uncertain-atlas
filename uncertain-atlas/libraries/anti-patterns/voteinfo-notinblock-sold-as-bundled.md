# 反模式：把 按投票权降序排 not already in-block / not already settled / not already slashed 正式三事（365 余量） 卖成 已经进了块 / 已经交差 / 已经罚没

**层次**：实现 / VoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-voteinfo-notinblock-vs-bundled.md](../../tracks/implementation/worked-example-voteinfo-notinblock-vs-bundled.md)。

官方把 VoteInfo 能按到场定奖惩 / 从拟议块或已决块抽出 / 按投票权降序排三条核心句写成三件独立的实现事。把它们卖成已经进了块 / 已经交差 / 已经罚没，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按投票权降序排 正式三事（365 余量），必须分开 not already in-block、not already settled、not already slashed 三件事，不要和 365 / 300 / 363 / 21 / 830 / 831 糊成一句。

## 和相邻反模式

- [voteinfo-notpubkey-sold-as-bundled](voteinfo-notpubkey-sold-as-bundled.md) 是从块抽出单句边界（831 item 2），不是本页降序排边界。
- 本地 State 就已经进了块是不变量 300，不是本页降序排边界。
