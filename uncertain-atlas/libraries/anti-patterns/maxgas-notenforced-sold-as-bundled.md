# 反模式：把 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量）说成已经在执行 / 已经和 MaxBytes -1 同一句 / 已经有费用市场

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[字段在 not already enforcing ≠ bundled（315）](../../tracks/implementation/worked-example-maxgas-notenforced-vs-bundled.md)。

## 卖法

把 MaxGas / 字段在 / 回包里有气字段 写成已经在执行 interchangeable / 已经 enforcing interchangeable / 已经在卡 interchangeable / 315 maxgas bundled interchangeable / 299 maxbytes interchangeable / maxgas-sold-as-enforced interchangeable；把写成 -1 / 默认 -1 / MaxGas = -1 写成已经和 MaxBytes 写成 -1 同一句 interchangeable / 已经 MaxBytes synonym interchangeable；把学了以太坊 / 官方说学了类似抽象 写成已经有费用市场 interchangeable / 已经 fee market interchangeable，或已经和 315 maxgas bundled / maxgas-sold-as-enforced interchangeable / 704 maxgas-notenforced interchangeable。

## 为什么错

官方把字段在单句、already enforcing、already MaxBytes synonym、already fee market 写成三件独立的实现事。把它们卖成 already enforcing interchangeable / already MaxBytes synonym interchangeable / already fee market interchangeable，会把 not already enforcing、not already MaxBytes synonym、not already fee market 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxGas 不是已经在执行 not already enforcing / not already MaxBytes synonym / not already fee market 正式三事（315 余量），必须分开 not already enforcing、not already MaxBytes synonym、not already fee market 三件事，不要和 315 / 299 / 705 / 706 / 33 糊成一句。

## 和相邻反模式

- [maxgas-sold-as-enforced](maxgas-sold-as-enforced.md) 是 MaxGas vs enforced bundled 全段，不是本页字段在 item 1 单句边界。
- [querystate-notsnapshot-sold-as-bundled](querystate-notsnapshot-sold-as-bundled.md) 是启动对齐 ≠ 快照重放（314），不是本页 MaxGas 边界。
- [cap-sold-as-gas](cap-sold-as-gas.md) 是另一气上限卖法，不是本页默认 -1 与 MaxBytes 边界。
