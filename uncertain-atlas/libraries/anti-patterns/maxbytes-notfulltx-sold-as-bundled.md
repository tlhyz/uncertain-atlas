# 反模式：把 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量）说成已经整块都能装交易 / 已经是证据 MaxBytes / 已经算出开销字节

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[MaxBytes 减去头集合证据才是交易上限 not already full-tx ≠ bundled（344）](../../tracks/implementation/worked-example-maxbytes-notfulltx-vs-bundled.md)。

## 卖法

把 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 完整块上限 / 填了块上限 写成已经整块都能装交易 interchangeable / 已经 full-tx interchangeable / 已经整块装交易交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable；把能装交易 / 交易上限还在 写成已经是证据 MaxBytes interchangeable / 已经 evidence-max interchangeable / 已经证据那把尺交差 interchangeable；把扣了开销 / 减去头集合证据 写成已经算出那几个字节 interchangeable / 已经 overhead-known interchangeable / 已经开销字节交差 interchangeable，或已经和 344 maxbytesoverhead bundled / maxbytesoverhead-sold-as-full interchangeable / 785 maxbytes-notfulltx interchangeable。

## 为什么错

官方把完整块上限、交易上限还要扣开销、开销字节尚未算出写成三件独立的实现事。把它们卖成 already full-tx interchangeable / already evidence-max interchangeable / already overhead-known interchangeable，会把 not already full-tx、not already evidence-max、not already overhead-known 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量），必须分开 not already full-tx、not already evidence-max、not already overhead-known 三件事，不要和 344 / 331 / 337 / 786 / 787 糊成一句。

## 和相邻反模式

- [maxbytes-notonly21-sold-as-bundled](maxbytes-notonly21-sold-as-bundled.md) 是诚实验证者 MAY 出满 ≠ 只会出默认 21 MB（344 item 2），不是本页完整块上限 item 1 单句边界。
- [maxbytes-nottimeoutfit-sold-as-bundled](maxbytes-nottimeoutfit-sold-as-bundled.md) 是 timeout 必须按满块投递 ≠ 装得下 Prepare（344 item 3），不是本页完整块上限 item 1 单句边界。
- [maxbytesoverhead-sold-as-full](maxbytesoverhead-sold-as-full.md) 是 MaxBytes 开销与投递 bundled 全段，不是本页完整块上限 item 1 单句边界。
- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是证据 MaxBytes 不是已经是块 MaxBytes（331），不是本页能装交易 ≠ 证据那把尺 边界。
- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验不是已经没有上限（337），不是本页扣开销边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行不是已经离开关键路径（327），不是本页完整块上限边界。
