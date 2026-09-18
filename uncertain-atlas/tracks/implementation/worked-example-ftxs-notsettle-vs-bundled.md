# 例：看见 Finalize exec-txs-return-control is not already settled interchangeable / not already like-Prepare interchangeable / not already last-state-only interchangeable

**层次**：实现 / Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量）/ not 1112 ftxs-notsettle interchangeable / not 408 fintxs-vs-control bundled interchangeable」，不是 Finalize 执行余量 bundled（408），也不是 Finalize 实现必须确定因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样（1110），也不是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样（342）。不要另写怎样写 Finalize 执行余量。

## 官方三件事

1. **看见 Finalize 按应用自己的规则确定地执行 txs、再交还控制权 / 看见先跑了 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1112 ftxs-notsettle interchangeable / 1113 ftxs-notdec interchangeable / 408 fintxs item 2 process-not-decided interchangeable，也不是已经 Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事 bundled（408 item 1 余量） interchangeable / 408 fintxs item 1 interchangeable。**  
   官方写：应用按自己定的规则，确定地执行 FinalizeBlockRequest.txs 里的交易，再把控制权交还给 CometBFT。看见先跑了，不是已经交差 interchangeable——本页从 408 item 1 侧钉 not already settled 单句。408 fintxs vs control bundled unbundling 在本页 item 1 启动。

2. **看见必须确定 / 看见先跑了 / 这份栏 is not already 已经可以像 Prepare 那样 interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1112 ftxs-notsettle interchangeable / 408 fintxs item 3 process-not-exec interchangeable / 1114 ftxs-notexec interchangeable，也不是已经 Finalize 实现必须确定因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样 interchangeable / 1110 ffields-notprep interchangeable。**  
   官方把必须确定和已经可以像 Prepare 那样分开。看见必须确定，不是已经可以像 Prepare 那样 interchangeable。本页钉 not already like-Prepare 单句。

3. **看见按自己的规则 / 看见先跑了 / 这份栏 is not already 已经只依赖上一份状态和决定块 interchangeable，也不是已经 Finalize 执行余量 bundled（408） interchangeable / 1112 ftxs-notsettle interchangeable / 1113 ftxs-notdec interchangeable，也不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样 interchangeable / 342 finalize-det interchangeable。**  
   官方把按自己的规则和已经只依赖上一份状态和决定块分开。看见按自己的规则，不是已经只依赖上一份状态和决定块 interchangeable。408 fintxs vs control bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize exec-txs-return-control not already settled ≠ 已经交差 interchangeable：** 官方把交还控制权和已经交差分开。
- **看见必须确定 not already like-Prepare ≠ 已经可以像 Prepare 那样 interchangeable：** 官方把必须确定和已经可以像 Prepare 那样分开。
- **看见按自己的规则 not already last-state-only ≠ 已经只依赖上一份状态和决定块 interchangeable：** 官方把按自己的规则和已经只依赖上一份状态和决定块分开；408 fintxs vs control bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 按应用自己的规则确定地执行 txs、再交还控制权 | 不是已经交差 | 不是 Finalize 实现必须确定因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样（1110） |
| 看见必须确定 | 不是已经可以像 Prepare 那样 | 不是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样（342） |
| 看见按自己的规则 | 不是已经只依赖上一份状态和决定块 | 不是填了信息就已经是刚决定那块的字段（1113） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量），必须分开是不是已经交差、是不是已经可以像 Prepare 那样、是不是已经只依赖上一份状态和决定块。可以跳过「看见填了 Finalize 执行余量就已经交差」。不要另写怎样写 Finalize 执行余量。408 fintxs vs control bundled unbundling 在本页 item 1 启动；续 [`worked-example-ftxs-notdec-vs-bundled.md`](worked-example-ftxs-notdec-vs-bundled.md)（不变量 1113 item 2）。

## 本页不抄

- 怎样写 Finalize 执行余量、怎样写确定性、怎样整块执行。
- Finalize 执行余量 bundled。那是不变量 408。
- Finalize 实现必须确定因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样。那是不变量 1110。
- Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样。那是不变量 342。
