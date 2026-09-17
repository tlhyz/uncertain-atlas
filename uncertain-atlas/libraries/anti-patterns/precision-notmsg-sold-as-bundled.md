# 反模式：把 填了 Precision not already MessageDelay / not already timely / not already settled 正式三事（336 余量） 卖成 已经是 MessageDelay / 已经 timely / 已经交差

**层次**：实现 / SynchronyParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-precision-notmsg-vs-bundled.md](../../tracks/implementation/worked-example-precision-notmsg-vs-bundled.md)。

官方把填了 Precision / 填了两个 / 用于 PBTS 三条核心句写成三件独立的实现事。把它们卖成已经是 MessageDelay / 已经 timely / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 Precision 正式三事（336 余量），必须分开 not already MessageDelay、not already timely、not already settled 三件事，不要和 336 / 40 / 330 / 924 / 925 糊成一句。

## 和相邻反模式

- [evidence-maxbytes-notblock-sold-as-bundled](evidence-maxbytes-notblock-sold-as-bundled.md) 是证据尺还不是块尺边界（331/922），不是本页钟偏还不是消息延迟边界。
- 块时间必须点名算法是不变量 40，不是本页 Precision 还不是 MessageDelay 边界。
