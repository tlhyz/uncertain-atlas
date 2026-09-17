# 反模式：把 ConsensusParams.validator not already has pubkey / not already selected type / not already settled 正式三事（385 余量） 说成已经带了公钥 / 已经选型 / 已经改了集合

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ConsensusParams.validator ≠ bundled（385）](../../tracks/implementation/worked-example-paramsblock-notpubkey-vs-bundled.md)。

## 卖法

把 ConsensusParams 字段这句写成已经已经带了公钥 / 已经选型 / 已经改了集合 interchangeable，或已经和 385 paramsblock-vs-maxbytes bundled / paramsblock-notpubkey-sold-as-bundled interchangeable。

## 为什么错

官方把 ConsensusParams.block / validator / version 三条核心句写成三件独立的实现事。把它们卖成已经带了公钥 / 已经选型 / 已经改了集合，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.validator 正式三事（385 余量），必须分开 not already has pubkey、not already selected type、not already settled 三件事，不要和 385 / 364 / 773 / 775 糊成一句。

## 和相邻反模式

- [paramsblock-sold-as-maxbytes](paramsblock-sold-as-maxbytes.md) 是 ConsensusParams 字段 bundled（385），不是本页 item 2 单句边界。
- [paramsblock-notmaxbytes-sold-as-bundled](paramsblock-notmaxbytes-sold-as-bundled.md) 是 block 单句边界（773 item 1），不是本页 validator 边界。
