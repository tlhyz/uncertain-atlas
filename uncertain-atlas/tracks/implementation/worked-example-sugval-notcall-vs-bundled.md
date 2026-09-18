# 例：看见按 Verify 同款逻辑自验不是已经 Verify When step 2 call bundled；看见same manner as VerifyVoteExtension不是已经 CometBFT 会叫；看见按 Verify 同款逻辑自验不是已经 VerifyVoteExtension MUST be deterministic

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「SuggestValidate same-manner not already step-2-call / not already Verify-When / not already MUST-det 正式三事（520 余量）/ not 1317 sugval-notcall interchangeable / not 520 preparewhen-suggestvalidate-vs-bundled bundled interchangeable」，不是 preparewhen suggestvalidate vs bundled bundled（520），也不是已经 Verify When step 2 call（515），也不是已经 Verify When bundled（435）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见按 Verify 同款逻辑自验 / 看见按 Verify 同款逻辑自验 这份对象 is not already 已经 Verify When step 2 call bundled interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1317 sugval-notcall interchangeable / 1316 sugval-notmust interchangeable，也不是已经 SuggestValidate same-manner not already step-2-call / not already Verify-When / not already MUST-det 正式三事 bundled（520 item 2 余量） interchangeable / 520 sugval item 2 interchangeable。**  
   官方把按 Verify 同款逻辑自验和已经 Verify When step 2 call bundled写成两件。看见按 Verify 同款逻辑自验，不是已经 Verify When step 2 call bundled。

2. **看见same manner as VerifyVoteExtension / 看见按 Verify 同款逻辑自验 / 这份对象 is not already 已经 CometBFT 会叫 interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1317 sugval-notcall interchangeable / 1318 sugval-notreverify interchangeable，也不是已经 Verify When step 2 call interchangeable / 515 Verify When step 2 call interchangeable。**  
   官方把same manner as VerifyVoteExtension和已经 CometBFT 会叫写成两件。看见same manner as VerifyVoteExtension，不是已经 CometBFT 会叫。

3. **看见按 Verify 同款逻辑自验 / 看见same manner as VerifyVoteExtension / 这份对象 is not already 已经 VerifyVoteExtension MUST be deterministic interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1317 sugval-notcall interchangeable / 1316 sugval-notmust interchangeable，也不是已经 Verify When bundled interchangeable / 435 Verify When bundled interchangeable。**  
   官方把按 Verify 同款逻辑自验和已经 VerifyVoteExtension MUST be deterministic写成两件。看见按 Verify 同款逻辑自验，不是已经 VerifyVoteExtension MUST be deterministic。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **same manner as VerifyVoteExtension 不是 step 2 call bundled interchangeable：官方把应用复用 Verify 逻辑和 CometBFT 再 call Verify 分开。**
- **看见按同款逻辑自验 不是已经 CometBFT 会叫：515 钉引擎 step 2 call，本页钉应用侧复用逻辑。**
- **看见 validated 不是已经 VerifyVoteExtension MUST be deterministic：那是不变量 433。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When step 2 call bundled | 不是已经 Verify When step 2 call bundled | 不是已经Verify When step 2 call（515） |
| 已经 CometBFT 会叫 | 不是已经 CometBFT 会叫 | 不是已经Verify When bundled（435） |
| 已经 VerifyVoteExtension MUST be deterministic | 不是已经 VerifyVoteExtension MUST be deterministic | 不是已经1316 sugval-notmust |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 SuggestValidate same-manner not already step-2-call / not already Verify-When / not already MUST-det 正式三事（520 余量），必须分开是不是已经 Verify When step 2 call bundled、是不是已经 CometBFT 会叫、是不是已经 VerifyVoteExtension MUST be deterministic。可以跳过「看见建议按 Verify 同款逻辑再看一遍就已经是引擎会再 Verify interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。520 PrepareProposal When suggestvalidate bundled unbundling 在本页 item 2 续；续 [`worked-example-sugval-notreverify-vs-bundled.md`](worked-example-sugval-notreverify-vs-bundled.md)（不变量 1318 item 3）。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
