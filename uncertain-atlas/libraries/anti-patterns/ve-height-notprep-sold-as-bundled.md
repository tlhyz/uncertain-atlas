# 反模式：把 到了 H not already Prepare carrying extensions / not already written into this-height proposal / not already settled 正式三事（330 余量） 卖成 已经 Prepare 带了扩展 / 已经写进本高提议 / 已经交差

**层次**：实现 / VoteExtensionsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-ve-height-notprep-vs-bundled.md](../../tracks/implementation/worked-example-ve-height-notprep-vs-bundled.md)。

官方把到了 H / H+1 带了扩展 / h < H 带了扩展 三条核心句写成三件独立的实现事。把它们卖成已经 Prepare 带了扩展 / 已经写进本高提议 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看到了 H 正式三事（330 余量），必须分开 not already Prepare carrying extensions、not already written into this-height proposal、not already settled 三件事，不要和 330 / 34 / 336 / 927 / 928 糊成一句。

## 和相邻反模式

- [precision-noton-sold-as-bundled](precision-noton-sold-as-bundled.md) 是填了两个还没启用 PBTS 边界（336/924），不是本页到了 H 还没 Prepare 带扩展边界。
- 验签拒收整张预提交是不变量 34，不是本页到了 H 仍不带扩展边界。
