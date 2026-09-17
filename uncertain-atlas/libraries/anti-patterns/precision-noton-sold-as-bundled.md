# 反模式：把 填了两个 not already PBTS enabled / not already cannot-disable / not already settled 正式三事（336 余量） 卖成 已经启用 PBTS / 已经不能关 / 已经交差

**层次**：实现 / SynchronyParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-precision-noton-vs-bundled.md](../../tracks/implementation/worked-example-precision-noton-vs-bundled.md)。

官方把填了 Precision / 填了两个 / 用于 PBTS 三条核心句写成三件独立的实现事。把它们卖成已经启用 PBTS / 已经不能关 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了两个 正式三事（336 余量），必须分开 not already PBTS enabled、not already cannot-disable、not already settled 三件事，不要和 336 / 330 / 327 / 923 / 925 糊成一句。

## 和相邻反模式

- [precision-notmsg-sold-as-bundled](precision-notmsg-sold-as-bundled.md) 是 Precision 还不是 MessageDelay 单句边界（923 item 1），不是本页参数在还没启用 PBTS 边界。
- 到了 H 已经 Prepare 带了扩展是不变量 330，不是本页填了两个还没到 PbtsEnableHeight 边界。
