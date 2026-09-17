# 反模式：把 不该验排序相关有效性 not already should-check-in-CheckTx / not already execute-state-checked / not already settled 正式三事（339 余量） 卖成 已经该在 CheckTx 里验 / 已经按将要执行的那份验过 / 已经交差

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-weak-notsort-vs-bundled.md](../../tracks/implementation/worked-example-checktx-weak-notsort-vs-bundled.md)。

官方把不该验排序相关有效性 / 拜占庭能提案一满块无效交易 / ProcessProposal 对付这种行为 三条核心句写成三件独立的实现事。把它们卖成已经该在 CheckTx 里验 / 已经按将要执行的那份验过 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不该验排序相关有效性 正式三事（339 余量），必须分开 not already should-check-in-CheckTx、not already execute-state-checked、not already settled 三件事，不要和 339 / 312 / 33 / 930 / 931 糊成一句。

## 和相邻反模式

- [ve-height-notlegal-sold-as-bundled](ve-height-notlegal-sold-as-bundled.md) 是启用前带扩展仍畸形边界（330/928），不是本页 CheckTx 不该验排序边界。
- CheckTxState 已经是 ExecuteTxState 是不变量 312，不是本页不该验排序仍不该写进 CheckTx 边界。
