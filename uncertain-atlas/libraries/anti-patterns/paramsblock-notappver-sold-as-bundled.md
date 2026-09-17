# 反模式：把 ConsensusParams.version not already app_version in header / not already header AppHash / not already settled 正式三事（385 余量） 说成已经是 app_version 进了头 / 已经印进本头 AppHash / 已经是握手对齐

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ConsensusParams.version ≠ bundled（385）](../../tracks/implementation/worked-example-paramsblock-notappver-vs-bundled.md)。

## 卖法

把 ConsensusParams 字段这句写成已经已经是 app_version 进了头 / 已经印进本头 AppHash / 已经是握手对齐 interchangeable，或已经和 385 paramsblock-vs-maxbytes bundled / paramsblock-notappver-sold-as-bundled interchangeable。

## 为什么错

官方把 ConsensusParams.block / validator / version 三条核心句写成三件独立的实现事。把它们卖成已经是 app_version 进了头 / 已经印进本头 AppHash / 已经是握手对齐，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.version 正式三事（385 余量），必须分开 not already app_version in header、not already header AppHash、not already settled 三件事，不要和 385 / 370 / 389 / 762 / 773 / 774 糊成一句。

## 和相邻反模式

- [paramsblock-sold-as-maxbytes](paramsblock-sold-as-maxbytes.md) 是 ConsensusParams 字段 bundled（385），不是本页 item 3 单句边界。
- [infodata-notappversion-sold-as-bundled](infodata-notappversion-sold-as-bundled.md) 是 Info 回包 version 就已经是 app_version（389/762），不是本页 ConsensusParams.version 边界。
