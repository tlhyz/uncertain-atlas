# 模式：把 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**例**：[有总权 not already rewarded ≠ bundled（372）](../../tracks/implementation/worked-example-misbehavior-notrewarded-vs-bundled.md)。

## 三个名字

1. **有总权 不是 already rewarded：** 看见有总权 / `total_voting_power` 是那一高验证者集合的总权 / 有总权，不是已经按到场定奖惩 interchangeable / 已经 rewarded interchangeable / 已经按到场定奖惩交差 interchangeable，不是 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable。

2. **填了权 不是 already setchanged：** 看见填了权 / 填了总权 / 权在，不是已经改了集合 interchangeable / 已经 setchanged interchangeable / 已经改了集合交差 interchangeable，不是 318 ValidatorUpdate interchangeable / 864 misbehavior-notverified interchangeable。

3. **有集合 不是 already slashed：** 看见有集合 / 那一高验证者集合 / 集合在，不是已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable，不是 21 evidence-slash interchangeable / 863 misbehavior-notslashed interchangeable。

官方把有总权、不是已经改了集合、不是已经罚没写成三个名字。把它们叫成一个「看见有总权就已经按到场定奖惩 interchangeable / 就已经改了集合 interchangeable / 就已经罚没 interchangeable」，会把 not already rewarded、not already setchanged、not already slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量），先数清问的是有总权 是不是 already rewarded / 372 / misbehavior-sold-as-enum，是不是填了权 是不是 already setchanged，还是有集合 是不是 already slashed，再决定要不要同一次发布。372 misbehavior-vs-enum bundled unbundling 在本页 item 3 完成。
