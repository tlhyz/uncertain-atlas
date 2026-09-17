# 反模式：把 ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事（339 余量） 卖成 已经是 CheckTx / 已经是 Finalize / 已经交差

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-weak-notproc-vs-bundled.md](../../tracks/implementation/worked-example-checktx-weak-notproc-vs-bundled.md)。

官方把不该验排序相关有效性 / 拜占庭能提案一满块无效交易 / ProcessProposal 对付这种行为 三条核心句写成三件独立的实现事。把它们卖成已经是 CheckTx / 已经是 Finalize / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal 对付这种行为 正式三事（339 余量），必须分开 not already CheckTx、not already Finalize、not already settled 三件事，不要和 339 / 313 / 328 / 929 / 930 糊成一句。

## 和相邻反模式

- [checktx-weak-notpool-sold-as-bundled](checktx-weak-notpool-sold-as-bundled.md) 是拜占庭仍能提案无效块单句边界（930 item 2），不是本页 ProcessProposal 还不是 CheckTx 边界。
- 索引器已经保证不重放是不变量 313，不是本页 ProcessProposal 对付弱过滤器边界。
