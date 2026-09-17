# 例：看见 Req 2 保证回的列表不让块超字节上限 is not already engine trims interchangeable / not already 344 overhead interchangeable / not already settled interchangeable

**层次**：实现 / Req 2 保证回的列表不让块超字节上限 not already engine trims / not already 344 overhead / not already settled 正式三事（345 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Req 2 保证回的列表不让块超字节上限 not already engine trims / not already 344 overhead / not already settled 正式三事（345 余量）/ not 880 prepare-return-notengine interchangeable / not 345 prepare-return-vs-pool bundled interchangeable」，不是 Prepare 回包上限 bundled（345），也不是 MaxBytes 减去头集合证据才是交易上限（344），也不是四门已经结算（33）。不要另写怎样裁回包。

## 官方三件事

1. **看见 Requirement 2 保证回的列表不让块超字节上限 / 看见回包不得超过 `max_tx_bytes` 这份保证 is not already 已经是引擎会帮你裁 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 880 prepare-return-notengine interchangeable / 878 prepare-return-notsubset interchangeable / 345 prepare-return item 1 整池可见 interchangeable，也不是已经 Req 2 保证回的列表不让块超字节上限 not already engine trims / not already 344 overhead / not already settled 正式三事 bundled（345 item 3 余量） interchangeable / 345 prepare-return item 3 interchangeable。**  
   官方写：因此 Requirement 2 保证应用回的交易列表体积永远不会让这块超过字节上限。看见有这道要求，不是引擎已经替你裁 interchangeable——本页从 345 item 3 侧钉 not already engine trims 单句。345 prepare-return vs pool bundled unbundling 在本页 item 3 完成。

2. **看见回包绿了 / 看见块不会超 / 这份保证 is not already 已经是 MaxBytes 扣掉头集合证据之后的交易上限 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 880 prepare-return-notengine interchangeable / 345 prepare-return item 2 聚合超限 interchangeable / 879 prepare-return-notover interchangeable，也不是已经 MaxBytes 减去头集合证据才是交易上限 interchangeable / 344 overhead interchangeable。**  
   官方把回包绿了和已经扣过开销分开——345 bundled 第三件事常与 344 混成「看见块不会超就已经是引擎会裁或已经扣过头集合证据 interchangeable」，本页钉 not already 344 overhead 单句。

3. **看见块不会超 / 看见写了回包上限 / 这份保证 is not already 已经交差 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 880 prepare-return-notengine interchangeable / 878 prepare-return-notsubset interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把写了回包上限和已经交差分开。看见块不会超，不是已经交差 interchangeable。345 prepare-return vs pool bundled unbundling 在本页 item 3 完成。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Req 2 保证回的列表不让块超字节上限 not already engine trims ≠ 已经是引擎会帮你裁 interchangeable：** 官方把应用必须守回包上限和引擎替你裁分开。
- **看见回包绿了 not already 344 overhead ≠ 已经扣过头集合证据 interchangeable：** 官方把回包绿了和已经扣过开销分开。
- **看见写了回包上限 not already settled ≠ 已经交差 interchangeable：** 官方把写了回包上限和已经交差分开；345 prepare-return vs pool bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Req 2 保证回的列表不让块超字节上限 | 不是已经是引擎会帮你裁 | 不是 MaxBytes 减去头集合证据才是交易上限（344） |
| 看见回包绿了 | 不是已经扣过头集合证据 | 不是四门已经结算（33） |
| 看见写了回包上限 | 不是已经交差 | 不是整池可见就已经没有上限（878） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 2 保证回的列表不让块超字节上限 not already engine trims / not already 344 overhead / not already settled 正式三事（345 余量），必须分开是不是已经是引擎会帮你裁、是不是已经扣过头集合证据、是不是已经交差。可以跳过「看见写了回包上限就已经是引擎会裁」。不要另写怎样裁回包。345 prepare-return vs pool bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- Prepare 回包上限 bundled。那是不变量 345。
- 整池可见。那是不变量 345 item 1 余量 / 878。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344。
- 四门已经结算。那是不变量 33。
