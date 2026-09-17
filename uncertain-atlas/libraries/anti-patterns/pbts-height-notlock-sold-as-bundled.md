# 反模式：把 启用之后不能关 not already vote-extension switch / not already can disable / not already settled 正式三事（343 余量） 卖成 已经是扩展启用高度那种切换 / 已经能关 / 已经交差

**层次**：实现 / PbtsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-pbts-height-notlock-vs-bundled.md](../../tracks/implementation/worked-example-pbts-height-notlock-vs-bundled.md)。

官方把写成 0 不是已经启用 PBTS / H 之前仍用 BFT Time / 启用之后不能关 三条核心句写成三件独立的实现事。把它们卖成已经是扩展启用高度那种切换 / 已经能关 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启用之后不能关 正式三事（343 余量），必须分开 not already vote-extension switch、not already can disable、not already settled 三件事，不要和 343 / 330 / 346 / 884 / 885 糊成一句。

## 和相邻反模式

- [pbts-height-notbft-sold-as-bundled](pbts-height-notbft-sold-as-bundled.md) 是旧钟单句边界（885 item 2），不是本页不能关边界。
- 到了 H 已经 Prepare 带了扩展是不变量 330，不是本页不能关边界。
