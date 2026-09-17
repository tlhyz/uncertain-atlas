# 反模式：把 GasUsed not already consensus-checked / not already counted / not already settled 正式三事（315 余量） 卖成 已经按实用气验过 / 已经算进共识 / 已经交差

**层次**：实现 / 气。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxgas-notused-vs-bundled.md](../../tracks/implementation/worked-example-maxgas-notused-vs-bundled.md)。

官方把 MaxGas / GasUsed / 已提交块 三条核心句写成三件独立的实现事。把它们卖成已经按实用气验过 / 已经算进共识 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 GasUsed 正式三事（315 余量），必须分开 not already consensus-checked、not already counted、not already settled 三件事，不要和 315 / 63 / 33 / 914 / 916 糊成一句。

## 和相邻反模式

- [maxgas-noton-sold-as-bundled](maxgas-noton-sold-as-bundled.md) 是 MaxGas 默认 -1 单句边界（914 item 1），不是本页引擎忽略 GasUsed 边界。
- 仓库默认 MaxBytes 已经是第一轮 SLA 是不变量 63，不是本页 GasUsed 被忽略边界。
