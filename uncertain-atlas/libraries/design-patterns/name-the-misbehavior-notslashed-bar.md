# 模式：把 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**例**：[有类型 not already slashed ≠ bundled（372）](../../tracks/implementation/worked-example-misbehavior-notslashed-vs-bundled.md)。

## 三个名字

1. **有类型 不是 already slashed：** 看见有类型 / `Misbehavior.type` 只是过错枚举 / 有类型，不是已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable，不是 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable。

2. **写成双签 不是 already settled：** 看见写成双签 / 写成 `DUPLICATE_VOTE` / 枚举写成双签，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 21 evidence-slash interchangeable / 304 Timestamp verified interchangeable。

3. **枚举在 不是 already rewarded：** 看见枚举在 / 枚举种类在 / 有枚举，不是已经定了奖惩 interchangeable / 已经 rewarded interchangeable / 已经定了奖惩交差 interchangeable，不是 365 VoteInfo rewards interchangeable / 372 misbehavior item 3 interchangeable。

官方把有类型、不是已经交差、不是已经定了奖惩写成三个名字。把它们叫成一个「看见有类型就已经罚没 interchangeable / 就已经交差 interchangeable / 就已经定了奖惩 interchangeable」，会把 not already slashed、not already settled、not already rewarded 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量），先数清问的是有类型 是不是 already slashed / 372 / misbehavior-sold-as-enum，是不是写成双签 是不是 already settled，还是枚举在 是不是 already rewarded，再决定要不要同一次发布。372 misbehavior-vs-enum bundled unbundling 在本页 item 1 启动。
