# 反模式：把 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量）说成已经没有集合 / 已经删掉创世名单 / 已经用了应用自己的空集

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了空 not already no set ≠ bundled（318）](../../tracks/implementation/worked-example-validatorupdate-notempty-vs-bundled.md)。

## 卖法

把回了空 / InitChain 回了空名单 / 名单空 写成已经没有集合 interchangeable / 已经 no set interchangeable / 已经空集交差 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable；把没回人 / 没回验证者 / 回包没有验证者 写成已经删掉创世名单 interchangeable / 已经 deleted genesis interchangeable；把能设初始集合 / InitChain 能设集合 / 应用可设集合 写成已经用了应用自己的空集 interchangeable / 已经 app empty set interchangeable / 已经和创世 validators 空同一句 interchangeable，或已经和 318 validatorupdate bundled / validatorupdate-sold-as-set interchangeable / 713 validatorupdate-notempty interchangeable。

## 为什么错

官方把回了空单句、already no set、already deleted genesis、already app empty set 写成三件独立的实现事。把它们卖成 already no set interchangeable / already deleted genesis interchangeable / already app empty set interchangeable，会把 not already no set、not already deleted genesis、not already app empty set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量），必须分开 not already no set、not already deleted genesis、not already app empty set 三件事，不要和 318 / 33 / 714 / 715 / 303 / 35 糊成一句。

## 和相邻反模式

- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 ValidatorUpdate vs set bundled 全段，不是本页回了空 item 1 单句边界。
- [checktxresponse-notpriority-sold-as-bundled](checktxresponse-notpriority-sold-as-bundled.md) 是 Priority 共识顺序（317），不是本页 InitChain 空名单边界。
- [initchainusage-decide-sold-as-bundled](initchainusage-decide-sold-as-bundled.md) 是 InitChain Usage 另一对象，不是本页 Requirements Updating the Validator Set 空名单边界。
