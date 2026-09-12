# 模式：把 MaxBytes 开销与投递三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[MaxBytes 减去头集合证据才是交易上限 ≠ 已经整块都能装交易](../../tracks/implementation/worked-example-maxbytes-overhead-vs-full.md)。

## 三个名字

1. **MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易：** 看见填了块上限不是交易已经能占满整块。
2. **诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB：** 看见默认能接到 21 MB 不是诚实者已经只会出那一档。
3. **timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行：** 看见填了 TimeoutPropose 不是已经按满块投递算过。

## 为什么要分开叫

官方把扣掉开销之后的交易上限、诚实者可以打到配置上限、超时按满块投递延迟来配写成三件事。把它们叫成一个「看见填了 MaxBytes 就已经整块都能装交易」，会把 -1 / 100 MB、证据体积和 Prepare 执行超时一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 MaxBytes 就已经整块都能装交易」，先数清问的是 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易、诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB，还是 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行，再决定要不要同一次发布。
