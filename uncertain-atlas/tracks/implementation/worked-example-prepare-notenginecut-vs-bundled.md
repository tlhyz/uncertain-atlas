# 例：看见 Requirement 2 保证回的列表不让块超字节上限 / 看见回包不得超过 max_tx_bytes / 看见块不会超 is not already already engine-cuts interchangeable / already overhead-deducted interchangeable / already four-gates-settled interchangeable

**层次**：实现 / Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量）/ not 790 prepare-notenginecut interchangeable / not 345 preparereturn bundled interchangeable」，不是 PrepareProposal 回包上限 bundled（345），也不是整池可见不是已经只能看见装得进一块的子集（788 item 1 余量）或聚合体积可以超过 max_tx_bytes 不是已经能回超限列表（789 item 2 余量）。不要另写怎样裁回包。

## 官方三件事

规范把 Requirements 里 Requirement 2 保证应用回的交易列表体积永远不会让这块超过字节上限 和「已经是有这道要求就已经是引擎会帮你裁 interchangeable / 已经是回包绿了就已经扣过开销 interchangeable / 已经是块不会超就已经四门结算 interchangeable / 已经是 preparereturn bundled interchangeable」分开写成三件独立的实现事，不是「看见 Req 2 保证回的列表不让块超字节上限就已经是引擎会帮你裁 interchangeable / 就已经扣过开销 interchangeable / 就已经四门结算 interchangeable」一件事：

1. **看见 Requirement 2 保证回的列表不让块超字节上限 / 看见回包不得超过 `max_tx_bytes` / 看见有这道要求 is not already 已经是引擎会帮你裁 interchangeable / 已经 engine-cuts interchangeable / 已经引擎裁交差 interchangeable / 345 preparereturn bundled interchangeable / 344 maxbytesoverhead interchangeable / preparereturn-sold-as-trimmed interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 790 prepare-notenginecut interchangeable / 345 preparereturn item 3 interchangeable，也不是已经 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事 bundled（345 item 3 余量） interchangeable / 345 preparereturn item 3 interchangeable，也不是已经整池可见不是已经只能看见一块子集（788） interchangeable / 789 prepare-notoversize interchangeable / 337 maxbytescap interchangeable，也不是已经 MaxBytes 减去头集合证据才是交易上限（344） interchangeable。**  
   官方写：因此 Requirement 2 保证应用回的交易列表体积**永远不会**让这块超过字节上限。看见有这道要求，不是引擎已经替你裁。看见 Req 2 保证回的列表不让块超字节上限，不是已经 engine-cuts interchangeable——345 钉 bundled 三事，本页从 item 3 侧钉 not already engine-cuts 单句。看见回包不得超过 `max_tx_bytes`，不是已经 PrepareProposal 回包上限 bundled（345） interchangeable——345 钉 bundled，本页钉 item 3 第一件事。看见有这道要求，不是已经 MaxBytes 减去头集合证据才是交易上限（344） interchangeable——344 另钉。345 preparereturn vs pool bundled unbundling 在本页 item 3 完成。

2. **看见回包绿了 / 看见回包不超过上限 / 看见列表体积守住了 is not already 已经扣过开销 interchangeable / 已经 overhead-deducted interchangeable / 已经扣开销交差 interchangeable / 345 preparereturn bundled interchangeable / 344 maxbytesoverhead interchangeable / maxbytesoverhead-sold-as-full interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 790 prepare-notenginecut interchangeable / 345 preparereturn item 1 整池可见 interchangeable / 345 preparereturn item 2 超限列表 interchangeable，也不是已经 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事 bundled（345 item 3 余量） interchangeable / 345 preparereturn item 3 interchangeable，也不是已经是引擎会帮你裁（本页第一件事） interchangeable。**  
   官方写：看见回包绿了，不是已经扣过开销。看见回包不超过上限，不是已经 overhead-deducted interchangeable——本页钉 not already overhead-deducted 单句。看见列表体积守住了，不是已经是引擎会帮你裁（本页第一件事） interchangeable——三件事分开钉。345 preparereturn vs pool bundled unbundling 在本页 item 3 完成。

3. **看见块不会超 / 看见回的列表不让块超字节上限 / 看见块字节上限守住 is not already 已经四门结算 interchangeable / 已经 four-gates-settled interchangeable / 已经四门交差 interchangeable / 345 preparereturn bundled interchangeable / 33 abci-gates interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 790 prepare-notenginecut interchangeable / 345 preparereturn item 1 / 345 preparereturn item 2，也不是已经 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事 bundled（345 item 3 余量） interchangeable / 345 preparereturn item 3 interchangeable，也不是已经是引擎会帮你裁（本页第一件事） interchangeable / 已经扣过开销（本页第二件事） interchangeable。**  
   官方写：看见块不会超，不是已经是 344 那种扣掉头 / 集合 / 证据才是交易上限，也不是已经四门结算。看见回的列表不让块超字节上限，不是已经 four-gates-settled interchangeable——本页钉 not already four-gates-settled 单句。看见块字节上限守住，不是已经扣过开销（本页第二件事） interchangeable——三件事分开钉。345 preparereturn vs pool bundled unbundling 在本页 item 3 完成。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。PrepareProposal 回包上限 bundled（345）、整池可见不是已经只能看见装得进一块的子集（345 item 1 余量 / 788）、聚合体积可以超过 max_tx_bytes 不是已经能回超限列表（345 item 2 余量 / 789）、整池都给 Prepare 就已经没有上限（299）、-1 就按 100 MB 验已经没有上限（337）、MaxBytes 减去头集合证据才是交易上限（344）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Req 2 保证回的列表不让块超 not already engine-cuts ≠ 345 / 344 interchangeable：** 官方把应用必须守回包上限和引擎替你裁分开。
- **回包绿了 not already overhead-deducted ≠ 已经扣过开销 interchangeable：** 官方把回包守住上限和已经扣掉头集合证据开销分开。
- **块不会超 not already four-gates-settled ≠ 已经四门结算 interchangeable：** 官方把块字节上限守住和四门已经结算分开；345 preparereturn vs pool bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Req 2 保证回的列表不让块超 | 不是 already engine-cuts | 不是 MaxBytes 减去头集合证据才是交易上限 alone（344） |
| 回包绿了 | 不是 already overhead-deducted | 不是聚合体积可以超过 max_tx_bytes alone（789） |
| 块不会超 | 不是 already four-gates-settled | 不是四门已经结算 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 余量），必须分开 Req 2 保证回的列表不让块超 是不是 already engine-cuts interchangeable / 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable、回包绿了 是不是 already overhead-deducted interchangeable、块不会超 是不是 already four-gates-settled interchangeable。可以跳过「看见 Req 2 保证回的列表不让块超字节上限就已经是引擎会帮你裁 interchangeable / 就已经扣过开销 interchangeable / 就已经四门结算 interchangeable」。不要另写怎样裁回包。345 preparereturn vs pool bundled unbundling 在本页 item 3 完成（788 + 789 + 790）。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- PrepareProposal 回包上限 bundled。那是不变量 345。
- 整池可见不是已经只能看见装得进一块的子集。那是不变量 345 item 1 余量 / 788。
- 聚合体积可以超过 max_tx_bytes 不是已经能回超限列表。那是不变量 345 item 2 余量 / 789。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344。
- 四门已经结算。那是不变量 33。
