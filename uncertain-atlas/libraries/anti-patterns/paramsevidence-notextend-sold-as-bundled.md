# 反模式：把 ConsensusParams.abci not already Prepare extension / not already ABCI 2.0 / not already settled 正式三事（386 余量） 说成已经 Prepare 带了扩展 / 已经切到 ABCI 2.0 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ConsensusParams.abci ≠ bundled（386）](../../tracks/implementation/worked-example-paramsevidence-notextend-vs-bundled.md)。

## 卖法

把 ConsensusParams 余栏这句写成已经已经 Prepare 带了扩展 / 已经切到 ABCI 2.0 / 已经交差 interchangeable，或已经和 386 paramsevidence-vs-maxbytes bundled / paramsevidence-notextend-sold-as-bundled interchangeable。

## 为什么错

官方把 ConsensusParams.evidence / abci / synchrony 三条核心句写成三件独立的实现事。把它们卖成已经 Prepare 带了扩展 / 已经切到 ABCI 2.0 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.abci 正式三事（386 余量），必须分开 not already Prepare extension、not already ABCI 2.0、not already settled 三件事，不要和 386 / 330 / 770 / 772 糊成一句。

## 和相邻反模式

- [paramsevidence-sold-as-maxbytes](paramsevidence-sold-as-maxbytes.md) 是 ConsensusParams 余栏 bundled（386），不是本页 item 2 单句边界。
- [paramsevidence-notmaxbytes-sold-as-bundled](paramsevidence-notmaxbytes-sold-as-bundled.md) 是 evidence 单句边界（770 item 1），不是本页 abci 边界。
