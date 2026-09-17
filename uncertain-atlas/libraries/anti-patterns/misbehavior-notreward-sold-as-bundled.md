# 反模式：把 total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事（372 余量） 卖成 已经按到场定奖惩 / 已经改了集合 / 已经罚没

**层次**：实现 / Misbehavior 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-misbehavior-notreward-vs-bundled.md](../../tracks/implementation/worked-example-misbehavior-notreward-vs-bundled.md)。

官方把 Misbehavior.type 枚举 / height 与 time / total_voting_power 三条核心句写成三件独立的实现事。把它们卖成已经按到场定奖惩 / 已经改了集合 / 已经罚没，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 total_voting_power 正式三事（372 余量），必须分开 not already rewarded by presence、not already changed set、not already slashed 三件事，不要和 372 / 365 / 569 / 388 / 765 / 809 / 810 糊成一句。

## 和相邻反模式

- [misbehavior-nottime-sold-as-bundled](misbehavior-nottime-sold-as-bundled.md) 是 height/time 单句边界（810 item 2），不是本页总权边界。
- [finmisbeh-notvoteinfo-sold-as-bundled](finmisbeh-notvoteinfo-sold-as-bundled.md) 是 Finalize misbehavior 就已经是 VoteInfo（569），不是本页总权边界。
