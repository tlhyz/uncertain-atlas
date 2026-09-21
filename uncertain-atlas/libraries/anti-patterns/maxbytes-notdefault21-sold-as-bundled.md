# 反模式：把必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量）说成已经是默认 21 MB / 已经评估过带宽 / 已经下调

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[合法范围 not already default-21 ≠ bundled（337）](../../tracks/implementation/worked-example-maxbytes-notdefault21-vs-bundled.md)。

## 卖法

把必须 MaxBytes == -1 或 0 < MaxBytes <= 100 MB / 合法取值范围 / 合法范围那一档 写成已经是默认 21 MB interchangeable / 已经 default-21 interchangeable / 已经默认那档交差 interchangeable / 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable / maxbytescap-sold-as-unlimited interchangeable；把默认能接到 21 MB / 默认值把最大 21 MB 当成合法 / 默认 21 MB 写成已经评估过带宽 interchangeable / 已经 bandwidth-assessed interchangeable；把建议下调 / 强烈建议把默认往下调 / 建议调小 写成已经下调 interchangeable / 已经 tuned-down interchangeable，或已经和 337 maxbytescap bundled / maxbytescap-sold-as-unlimited interchangeable / 766 maxbytes-notdefault21 interchangeable。

## 为什么错

官方把合法范围单句、already default-21、already bandwidth-assessed、already tuned-down 写成三件独立的实现事。把它们卖成 already default-21 interchangeable / already bandwidth-assessed interchangeable / already tuned-down interchangeable，会把 not already default-21、not already bandwidth-assessed、not already tuned-down 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量），必须分开 not already default-21、not already bandwidth-assessed、not already tuned-down 三件事，不要和 337 / 299 / 63 / 331 / 764 / 765 糊成一句。

## 和相邻反模式

- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 MaxBytes cap bundled 全段，不是本页合法范围 item 3 单句边界。
- [maxbytes-notunlimited-sold-as-bundled](maxbytes-notunlimited-sold-as-bundled.md) 是写成 -1 ≠ 已经没有上限（337 item 1），不是本页合法范围 ≠ 已经是默认 21 MB 边界。
- [maxbytes-notengineoff-sold-as-bundled](maxbytes-notengineoff-sold-as-bundled.md) 是应用自己卡体积 ≠ 已经引擎不管了（337 item 2），不是本页合法范围 item 3 单句边界。
- [maxbytes-sold-as-sla](maxbytes-sold-as-sla.md) 是仓库默认 MaxBytes ≠ 已经是活性 SLA（63），不是本页默认能接到 ≠ 已经评估过带宽 边界。
