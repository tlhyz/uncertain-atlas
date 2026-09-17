# 反模式：把 两边对任意块同一裁决 not already only honest same verdict / not already Req 3 honest Accept / not already settled 正式三事（340 余量） 卖成 已经只对诚实提案同一裁决 / 已经是 Req 3 诚实对诚实 / 已经交差

**层次**：实现 / ProcessProposal 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-det-nothonest-vs-bundled.md](../../tracks/implementation/worked-example-process-det-nothonest-vs-bundled.md)。

官方把 Process 必须只依赖请求和上一份状态 / 两边对任意块同一裁决 / Process 非确定 bug 没有现成解法 三条核心句写成三件独立的实现事。把它们卖成已经只对诚实提案同一裁决 / 已经是 Req 3 诚实对诚实 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意块同一裁决 正式三事（340 余量），必须分开 not already only honest same verdict、not already Req 3 honest Accept、not already settled 三件事，不要和 340 / 33 / 347 / 893 / 895 糊成一句。

## 和相邻反模式

- [process-det-notprep-sold-as-bundled](process-det-notprep-sold-as-bundled.md) 是 Process 必须确定单句边界（893 item 1），不是本页任意块同判边界。
- Req 3 必须 Accept 是不变量 347 / 872，不是本页任意块同判边界。
