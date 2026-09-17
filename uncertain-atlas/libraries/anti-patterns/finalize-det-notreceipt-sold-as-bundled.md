# 反模式：把 Finalize 算出的结果必须只依赖上一份状态和决定块 not already Code/Data in header / not already same list order / not already settled 正式三事（342 余量） 卖成 已经是 Code/Data 印进本头 / 已经是回执顺序对上 / 已经交差

**层次**：实现 / FinalizeBlock 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-det-notreceipt-vs-bundled.md](../../tracks/implementation/worked-example-finalize-det-notreceipt-vs-bundled.md)。

官方把 Finalize 算出的状态必须只依赖上一份状态和决定块 / Finalize 算出的结果必须只依赖上一份状态和决定块 / 两边状态机复制 三条核心句写成三件独立的实现事。把它们卖成已经是 Code/Data 印进本头 / 已经是回执顺序对上 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的结果必须只依赖上一份状态和决定块 正式三事（342 余量），必须分开 not already Code/Data in header、not already same list order、not already settled 三件事，不要和 342 / 316 / 338 / 887 / 889 糊成一句。

## 和相邻反模式

- [finalize-det-notprep-sold-as-bundled](finalize-det-notprep-sold-as-bundled.md) 是状态必须确定单句边界（887 item 1），不是本页结果确定性边界。
- 结果列表已经同一顺序是不变量 316，不是本页结果确定性边界。
