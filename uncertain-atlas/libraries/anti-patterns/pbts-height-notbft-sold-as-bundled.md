# 反模式：把 H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事（343 余量） 卖成 已经切到 PBTS / 已经是 MTP / 已经交差

**层次**：实现 / PbtsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-pbts-height-notbft-vs-bundled.md](../../tracks/implementation/worked-example-pbts-height-notbft-vs-bundled.md)。

官方把写成 0 不是已经启用 PBTS / H 之前仍用 BFT Time / 启用之后不能关 三条核心句写成三件独立的实现事。把它们卖成已经切到 PBTS / 已经是 MTP / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H 之前仍用 BFT Time 正式三事（343 余量），必须分开 not already switched to PBTS、not already MTP、not already settled 三件事，不要和 343 / 40 / 330 / 884 / 886 糊成一句。

## 和相邻反模式

- [pbts-height-notzero-sold-as-bundled](pbts-height-notzero-sold-as-bundled.md) 是写成 0 单句边界（884 item 1），不是本页旧钟边界。
- 块时间必须点名算法是不变量 40，不是本页旧钟边界。
