# 反模式：把填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量）说成已经落在块上限下面 / 已经扣掉开销 / 已经装得下预算

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了证据 MaxBytes not already under-block ≠ bundled（331）](../../tracks/implementation/worked-example-evidencemaxbytes-notunder-vs-bundled.md)。

## 卖法

把填了证据 MaxBytes / 填了这个字段 / EvidenceParams.MaxBytes 有值 写成已经落在块上限下面 interchangeable / 已经 under-block interchangeable / 已经落在下面交差 interchangeable / 331 evidencemaxbytes bundled interchangeable / 33 four gates interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable；把一块里证据有上限 / 有上限 / 证据体积有顶 写成已经扣掉开销 interchangeable / 已经 overhead-deducted interchangeable；把取值有顶 / 不得超过一块减去开销 / 约 BlockParams.MaxBytes 那条 写成已经装得下预算 interchangeable / 已经 fits-budget interchangeable，或已经和 331 evidencemaxbytes bundled / evidencemaxbytes-sold-as-blockmax interchangeable / 749 evidencemaxbytes-notunder interchangeable。

## 为什么错

官方把填了证据 MaxBytes 单句、already under-block、already overhead-deducted、already fits-budget 写成三件独立的实现事。把它们卖成 already under-block interchangeable / already overhead-deducted interchangeable / already fits-budget interchangeable，会把 not already under-block、not already overhead-deducted、not already fits-budget 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了证据 MaxBytes 不是已经落在块上限下面 not already under-block / not already overhead-deducted / not already fits-budget 正式三事（331 余量），必须分开 not already under-block、not already overhead-deducted、not already fits-budget 三件事，不要和 331 / 33 / 63 / 299 / 750 / 751 糊成一句。

## 和相邻反模式

- [evidencemaxbytes-sold-as-blockmax](evidencemaxbytes-sold-as-blockmax.md) 是 EvidenceParams.MaxBytes bundled 全段，不是本页落在块上限下面 item 1 单句边界。
- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是先装证据 ≠ 已经装满交易（299），不是本页扣开销边界。
- [veheight-notlegal-sold-as-bundled](veheight-notlegal-sold-as-bundled.md) 是 h < H 带了扩展不是已经合法（330 item 3），不是本页证据体积尺边界。
