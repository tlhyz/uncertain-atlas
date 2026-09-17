# 反模式：把 H+1 带了扩展 not already this-height just-signed / not already this-height e / not already settled 正式三事（330 余量） 卖成 已经是本高度刚签的 / 已经是这一高的 e / 已经交差

**层次**：实现 / VoteExtensionsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-ve-height-notthis-vs-bundled.md](../../tracks/implementation/worked-example-ve-height-notthis-vs-bundled.md)。

官方把到了 H / H+1 带了扩展 / h < H 带了扩展 三条核心句写成三件独立的实现事。把它们卖成已经是本高度刚签的 / 已经是这一高的 e / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 带了扩展 正式三事（330 余量），必须分开 not already this-height just-signed、not already this-height e、not already settled 三件事，不要和 330 / 58 / 35 / 926 / 928 糊成一句。

## 和相邻反模式

- [ve-height-notprep-sold-as-bundled](ve-height-notprep-sold-as-bundled.md) 是到了 H 还没 Prepare 带扩展单句边界（926 item 1），不是本页 H+1 带的是高度 H 的扩展边界。
- 治理改 enable-height 会 panic 是不变量 58，不是本页 H+1 带的不是本高刚签边界。
