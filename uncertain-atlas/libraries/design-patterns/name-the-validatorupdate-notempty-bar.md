# 模式：把 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**例**：[回了空 not already no set ≠ bundled（318）](../../tracks/implementation/worked-example-validatorupdate-notempty-vs-bundled.md)。

## 三个名字

1. **回了空 不是 already no set：** 看见 InitChain 回了空名单 / 名单空，不是已经没有集合 interchangeable / 已经空集交差 interchangeable，不是 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable。

2. **没回人 不是 already deleted genesis：** 看见没回验证者 / 回包没有验证者，不是已经删掉创世名单 interchangeable / 已经清掉创世集合 interchangeable，不是 318 validatorupdate item 2 interchangeable / 714 validatorupdate-notdup interchangeable。

3. **能设初始集合 不是 already app empty set：** 看见 InitChain 能设集合 / 应用可设集合，不是已经用了应用自己的空集 interchangeable / 已经和创世 validators 空同一句 interchangeable，不是 318 validatorupdate item 3 interchangeable / 715 validatorupdate-notpower0 interchangeable。

官方把回了空单句、already no set、already deleted genesis、already app empty set 写成三个名字。把它们叫成一个「看见回了空就已经没有集合 interchangeable / 就已经删掉创世名单 interchangeable / 就已经和创世 validators 空同一句 interchangeable」，会把 not already no set、not already deleted genesis、not already app empty set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量），先数清问的是回了空 是不是 already no set / 318 / validatorupdate-sold-as-set，是不是没回人 是不是 already deleted genesis，还是能设初始集合 是不是 already app empty set，再决定要不要同一次发布。318 validatorupdate vs set bundled unbundling 在本页 item 1 完成。
