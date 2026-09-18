# 例：看见Precommit 没有带有效签的扩展就会当非法丢掉不是已经 Verify When 正式流程 bundled；看见discards as invalid不是已经跳过 Verify；看见Precommit 没有带有效签的扩展就会当非法丢掉不是已经验过扩展

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyDiscard discard not already Verify-When / not already skip-Verify / not already verified 正式三事（514 余量）/ not 1325 vwdisc-notsig interchangeable / not 514 verifywhen-discard-vs-bundled bundled interchangeable」，不是 verifywhen discard vs bundled bundled（514），也不是已经 Verify When 正式流程（435），也不是已经 空扩展仍会调 Verify（353）。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方三件事

1. **看见Precommit 没有带有效签的扩展就会当非法丢掉 / 看见Precommit 没有带有效签的扩展就会当非法丢掉 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1325 vwdisc-notsig interchangeable / 1326 vwdisc-notzero interchangeable，也不是已经 VerifyDiscard discard not already Verify-When / not already skip-Verify / not already verified 正式三事 bundled（514 item 1 余量） interchangeable / 514 vwdisc item 1 interchangeable。**  
   官方把Precommit 没有带有效签的扩展就会当非法丢掉和已经 Verify When 正式流程 bundled写成两件。看见Precommit 没有带有效签的扩展就会当非法丢掉，不是已经 Verify When 正式流程 bundled。

2. **看见discards as invalid / 看见Precommit 没有带有效签的扩展就会当非法丢掉 / 这份对象 is not already 已经跳过 Verify interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1325 vwdisc-notsig interchangeable / 1327 vwdisc-notstep interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把discards as invalid和已经跳过 Verify写成两件。看见discards as invalid，不是已经跳过 Verify。

3. **看见Precommit 没有带有效签的扩展就会当非法丢掉 / 看见discards as invalid / 这份对象 is not already 已经验过扩展 interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1325 vwdisc-notsig interchangeable / 1326 vwdisc-notzero interchangeable，也不是已经 空扩展仍会调 Verify interchangeable / 353 空扩展仍会调 Verify interchangeable。**  
   官方把Precommit 没有带有效签的扩展就会当非法丢掉和已经验过扩展写成两件。看见Precommit 没有带有效签的扩展就会当非法丢掉，不是已经验过扩展。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方为什么这样拆

- **discards invalid Precommit 不是 Verify When 正式流程 bundled interchangeable：官方把 step 1 discard 单句和 steps 2–4 call/ACCEPT/REJECT bundled 分开。**
- **看见丢掉了 不是已经空扩展仍会调 Verify：353 钉 Usage 侧 0 长仍叫 Verify，本页钉 When step 1 无有效签先丢掉。**
- **看见没调 Verify 不是已经带有效签就会调 Verify：435 钉 step 2 call，本页钉 step 1 在 call 之前。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经跳过 Verify | 不是已经跳过 Verify | 不是已经空扩展仍会调 Verify（353） |
| 已经验过扩展 | 不是已经验过扩展 | 不是已经1326 vwdisc-notzero |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyDiscard discard not already Verify-When / not already skip-Verify / not already verified 正式三事（514 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经跳过 Verify、是不是已经验过扩展。可以跳过「看见收到 Precommit 就已经跳过 Verify interchangeable、已经验过扩展 interchangeable」。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。514 VerifyVoteExtension When discard bundled unbundling 在本页 item 1 启动；续 [`worked-example-vwdisc-notzero-vs-bundled.md`](worked-example-vwdisc-notzero-vs-bundled.md)（不变量 1326 item 2）。

## 本页不抄

- 怎样做验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
- 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
