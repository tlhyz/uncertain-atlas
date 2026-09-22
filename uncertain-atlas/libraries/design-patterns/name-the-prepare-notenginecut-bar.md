# 模式：把 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**例**：[Req 2 保证回的列表不让块超 not already engine-cuts ≠ bundled（345）](../../tracks/implementation/worked-example-prepare-notenginecut-vs-bundled.md)。

## 三个名字

1. **Req 2 保证回的列表不让块超 不是 already engine-cuts：** 看见 Requirement 2 保证回的列表不让块超字节上限 / 回包不得超过 `max_tx_bytes` / 有这道要求，不是已经是引擎会帮你裁 interchangeable / 已经 engine-cuts interchangeable / 已经引擎裁交差 interchangeable，不是 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable。

2. **回包绿了 不是 already overhead-deducted：** 看见回包绿了 / 回包不超过上限 / 列表体积守住了，不是已经扣过开销 interchangeable / 已经 overhead-deducted interchangeable / 已经扣开销交差 interchangeable，不是 344 maxbytesoverhead interchangeable / maxbytesoverhead-sold-as-full interchangeable。

3. **块不会超 不是 already four-gates-settled：** 看见块不会超 / 回的列表不让块超字节上限 / 块字节上限守住，不是已经四门结算 interchangeable / 已经 four-gates-settled interchangeable / 已经四门交差 interchangeable，不是 788 prepare-notblocksubset interchangeable / 789 prepare-notoversize interchangeable / 33 abci-gates interchangeable。

官方把应用必须守回包上限、回包绿了不是已经扣开销、块不会超不是已经四门结算写成三个名字。把它们叫成一个「看见 Req 2 保证回的列表不让块超字节上限就已经是引擎会帮你裁 interchangeable / 就已经扣过开销 interchangeable / 就已经四门结算 interchangeable」，会把 not already engine-cuts、not already overhead-deducted、not already four-gates-settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量），先数清问的是 Req 2 保证回的列表不让块超 是不是 already engine-cuts / 345 / preparereturn-sold-as-trimmed，是不是回包绿了 是不是 already overhead-deducted，还是块不会超 是不是 already four-gates-settled，再决定要不要同一次发布。345 preparereturn vs pool bundled unbundling 在本页 item 3 完成。
