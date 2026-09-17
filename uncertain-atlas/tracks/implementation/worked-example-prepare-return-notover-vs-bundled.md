# 例：看见聚合体积可以超过 max_tx_bytes is not already can return oversize interchangeable / not already pool already trimmed interchangeable / not already settled interchangeable

**层次**：实现 / 聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事（345 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事（345 余量）/ not 879 prepare-return-notover interchangeable / not 345 prepare-return-vs-pool bundled interchangeable」，不是 Prepare 回包上限 bundled（345），也不是整池都给 Prepare 就已经没有上限（299），也不是四门已经结算（33）。不要另写怎样裁回包。

## 官方三件事

1. **看见聚合体积可以超过 `PrepareProposalRequest.max_tx_bytes` / 看见池子加起来比这次上限大 这份超限 is not already 已经能回超限列表 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 879 prepare-return-notover interchangeable / 878 prepare-return-notsubset interchangeable / 345 prepare-return item 1 整池可见 interchangeable，也不是已经聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事 bundled（345 item 2 余量） interchangeable / 345 prepare-return item 2 interchangeable。**  
   官方写：在这种设置下，所有交易加起来的体积可以超过这次请求里的 `max_tx_bytes`。看见池子比上限大，不是已经能整包交回去 interchangeable——本页从 345 item 2 侧钉 not already can return oversize 单句。345 prepare-return vs pool bundled unbundling 在本页 item 2 续。

2. **看见请求里带了上限 / 看见池子比上限大 / 这份超限 is not already 已经按这个上限裁过 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 879 prepare-return-notover interchangeable / 345 prepare-return item 3 回包保证 interchangeable / 880 prepare-return-notengine interchangeable，也不是已经整池都给 Prepare 就已经没有上限 interchangeable / 299 pool-no-limit interchangeable。**  
   官方把请求里带了上限和池子已经按这个上限裁过分开——345 bundled 第二件事常与 299 混成「看见池子超了就已经能回超限或已经裁过 interchangeable」，本页钉 not already pool already trimmed 单句。

3. **看见能看见超限的池 / 看见池子比上限大 / 这份超限 is not already 已经交差 interchangeable，也不是已经 Prepare 回包上限 bundled（345） interchangeable / 879 prepare-return-notover interchangeable / 878 prepare-return-notsubset interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把能看见超限的池和已经能回超限 / 已经交差分开。看见能看见超限的池，不是已经能回超限 interchangeable。345 prepare-return vs pool bundled unbundling 在本页 item 2 续。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **聚合体积可以超过 max_tx_bytes not already can return oversize ≠ 已经能回超限列表 interchangeable：** 官方把池子可以超这次上限和回包仍不得超过分开。
- **看见请求里带了上限 not already pool already trimmed ≠ 已经按这个上限裁过 interchangeable：** 官方把请求里带了上限和池子已经按这个上限裁过分开。
- **看见能看见超限的池 not already settled ≠ 已经交差 interchangeable：** 官方把能看见超限的池和已经交差分开；345 prepare-return vs pool bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 聚合体积可以超过 max_tx_bytes | 不是已经能回超限列表 | 不是整池都给 Prepare 就已经没有上限（299） |
| 看见请求里带了上限 | 不是已经按这个上限裁过 | 不是四门已经结算（33） |
| 看见能看见超限的池 | 不是已经交差 | 不是整池可见就已经没有上限（878） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事（345 余量），必须分开是不是已经能回超限列表、是不是已经按这个上限裁过、是不是已经交差。可以跳过「看见池子超了就已经能回超限」。不要另写怎样裁回包。345 prepare-return vs pool bundled unbundling 在本页 item 2 续；续 [`worked-example-prepare-return-notengine-vs-bundled.md`](worked-example-prepare-return-notengine-vs-bundled.md)（不变量 880 item 3）。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- Prepare 回包上限 bundled。那是不变量 345。
- 整池可见。那是不变量 345 item 1 余量 / 878。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- 四门已经结算。那是不变量 33。
