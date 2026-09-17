# 反模式：把 MaxGas not already executing / not already meaningful / not already settled 正式三事（315 余量） 卖成 已经在执行 / 已经有意义 / 已经交差

**层次**：实现 / 气。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxgas-noton-vs-bundled.md](../../tracks/implementation/worked-example-maxgas-noton-vs-bundled.md)。

官方把 MaxGas / GasUsed / 已提交块 三条核心句写成三件独立的实现事。把它们卖成已经在执行 / 已经有意义 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxGas 正式三事（315 余量），必须分开 not already executing、not already meaningful、not already settled 三件事，不要和 315 / 299 / 319 / 915 / 916 糊成一句。

## 和相邻反模式

- [consensusparams-notpartial-sold-as-bundled](consensusparams-notpartial-sold-as-bundled.md) 是只填一项（319/910），不是本页 MaxGas 默认 -1 还不执行边界。
- MaxBytes 写成 -1 已经没有上限是不变量 299，不是本页 MaxGas -1 没有意义边界。
