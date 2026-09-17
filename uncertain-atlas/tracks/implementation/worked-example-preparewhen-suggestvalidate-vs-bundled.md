# 例：看见 it is suggested that extensions be validated / validated in the same manner as VerifyVoteExtension / not CometBFT calls VerifyVoteExtension again 不是已经迟到扩展 bundled interchangeable / 已经是引擎会再 Verify interchangeable / 已经 Accept interchangeable

**层次**：实现 / PrepareProposal When suggested validate like Verify 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「it is suggested / same manner as VerifyVoteExtension / not engine re-Verify 不是迟到扩展 bundled interchangeable / 不是已经是引擎会再 Verify interchangeable / 不是已经 Accept interchangeable」，不是迟到扩展 bundled（352 第二件事），也不是 +2/3 late extensions not verified 三事 bundled（519），也不是 Verify When step 2 call（515）。不要另写怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

规范把 PrepareProposal When step 3 里建议自验句拆成三件独立的实现事，不是「看见建议按 Verify 同款逻辑再看一遍就已经是引擎会再 Verify interchangeable、已经 Accept interchangeable、已经 Verify 过 interchangeable」一件事：

1. **看见 it is suggested that extensions be validated / 看见建议自验 不是已经迟到扩展 bundled（352 第二件事） interchangeable / 已经是引擎会再 Verify interchangeable / 已经 Accept interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable / 已经 Req 6 已经测过 interchangeable，也不是已经 Verify When 正式流程 step 3 return status bundled（516） interchangeable / 已经 Application returns ACCEPT interchangeable，也不是已经 +2/3 late extensions not verified bundled（519） interchangeable / 已经 MAY use commit info extensions interchangeable / 已经 suggested validate interchangeable，也不是已经 MUST 只依赖请求和上一份状态 bundled（433 Usage） interchangeable / 已经 SHOULD Accept interchangeable。**  
   官方 PrepareProposal When step 3 续写：it is suggested that extensions be validated。看见 suggested，不是 MUST——348 钉 Req 6 必须 Accept，本页钉 suggested 不是 must。看见建议自验，不是已经 Verify When step 3 return status（516） interchangeable——516 钉 When 侧 ACCEPT/REJECT return，本页钉 Prepare 侧 suggested 不是 return。看见 it is suggested，不是已经迟到扩展（352 第二件事） bundled interchangeable——352 把 MAY use + suggested + not engine re-Verify 捆在一起，本页钉 suggested 单句。
2. **看见 in the same manner as done in `VerifyVoteExtension` / 看见按 Verify 同款逻辑自验 不是已经迟到扩展 bundled（352 第二件事） interchangeable / 已经是引擎会再 Verify interchangeable，也不是已经 Verify When 正式流程 step 2 call bundled（515） interchangeable / 已经 CometBFT 会叫 interchangeable / 已经带有效签就会调 Verify interchangeable，也不是已经 VerifyVoteExtension MUST be deterministic bundled（433 Usage） interchangeable / 已经 status 必须只依赖请求和上一份状态 interchangeable，也不是已经 +2/3 late extensions not verified bundled（519 第三件事） interchangeable / 已经 suggested validate interchangeable / 已经 Accept interchangeable，也不是已经 MAY add without calling Verify bundled（518） interchangeable / 已经又叫了 Verify interchangeable。**  
   官方 PrepareProposal When step 3 续写：validated in the same manner as done in VerifyVoteExtension。看见 same manner as VerifyVoteExtension，不是 CometBFT 再 call VerifyVoteExtension——515 钉引擎 step 2 call，本页钉应用侧复用 Verify 逻辑、不是 ABCI 再叫。看见按同款逻辑自验，不是已经 Verify When 正式流程（435） interchangeable——435 钉 When 侧 call + return + keep/discard，本页钉 Prepare 侧应用自验。看见 validated，不是已经 Application returns ACCEPT（516） interchangeable——516 钉 When return status，本页钉 Prepare 侧 suggested 自验逻辑。
3. **看见 suggested validate is not CometBFT calling `VerifyVoteExtension` again / 看见建议自验不是引擎会再 Verify 不是已经迟到扩展 bundled（352 第二件事） interchangeable / 已经是引擎会再 Verify interchangeable / 已经又叫了 Verify interchangeable，也不是已经 Verify When 正式流程 step 2 call bundled（515） interchangeable / 已经 CometBFT 会叫 interchangeable，也不是已经 +2/3 commit info extensions not verified bundled（519 第一件事） interchangeable / 已经 Verify 过 interchangeable，也不是已经 MAY add without calling Verify bundled（518） interchangeable / 已经 without calling VerifyVoteExtension interchangeable，也不是已经 Verify 过迟到扩展 interchangeable / 已经写进 last_commit interchangeable。**  
   官方 PrepareProposal When step 3 把 suggested validate 和引擎再 call Verify 分开——352 第二件事 bundled 常被写成「建议再看就是引擎会再 Verify」，本页钉 not engine re-Verify 单句。看见建议自验，不是 step 2 call（515） interchangeable——515 钉 Else CometBFT calls VerifyVoteExtension，本页钉 Prepare 侧 suggested 不是 call。看见 not calling VerifyVoteExtension again，不是已经 Verify 过 interchangeable——519 第一件事钉 +2/3 未 Verify，本页钉 suggested 路径仍不是引擎再 call。

怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。迟到扩展 bundled（352）、+2/3 late extensions not verified（519）、Verify When step 2 call（515）是另外那套，本页不抄。

## 官方为什么这样拆

- **it is suggested ≠ 已经是引擎会再 Verify interchangeable：** 官方把 suggested 和 must / engine call 分开。
- **same manner as VerifyVoteExtension ≠ step 2 call bundled interchangeable：** 官方把应用复用 Verify 逻辑和 CometBFT 再 call Verify 分开。
- **not engine re-Verify ≠ 已经 Accept interchangeable：** 官方把建议自验和 When 侧 ACCEPT return / Req 6 must Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| it is suggested that extensions be validated | 不是 Req 6 must Accept（348） | 不是 When return ACCEPT（516） |
| same manner as VerifyVoteExtension | 不是 step 2 call（515） | 不是 Verify When bundled（435） |
| not CometBFT calling VerifyVoteExtension again | 不是 already verified | 不是 MAY add without Verify（518） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When suggested validate like Verify 正式三事，必须分开 it is suggested 是不是已经是引擎会再 Verify interchangeable / 已经 Accept interchangeable、same manner as VerifyVoteExtension 是不是 step 2 call bundled interchangeable / 已经 CometBFT 会叫 interchangeable、not engine re-Verify 是不是已经 Verify 过 interchangeable / 已经又叫了 Verify interchangeable。可以跳过「看见建议按 Verify 同款逻辑再看一遍就已经是引擎会再 Verify interchangeable」。不要另写怎样再验迟到扩展。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- +2/3 commit info extensions not verified / MAY use extensions。那是不变量 519。
- Verify When step 2 call / return status / ACCEPT keep。那是不变量 515 / 516 / 517。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
