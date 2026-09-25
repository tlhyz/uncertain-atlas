# 反模式：把 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量）说成已经验过票上的时间 / 已经交差 / 已经是本高 +2/3

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有高度 not already verified ≠ bundled（372）](../../tracks/implementation/worked-example-misbehavior-notverified-vs-bundled.md)。

## 卖法

把有高度 / `height` 是过错发生的高度 / 有高度 写成已经验过票上的时间 interchangeable / 已经 verified interchangeable / 已经验过票上的时间交差 interchangeable / 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable；把有时间 / `time` 是那一高已提交块的时间 / 有时间戳 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把对上了高度 / 高度对上 / 过错高度对上 写成已经是本高 +2/3 interchangeable / 已经 plus23 interchangeable / 已经是本高 +2/3 交差 interchangeable，或已经和 372 misbehavior bundled / misbehavior-sold-as-enum interchangeable / 864 misbehavior-notverified interchangeable。

## 为什么错

官方把有高度、不是已经交差、不是已经是本高 +2/3 写成三件独立的实现事。把它们卖成 already verified interchangeable / already settled interchangeable / already plus23 interchangeable，会把 not already verified、not already settled、not already plus23 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 not already verified / not already settled / not already plus23 正式三事（372 余量），必须分开 not already verified、not already settled、not already plus23 三件事，不要和 372 / 304 / 148 / 863 糊成一句。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 misbehavior bundled 全段，不是本页有高度 item 2 单句边界。
- [misbehavior-notslashed-sold-as-bundled](misbehavior-notslashed-sold-as-bundled.md) 是有类型 not already slashed（372 item 1），不是本页 not already verified 边界。
- [timestamp-sold-as-checked](timestamp-sold-as-checked.md) 是票上 Timestamp 就已经验过（304），不是本页 not already verified 单句。
- [lastcommit-sold-as-this-block](lastcommit-sold-as-this-block.md) 是本头 LastCommit 就已经是本高 +2/3（148），不是本页 not already plus23 单句。
