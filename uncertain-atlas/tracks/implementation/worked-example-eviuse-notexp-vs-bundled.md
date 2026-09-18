# 例：看见extension_signature 暴露给应用再处理不是已经 Verify 过不是已经应用 finished verifying；看见extension_signature exposed for further processing is not already Verify不是已经跑过 VerifyVoteExtension；看见extension_signature 暴露给应用再处理不是已经 Verify 过不是已经按原样签

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtViUse extension_signature exposed for further processing not already app-verified / not already Verify / not already 421-handed 正式三事（447 余量）/ not 1366 eviuse-notexp interchangeable / not 447 extviusage-vs-expose bundled interchangeable」，不是 extviusage vs expose bundled（447），也不是已经 extension_signature 表栏就已经把验过的签交给应用（421），也不是已经 VerifyVoteExtension Usage（353）。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。

## 官方三件事

1. **看见extension_signature 暴露给应用再处理不是已经 Verify 过 / 看见extension_signature 暴露给应用再处理不是已经 Verify 过 这份对象 is not already 已经应用 finished verifying interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1366 eviuse-notexp interchangeable / 1365 eviuse-notapp interchangeable，也不是已经 ExtViUse extension_signature exposed for further processing not already app-verified / not already Verify / not already 421-handed 正式三事 bundled（447 item 2 余量） interchangeable / 447 eviuse item 2 interchangeable。**  
   官方把extension_signature 暴露给应用再处理不是已经 Verify 过和已经应用 finished verifying写成两件。看见extension_signature 暴露给应用再处理不是已经 Verify 过，不是已经应用 finished verifying。

2. **看见extension_signature exposed for further processing is not already Verify / 看见extension_signature 暴露给应用再处理不是已经 Verify 过 / 这份对象 is not already 已经跑过 VerifyVoteExtension interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1366 eviuse-notexp interchangeable / 1367 eviuse-nottwo interchangeable，也不是已经 extension_signature 表栏就已经把验过的签交给应用 interchangeable / 421 extension_signature 表栏就已经把验过的签交给应用 interchangeable。**  
   官方把extension_signature exposed for further processing is not already Verify和已经跑过 VerifyVoteExtension写成两件。看见extension_signature exposed for further processing is not already Verify，不是已经跑过 VerifyVoteExtension。

3. **看见extension_signature 暴露给应用再处理不是已经 Verify 过 / 看见extension_signature exposed for further processing is not already Verify / 这份对象 is not already 已经按原样签 interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1366 eviuse-notexp interchangeable / 1365 eviuse-notapp interchangeable，也不是已经 VerifyVoteExtension Usage interchangeable / 353 VerifyVoteExtension Usage interchangeable。**  
   官方把extension_signature 暴露给应用再处理不是已经 Verify 过和已经按原样签写成两件。看见extension_signature 暴露给应用再处理不是已经 Verify 过，不是已经按原样签。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。

## 官方为什么这样拆

- **expose for further processing 不是已经应用验完 interchangeable：官方把暴露再处理和已经跑过 Verify 分开。**
- **看见已由引擎验过 不是已经 finished verifying。**
- **看见有签 不是已经 421 表栏就已经交给应用那种已经交差。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经应用 finished verifying | 不是已经应用 finished verifying | 不是已经extension_signature 表栏就已经把验过的签交给应用（421） |
| 已经跑过 VerifyVoteExtension | 不是已经跑过 VerifyVoteExtension | 不是已经VerifyVoteExtension Usage（353） |
| 已经按原样签 | 不是已经按原样签 | 不是已经1365 eviuse-notapp |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtViUse extension_signature exposed for further processing not already app-verified / not already Verify / not already 421-handed 正式三事（447 余量），必须分开是不是已经应用 finished verifying、是不是已经跑过 VerifyVoteExtension、是不是已经按原样签。可以跳过「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完」。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。447 ExtendedVoteInfo Usage expose signature bundled unbundling 在本页 item 2 续；续 [`worked-example-eviuse-nottwo-vs-bundled.md`](worked-example-eviuse-nottwo-vs-bundled.md)（不变量 1367 item 3）。

## 本页不抄

- 怎样写 ExtendedVoteInfo Usage 暴露签正式三事、怎样再验签、怎样读空切片。
- 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。
