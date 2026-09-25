# 反模式：把 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量）说成已经罚没 / 已经交差 / 已经定了奖惩

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有类型 not already slashed ≠ bundled（372）](../../tracks/implementation/worked-example-misbehavior-notslashed-vs-bundled.md)。

## 卖法

把有类型 / `Misbehavior.type` 只是过错枚举 / 有类型 写成已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable / 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable；把写成双签 / 写成 `DUPLICATE_VOTE` / 枚举写成双签 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把枚举在 / 枚举种类在 / 有枚举 写成已经定了奖惩 interchangeable / 已经 rewarded interchangeable / 已经定了奖惩交差 interchangeable，或已经和 372 misbehavior bundled / misbehavior-sold-as-enum interchangeable / 863 misbehavior-notslashed interchangeable。

## 为什么错

官方把有类型、不是已经交差、不是已经定了奖惩写成三件独立的实现事。把它们卖成 already slashed interchangeable / already settled interchangeable / already rewarded interchangeable，会把 not already slashed、not already settled、not already rewarded 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量），必须分开 not already slashed、not already settled、not already rewarded 三件事，不要和 372 / 21 / 304 / 365 糊成一句。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 misbehavior bundled 全段，不是本页有类型 item 1 单句边界。
- [evidence-equals-slash](evidence-equals-slash.md) 是证据上链就已经罚没（21），不是本页 not already slashed 单句。
- [timestamp-sold-as-checked](timestamp-sold-as-checked.md) 是票上 Timestamp 就已经验过（304），不是本页 not already settled 单句。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没（365），不是本页 not already rewarded 单句。
