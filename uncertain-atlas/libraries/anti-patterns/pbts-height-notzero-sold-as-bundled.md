# 反模式：把 写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事（343 余量） 卖成 已经启用 PBTS / 已经填了 Precision 就是 PBTS / 已经交差

**层次**：实现 / PbtsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-pbts-height-notzero-vs-bundled.md](../../tracks/implementation/worked-example-pbts-height-notzero-vs-bundled.md)。

官方把写成 0 不是已经启用 PBTS / H 之前仍用 BFT Time / 启用之后不能关 三条核心句写成三件独立的实现事。把它们卖成已经启用 PBTS / 已经填了 Precision 就是 PBTS / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写成 0 不是已经启用 PBTS 正式三事（343 余量），必须分开 not already enabled、not already Precision is PBTS、not already settled 三件事，不要和 343 / 336 / 330 / 885 / 886 糊成一句。

## 和相邻反模式

- [maxbytes-overhead-notfull-sold-as-bundled](maxbytes-overhead-notfull-sold-as-bundled.md) 是 MaxBytes 扣开销（344/881），不是本页写成 0 边界。
- Precision 已经是 MessageDelay 是不变量 336，不是本页写成 0 边界。
