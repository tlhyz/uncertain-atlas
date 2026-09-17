# 反模式：把 还在振荡 not already past h_stable / not already left the pool / not already settled 正式三事（328 余量） 卖成 已经过了 h_stable / 已经离池 / 已经交差

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-oscillate-notstable-vs-bundled.md](../../tracks/implementation/worked-example-checktx-oscillate-notstable-vs-bundled.md)。

官方把同一高度回了不同码 / 还在振荡 / 本地不再振荡 三条核心句写成三件独立的实现事。把它们卖成已经过了 h_stable / 已经离池 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看还在振荡 正式三事（328 余量），必须分开 not already past h_stable、not already left the pool、not already settled 三件事，不要和 328 / 301 / 33 / 941 / 943 糊成一句。

## 和相邻反模式

- [checktx-oscillate-notcode-sold-as-bundled](checktx-oscillate-notcode-sold-as-bundled.md) 是多码集合仍未定义单码单句边界（941 item 1），不是本页还在振荡仍未过 h_stable 边界。
- 提案收了已经从池里删掉是不变量 301，不是本页还在振荡仍未离池边界。
