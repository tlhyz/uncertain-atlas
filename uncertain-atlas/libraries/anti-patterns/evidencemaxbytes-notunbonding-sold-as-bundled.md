# 反模式：把 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量）说成已经盖住解绑 / 已经够罚 / 已经窗盖住

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[> 0 not already covers-unbonding ≠ bundled（331）](../../tracks/implementation/worked-example-evidencemaxbytes-notunbonding-vs-bundled.md)。

## 卖法

把 MaxBytes > 0 / 大于 0 / 有正上限 写成已经盖住解绑 interchangeable / 已经 covers-unbonding interchangeable / 已经盖住解绑交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable；把合法 / 过了下限 / 字段合法 写成已经够罚 interchangeable / 已经 enough-to-slash interchangeable；把盖住解绑期 / 证据窗盖住 / 窗盖住 写成已经窗盖住交差 interchangeable / 已经 window-covers interchangeable，或已经和 331 evidencemaxbytes bundled / evidencemaxbytes-sold-as-blockmax interchangeable / 750 evidencemaxbytes-notunbonding interchangeable。

## 为什么错

官方把 > 0 单句、already covers-unbonding、already enough-to-slash、already window-covers 写成三件独立的实现事。把它们卖成 already covers-unbonding interchangeable / already enough-to-slash interchangeable / already window-covers interchangeable，会把 not already covers-unbonding、not already enough-to-slash、not already window-covers 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 > 0 不是已经盖住解绑 not already covers-unbonding / not already enough-to-slash / not already window-covers 正式三事（331 余量），必须分开 not already covers-unbonding、not already enough-to-slash、not already window-covers 三件事，不要和 331 / 33 / 46 / 749 / 751 糊成一句。

## 和相邻反模式

- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是 EvidenceParams.MaxBytes bundled 全段，不是本页盖住解绑 item 2 单句边界。
- [evidencemaxbytes-notunder-sold-as-bundled](evidencemaxbytes-notunder-sold-as-bundled.md) 是落在块上限下面 item 1，不是本页 > 0 与解绑边界。
- [evidencemaxbytes-notblockmax-sold-as-bundled](evidencemaxbytes-notblockmax-sold-as-bundled.md) 是块 MaxBytes（331 item 3），不是本页盖住解绑 item 2 单句边界。
- [evidence-default-sold-as-unbonding](evidence-default-sold-as-unbonding.md) 是默认证据窗已经够罚（46），不是本页 MaxBytes > 0 单句边界。
