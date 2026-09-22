# 反模式：把诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量）说成已经只会出默认 21 MB / 已经没有上限 / 已经必须打满

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[诚实验证者 MAY 出满 MaxBytes not already default-21 ≠ bundled（344）](../../tracks/implementation/worked-example-maxbytes-notonly21-vs-bundled.md)。

## 卖法

把诚实验证者 MAY 出满 MaxBytes / 能广播到配置上限 / 默认能接到 21 MB 写成已经只会出默认 21 MB interchangeable / 已经 default-21 interchangeable / 已经只会出那一档交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable；把能打到配置上限 / 配置上限在 写成已经没有上限 interchangeable / 已经 unlimited interchangeable / 已经无上限交差 interchangeable；把写了 MAY / 可以出满 写成已经必须打满 interchangeable / 已经 may-is-must interchangeable / 已经打满交差 interchangeable，或已经和 344 maxbytesoverhead bundled / maxbytesoverhead-sold-as-full interchangeable / 786 maxbytes-notonly21 interchangeable。

## 为什么错

官方把配置上限、默认 21 MB 那一档、MAY 不是必须打满写成三件独立的实现事。把它们卖成 already default-21 interchangeable / already unlimited interchangeable / already may-is-must interchangeable，会把 not already default-21、not already unlimited、not already may-is-must 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量），必须分开 not already default-21、not already unlimited、not already may-is-must 三件事，不要和 344 / 337 / 766 / 785 / 787 糊成一句。

## 和相邻反模式

- [maxbytes-notfulltx-sold-as-bundled](maxbytes-notfulltx-sold-as-bundled.md) 是完整块上限 ≠ 整块都能装交易（344 item 1），不是本页 MAY 出满 item 2 单句边界。
- [maxbytesoverhead-sold-as-full](maxbytesoverhead-sold-as-full.md) 是 MaxBytes 开销与投递 bundled 全段，不是本页 item 2 单句边界。
- [maxbytes-notdefault21-sold-as-bundled](maxbytes-notdefault21-sold-as-bundled.md) 是必须 -1 或不超过 100 MB ≠ 默认 21 MB（766 / 337 item 3），不是本页诚实 MAY 出满边界。
- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验不是已经没有上限（337），不是本页能打到配置上限 ≠ 无上限 边界。
