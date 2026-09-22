# 反模式：把 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量）说成已经装得下 Prepare 执行 / 已经是 Prepare 执行超时 / 已经离开关键路径

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[timeout 必须按满块投递 not already timeoutpropose-fit ≠ bundled（344）](../../tracks/implementation/worked-example-maxbytes-nottimeoutfit-vs-bundled.md)。

## 卖法

把 timeout 必须按满块投递延迟算 / 最坏投递延迟 / 填了 TimeoutPropose 写成已经填了 TimeoutPropose 就装得下这次 Prepare 执行 interchangeable / 已经 timeoutpropose-fit interchangeable / 已经装得下交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable；把超时在 / 有共识超时 写成已经装得下这次 Prepare 执行 interchangeable / 已经 prepare-exec interchangeable / 已经 Prepare 执行交差 interchangeable；把投递延迟 / 满块投递延迟 写成已经离开关键路径 interchangeable / 已经 critical-path interchangeable / 已经离开关键路径交差 interchangeable，或已经和 344 maxbytesoverhead bundled / maxbytesoverhead-sold-as-full interchangeable / 787 maxbytes-nottimeoutfit interchangeable。

## 为什么错

官方把满块投递延迟、有超时参数、不是已经离开关键路径写成三件独立的实现事。把它们卖成 already timeoutpropose-fit interchangeable / already prepare-exec interchangeable / already critical-path interchangeable，会把 not already timeoutpropose-fit、not already prepare-exec、not already critical-path 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量），必须分开 not already timeoutpropose-fit、not already prepare-exec、not already critical-path 三件事，不要和 344 / 327 / 737 / 738 / 785 / 786 糊成一句。

## 和相邻反模式

- [maxbytes-notfulltx-sold-as-bundled](maxbytes-notfulltx-sold-as-bundled.md) 是完整块上限 ≠ 整块都能装交易（344 item 1），不是本页满块投递 item 3 单句边界。
- [maxbytes-notonly21-sold-as-bundled](maxbytes-notonly21-sold-as-bundled.md) 是诚实验证者 MAY 出满 ≠ 只会出默认 21 MB（344 item 2），不是本页 item 3 单句边界。
- [maxbytesoverhead-sold-as-full](maxbytesoverhead-sold-as-full.md) 是 MaxBytes 开销与投递 bundled 全段，不是本页 item 3 单句边界。
- [preparetimeout-notfit-sold-as-bundled](preparetimeout-notfit-sold-as-bundled.md) 是填了 TimeoutPropose ≠ 装得下（738 / 327 item 2），不是本页满块投递延迟边界。
- [preparetimeout-notcriticalpath-sold-as-bundled](preparetimeout-notcriticalpath-sold-as-bundled.md) 是立刻整块执行 ≠ 离开关键路径（737 / 327 item 1），不是本页投递延迟边界。
