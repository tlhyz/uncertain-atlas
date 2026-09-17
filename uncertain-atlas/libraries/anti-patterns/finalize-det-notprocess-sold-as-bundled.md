# 反模式：把 两边状态机复制 not already Process same verdict / not already Prepare may be nondet / not already settled 正式三事（342 余量） 卖成 已经是 Process 对任意块同一裁决 / 已经是 Prepare 可以不确定 / 已经交差

**层次**：实现 / FinalizeBlock 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-det-notprocess-vs-bundled.md](../../tracks/implementation/worked-example-finalize-det-notprocess-vs-bundled.md)。

官方把 Finalize 算出的状态必须只依赖上一份状态和决定块 / Finalize 算出的结果必须只依赖上一份状态和决定块 / 两边状态机复制 三条核心句写成三件独立的实现事。把它们卖成已经是 Process 对任意块同一裁决 / 已经是 Prepare 可以不确定 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边状态机复制 正式三事（342 余量），必须分开 not already Process same verdict、not already Prepare may be nondet、not already settled 三件事，不要和 342 / 340 / 338 / 887 / 888 糊成一句。

## 和相邻反模式

- [finalize-det-notreceipt-sold-as-bundled](finalize-det-notreceipt-sold-as-bundled.md) 是结果必须确定单句边界（888 item 2），不是本页状态机复制边界。
- Process 必须只依赖请求和上一份状态是不变量 340，不是本页状态机复制边界。
