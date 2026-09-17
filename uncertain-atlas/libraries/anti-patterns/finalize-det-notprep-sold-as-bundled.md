# 反模式：把 Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（342 余量） 卖成 已经可以像 Prepare 那样依赖其它值 / 已经和 Prepare 同一把尺 / 已经交差

**层次**：实现 / FinalizeBlock 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-det-notprep-vs-bundled.md](../../tracks/implementation/worked-example-finalize-det-notprep-vs-bundled.md)。

官方把 Finalize 算出的状态必须只依赖上一份状态和决定块 / Finalize 算出的结果必须只依赖上一份状态和决定块 / 两边状态机复制 三条核心句写成三件独立的实现事。把它们卖成已经可以像 Prepare 那样依赖其它值 / 已经和 Prepare 同一把尺 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的状态必须只依赖上一份状态和决定块 正式三事（342 余量），必须分开 not already Prepare-style other values、not already same ruler as Prepare、not already settled 三件事，不要和 342 / 338 / 316 / 888 / 889 糊成一句。

## 和相邻反模式

- [pbts-height-notlock-sold-as-bundled](pbts-height-notlock-sold-as-bundled.md) 是 PBTS 启用后不能关（343/886），不是本页 Finalize 状态确定性边界。
- Prepare 没有确定性要求是不变量 338，不是本页 Finalize 状态确定性边界。
