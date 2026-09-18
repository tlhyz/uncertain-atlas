# 例：看见vote_extension 签已由引擎验过且可以空不是已经应用验完不是已经应用验完；看见vote_extension engine-verified and can be empty is not already app-verified不是已经必须填内容；看见vote_extension 签已由引擎验过且可以空不是已经应用验完不是已经 Verify Accept

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtViUse vote_extension engine-verified can-be-empty not already app-verified / not already must-fill / not already Accept 正式三事（447 余量）/ not 1365 eviuse-notapp interchangeable / not 447 extviusage-vs-expose bundled interchangeable」，不是 extviusage vs expose bundled（447），也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369），也不是已经 Verify When ACCEPT keep（435）。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。

## 官方三件事

1. **看见vote_extension 签已由引擎验过且可以空不是已经应用验完 / 看见vote_extension 签已由引擎验过且可以空不是已经应用验完 这份对象 is not already 已经应用验完 interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1365 eviuse-notapp interchangeable / 1366 eviuse-notexp interchangeable，也不是已经 ExtViUse vote_extension engine-verified can-be-empty not already app-verified / not already must-fill / not already Accept 正式三事 bundled（447 item 1 余量） interchangeable / 447 eviuse item 1 interchangeable。**  
   官方把vote_extension 签已由引擎验过且可以空不是已经应用验完和已经应用验完写成两件。看见vote_extension 签已由引擎验过且可以空不是已经应用验完，不是已经应用验完。

2. **看见vote_extension engine-verified and can be empty is not already app-verified / 看见vote_extension 签已由引擎验过且可以空不是已经应用验完 / 这份对象 is not already 已经必须填内容 interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1365 eviuse-notapp interchangeable / 1367 eviuse-nottwo interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable / 369 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable。**  
   官方把vote_extension engine-verified and can be empty is not already app-verified和已经必须填内容写成两件。看见vote_extension engine-verified and can be empty is not already app-verified，不是已经必须填内容。

3. **看见vote_extension 签已由引擎验过且可以空不是已经应用验完 / 看见vote_extension engine-verified and can be empty is not already app-verified / 这份对象 is not already 已经 Verify Accept interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1365 eviuse-notapp interchangeable / 1366 eviuse-notexp interchangeable，也不是已经 Verify When ACCEPT keep interchangeable / 435 Verify When ACCEPT keep interchangeable。**  
   官方把vote_extension 签已由引擎验过且可以空不是已经应用验完和已经 Verify Accept写成两件。看见vote_extension 签已由引擎验过且可以空不是已经应用验完，不是已经 Verify Accept。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。

## 官方为什么这样拆

- **引擎验过且可以空 不是已经应用验完 interchangeable：官方把 CometBFT 验签和应用再处理分开。**
- **看见可以空 不是已经必须填内容。**
- **看见有扩展字节 不是已经 VerifyVoteExtension Accept。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经应用验完 | 不是已经应用验完 | 不是已经ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| 已经必须填内容 | 不是已经必须填内容 | 不是已经Verify When ACCEPT keep（435） |
| 已经 Verify Accept | 不是已经 Verify Accept | 不是已经1366 eviuse-notexp |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtViUse vote_extension engine-verified can-be-empty not already app-verified / not already must-fill / not already Accept 正式三事（447 余量），必须分开是不是已经应用验完、是不是已经必须填内容、是不是已经 Verify Accept。可以跳过「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完」。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。447 ExtendedVoteInfo Usage expose signature bundled unbundling 在本页 item 1 启动；续 [`worked-example-eviuse-notexp-vs-bundled.md`](worked-example-eviuse-notexp-vs-bundled.md)（不变量 1366 item 2）。

## 本页不抄

- 怎样写 ExtendedVoteInfo Usage 暴露签正式三事、怎样再验签、怎样读空切片。
- 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。
