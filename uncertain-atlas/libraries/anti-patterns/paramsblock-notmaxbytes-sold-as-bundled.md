# 反模式：把 ConsensusParams.block not already MaxBytes cap / not already next_block_delay / not already settled 正式三事（385 余量） 说成已经是 MaxBytes 上限 / 已经是 next_block_delay / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ConsensusParams.block ≠ bundled（385）](../../tracks/implementation/worked-example-paramsblock-notmaxbytes-vs-bundled.md)。

## 卖法

把 ConsensusParams 字段这句写成已经已经是 MaxBytes 上限 / 已经是 next_block_delay / 已经交差 interchangeable，或已经和 385 paramsblock-vs-maxbytes bundled / paramsblock-notmaxbytes-sold-as-bundled interchangeable。

## 为什么错

官方把 ConsensusParams.block / validator / version 三条核心句写成三件独立的实现事。把它们卖成已经是 MaxBytes 上限 / 已经是 next_block_delay / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.block 正式三事（385 余量），必须分开 not already MaxBytes cap、not already next_block_delay、not already settled 三件事，不要和 385 / 337 / 386 / 770 / 774 / 775 糊成一句。

## 和相邻反模式

- [paramsblock-sold-as-maxbytes](paramsblock-sold-as-maxbytes.md) 是 ConsensusParams 字段 bundled（385），不是本页 item 1 单句边界。
- [paramsevidence-notmaxbytes-sold-as-bundled](paramsevidence-notmaxbytes-sold-as-bundled.md) 是 ConsensusParams.evidence 就已经是证据 MaxBytes（386/770），不是本页 block 边界。
