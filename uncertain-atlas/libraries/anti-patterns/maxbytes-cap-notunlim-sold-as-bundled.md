# 反模式：把 -1 就按 100 MB 验 not already unlimited / not already free to return anything / not already settled 正式三事（337 余量） 卖成 已经没有上限 / 已经随便回 / 已经交差

**层次**：实现 / BlockParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-cap-notunlim-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-cap-notunlim-vs-bundled.md)。

官方把 -1 就按 100 MB 验 / 应用自己卡体积 / 必须 -1 或不超过 100 MB 三条核心句写成三件独立的实现事。把它们卖成已经没有上限 / 已经随便回 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 -1 就按 100 MB 验 正式三事（337 余量），必须分开 not already unlimited、not already free to return anything、not already settled 三件事，不要和 337 / 299 / 315 / 918 / 919 糊成一句。

## 和相邻反模式

- [maxgas-noton-sold-as-bundled](maxgas-noton-sold-as-bundled.md) 是 MaxGas 默认 -1 还不执行边界（315/914），不是本页 MaxBytes -1 仍按 100 MB 验边界。
- 整池都给 Prepare 就已经没有上限是不变量 299，不是本页 -1 仍按 100 MB 验边界。
