# 反模式：把 本地不再振荡 not already global same height / not already same b / not already settled 正式三事（328 余量） 卖成 已经是全局同一高度 / 已经各节点同一份 b / 已经交差

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-oscillate-notsameb-vs-bundled.md](../../tracks/implementation/worked-example-checktx-oscillate-notsameb-vs-bundled.md)。

官方把同一高度回了不同码 / 还在振荡 / 本地不再振荡 三条核心句写成三件独立的实现事。把它们卖成已经是全局同一高度 / 已经各节点同一份 b / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地不再振荡 正式三事（328 余量），必须分开 not already global same height、not already same b、not already settled 三件事，不要和 328 / 313 / 33 / 941 / 942 糊成一句。

## 和相邻反模式

- [checktx-oscillate-notstable-sold-as-bundled](checktx-oscillate-notstable-sold-as-bundled.md) 是还在振荡仍未过 h_stable 单句边界（942 item 2），不是本页本地稳住仍不是全网同一份 b 边界。
- 索引器已经保证不重放是不变量 313，不是本页本地稳住仍不是同一份 b 边界。
