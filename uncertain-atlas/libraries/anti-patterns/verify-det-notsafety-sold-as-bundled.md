# 反模式：把 Verify 非确定会伤活性 not already lost safety / not already engine patch / not already settled 正式三事（341 余量） 卖成 已经丢了安全性 / 已经有协议层补丁 / 已经交差

**层次**：实现 / VerifyVoteExtension 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-verify-det-notsafety-vs-bundled.md](../../tracks/implementation/worked-example-verify-det-notsafety-vs-bundled.md)。

官方把 Verify 必须只依赖扩展、这块和上一份状态 / 两边对任意扩展同一裁决 / Verify 非确定会伤活性 三条核心句写成三件独立的实现事。把它们卖成已经丢了安全性 / 已经有协议层补丁 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 非确定会伤活性 正式三事（341 余量），必须分开 not already lost safety、not already engine patch、not already settled 三件事，不要和 341 / 340 / 348 / 890 / 891 糊成一句。

## 和相邻反模式

- [verify-det-nothonest-sold-as-bundled](verify-det-nothonest-sold-as-bundled.md) 是任意扩展同判单句边界（891 item 2），不是本页活性边界。
- Process 非确定 bug 没有现成解法是不变量 340，不是本页活性边界。
