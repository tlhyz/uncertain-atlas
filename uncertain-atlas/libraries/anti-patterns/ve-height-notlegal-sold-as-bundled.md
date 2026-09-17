# 反模式：把 h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事（330 余量） 卖成 已经合法 / 已经启用 / 已经交差

**层次**：实现 / VoteExtensionsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-ve-height-notlegal-vs-bundled.md](../../tracks/implementation/worked-example-ve-height-notlegal-vs-bundled.md)。

官方把到了 H / H+1 带了扩展 / h < H 带了扩展 三条核心句写成三件独立的实现事。把它们卖成已经合法 / 已经启用 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h < H 带了扩展 正式三事（330 余量），必须分开 not already legal、not already enabled、not already settled 三件事，不要和 330 / 34 / 346 / 926 / 927 糊成一句。

## 和相邻反模式

- [ve-height-notthis-sold-as-bundled](ve-height-notthis-sold-as-bundled.md) 是 H+1 带的不是本高刚签单句边界（927 item 2），不是本页启用前带扩展仍畸形边界。
- ABCI 2.0 升级已经切完是不变量 346，不是本页 h < H 带扩展仍不合法边界。
