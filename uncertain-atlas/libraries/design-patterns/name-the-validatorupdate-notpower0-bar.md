# 模式：把 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**例**：[写成 0 not already delete outsider ≠ bundled（318）](../../tracks/implementation/worked-example-validatorupdate-notpower0-vs-bundled.md)。

## 三个名字

1. **写成 0 不是 already delete outsider：** 看见 power 写成 0 / 名单里没有这个人，不是已经能删一个不在名单里的人 interchangeable / 已经对不在集合里的人写 0 interchangeable，不是 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable。

2. **看见总权 不是 already no max：** 看见新集合总投票权 / MaxTotalVotingPower，不是已经没有上限 interchangeable / 已经无限总权 interchangeable，不是 318 validatorupdate item 1 interchangeable / 713 validatorupdate-notempty interchangeable。

3. **看见四种钥型 不是 already key-type chosen：** 看见公钥类型表 / 钥型列表，不是已经选型 interchangeable / 已经选定钥型 interchangeable，不是 318 validatorupdate item 2 interchangeable / 714 validatorupdate-notdup interchangeable。

官方把写成 0 单句、already delete outsider、already no max、already key-type chosen 写成三个名字。把它们叫成一个「看见写成 0 就已经能删不在名单里的人 interchangeable / 就已经没有总权上限 interchangeable / 就已经选型 interchangeable」，会把 not already delete outsider、not already no max、not already key-type chosen 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 power 0 不是已经删掉不在集合里的人 not already delete outsider / not already no max / not already key-type chosen 正式三事（318 余量），先数清问的是写成 0 是不是 already delete outsider / 318 / validatorupdate-sold-as-set，是不是看见总权 是不是 already no max，还是看见四种钥型 是不是 already key-type chosen，再决定要不要同一次发布。318 validatorupdate vs set bundled unbundling 在本页 item 3 完成。
