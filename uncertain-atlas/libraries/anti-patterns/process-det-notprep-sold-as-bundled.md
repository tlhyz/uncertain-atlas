# 反模式：把 Process 必须只依赖请求和上一份状态 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（340 余量） 卖成 已经可以像 Prepare 那样依赖其它值 / 已经和 Prepare 同一把尺 / 已经交差

**层次**：实现 / ProcessProposal 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-det-notprep-vs-bundled.md](../../tracks/implementation/worked-example-process-det-notprep-vs-bundled.md)。

官方把 Process 必须只依赖请求和上一份状态 / 两边对任意块同一裁决 / Process 非确定 bug 没有现成解法 三条核心句写成三件独立的实现事。把它们卖成已经可以像 Prepare 那样依赖其它值 / 已经和 Prepare 同一把尺 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 必须只依赖请求和上一份状态 正式三事（340 余量），必须分开 not already Prepare-style other values、not already same ruler as Prepare、not already settled 三件事，不要和 340 / 338 / 33 / 894 / 895 糊成一句。

## 和相邻反模式

- [verify-det-notext-sold-as-bundled](verify-det-notext-sold-as-bundled.md) 是 Verify 必须确定（341/890），不是本页 Process 确定性边界。
- Prepare 没有确定性要求是不变量 338，不是本页 Process 确定性边界。
