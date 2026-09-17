# 反模式：把 用于 PBTS not already eternal constant / not already BFT Time median / not already settled 正式三事（336 余量） 卖成 已经是永恒常数 / 已经是 BFT Time 中位数 / 已经交差

**层次**：实现 / SynchronyParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-precision-notconst-vs-bundled.md](../../tracks/implementation/worked-example-precision-notconst-vs-bundled.md)。

官方把填了 Precision / 填了两个 / 用于 PBTS 三条核心句写成三件独立的实现事。把它们卖成已经是永恒常数 / 已经是 BFT Time 中位数 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看用于 PBTS 正式三事（336 余量），必须分开 not already eternal constant、not already BFT Time median、not already settled 三件事，不要和 336 / 40 / 343 / 923 / 924 糊成一句。

## 和相邻反模式

- [precision-noton-sold-as-bundled](precision-noton-sold-as-bundled.md) 是填了两个还没启用 PBTS 单句边界（924 item 2），不是本页用于 PBTS 还不是永恒常数边界。
- PBTS 启用高度已经切了是不变量 343，不是本页用于 PBTS 还不是产品常数边界。
