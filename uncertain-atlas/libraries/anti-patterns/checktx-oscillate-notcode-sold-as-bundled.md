# 反模式：把 同一高度回了不同码 not already CheckTxCode / not already OK / not already settled 正式三事（328 余量） 卖成 已经有了 CheckTxCode / 已经能说 OK / 已经交差

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-oscillate-notcode-vs-bundled.md](../../tracks/implementation/worked-example-checktx-oscillate-notcode-vs-bundled.md)。

官方把同一高度回了不同码 / 还在振荡 / 本地不再振荡 三条核心句写成三件独立的实现事。把它们卖成已经有了 CheckTxCode / 已经能说 OK / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一高度回了不同码 正式三事（328 余量），必须分开 not already CheckTxCode、not already OK、not already settled 三件事，不要和 328 / 312 / 339 / 942 / 943 糊成一句。

## 和相邻反模式

- [query-notmust-sold-as-bundled](query-notmust-sold-as-bundled.md) 是实现了 Query 仍不是必须有边界（329/940），不是本页集合仍不是 CheckTxCode 边界。
- CheckTxState 已经是 ExecuteTxState 是不变量 312，不是本页多码集合仍未定义单码边界。
