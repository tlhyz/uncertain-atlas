# 反模式：把 Extend 和 Verify 不得改已提交状态 not already signed into state / not already sh independent of e / not already settled 正式三事（349 余量） 卖成 已经签了扩展就已经进状态 / 已经是 sh 不依赖 e / 已经交差

**层次**：实现 / 四门无副作用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req9-notext-vs-bundled.md](../../tracks/implementation/worked-example-req9-notext-vs-bundled.md)。

官方把 Prepare 不得改已提交状态 / Process 不得改已提交状态 / Extend 和 Verify 不得改已提交状态 三条核心句写成三件独立的实现事。把它们卖成已经签了扩展就已经进状态 / 已经是 sh 不依赖 e / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 和 Verify 不得改已提交状态 正式三事（349 余量），必须分开 not already signed into state、not already sh independent of e、not already settled 三件事，不要和 349 / 34 / 350 / 865 / 866 / 867 糊成一句。

## 和相邻反模式

- [req9-notproc-sold-as-bundled](req9-notproc-sold-as-bundled.md) 是 Process 无副作用单句边界（867 item 2），不是本页扩展两门无副作用边界。
- 本高度状态不得依赖本高度收到的扩展是不变量 34，不是本页扩展两门无副作用边界。
