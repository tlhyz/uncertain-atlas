# 反模式：把 Process 不得改已提交状态 not already Accept mutated / not already candidate ExecuteTxState / not already settled 正式三事（349 余量） 卖成 已经 Accept 就已经改了 / 已经是候选 ExecuteTxState / 已经交差

**层次**：实现 / 四门无副作用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req9-notproc-vs-bundled.md](../../tracks/implementation/worked-example-req9-notproc-vs-bundled.md)。

官方把 Prepare 不得改已提交状态 / Process 不得改已提交状态 / Extend 和 Verify 不得改已提交状态 三条核心句写成三件独立的实现事。把它们卖成已经 Accept 就已经改了 / 已经是候选 ExecuteTxState / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 不得改已提交状态 正式三事（349 余量），必须分开 not already Accept mutated、not already candidate ExecuteTxState、not already settled 三件事，不要和 349 / 311 / 33 / 866 / 868 糊成一句。

## 和相邻反模式

- [req9-notprep-sold-as-bundled](req9-notprep-sold-as-bundled.md) 是 Prepare 无副作用单句边界（866 item 1），不是本页 Process 无副作用边界。
- 候选已经是 ExecuteTxState 是不变量 311，不是本页 Process 无副作用边界。
