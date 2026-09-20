# 反模式：把证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量）说成已经是块 MaxBytes / 已经是 -1 无上限 / 已经是活性 SLA

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[证据 MaxBytes not already block-maxbytes ≠ bundled（331）](../../tracks/implementation/worked-example-evidencemaxbytes-notblockmax-vs-bundled.md)。

## 卖法

把证据 MaxBytes / 证据这边有 MaxBytes / 证据体积上限 写成已经是块 MaxBytes interchangeable / 已经 block-maxbytes interchangeable / 已经块上限交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable；把填了数 / 写成数 / 不是空白 写成已经是 -1 无上限 interchangeable / 已经 minus-one interchangeable；把有上限 / 对照第一轮超时 / 活性相关上限 写成已经是活性 SLA interchangeable / 已经 propose-sla interchangeable，或已经和 331 evidencemaxbytes bundled / evidencemaxbytes-sold-as-blockmax interchangeable / 751 evidencemaxbytes-notblockmax interchangeable。

## 为什么错

官方把证据 MaxBytes 单句、already block-maxbytes、already minus-one、already propose-sla 写成三件独立的实现事。把它们卖成 already block-maxbytes interchangeable / already minus-one interchangeable / already propose-sla interchangeable，会把 not already block-maxbytes、not already minus-one、not already propose-sla 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看证据 MaxBytes 不是已经是块 MaxBytes not already block-maxbytes / not already minus-one / not already propose-sla 正式三事（331 余量），必须分开 not already block-maxbytes、not already minus-one、not already propose-sla 三件事，不要和 331 / 33 / 63 / 299 / 749 / 750 糊成一句。

## 和相邻反模式

- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是 EvidenceParams.MaxBytes bundled 全段，不是本页块 MaxBytes item 3 单句边界。
- [evidencemaxbytes-notunder-sold-as-bundled](evidencemaxbytes-notunder-sold-as-bundled.md) 是落在块上限下面 item 1，不是本页两把尺边界。
- [evidencemaxbytes-notunbonding-sold-as-bundled](evidencemaxbytes-notunbonding-sold-as-bundled.md) 是盖住解绑 item 2，不是本页两把尺边界。
- [maxbytes-sold-as-sla](maxbytes-sold-as-sla.md) 是仓库默认块 MaxBytes 已经是活性 SLA（63），不是本页证据体积尺边界。
