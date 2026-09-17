# 反模式：把 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only liveness / not already Process nondet / not already settled 正式三事（347 余量） 卖成 已经只是活性问题 / 已经是非确定 bug / 已经交差

**层次**：实现 / Prepare–Process 一致性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req3-notbyz-vs-bundled.md](../../tracks/implementation/worked-example-req3-notbyz-vs-bundled.md)。

官方把正确提议者的准备提案必须被正确接收者 Accept / Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 / Req 3 是大量测试和自动验证的目标 三条核心句写成三件独立的实现事。把它们卖成已经只是活性问题 / 已经是非确定 bug / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 正式三事（347 余量），必须分开 not already only liveness、not already Process nondet、not already settled 三件事，不要和 347 / 340 / 33 / 872 / 874 糊成一句。

## 和相邻反模式

- [req3-notany-sold-as-bundled](req3-notany-sold-as-bundled.md) 是必须 Accept 单句边界（872 item 1），不是本页确定 bug 算拜占庭边界。
- Process 必须只依赖请求和上一份状态是不变量 340，不是本页确定 bug 算拜占庭边界。
