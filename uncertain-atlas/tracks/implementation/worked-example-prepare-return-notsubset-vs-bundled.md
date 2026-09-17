# 例：看见整池可见 is not already only subset that fits interchangeable / not already no limit interchangeable / not already settled interchangeable

**层次**：实现 / 整池可见 not already only subset that fits / not already no limit / not already settled 正式三事（345 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「整池可见 not already only subset that fits / not already no limit / not already settled 正式三事（345 余量）/ not 878 prepare-return-notsubset interchangeable / not 345 prepare-return-vs-pool bundled interchangeable」，不是 Prepare 回包上限 bundled（345），也不是整池都给 Prepare 就已经没有上限（299），也不是 -1 就按 100 MB 验已经没有上限（337）。不要另写怎样裁回包。

## 官方三件事

1. **看见整池可见 / 看见 MaxBytes 写成 -1 把池子都交来 这份可见 is not already 已经只能看见装得进一块的子集 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 878 prepare-return-notsubset interchangeable / 879 prepare-return-notover interchangeable / 345 prepare-return item 2 聚合超限 interchangeable，也不是已经整池可见 not already only subset that fits / not already no limit / not already settled 正式三事 bundled（345 item 1 余量） interchangeable / 345 prepare-return item 1 interchangeable。**  
   官方写：忙链可能想看见内存池里全部交易，而不是只看见装得进一块的那一子集。应用可以把 `ConsensusParams.Block.MaxBytes` 写成 -1，让引擎按最大可能的 `MaxBytes`（100 MB）验，并把池子里所有交易交给 `PrepareProposal`。看见整池都来了，不是已经只能看见装得进一块的那些 interchangeable——本页从 345 item 1 侧钉 not already only subset that fits 单句。345 prepare-return vs pool bundled unbundling 在本页 item 1 启动。

2. **看见能看见全部 / 看见整池都来了 / 这份可见 is not already 已经没有上限 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 878 prepare-return-notsubset interchangeable / 345 prepare-return item 3 回包保证 interchangeable / 880 prepare-return-notengine interchangeable，也不是已经整池都给 Prepare 就已经没有上限 interchangeable / 299 pool-no-limit interchangeable。**  
   官方把能看见全部和已经没有上限分开——345 bundled 第一件事常与 299 混成「看见整池都给了就已经只能看见子集或已经没有上限 interchangeable」，本页钉 not already no limit 单句。

3. **看见能看见全部 / 看见 MaxBytes 写成 -1 / 这份可见 is not already 已经交差 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 878 prepare-return-notsubset interchangeable / 879 prepare-return-notover interchangeable，也不是已经 -1 就按 100 MB 验已经没有上限 interchangeable / 337 minus-one interchangeable。**  
   官方把能看见全部和已经交差分开。看见 MaxBytes 写成 -1，不是已经交差 interchangeable。345 prepare-return vs pool bundled unbundling 在本页 item 1 启动。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **整池可见 not already only subset that fits ≠ 已经只能看见装得进一块的子集 interchangeable：** 官方把看见全部和只看见装得进一块分开。
- **看见能看见全部 not already no limit ≠ 已经没有上限 interchangeable：** 官方把能看见全部和已经没有上限分开。
- **看见 MaxBytes 写成 -1 not already settled ≠ 已经交差 interchangeable：** 官方把能看见全部和已经交差分开；345 prepare-return vs pool bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 整池可见 | 不是已经只能看见装得进一块的子集 | 不是整池都给 Prepare 就已经没有上限（299） |
| 看见能看见全部 | 不是已经没有上限 | 不是 -1 就按 100 MB 验已经没有上限（337） |
| 看见 MaxBytes 写成 -1 | 不是已经交差 | 不是聚合体积可以超过 max_tx_bytes（879） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看整池可见 not already only subset that fits / not already no limit / not already settled 正式三事（345 余量），必须分开是不是已经只能看见装得进一块的子集、是不是已经没有上限、是不是已经交差。可以跳过「看见整池都给了就已经能整包交回去」。不要另写怎样裁回包。345 prepare-return vs pool bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-return-notover-vs-bundled.md`](worked-example-prepare-return-notover-vs-bundled.md)（不变量 879 item 2）。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- Prepare 回包上限 bundled。那是不变量 345。
- 聚合体积可以超过 max_tx_bytes。那是不变量 345 item 2 余量 / 879。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
