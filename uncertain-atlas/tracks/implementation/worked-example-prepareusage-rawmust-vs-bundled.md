# 例：看见 preliminary txs called raw proposal / can modify this set 不是已经 Prepare 改列表 bundled interchangeable；看见 MAY configure txs exceeding max_tx_bytes 不是已经 Req 2 bundled interchangeable；看见 MUST remove if size > max_tx_bytes 不是已经引擎会帮你裁 interchangeable

**层次**：实现 / PrepareProposal Usage raw proposal / MUST remove 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「preliminary raw proposal / can modify this set 不是 Prepare 改列表 bundled interchangeable / MAY configure exceeding 不是 Req 2 bundled interchangeable / MUST remove 不是引擎会帮你裁 interchangeable」，不是 Prepare 改列表后果（355），也不是 Prepare 回包上限 Req 2 bundled（345）。不要另写怎样裁回包、怎样改 Prepare 列表。

## 官方三件事

规范把 PrepareProposal Methods Usage 里 raw proposal / 可超上限配置 / MUST remove 写成三件独立的实现事，不是「看见 Prepare 请求里带了 txs 就已经改列表 bundled interchangeable、已经能回超限、已经是引擎会帮你裁」一件事：

1. **看见 `PrepareProposalRequest` contains a preliminary set of transactions `txs` called _raw proposal_ / Application can modify this set and return via `PrepareProposalResponse.txs` / 看见初步交易列表叫 raw proposal、应用可以改这套并通过回包交回 不是已经 Prepare 改列表 bundled（355） interchangeable / 已经从内存池删掉 / 已经进了内存池 / 已经还能按 t1 查到 interchangeable，也不是已经 `PrepareProposalRequest.txs` 是初步交易列表 Request栏（423） interchangeable / 已经跑过 Process interchangeable，也不是已经 ProcessProposal 含执行所需全部信息（453） interchangeable / 已经只有 raw proposal interchangeable。**  
   官方 Usage 写：`PrepareProposalRequest` contains a preliminary set of transactions `txs` retrieved from the mempool, called _raw proposal_. The Application can modify this set and return a modified set via `PrepareProposalResponse.txs`。看见 preliminary / raw proposal，不是已经 Prepare 改列表 consequences bundled（355） interchangeable——355 钉拿掉/加入/改追踪性，本页钉 Methods Usage raw proposal 单句。看见 can modify this set，不是已经 Request 栏 txs 是初步列表（423） interchangeable——423 钉 Request 栏，本页钉 Usage 侧 can modify set 语义。看见 return via `PrepareProposalResponse.txs`，不是已经 ProcessProposal Contains all information needed to fully execute（453） interchangeable——453 钉 Process 八栏 vs Prepare 只有 txs，本页钉 Usage raw proposal 单句。
2. **看见 The Application MAY configure CometBFT to include txs whose total size exceeds `PrepareProposalRequest.max_tx_bytes` / if `MaxBytes`=-1 include all mempool txs / 看见应用 MAY 让引擎交来总体积可以超过这次 max_tx_bytes 的列表 不是已经整池可见 / Req 2 保证回的列表 bundled（345） interchangeable / 已经只能看见装得进一块的子集 / 已经能回超限列表 interchangeable，也不是已经 `PrepareProposalRequest.max_tx_bytes` 是当前配置（423） interchangeable / 已经引擎会帮你裁 interchangeable，也不是已经整池都给 Prepare 就没有上限（299） interchangeable。**  
   官方 Usage 写：The Application MAY configure CometBFT to include a list of transactions in `PrepareProposalRequest.txs` whose total size in bytes exceeds `PrepareProposalRequest.max_tx_bytes`. If the Application sets `ConsensusParams.Block.MaxBytes` to -1, CometBFT will include _all_ transactions currently in the mempool in `PrepareProposalRequest.txs`, which may not fit in `PrepareProposalRequest.max_tx_bytes`。看见 MAY configure exceeding，不是已经 Req 2 bundled（345） interchangeable——345 钉 app_requirements Formal Requirement 2，本页钉 Methods Usage MAY configure 单句。看见 all mempool may not fit max_tx_bytes，不是已经聚合体积可以超过 max_tx_bytes 那种已经能回超限列表 interchangeable——345 第三件事钉回包不得超过，本页钉 Usage 侧 MAY 让请求超上限。看见 MaxBytes=-1 include all，不是已经整池都给 Prepare 就没有上限（299） interchangeable。
3. **看见 if size of `PrepareProposalRequest.txs` > `max_tx_bytes` Application MUST remove transactions to ensure limit respected by `PrepareProposalResponse.txs` (Requirement 2) / 看见初步列表比 max_tx_bytes 大应用 MUST 删掉一些让回包遵守上限 不是已经 Req 2 保证回的列表 bundled（345） interchangeable / 已经引擎会帮你裁 / 已经能回超限列表 interchangeable，也不是已经 Prepare 改列表拿掉 tx bundled（355） interchangeable / 已经从内存池删掉 interchangeable，也不是已经 -1 就按 100 MB 验已经没有上限（337） interchangeable。**  
   官方 Usage 写：if the size of `PrepareProposalRequest.txs` is greater than `PrepareProposalRequest.max_tx_bytes`, the Application MUST remove transactions to ensure that the `PrepareProposalRequest.max_tx_bytes` limit is respected by those transactions returned in `PrepareProposalResponse.txs`. This is specified in Requirement 2。看见 MUST remove if greater，不是已经 Req 2 保证回的列表 bundled（345） interchangeable——345 钉 requirements 侧保证，本页钉 Methods Usage MUST remove 单句。看见 ensure limit respected by Response.txs，不是已经引擎会帮你裁 interchangeable。看见 MUST remove，不是已经从提案拿掉 tx 就不从内存池删掉（355） interchangeable——355 钉池后果，本页钉 Usage MUST remove 体积义务。

怎样做裁回包、怎样设 `MaxBytes = -1`、怎样改 Prepare 列表是规范里的做法，本页不抄。Prepare 改列表 consequences（355）、Prepare 回包上限 Req 2 bundled（345）、Prepare 请求栏（423）是另外那套，本页不抄。

## 官方为什么这样拆

- **raw proposal / can modify this set ≠ Prepare 改列表 bundled interchangeable：** 官方把 Methods Usage raw proposal 单句和改列表后果 bundled 分开。
- **MAY configure exceeding ≠ Req 2 bundled interchangeable：** 官方把 MAY 让请求超上限和 requirements 侧 Req 2 保证分开。
- **MUST remove if > max_tx_bytes ≠ 引擎会帮你裁 interchangeable：** 官方把 Methods Usage MUST remove 单句和应用必须自己裁回包分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| raw proposal / can modify this set | 不是 Prepare 改列表 bundled（355） | 不是 Request 栏 txs 初步列表（423） |
| MAY configure exceeding max_tx_bytes | 不是 Req 2 bundled（345） | 不是整池都给 Prepare 就没有上限（299） |
| MUST remove if size > max_tx_bytes | 不是引擎会帮你裁 | 不是 -1 就按 100 MB 验已经没有上限（337） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal Usage raw proposal / MUST remove 正式三事，必须分开 preliminary raw proposal / can modify this set 是不是 Prepare 改列表 bundled interchangeable / 已经只有 raw proposal interchangeable、MAY configure txs exceeding max_tx_bytes 是不是 Req 2 bundled interchangeable / 已经能回超限列表 interchangeable、MUST remove if size > max_tx_bytes 是不是引擎会帮你裁 interchangeable / 已经从内存池删掉 interchangeable。可以跳过「看见 Prepare 请求里带了 txs 就已经改列表 bundled interchangeable、已经能回超限、已经是引擎会帮你裁 interchangeable」。503 PrepareProposal Usage rawmust bundled unbundling 完成（1304 item 1 / 1305 item 2 / 1306 item 3）；精读 [`worked-example-prepusage-notraw-vs-bundled.md`](worked-example-prepusage-notraw-vs-bundled.md)（不变量 1304 item 1）、[`worked-example-prepusage-notexceed-vs-bundled.md`](worked-example-prepusage-notexceed-vs-bundled.md)（不变量 1305 item 2）、[`worked-example-prepusage-notmust-vs-bundled.md`](worked-example-prepusage-notmust-vs-bundled.md)（不变量 1306 item 3）。不要另写怎样裁回包、怎样改 Prepare 列表。

## 本页不抄

- 怎样做裁回包、怎样设 `MaxBytes = -1`、怎样改 Prepare 列表。
- Prepare 改列表 consequences。那是不变量 355。
- Prepare 回包上限 Req 2 bundled。那是不变量 345。
- Prepare 请求栏 max_tx_bytes / txs / height。那是不变量 423。
- ProcessProposal 含执行所需全部信息 vs raw proposal。那是不变量 453。
