# 例：看见step 1 在调 VerifyVoteExtension 之前不是已经 Verify When 正式流程 bundled；看见step 1 before call不是已经验过扩展；看见step 1 在调 VerifyVoteExtension 之前不是已经写进 last_commit

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事（514 余量）/ not 1327 vwdisc-notstep interchangeable / not 514 verifywhen-discard-vs-bundled bundled interchangeable」，不是 verifywhen discard vs bundled bundled（514），也不是已经 Verify When 正式流程（435），也不是已经 迟到扩展 MAY 不加 Verify（352）。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方三件事

1. **看见step 1 在调 VerifyVoteExtension 之前 / 看见step 1 在调 VerifyVoteExtension 之前 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1327 vwdisc-notstep interchangeable / 1325 vwdisc-notsig interchangeable，也不是已经 VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事 bundled（514 item 3 余量） interchangeable / 514 vwdisc item 3 interchangeable。**  
   官方把step 1 在调 VerifyVoteExtension 之前和已经 Verify When 正式流程 bundled写成两件。看见step 1 在调 VerifyVoteExtension 之前，不是已经 Verify When 正式流程 bundled。

2. **看见step 1 before call / 看见step 1 在调 VerifyVoteExtension 之前 / 这份对象 is not already 已经验过扩展 interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1327 vwdisc-notstep interchangeable / 1326 vwdisc-notzero interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把step 1 before call和已经验过扩展写成两件。看见step 1 before call，不是已经验过扩展。

3. **看见step 1 在调 VerifyVoteExtension 之前 / 看见step 1 before call / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1327 vwdisc-notstep interchangeable / 1325 vwdisc-notsig interchangeable，也不是已经 迟到扩展 MAY 不加 Verify interchangeable / 352 迟到扩展 MAY 不加 Verify interchangeable。**  
   官方把step 1 在调 VerifyVoteExtension 之前和已经写进 last_commit写成两件。看见step 1 在调 VerifyVoteExtension 之前，不是已经写进 last_commit。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方为什么这样拆

- **step 1 before VerifyVoteExtension call 不是已经验过扩展 interchangeable：官方把 step 1 门槛和 step 2 call 分开。**
- **看见先丢掉无有效签 不是已经 Application returns ACCEPT/REJECT：435 钉 step 3–4 后效，本页钉 step 1 在 return 之前。**
- **看见收到他人 Precommit 不是已经迟到扩展已经 Verify 过：352 钉 MAY 不加 Verify，本页钉 When step 1 收到侧有效性门槛。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经验过扩展 | 不是已经验过扩展 | 不是已经迟到扩展 MAY 不加 Verify（352） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经1325 vwdisc-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyDiscard before-call not already Verify-When / not already ACCEPT-REJECT / not already local-also-Verify 正式三事（514 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经验过扩展、是不是已经写进 last_commit。可以跳过「看见收到 Precommit 就已经跳过 Verify interchangeable、已经验过扩展 interchangeable」。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。514 VerifyVoteExtension When discard bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
- 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
