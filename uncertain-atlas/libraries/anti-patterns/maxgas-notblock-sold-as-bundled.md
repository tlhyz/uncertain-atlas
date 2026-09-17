# 反模式：把 已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事（315 余量） 卖成 已经按气验过 / 已经由共识层验过 / 已经交差

**层次**：实现 / 气。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxgas-notblock-vs-bundled.md](../../tracks/implementation/worked-example-maxgas-notblock-vs-bundled.md)。

官方把 MaxGas / GasUsed / 已提交块 三条核心句写成三件独立的实现事。把它们卖成已经按气验过 / 已经由共识层验过 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看已提交块 正式三事（315 余量），必须分开 not already gas-checked、not already consensus-enforced、not already settled 三件事，不要和 315 / 33 / 914 / 915 糊成一句。

## 和相邻反模式

- [maxgas-notused-sold-as-bundled](maxgas-notused-sold-as-bundled.md) 是 GasUsed 被忽略单句边界（915 item 2），不是本页已提交块不保证守气限边界。
- 四门已经结算是不变量 33，不是本页旧版只在池里管气边界。
