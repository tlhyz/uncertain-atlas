# 例：看见 no calls to `CheckTx` on new transactions / 看见新交易不再进 CheckTx is not already 已经 CheckTx 技术上可选 / 不参与处理块 interchangeable / 已经进了池 / 已经开始流言 interchangeable / 已经 finlock bundled interchangeable

**层次**：实现 / FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 7。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool 正文。本页是「FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量）/ not 630 notoptional interchangeable / not 373 checktxopt interchangeable / not 312 checktxtype interchangeable / not 629 notsettled interchangeable / not 631 notcommitlock interchangeable」，不是 FinalizeBlock When locks mempool 正式三事 bundled（588），也不是 CheckTx 技术上可选（373），也不是 Finalize 之后 bundled（403）。不要另写怎样锁内存池、怎样再验、怎样解锁。

## 官方三件事

规范把 FinalizeBlock When 第 7 步 _p_'s CometBFT locks the mempool — no calls to `CheckTx` on new transactions 和「已经是已经 CheckTx 技术上可选 / 不参与处理块 interchangeable / 已经是已经进了池 / 已经开始流言 interchangeable / 已经是 finlock bundled interchangeable」分开写成三件独立的实现事，不是「看见新交易不再进 CheckTx 就已经 CheckTx 可选、就已经进池、就已经 finlock bundled interchangeable」一件事：

1. **看见 no calls to `CheckTx` on new transactions / 看见新交易不再进 CheckTx / 看见 When 第 7 步 no calls on new transactions is not already 已经 CheckTx 技术上可选 interchangeable / 不参与处理块 interchangeable / 373 checktxopt interchangeable / 312 checktxopt interchangeable / 313 checktxguard interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 630 notoptional interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 631 notcommitlock interchangeable，也不是已经 CheckTx 技术上可选、不参与处理块 bundled（373 余量） interchangeable / 373 checktxopt interchangeable / 312 checktxopt interchangeable / 489 chktxcodereject interchangeable / 33 four gates interchangeable，也不是已经 CheckTx 守卫 bundled（313 余量） interchangeable / 313 checktxguard interchangeable / 339 checktxweak interchangeable / 373 checktxresponse interchangeable / 312 checktxopt interchangeable，也不是已经 CheckTx Usage Code≠0 rejected bundled（489 余量） interchangeable / 489 chktxcodereject interchangeable / 312 checktxopt interchangeable / 339 checktxweak interchangeable / 373 checktxopt interchangeable。**  
   官方 When 第 7 步写：no calls to `CheckTx` on new transactions。Usage 另写：CheckTx 技术上可选，不参与处理块。看见锁住期间不接新 CheckTx，不是已经 CheckTx optional / not involved in processing blocks（373） interchangeable——588 bundled 第二件事常被写成「看见 no calls on new transactions 就已经 CheckTx 技术上可选 interchangeable」，本页从 588 item 2 侧钉 not CheckTx optional 单句。看见 no calls on **new** transactions，不是已经 CheckTx 是内存池守卫（313） interchangeable——313 另钉 CheckTx 守卫 / 每条节点先跑 CheckTx，本页钉 588 item 2 第一件事。看见新交易不再进 CheckTx，不是已经 Code≠0 会被拒不会进提案（312 / 489） interchangeable——312 / 489 钉池门 / 提案前拒，本页钉 not CheckTx optional 单句。
2. **看见 no calls to `CheckTx` on new transactions / 看见新交易不再进 CheckTx is not already 已经进了池 interchangeable / 已经开始流言 interchangeable / Check 通过就是已进提案 interchangeable / 33 four gates interchangeable / 301 mempool interchangeable / 339 checktxweak interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 630 notoptional interchangeable / 588 finlock interchangeable / 629 notsettled interchangeable / 631 notcommitlock interchangeable，也不是已经 CheckTx 技术上可选 bundled（373 余量） interchangeable / 373 checktxopt item 2 Code≠0 rejected interchangeable / 312 checktxopt item 2 not in block interchangeable / 489 chktxcodereject interchangeable / 316 exectxresult interchangeable，也不是已经 CheckTx 弱过滤器 bundled（339 余量） interchangeable / 339 checktxweak interchangeable / 339 item 3 mempool interchangeable / 355 preparedrop interchangeable / 301 proposed-sold-as-removed interchangeable，也不是已经 Prepare 改列表 bundled（355 余量） interchangeable / 355 preparedrop interchangeable / 345 preparereturn interchangeable / 301 mempool interchangeable / 33 four gates interchangeable。**  
   官方把 When 第 7 步锁期间不接新 CheckTx 和已经进池 / 已经开始流言分开——588 item 2 常与 33 / 301 混成「看见 no calls on new transactions 就已经进了池 interchangeable」，本页钉 not already in pool 单句。看见 no calls on new transactions，不是已经 Check 通过就是已进提案（33） interchangeable——33 钉四门已经结算，本页钉 588 item 2 第二件事。看见新交易不再进 CheckTx，不是已经 CheckTx Code≠0 会被拒不会广播（373 / 312） interchangeable——373 另钉 optional / 不参与处理块，本页钉 not already in pool / not gossiped 单句。
3. **看见 no calls to `CheckTx` on new transactions / 看见新交易不再进 CheckTx is not already finlock bundled（588） interchangeable / 已经 CometBFT locks the mempool interchangeable / 已经 locks mempool after persist interchangeable / 588 finlock item 1 interchangeable / 588 finlock item 3 interchangeable / 629 notsettled interchangeable / 631 notcommitlock interchangeable，也不是已经 FinalizeBlock When locks mempool 正式三事 bundled（588） interchangeable / 630 notoptional interchangeable / 588 finlock interchangeable / 373 checktxopt interchangeable / 310 commitlock interchangeable / 312 checktxtype interchangeable，也不是已经 CometBFT locks the mempool not already settled bundled（588 item 1 余量 / 629） interchangeable / 629 notsettled interchangeable / 403 finafter interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable，也不是已经 locks mempool after persist not Commit lock bundled（588 item 3 余量 / 631） interchangeable / 631 notcommitlock interchangeable / 310 commitlock interchangeable / 403 finafter item 3 optional recheck interchangeable / 312 checktxtype RECHECK interchangeable，也不是已经 Finalize 之后 bundled（403 余量） interchangeable / 403 finafter interchangeable / 403 item 2 落完再锁内存池 interchangeable / 403 item 3 optional recheck interchangeable / 592 finunlock interchangeable。**  
   官方把 588 finlock bundled 三事里的 no calls to CheckTx on new transactions 和 locks the mempool / locks mempool after persist 分开——588 bundled 常与 item 1 / item 3 混成「看见 no calls on new transactions 就已经 finlock bundled interchangeable」，本页钉 588 item 2 第三件事。看见 no calls on new transactions，不是已经 CometBFT locks the mempool not already settled（588 item 1 余量 / 629） interchangeable——629 另钉 not settled / not four gates，本页钉 item 2 单句。看见 When 第 7 步，不是已经 locks mempool after persist not Commit lock（588 item 3 余量 / 631） interchangeable——631 另钉 not Commit lock / not unlock / not Recheck，本页钉 not finlock bundled 单句。

怎样锁内存池、怎样再验池里剩下的、怎样解锁是规范里的做法，本页不抄。FinalizeBlock When locks mempool 正式三事 bundled（588）、CometBFT locks the mempool not already settled（588 item 1 余量 / 629）、locks mempool after persist not Commit lock（588 item 3 余量 / 631）、CheckTx 技术上可选（373）、CheckTx Type（312）、Finalize 之后 bundled（403）、Commit 前上锁（310）是另外那套，本页不抄。

## 官方为什么这样拆

- **no calls on new transactions not CheckTx optional ≠ 373 checktxopt / 313 checktxguard interchangeable：** 官方把 When 第 7 步锁期间不接新 CheckTx 和 CheckTx optional / 不参与处理块 分开。
- **no calls on new transactions not already in pool ≠ 33 four gates / 301 mempool interchangeable：** 官方把 588 item 2 和已经进池 / 已经开始流言 分开。
- **no calls on new transactions not finlock bundled ≠ 629 notsettled / 631 notcommitlock interchangeable：** 官方把 588 item 2 和 item 1 / item 3 分开；588 finlock unbundling 续（630 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| no calls on new transactions | 不是 already CheckTx optional | 不是 CheckTx 可选（373） |
| no calls on new transactions | 不是 already 进池 / 流言 | 不是四门已经结算（33） |
| no calls on new transactions | 不是 already finlock bundled | 不是 locks mempool not settled（588 item 1 / 629） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When no calls to CheckTx on new transactions not CheckTx optional / not already in pool / not finlock bundled 正式三事（588 余量），必须分开 no calls on new transactions 是不是 already CheckTx optional interchangeable / 373 checktxopt interchangeable / 313 checktxguard interchangeable、no calls on new transactions 是不是 already 进池 interchangeable / 301 mempool interchangeable / 33 four gates interchangeable / 339 checktxweak interchangeable、no calls on new transactions 是不是 already finlock bundled interchangeable / 629 notsettled interchangeable / 631 notcommitlock interchangeable / 588 finlock item 1 locks the mempool interchangeable。可以跳过「看见新交易不再进 CheckTx 就已经 CheckTx 技术上可选 interchangeable」。不要另写怎样锁内存池。588 finlock unbundling 在本页 item 2 续。

## 本页不抄

- 怎样锁内存池、怎样再验池里剩下的、怎样解锁。
- FinalizeBlock When locks mempool 正式三事 bundled。那是不变量 588。
- CometBFT locks the mempool not already settled。那是不变量 588 item 1 余量 / 629。
- locks mempool after persist not Commit lock。那是不变量 588 item 3 余量 / 631。
- CheckTx 技术上可选。那是不变量 373。
- RECHECK 就已经是新交易。那是不变量 312。
- Finalize 之后 bundled。那是不变量 403。
- Commit 前上锁就已经解锁。那是不变量 310。
