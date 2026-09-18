# 例：看见建议自验不是已经迟到扩展 bundled；看见it is suggested不是已经是引擎会再 Verify；看见建议自验不是已经 Accept

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「SuggestValidate suggested not already late-ext / not already engine-re-Verify / not already Accept 正式三事（520 余量）/ not 1316 sugval-notmust interchangeable / not 520 preparewhen-suggestvalidate-vs-bundled bundled interchangeable」，不是 preparewhen suggestvalidate vs bundled bundled（520），也不是已经 迟到扩展（352），也不是已经 Req 6 must Accept（348）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见建议自验 / 看见建议自验 这份对象 is not already 已经迟到扩展 bundled interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1316 sugval-notmust interchangeable / 1317 sugval-notcall interchangeable，也不是已经 SuggestValidate suggested not already late-ext / not already engine-re-Verify / not already Accept 正式三事 bundled（520 item 1 余量） interchangeable / 520 sugval item 1 interchangeable。**  
   官方把建议自验和已经迟到扩展 bundled写成两件。看见建议自验，不是已经迟到扩展 bundled。

2. **看见it is suggested / 看见建议自验 / 这份对象 is not already 已经是引擎会再 Verify interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1316 sugval-notmust interchangeable / 1318 sugval-notreverify interchangeable，也不是已经 迟到扩展 interchangeable / 352 迟到扩展 interchangeable。**  
   官方把it is suggested和已经是引擎会再 Verify写成两件。看见it is suggested，不是已经是引擎会再 Verify。

3. **看见建议自验 / 看见it is suggested / 这份对象 is not already 已经 Accept interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1316 sugval-notmust interchangeable / 1317 sugval-notcall interchangeable，也不是已经 Req 6 must Accept interchangeable / 348 Req 6 must Accept interchangeable。**  
   官方把建议自验和已经 Accept写成两件。看见建议自验，不是已经 Accept。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **it is suggested 不是已经是引擎会再 Verify interchangeable：官方把 suggested 和 must / engine call 分开。**
- **看见建议自验 不是已经迟到扩展 bundled：352 把 MAY use + suggested + not engine re-Verify 捆在一起，本页钉 suggested 单句。**
- **看见 it is suggested 不是已经 Accept：348 钉 Req 6 必须 Accept，516 钉 When return status，本页钉 suggested 不是 return。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经迟到扩展 bundled | 不是已经迟到扩展 bundled | 不是已经迟到扩展（352） |
| 已经是引擎会再 Verify | 不是已经是引擎会再 Verify | 不是已经Req 6 must Accept（348） |
| 已经 Accept | 不是已经 Accept | 不是已经1317 sugval-notcall |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 SuggestValidate suggested not already late-ext / not already engine-re-Verify / not already Accept 正式三事（520 余量），必须分开是不是已经迟到扩展 bundled、是不是已经是引擎会再 Verify、是不是已经 Accept。可以跳过「看见建议按 Verify 同款逻辑再看一遍就已经是引擎会再 Verify interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。520 PrepareProposal When suggestvalidate bundled unbundling 在本页 item 1 启动；续 [`worked-example-sugval-notcall-vs-bundled.md`](worked-example-sugval-notcall-vs-bundled.md)（不变量 1317 item 2）。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
