# 反模式：把 填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事（331 余量） 卖成 已经落在块上限下面 / 已经扣掉开销 / 已经交差

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-evidence-maxbytes-notunder-vs-bundled.md](../../tracks/implementation/worked-example-evidence-maxbytes-notunder-vs-bundled.md)。

官方把填了证据 MaxBytes / > 0 / 证据 MaxBytes 三条核心句写成三件独立的实现事。把它们卖成已经落在块上限下面 / 已经扣掉开销 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了证据 MaxBytes 正式三事（331 余量），必须分开 not already under block cap、not already overhead-deducted、not already settled 三件事，不要和 331 / 299 / 337 / 921 / 922 糊成一句。

## 和相邻反模式

- [maxbytes-cap-notunlim-sold-as-bundled](maxbytes-cap-notunlim-sold-as-bundled.md) 是块 MaxBytes -1 仍按 100 MB 验边界（337/917），不是本页证据体积应当落在块上限下面边界。
- 先装证据已经装满交易是不变量 299，不是本页填了证据字段仍未落在块上限下面边界。
