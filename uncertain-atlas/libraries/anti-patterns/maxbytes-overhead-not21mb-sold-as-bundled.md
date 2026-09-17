# 反模式：把 诚实验证者 MAY 出满 MaxBytes not already only default 21 MB / not already no limit / not already settled 正式三事（344 余量） 卖成 已经只会出默认 21 MB / 已经没有上限 / 已经交差

**层次**：实现 / BlockParams.MaxBytes 开销与投递。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-overhead-not21mb-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-overhead-not21mb-vs-bundled.md)。

官方把 MaxBytes 减去头集合证据才是交易上限 / 诚实验证者 MAY 出满 MaxBytes / timeout 必须按满块投递延迟算 三条核心句写成三件独立的实现事。把它们卖成已经只会出默认 21 MB / 已经没有上限 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看诚实验证者 MAY 出满 MaxBytes 正式三事（344 余量），必须分开 not already only default 21 MB、not already no limit、not already settled 三件事，不要和 344 / 337 / 33 / 881 / 883 糊成一句。

## 和相邻反模式

- [maxbytes-overhead-notfull-sold-as-bundled](maxbytes-overhead-notfull-sold-as-bundled.md) 是扣开销单句边界（881 item 1），不是本页 MAY 出满边界。
- -1 就按 100 MB 验已经没有上限是不变量 337，不是本页 MAY 出满边界。
