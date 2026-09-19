# 反模式：把 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量）说成已经能删不在名单里的人 / 已经没有上限 / 已经选型

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写成 0 not already delete outsider ≠ bundled（318）](../../tracks/implementation/worked-example-validatorupdate-notpower0-vs-bundled.md)。

## 卖法

把写成 0 / power 写成 0 / 名单里没有这个人 写成已经能删一个不在名单里的人 interchangeable / 已经 delete outsider interchangeable / 已经对不在集合里的人写 0 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable；把看见总权 / 新集合总投票权 / MaxTotalVotingPower 写成已经没有上限 interchangeable / 已经 no max interchangeable；把看见四种钥型 / 公钥类型表 / 钥型列表 写成已经选型 interchangeable / 已经 key-type chosen interchangeable，或已经和 318 validatorupdate bundled / validatorupdate-sold-as-set interchangeable / 715 validatorupdate-notpower0 interchangeable。

## 为什么错

官方把写成 0 单句、already delete outsider、already no max、already key-type chosen 写成三件独立的实现事。把它们卖成 already delete outsider interchangeable / already no max interchangeable / already key-type chosen interchangeable，会把 not already delete outsider、not already no max、not already key-type chosen 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量），必须分开 not already delete outsider、not already no max、not already key-type chosen 三件事，不要和 318 / 33 / 713 / 714 / 35 / 315 糊成一句。不要把 `MaxTotalVotingPower` 当不确定默认。

## 和相邻反模式

- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 ValidatorUpdate vs set bundled 全段，不是本页 power 0 item 3 单句边界。
- [validatorupdate-notdup-sold-as-bundled](validatorupdate-notdup-sold-as-bundled.md) 是同一批重复公钥 item 2，不是本页 power 0 边界。
- [validatorupdate-notempty-sold-as-bundled](validatorupdate-notempty-sold-as-bundled.md) 是 InitChain 空名单 item 1，不是本页 power 0 边界。
