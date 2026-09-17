# 反模式：把 Info 请求 version not already app_version / not already header AppHash / not already settled 正式三事（379 余量） 说成已经是 app_version / 已经印进本头 AppHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notappver-vs-bundled.md)。

## 卖法

把 Info 请求版本这句写成已经已经是 app_version / 已经印进本头 AppHash / 已经交差 interchangeable，或已经和 379 infover-vs-appversion bundled / infover-notappver-sold-as-bundled interchangeable。

## 为什么错

官方把 Info 请求 version / block_version / p2p_version / abci_version 三条核心句写成三件独立的实现事。把它们卖成已经是 app_version / 已经印进本头 AppHash / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 请求 version 正式三事（379 余量），必须分开 not already app_version、not already header AppHash、not already settled 三件事，不要和 379 / 370 / 389 / 762 / 385 / 775 / 792 / 793 糊成一句。

## 和相邻反模式

- [infodata-notappversion-sold-as-bundled](infodata-notappversion-sold-as-bundled.md) 是 Info 回包 version 就已经是 app_version（389/762），不是本页 Info 请求 version 边界。
- [paramsblock-notappver-sold-as-bundled](paramsblock-notappver-sold-as-bundled.md) 是 ConsensusParams.version 就已经是 app_version 进了头（385/775），不是本页 Info 请求 version 边界。
