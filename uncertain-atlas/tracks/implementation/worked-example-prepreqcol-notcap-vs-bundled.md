# 例：看见 PrepareProposalRequest.max_tx_bytes is not already over-limit-ok interchangeable / not already engine-trimmed interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量）/ not 1046 prepreqcol-notcap interchangeable / not 423 prepreq-vs-return bundled interchangeable」，不是 Prepare 请求栏 bundled（423），也不是聚合体积可以超过 max_tx_bytes 就已经能回超限列表（345），也不是 MaxBytes -1 就已经没有上限（337/299）。不要另写怎样写 Prepare 请求栏。

## 官方三件事

1. **看见 PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节 / 看见填了 max_tx_bytes 这份栏 is not already 已经能回超限列表 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1046 prepreqcol-notcap interchangeable / 1047 prepreqcol-notproc interchangeable / 423 prepreq item 2 txs interchangeable，也不是已经 PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事 bundled（423 item 1 余量） interchangeable / 423 prepreq item 1 interchangeable。**  
   官方写：max_tx_bytes 是当前配置的、改过的交易占的最大字节。看见填了 max_tx_bytes，不是已经聚合体积可以超过 PrepareProposalRequest.max_tx_bytes 那种已经能回超限列表 interchangeable——本页从 423 item 1 侧钉 not already over-limit-ok 单句。423 prepreq vs return bundled unbundling 在本页 item 1 启动。

2. **看见有当前配置上限 / 看见填了 max_tx_bytes / 这份栏 is not already 已经是引擎会帮你裁 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1046 prepreqcol-notcap interchangeable / 423 prepreq item 3 height interchangeable / 1048 prepreqcol-nothead interchangeable，也不是已经聚合体积可以超过 max_tx_bytes 就已经能回超限列表 interchangeable / 345 preparereturn interchangeable。**  
   官方把有当前配置上限和已经是引擎会帮你裁分开。看见有当前配置上限，不是已经是引擎会帮你裁 interchangeable。本页钉 not already engine-trimmed 单句。

3. **看见能指上限 / 看见填了 max_tx_bytes / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1046 prepreqcol-notcap interchangeable / 1047 prepreqcol-notproc interchangeable，也不是已经 MaxBytes -1 就已经没有上限 interchangeable / 337 maxbytes-cap interchangeable。**  
   官方把能指上限和已经交差分开。看见能指上限，不是已经交差 interchangeable。423 prepreq vs return bundled unbundling 在本页 item 1 启动。

怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.max_tx_bytes not already over-limit-ok ≠ 已经能回超限列表 interchangeable：** 官方把当前配置的、改过的交易占的最大字节和已经能回超限列表分开。
- **看见有当前配置上限 not already engine-trimmed ≠ 已经是引擎会帮你裁 interchangeable：** 官方把有当前配置上限和已经是引擎会帮你裁分开。
- **看见能指上限 not already settled ≠ 已经交差 interchangeable：** 官方把能指上限和已经交差分开；423 prepreq vs return bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.max_tx_bytes 是当前配置的、改过的交易占的最大字节 | 不是已经能回超限列表 | 不是聚合体积可以超过 max_tx_bytes 就已经能回超限列表（345） |
| 看见有当前配置上限 | 不是已经是引擎会帮你裁 | 不是 Requirement 2 保证回的列表不让块超字节上限那种已经是引擎会帮你裁 |
| 看见能指上限 | 不是已经交差 | 不是 txs 就已经跑过 Process（1047） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量），必须分开是不是已经能回超限列表、是不是已经是引擎会帮你裁、是不是已经交差。可以跳过「看见填了 Prepare 请求栏就已经能回超限列表」。不要另写怎样写 Prepare 请求栏。423 prepreq vs return bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepreqcol-notproc-vs-bundled.md`](worked-example-prepreqcol-notproc-vs-bundled.md)（不变量 1047 item 2）。

## 本页不抄

- 怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs。
- Prepare 请求栏 bundled。那是不变量 423。
- 聚合体积可以超过 max_tx_bytes 就已经能回超限列表。那是不变量 345。
- MaxBytes -1 就已经没有上限。那是不变量 337 / 299。
