# 反模式：把 Prepare 不得改已提交状态 not already immediate exec settled / not already Finalize+Commit / not already can mutate s 正式三事（349 余量） 卖成 已经立刻执行就已经交差 / 已经是 Finalize + Commit / 已经能改已提交状态

**层次**：实现 / 四门无副作用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req9-notprep-vs-bundled.md](../../tracks/implementation/worked-example-req9-notprep-vs-bundled.md)。

官方把 Prepare 不得改已提交状态 / Process 不得改已提交状态 / Extend 和 Verify 不得改已提交状态 三条核心句写成三件独立的实现事。把它们卖成已经立刻执行就已经交差 / 已经是 Finalize + Commit / 已经能改已提交状态，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 不得改已提交状态 正式三事（349 余量），必须分开 not already immediate exec settled、not already Finalize+Commit、not already can mutate s 三件事，不要和 349 / 33 / 350 / 863 / 867 / 868 糊成一句。

## 和相邻反模式

- [extend-once-notresign-sold-as-bundled](extend-once-notresign-sold-as-bundled.md) 是一轮一张 Precommit（350/863），不是本页 Prepare 无副作用边界。
- 四门已经结算是不变量 33，不是本页 Prepare 无副作用边界。
