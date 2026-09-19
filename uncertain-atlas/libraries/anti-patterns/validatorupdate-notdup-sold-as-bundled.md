# 反模式：把同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量）说成已经按后一条改权 / 已经能恢复 / 已经能写两行

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[看见重复 not already last-wins ≠ bundled（318）](../../tracks/implementation/worked-example-validatorupdate-notdup-vs-bundled.md)。

## 卖法

把看见重复 / 一次更新里同一把公钥出现两次 / 同一批重复 写成已经按后一条改权 interchangeable / 已经 last-wins interchangeable / 已经按后一条算 interchangeable / 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable；把看见失败 / 块执行失败 / 不可恢复失败 写成已经能重放修好 interchangeable / 已经 recoverable interchangeable；把看见同一把钥 / 同一把公钥 / 一把公钥出现两次 写成已经能写两行 interchangeable / 已经 two rows interchangeable，或已经和 318 validatorupdate bundled / validatorupdate-sold-as-set interchangeable / 714 validatorupdate-notdup interchangeable。

## 为什么错

官方把看见重复单句、already last-wins、already recoverable、already two rows 写成三件独立的实现事。把它们卖成 already last-wins interchangeable / already recoverable interchangeable / already two rows interchangeable，会把 not already last-wins、not already recoverable、not already two rows 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量），必须分开 not already last-wins、not already recoverable、not already two rows 三件事，不要和 318 / 33 / 713 / 715 / 320 / 35 糊成一句。

## 和相邻反模式

- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 ValidatorUpdate vs set bundled 全段，不是本页重复公钥 item 2 单句边界。
- [validatorupdate-notempty-sold-as-bundled](validatorupdate-notempty-sold-as-bundled.md) 是 InitChain 空名单 item 1，不是本页重复公钥边界。
- [checktxresponse-notpriority-sold-as-bundled](checktxresponse-notpriority-sold-as-bundled.md) 是 Priority 共识顺序（317），不是本页重复公钥边界。
