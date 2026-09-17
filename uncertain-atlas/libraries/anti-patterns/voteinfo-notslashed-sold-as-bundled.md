# 反模式：把 VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事（365 余量） 卖成 已经罚没 / 已经交差 / 已经用 decided_last_commit 算完

**层次**：实现 / VoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-voteinfo-notslashed-vs-bundled.md](../../tracks/implementation/worked-example-voteinfo-notslashed-vs-bundled.md)。

官方把 VoteInfo 能按到场定奖惩 / 从拟议块或已决块抽出 / 按投票权降序排三条核心句写成三件独立的实现事。把它们卖成已经罚没 / 已经交差 / 已经用 decided_last_commit 算完，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VoteInfo 定奖惩 正式三事（365 余量），必须分开 not already slashed、not already settled、not already decided_last_commit computed 三件事，不要和 365 / 21 / 372 / 809 / 811 / 363 / 831 / 832 糊成一句。

## 和相邻反模式

- [misbehavior-notslashed-sold-as-bundled](misbehavior-notslashed-sold-as-bundled.md) 是 Misbehavior.type 就已经罚没（372/809），不是本页 VoteInfo 定奖惩边界。
- [misbehavior-notreward-sold-as-bundled](misbehavior-notreward-sold-as-bundled.md) 是 total_voting_power 就已经按到场定奖惩（372/811），不是本页 VoteInfo 定奖惩边界。
