# 反模式：把 两边对任意扩展同一裁决 not already only honest same verdict / not already Req 6 honest Accept / not already settled 正式三事（341 余量） 卖成 已经只对诚实扩展同一裁决 / 已经是 Req 6 诚实对诚实 / 已经交差

**层次**：实现 / VerifyVoteExtension 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-verify-det-nothonest-vs-bundled.md](../../tracks/implementation/worked-example-verify-det-nothonest-vs-bundled.md)。

官方把 Verify 必须只依赖扩展、这块和上一份状态 / 两边对任意扩展同一裁决 / Verify 非确定会伤活性 三条核心句写成三件独立的实现事。把它们卖成已经只对诚实扩展同一裁决 / 已经是 Req 6 诚实对诚实 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意扩展同一裁决 正式三事（341 余量），必须分开 not already only honest same verdict、not already Req 6 honest Accept、not already settled 三件事，不要和 341 / 34 / 348 / 890 / 892 糊成一句。

## 和相邻反模式

- [verify-det-notext-sold-as-bundled](verify-det-notext-sold-as-bundled.md) 是 Verify 必须确定单句边界（890 item 1），不是本页任意扩展同判边界。
- Req 6 必须 Accept 是不变量 348 / 869，不是本页任意扩展同判边界。
