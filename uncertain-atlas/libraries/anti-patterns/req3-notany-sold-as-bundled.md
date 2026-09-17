# 反模式：把 正确提议者的准备提案必须被正确接收者 Accept not already any block Accepts / not already default Accept / not already settled 正式三事（347 余量） 卖成 已经是任意块都会 Accept / 已经写了默认 Accept / 已经交差

**层次**：实现 / Prepare–Process 一致性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req3-notany-vs-bundled.md](../../tracks/implementation/worked-example-req3-notany-vs-bundled.md)。

官方把正确提议者的准备提案必须被正确接收者 Accept / Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 / Req 3 是大量测试和自动验证的目标 三条核心句写成三件独立的实现事。把它们卖成已经是任意块都会 Accept / 已经写了默认 Accept / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确提议者的准备提案必须被正确接收者 Accept 正式三事（347 余量），必须分开 not already any block Accepts、not already default Accept、not already settled 三件事，不要和 347 / 33 / 348 / 869 / 873 / 874 糊成一句。

## 和相邻反模式

- [req6-notany-sold-as-bundled](req6-notany-sold-as-bundled.md) 是 Req 6 必须 Accept（348/869），不是本页提案必须 Accept 边界。
- 四门已经结算是不变量 33，不是本页提案必须 Accept 边界。
