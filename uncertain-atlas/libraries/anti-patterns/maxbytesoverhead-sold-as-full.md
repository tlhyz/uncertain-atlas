# 反模式：看见 MaxBytes 减去头集合证据才是交易上限就当成已经整块都能装交易 / 看见诚实验证者 MAY 出满 MaxBytes 就当成已经只会出默认 21 MB / 看见 timeout 必须按满块投递延迟算就当成已经填了 TimeoutPropose 就装得下这次 Prepare 执行

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[MaxBytes 减去头集合证据才是交易上限 ≠ 已经整块都能装交易](../../tracks/implementation/worked-example-maxbytes-overhead-vs-full.md)。

## 塌法

1. 看见 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 看见完整块上限，就当成已经整块都能装交易，或当成已经是证据 MaxBytes。
2. 看见诚实验证者 MAY 出满 MaxBytes / 看见能广播到配置上限，就当成已经只会出默认 21 MB，或当成已经没有上限。
3. 看见 timeout 必须按满块投递延迟算 / 看见最坏投递延迟，就当成已经填了 TimeoutPropose 就装得下这次 Prepare 执行，或当成已经是立刻整块执行离开关键路径。

## 为什么会出事

官方写：完整块上限蕴涵交易上限还要扣掉头、集合和证据。诚实验证者可以造出并广播达到配置 MaxBytes 的块。超时应当按把一份满 MaxBytes 的块投递给所有验证者的最坏延迟来配。

## 和相邻反模式

- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验不是已经没有上限，不是本页这种扣掉开销才是交易上限。
- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是证据 MaxBytes 不是已经是块 MaxBytes，不是本页这种交易上限还要扣开销。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行不是已经离开关键路径，不是本页这种满块投递延迟。
