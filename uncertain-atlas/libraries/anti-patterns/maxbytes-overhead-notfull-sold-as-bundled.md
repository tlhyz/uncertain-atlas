# 反模式：把 MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事（344 余量） 卖成 已经整块都能装交易 / 已经是证据 MaxBytes / 已经交差

**层次**：实现 / BlockParams.MaxBytes 开销与投递。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-overhead-notfull-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-overhead-notfull-vs-bundled.md)。

官方把 MaxBytes 减去头集合证据才是交易上限 / 诚实验证者 MAY 出满 MaxBytes / timeout 必须按满块投递延迟算 三条核心句写成三件独立的实现事。把它们卖成已经整块都能装交易 / 已经是证据 MaxBytes / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 减去头集合证据才是交易上限 正式三事（344 余量），必须分开 not already whole block holds txs、not already evidence MaxBytes、not already settled 三件事，不要和 344 / 331 / 337 / 882 / 883 糊成一句。

## 和相邻反模式

- [prepare-return-notengine-sold-as-bundled](prepare-return-notengine-sold-as-bundled.md) 是 Req 2 回包保证（345/880），不是本页扣开销边界。
- 证据 MaxBytes 已经是块 MaxBytes 是不变量 331，不是本页扣开销边界。
