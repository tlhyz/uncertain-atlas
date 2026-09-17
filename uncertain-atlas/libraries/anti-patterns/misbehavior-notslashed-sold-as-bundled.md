# 反模式：把 Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事（372 余量） 卖成 已经罚没 / 已经定了奖惩 / 已经交差

**层次**：实现 / Misbehavior 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-misbehavior-notslashed-vs-bundled.md](../../tracks/implementation/worked-example-misbehavior-notslashed-vs-bundled.md)。

官方把 Misbehavior.type 枚举 / height 与 time / total_voting_power 三条核心句写成三件独立的实现事。把它们卖成已经罚没 / 已经定了奖惩 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Misbehavior.type 正式三事（372 余量），必须分开 not already slashed、not already rewarded、not already settled 三件事，不要和 372 / 21 / 569 / 376 / 713 / 810 / 811 糊成一句。

## 和相邻反模式

- [finmisbeh-notvoteinfo-sold-as-bundled](finmisbeh-notvoteinfo-sold-as-bundled.md) 是 Finalize misbehavior 就已经定奖惩（569），不是本页 type 枚举边界。
- [propstatus-notunknown-sold-as-bundled](propstatus-notunknown-sold-as-bundled.md) 是 ProposalStatus UNKNOWN 就已经崩（376/713），不是本页 type 枚举边界。
