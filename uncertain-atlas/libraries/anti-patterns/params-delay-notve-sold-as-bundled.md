# 反模式：把 参数更新写了 H+1 not already VE enable-height switch / not already only that field / not already settled 正式三事（333 余量） 卖成 已经是扩展启用高度那种切换 / 已经只改填的那一项 / 已经交差

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：建议（产品）。  
**对应例**：[worked-example-params-delay-notve-vs-bundled.md](../../tracks/implementation/worked-example-params-delay-notve-vs-bundled.md)。

官方把本高回了 ConsensusParams / H+1 立刻用了新参数 / 参数更新写了 H+1 三条核心句写成三件独立的实现事。把它们卖成已经是扩展启用高度那种切换 / 已经只改填的那一项 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看参数更新写了 H+1 正式三事（333 余量），必须分开 not already VE enable-height switch、not already only that field、not already settled 三件事，不要和 333 / 330 / 319 / 911 / 912 糊成一句。

## 和相邻反模式

- [params-delay-notvalset-sold-as-bundled](params-delay-notvalset-sold-as-bundled.md) 是参数延迟 ≠ 集合延迟单句边界（912 item 2），不是本页 H+1 ≠ 扩展启用高度边界。
- 只填一项就已经只改这一项是不变量 319 / 910，不是本页参数生效写了 H+1 边界。
