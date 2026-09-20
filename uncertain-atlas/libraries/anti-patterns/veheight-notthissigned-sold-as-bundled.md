# 反模式：把 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量）说成已经是本高度刚签 / 已经是本高 e / 已经是同高 e

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[H+1 带了扩展 not already this-height-signed ≠ bundled（330）](../../tracks/implementation/worked-example-veheight-notthissigned-vs-bundled.md)。

## 卖法

把 H+1 带了扩展 / H+1 的 Prepare 带了 / 到了 H+1 写成已经是本高度刚签的 interchangeable / 已经 this-height-signed interchangeable / 已经本高刚签交差 interchangeable / 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable；把本高度刚签的那份 / 刚签的扩展 / 本高 e 写成已经是本高 e interchangeable / 已经 local-e interchangeable；把 Prepare 列表里有扩展 / 这一高的 e / 同高 e 写成已经是这一高的 e interchangeable / 已经 same-h-e interchangeable，或已经和 330 veheight bundled / veheight-sold-as-prepared interchangeable / 747 veheight-notthissigned interchangeable。

## 为什么错

官方把 H+1 带了扩展单句、already this-height-signed、already local-e、already same-h-e 写成三件独立的实现事。把它们卖成 already this-height-signed interchangeable / already local-e interchangeable / already same-h-e interchangeable，会把 not already this-height-signed、not already local-e、not already same-h-e 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量），必须分开 not already this-height-signed、not already local-e、not already same-h-e 三件事，不要和 330 / 33 / 34 / 35 / 746 / 748 糊成一句。

## 和相邻反模式

- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是 VoteExtensionsEnableHeight bundled 全段，不是本页本高度刚签 item 2 单句边界。
- [veheight-notprepare-sold-as-bundled](veheight-notprepare-sold-as-bundled.md) 是到了 H item 1，不是本页 H+1 与本高度刚签边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交（34），不是本页本高 e 边界。
