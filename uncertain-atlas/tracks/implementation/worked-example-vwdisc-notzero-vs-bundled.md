# 例：看见0 长扩展只要伴随签名也合法就算有效不是已经空扩展仍会调 Verify bundled；看见0-length with valid signature不是已经跳过 Verify；看见0 长扩展只要伴随签名也合法就算有效不是已经 0 长就不合法

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyDiscard zerolen not already still-calls-Verify / not already skip / not already 0-len-illegal 正式三事（514 余量）/ not 1326 vwdisc-notzero interchangeable / not 514 verifywhen-discard-vs-bundled bundled interchangeable」，不是 verifywhen discard vs bundled bundled（514），也不是已经 空扩展仍会调 Verify（353），也不是已经 ExtendVote 0 长（437）。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方三件事

1. **看见0 长扩展只要伴随签名也合法就算有效 / 看见0 长扩展只要伴随签名也合法就算有效 这份对象 is not already 已经空扩展仍会调 Verify bundled interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1326 vwdisc-notzero interchangeable / 1325 vwdisc-notsig interchangeable，也不是已经 VerifyDiscard zerolen not already still-calls-Verify / not already skip / not already 0-len-illegal 正式三事 bundled（514 item 2 余量） interchangeable / 514 vwdisc item 2 interchangeable。**  
   官方把0 长扩展只要伴随签名也合法就算有效和已经空扩展仍会调 Verify bundled写成两件。看见0 长扩展只要伴随签名也合法就算有效，不是已经空扩展仍会调 Verify bundled。

2. **看见0-length with valid signature / 看见0 长扩展只要伴随签名也合法就算有效 / 这份对象 is not already 已经跳过 Verify interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1326 vwdisc-notzero interchangeable / 1327 vwdisc-notstep interchangeable，也不是已经 空扩展仍会调 Verify interchangeable / 353 空扩展仍会调 Verify interchangeable。**  
   官方把0-length with valid signature和已经跳过 Verify写成两件。看见0-length with valid signature，不是已经跳过 Verify。

3. **看见0 长扩展只要伴随签名也合法就算有效 / 看见0-length with valid signature / 这份对象 is not already 已经 0 长就不合法 interchangeable，也不是已经 verifywhen discard vs bundled bundled（514） interchangeable / 1326 vwdisc-notzero interchangeable / 1325 vwdisc-notsig interchangeable，也不是已经 ExtendVote 0 长 interchangeable / 437 ExtendVote 0 长 interchangeable。**  
   官方把0 长扩展只要伴随签名也合法就算有效和已经 0 长就不合法写成两件。看见0 长扩展只要伴随签名也合法就算有效，不是已经 0 长就不合法。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方为什么这样拆

- **0-length with valid signature 不是空扩展仍会调 Verify bundled interchangeable：官方把 When step 1 0 长有效性单句和 Usage 侧仍叫 Verify 分开。**
- **看见 0 长 不是已经 0 长就不合法：本页钉 0 长看伴随签。**
- **看见有效 不是已经 ExtendVote 侧应用可以选 0 长：437 钉 ExtendVote Usage nil 路径，本页钉 Verify When 收到侧 0 长有效性。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经空扩展仍会调 Verify bundled | 不是已经空扩展仍会调 Verify bundled | 不是已经空扩展仍会调 Verify（353） |
| 已经跳过 Verify | 不是已经跳过 Verify | 不是已经ExtendVote 0 长（437） |
| 已经 0 长就不合法 | 不是已经 0 长就不合法 | 不是已经1325 vwdisc-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyDiscard zerolen not already still-calls-Verify / not already skip / not already 0-len-illegal 正式三事（514 余量），必须分开是不是已经空扩展仍会调 Verify bundled、是不是已经跳过 Verify、是不是已经 0 长就不合法。可以跳过「看见收到 Precommit 就已经跳过 Verify interchangeable、已经验过扩展 interchangeable」。不要另写 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。514 VerifyVoteExtension When discard bundled unbundling 在本页 item 2 续；续 [`worked-example-vwdisc-notstep-vs-bundled.md`](worked-example-vwdisc-notstep-vs-bundled.md)（不变量 1327 item 3）。

## 本页不抄

- 怎样做验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
- 怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
