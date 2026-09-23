# 例：看见通常紧跟 Prepare、列表对得上 / 看见通常对得上 / 看见 txs 一样 is not already already guaranteed-this interchangeable / already must-match interchangeable / already same-call interchangeable

**层次**：实现 / 通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量）/ not 807 process-notguaranteed interchangeable / not 351 processalso bundled interchangeable」，不是 Process 也会在提议者那边叫 bundled（351），也不是 Process 也会在提议者那边叫不是已经不用再 Process（806 item 1 余量）或失败时可能对上更早一次或根本不调不是已经每轮都会叫（808 item 3 余量）。不要另写怎样写 Process。

## 官方三件事

规范把 Methods 里通常这次 Process 紧跟 Prepare、请求对得上刚回的那块 和「已经是通常对得上就已经保证是这一次 interchangeable / 已经是 txs 一样就已经必须一样 interchangeable / 已经是刚 Prepare 完就已经是同一份调用 interchangeable / 已经是 processalso bundled interchangeable」分开写成三件独立的实现事，不是「看见通常对得上就已经保证是这一次 interchangeable / 就已经必须一样 interchangeable / 就已经是同一份调用 interchangeable」一件事：

1. **看见通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` / 看见通常对得上 / 看见列表对得上 is not already 已经保证是这一次 Prepare 的回包 interchangeable / 已经 guaranteed-this interchangeable / 已经保证这一次交差 interchangeable / 351 processalso bundled interchangeable / 347 req3coherence interchangeable / processalso-sold-as-matched interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 807 process-notguaranteed interchangeable / 351 processalso item 2 interchangeable，也不是已经通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事 bundled（351 item 2 余量） interchangeable / 351 processalso item 2 interchangeable，也不是已经不用再 Process（806） interchangeable / 808 process-notalways interchangeable / 33 fourgates interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable。**  
   官方写：通常这次 Process 紧跟 Prepare，而且请求对得上刚回的那块。看见通常对得上，不是已经保证。看见通常对得上，不是已经 guaranteed-this interchangeable——351 钉 bundled 三事，本页从 item 2 侧钉 not already guaranteed-this 单句。看见通常紧跟 Prepare、列表对得上，不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable——351 钉 bundled，本页钉 item 2 第一件事。看见通常对得上，不是已经不用再 Process（806） interchangeable——806 另钉 item 1。看见通常对得上，不是已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable——347 另钉。351 processalso vs prepare bundled unbundling 在本页 item 2 续。

2. **看见 txs 一样 / 看见请求 txs 等于回包 txs / 看见列表字节一样 is not already 已经必须一样 interchangeable / 已经 must-match interchangeable / 已经必须对上交差 interchangeable / 351 processalso bundled interchangeable / 33 fourgates interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 807 process-notguaranteed interchangeable / 351 processalso item 1 跳过 interchangeable / 351 processalso item 3 失败 interchangeable，也不是已经通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事 bundled（351 item 2 余量） interchangeable / 351 processalso item 2 interchangeable，也不是已经保证是这一次（本页第一件事） interchangeable。**  
   官方写：看见 txs 一样，不是已经必须一样。看见请求 txs 等于回包 txs，不是已经 must-match interchangeable——本页钉 not already must-match 单句。看见列表字节一样，不是已经保证是这一次（本页第一件事） interchangeable——三件事分开钉。351 processalso vs prepare bundled unbundling 在本页 item 2 续。

3. **看见刚 Prepare 完 / 看见刚回了 Prepare / 看见紧跟 Prepare is not already 已经是同一份调用 interchangeable / 已经 same-call interchangeable / 已经同一调用交差 interchangeable / 351 processalso bundled interchangeable / 311 candidate interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 807 process-notguaranteed interchangeable / 351 processalso item 1 / 351 processalso item 3，也不是已经通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事 bundled（351 item 2 余量） interchangeable / 351 processalso item 2 interchangeable，也不是已经保证是这一次（本页第一件事） interchangeable / 已经必须一样（本页第二件事） interchangeable。**  
   官方写：看见刚 Prepare 完，不是已经是同一份调用。看见刚回了 Prepare，不是已经 same-call interchangeable——本页钉 not already same-call 单句。看见紧跟 Prepare，不是已经必须一样（本页第二件事） interchangeable——三件事分开钉。351 processalso vs prepare bundled unbundling 在本页 item 2 续。

怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径是规范里的做法，本页不抄。Process 也会在提议者那边叫 bundled（351）、Process 也会在提议者那边叫不是已经不用再 Process（351 item 1 余量 / 806）、失败时可能对上更早一次或根本不调不是已经每轮都会叫（351 item 3 余量 / 808）、四门已经结算（33）、正确提议者的准备提案必须被正确接收者 Accept（347）、候选已经是 ExecuteTxState（311）是另外那套，本页不抄。

## 官方为什么这样拆

- **通常紧跟 Prepare、列表对得上 not already guaranteed-this ≠ 351 / 347 interchangeable：** 官方把通常对得上和已经保证是这一次分开。
- **txs 一样 not already must-match ≠ 已经必须一样 interchangeable：** 官方把 txs 一样和已经必须一样分开。
- **刚 Prepare 完 not already same-call ≠ 已经是同一份调用 interchangeable：** 官方把刚 Prepare 完和已经是同一份调用分开；351 processalso vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 通常紧跟 Prepare、列表对得上 | 不是 already guaranteed-this | 不是正确提议者的准备提案必须被正确接收者 Accept alone（347） |
| txs 一样 | 不是 already must-match | 不是不用再 Process already skip alone（806） |
| 刚 Prepare 完 | 不是 already same-call | 不是失败路径 already every-round alone（808） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常紧跟 Prepare、列表对得上不是已经保证是这一次 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 余量），必须分开通常紧跟 Prepare、列表对得上 是不是 already guaranteed-this interchangeable / 351 processalso bundled interchangeable / processalso-sold-as-matched interchangeable、txs 一样 是不是 already must-match interchangeable、刚 Prepare 完 是不是 already same-call interchangeable。可以跳过「看见通常对得上就已经保证是这一次 interchangeable / 就已经必须一样 interchangeable / 就已经是同一份调用 interchangeable」。不要另写怎样写 Process。351 processalso vs prepare bundled unbundling 在本页 item 2 续（806 + 807）；续 [`worked-example-process-notalways-vs-bundled.md`](worked-example-process-notalways-vs-bundled.md)（不变量 808 item 3）；完成见 808。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样缓存候选、怎样测失败路径。
- Process 也会在提议者那边叫 bundled。那是不变量 351。
- Process 也会在提议者那边叫不是已经不用再 Process。那是不变量 351 item 1 余量 / 806。
- 失败时可能对上更早一次或根本不调不是已经每轮都会叫。那是不变量 351 item 3 余量 / 808。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 候选已经是 ExecuteTxState。那是不变量 311。
