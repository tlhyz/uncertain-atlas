# 反模式：把 扩展关掉全空 not already enable height / not already settled / not already from block 正式三事（369 余量） 卖成 已经到了启用高度 / 已经交差 / 已经从块里抽出

**层次**：实现 / ExtendedVoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extvoteinfo-notenabled-vs-bundled.md](../../tracks/implementation/worked-example-extvoteinfo-notenabled-vs-bundled.md)。

官方把 ExtendedVoteInfo 从本进程抽出 / 把验过的签交给应用 / 扩展关掉则字段全空三条核心句写成三件独立的实现事。把它们卖成已经到了启用高度 / 已经交差 / 已经从块里抽出，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看扩展关掉全空 正式三事（369 余量），必须分开 not already enable height、not already settled、not already from block 三件事，不要和 369 / 330 / 361 / 365 / 818 / 819 糊成一句。

## 和相邻反模式

- [extvoteinfo-notsigned-sold-as-bundled](extvoteinfo-notsigned-sold-as-bundled.md) 是交给应用单句边界（819 item 2），不是本页关掉全空边界。
- 到了 H 就已经 Prepare 带了扩展是不变量 330，不是本页关掉全空边界。
