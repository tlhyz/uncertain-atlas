# 模式：把同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating the Validator Set。  
**例**：[看见重复 not already last-wins ≠ bundled（318）](../../tracks/implementation/worked-example-validatorupdate-notdup-vs-bundled.md)。

## 三个名字

1. **看见重复 不是 already last-wins：** 看见一次更新里同一把公钥出现两次 / 同一批重复，不是已经按后一条改权 interchangeable / 已经按后一条算 interchangeable，不是 318 validatorupdate bundled interchangeable / 33 four gates interchangeable / validatorupdate-sold-as-set interchangeable。

2. **看见失败 不是 already recoverable：** 看见块执行失败 / 不可恢复失败，不是已经能重放修好 interchangeable / 已经能恢复 interchangeable，不是 318 validatorupdate item 1 interchangeable / 713 validatorupdate-notempty interchangeable。

3. **看见同一把钥 不是 already two rows：** 看见同一把公钥 / 一把公钥出现两次，不是已经能写两行 interchangeable / 已经能写两份更新 interchangeable，不是 318 validatorupdate item 3 interchangeable / 715 validatorupdate-notpower0 interchangeable。

官方把看见重复单句、already last-wins、already recoverable、already two rows 写成三个名字。把它们叫成一个「看见重复就已经按后一条改权 interchangeable / 就已经能恢复 interchangeable / 就已经能写两行 interchangeable」，会把 not already last-wins、not already recoverable、not already two rows 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一批重复公钥不是已经能恢复 not already last-wins / not already recoverable / not already two rows 正式三事（318 余量），先数清问的是看见重复 是不是 already last-wins / 318 / validatorupdate-sold-as-set，是不是看见失败 是不是 already recoverable，还是看见同一把钥 是不是 already two rows，再决定要不要同一次发布。318 validatorupdate vs set bundled unbundling 在本页 item 2 完成。
