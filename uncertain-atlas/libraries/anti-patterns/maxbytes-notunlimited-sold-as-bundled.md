# 反模式：把 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量）说成已经没有上限 / 已经没有引擎帽 / 已经可以随便回

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写成 -1 not already unlimited ≠ bundled（337）](../../tracks/implementation/worked-example-maxbytes-notunlimited-vs-bundled.md)。

## 卖法

把 MaxBytes 写成 -1 / 写成 -1 / -1 那一档 写成已经没有上限 interchangeable / 已经 unlimited interchangeable / 已经无上限交差 interchangeable / 337 maxbytescap bundled interchangeable / 299 evidence-reap interchangeable / maxbytescap-sold-as-unlimited interchangeable；把引擎按 100 MB 验 / 实际要验的值是 100 MB / 100 MB 那把尺 写成已经没有引擎帽 interchangeable / 已经 no-cap interchangeable；把能打满 / 应用已经可以随便回的联想 / 整池都给了 Prepare 写成已经可以随便回 interchangeable / 已经 free-return interchangeable，或已经和 337 maxbytescap bundled / maxbytescap-sold-as-unlimited interchangeable / 764 maxbytes-notunlimited interchangeable。

## 为什么错

官方把写成 -1 单句、already unlimited、already no-cap、already free-return 写成三件独立的实现事。把它们卖成 already unlimited interchangeable / already no-cap interchangeable / already free-return interchangeable，会把 not already unlimited、not already no-cap、not already free-return 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量），必须分开 not already unlimited、not already no-cap、not already free-return 三件事，不要和 337 / 299 / 63 / 331 / 765 / 766 糊成一句。

## 和相邻反模式

- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 MaxBytes cap bundled 全段，不是本页写成 -1 item 1 单句边界。
- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是整池都给 Prepare ≠ 已经没有上限（299），不是本页写成 -1 ≠ 已经没有上限 边界。
- [maxbytes-sold-as-sla](maxbytes-sold-as-sla.md) 是仓库默认 MaxBytes ≠ 已经是活性 SLA（63），不是本页按 100 MB 验边界。
- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是证据 MaxBytes ≠ 已经是块 MaxBytes（331），不是本页能打满边界。
