# 反模式：把 height/time not already verified time / not already settled / not already +2/3 正式三事（372 余量） 卖成 已经验过这个时间 / 已经交差 / 已经是本高 +2/3

**层次**：实现 / Misbehavior 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-misbehavior-nottime-vs-bundled.md](../../tracks/implementation/worked-example-misbehavior-nottime-vs-bundled.md)。

官方把 Misbehavior.type 枚举 / height 与 time / total_voting_power 三条核心句写成三件独立的实现事。把它们卖成已经验过这个时间 / 已经交差 / 已经是本高 +2/3，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height/time 正式三事（372 余量），必须分开 not already verified time、not already settled、not already +2/3 三件事，不要和 372 / 304 / 387 / 767 / 420 / 809 / 811 糊成一句。

## 和相邻反模式

- [misbehavior-notslashed-sold-as-bundled](misbehavior-notslashed-sold-as-bundled.md) 是 type 枚举单句边界（809 item 1），不是本页 height/time 边界。
- [inittime-notgenesis-sold-as-bundled](inittime-notgenesis-sold-as-bundled.md) 是 InitChain time 就已经过了 genesis_time（387/767），不是本页 height/time 边界。
