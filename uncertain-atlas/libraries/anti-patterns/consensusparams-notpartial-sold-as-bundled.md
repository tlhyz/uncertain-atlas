# 反模式：把只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量）说成已经只改这一项 / 已经保持原值 / 已经是按字段合并

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[只填一项 not already only-that ≠ bundled（319）](../../tracks/implementation/worked-example-consensusparams-notpartial-vs-bundled.md)。

## 卖法

把只填一项 / Block 只填了 MaxBytes / 只改了其中一个字段 写成已经只改这一项 interchangeable / 已经 only-that interchangeable / 已经只改这一项交差 interchangeable / 319 consensusparams bundled interchangeable / 33 four gates interchangeable / consensusparams-sold-as-updated interchangeable；把没写字段 / 没写的 Block 字段 / 其余字段空着 写成已经保持原值 interchangeable / 已经 rest-unchanged interchangeable；把能整份套上 / 不空字段会套上 / 空的 ConsensusParams 会被忽略 写成已经是按字段合并 interchangeable / 已经 field-merge interchangeable，或已经和 319 consensusparams bundled / consensusparams-sold-as-updated interchangeable / 718 consensusparams-notpartial interchangeable。

## 为什么错

官方把只填一项单句、already only-that、already rest-unchanged、already field-merge 写成三件独立的实现事。把它们卖成 already only-that interchangeable / already rest-unchanged interchangeable / already field-merge interchangeable，会把 not already only-that、not already rest-unchanged、not already field-merge 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只改一个字段不是已经只改这一项 not already only-that / not already rest-unchanged / not already field-merge 正式三事（319 余量），必须分开 not already only-that、not already rest-unchanged、not already field-merge 三件事，不要和 319 / 33 / 716 / 717 / 315 / 299 / 35 糊成一句。

## 和相邻反模式

- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是 ConsensusParams vs update bundled 全段，不是本页只改字段 item 3 单句边界。
- [consensusparams-notempty-sold-as-bundled](consensusparams-notempty-sold-as-bundled.md) 是 InitChain 空参数 item 1，不是本页 partial 边界。
- [consensusparams-notclear-sold-as-bundled](consensusparams-notclear-sold-as-bundled.md) 是 Finalize 没回 item 2，不是本页 partial 边界。
