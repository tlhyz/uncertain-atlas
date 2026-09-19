# 反模式：把 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量）说成已经没有参数 / 已经删掉创世参数 / 已经用了应用自己的空参数

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了空 not already no params ≠ bundled（319）](../../tracks/implementation/worked-example-consensusparams-notempty-vs-bundled.md)。

## 卖法

把回了空 / InitChain 回了空 ConsensusParams / 参数空 写成已经没有参数 interchangeable / 已经 no params interchangeable / 已经空参数交差 interchangeable / 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable；把没回参数 / 没回 ConsensusParams / InitChain 没回参数 写成已经删掉创世参数 interchangeable / 已经 deleted genesis params interchangeable；把能设初始参数 / InitChain 能设参数 / 应用可设参数 写成已经用了应用自己的空参数 interchangeable / 已经 app empty params interchangeable / 已经和 InitChain 空验证者名单同一句 interchangeable，或已经和 319 consensusparams bundled / consensusparams-sold-as-updated interchangeable / 716 consensusparams-notempty interchangeable。

## 为什么错

官方把回了空单句、already no params、already deleted genesis params、already app empty params 写成三件独立的实现事。把它们卖成 already no params interchangeable / already deleted genesis params interchangeable / already app empty params interchangeable，会把 not already no params、not already deleted genesis params、not already app empty params 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空参数不是已经没有参数 not already no params / not already deleted genesis params / not already app empty params 正式三事（319 余量），必须分开 not already no params、not already deleted genesis params、not already app empty params 三件事，不要和 319 / 33 / 717 / 718 / 318 / 713 / 35 糊成一句。

## 和相邻反模式

- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是 ConsensusParams vs update bundled 全段，不是本页回了空 item 1 单句边界。
- [validatorupdate-notempty-sold-as-bundled](validatorupdate-notempty-sold-as-bundled.md) 是 InitChain 空验证者名单（318），不是本页空参数边界。
- [validatorupdate-notpower0-sold-as-bundled](validatorupdate-notpower0-sold-as-bundled.md) 是 power 0（318），不是本页 ConsensusParams 边界。
