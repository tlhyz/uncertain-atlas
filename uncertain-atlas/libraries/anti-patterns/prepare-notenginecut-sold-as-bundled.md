# 反模式：把 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量）说成已经是引擎会帮你裁 / 已经扣过开销 / 已经四门结算

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Req 2 保证回的列表不让块超 not already engine-cuts ≠ bundled（345）](../../tracks/implementation/worked-example-prepare-notenginecut-vs-bundled.md)。

## 卖法

把 Requirement 2 保证回的列表不让块超字节上限 / 回包不得超过 `max_tx_bytes` / 有这道要求 写成已经是引擎会帮你裁 interchangeable / 已经 engine-cuts interchangeable / 已经引擎裁交差 interchangeable / 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable；把回包绿了 / 回包不超过上限 写成已经扣过开销 interchangeable / 已经 overhead-deducted interchangeable / 已经扣开销交差 interchangeable；把块不会超 / 回的列表不让块超字节上限 写成已经四门结算 interchangeable / 已经 four-gates-settled interchangeable / 已经四门交差 interchangeable，或已经和 345 preparereturn bundled / preparereturn-sold-as-trimmed interchangeable / 790 prepare-notenginecut interchangeable。

## 为什么错

官方把应用必须守回包上限、回包绿了不是已经扣开销、块不会超不是已经四门结算写成三件独立的实现事。把它们卖成 already engine-cuts interchangeable / already overhead-deducted interchangeable / already four-gates-settled interchangeable，会把 not already engine-cuts、not already overhead-deducted、not already four-gates-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量），必须分开 not already engine-cuts、not already overhead-deducted、not already four-gates-settled 三件事，不要和 345 / 344 / 33 / 788 / 789 糊成一句。

## 和相邻反模式

- [preparereturn-sold-as-trimmed](preparereturn-sold-as-trimmed.md) 是 PrepareProposal 回包上限 bundled 全段，不是本页 Req 2 引擎裁 item 3 单句边界。
- [prepare-notoversize-sold-as-bundled](prepare-notoversize-sold-as-bundled.md) 是聚合体积可以超过 max_tx_bytes not already can-return-oversize（345 item 2），不是本页 not already engine-cuts 边界。
- [maxbytesoverhead-sold-as-full](maxbytesoverhead-sold-as-full.md) 是 MaxBytes 减去头集合证据才是交易上限（344），不是本页回包绿了 ≠ 已经扣开销 边界。
