# 例：看见 Else CometBFT calls VerifyVoteExtension / received from q≠p / step 2 before Application returns ACCEPT or REJECT 不是已经 Verify When 正式流程 interchangeable / 已经验过扩展 interchangeable / 已经 Accept interchangeable

**层次**：实现 / VerifyVoteExtension When call VerifyVoteExtension 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「calls VerifyVoteExtension / received from q≠p / step 2 before status return 不是 Verify When 正式流程 interchangeable / 不是已经验过扩展 interchangeable / 不是已经 Accept interchangeable」，不是 Verify When 正式流程（435），也不是 step 1 discard（514），也不是 Verify 回包 status（433）。不要另写怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

规范把 VerifyVoteExtension When step 2 里 Else 分支调 Verify、收到他人 Precommit、在应用回 status 之前写成三件独立的实现事，不是「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable、已经 Accept interchangeable、已经写进 last_commit interchangeable」一件事：

1. **看见 Else, _p_'s CometBFT calls `VerifyVoteExtension` / 看见带有效签就会调 VerifyVoteExtension 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经验过扩展 interchangeable / 已经 Accept interchangeable，也不是已经 step 1 discard bundled（514） interchangeable / 已经跳过 Verify interchangeable，也不是已经空扩展仍会调 Verify bundled（353） interchangeable / 已经 0 长就不叫 Verify interchangeable，也不是已经 Precommit 没有带有效签的扩展就会当非法丢掉 bundled（435 第一件事） interchangeable / 已经带有效签就会调 Verify bundled interchangeable。**  
   官方 When step 2 写：Else, _p_'s CometBFT calls `VerifyVoteExtension`。看见 calls VerifyVoteExtension，不是已经 Verify When 正式流程（435） interchangeable——435 钉 steps 1–4 bundled，本页钉 step 2 call 单句。看见 CometBFT 会调，不是已经验过扩展 interchangeable——435 第二件事 bundled 常被写成「会叫就是已经验过」，本页钉 step 2 只是 call。看见调了，不是已经 Accept（433 / 434） interchangeable——433 钉 step 3 return status，本页钉 step 2 在 return 之前。看见 Else，不是已经 step 1 discard（514） interchangeable——514 钉 step 1 无有效签先丢掉，本页钉 step 1 通过后才会 call。
2. **看见 When a node _p_ receives a Precommit message for round _r_, height _h_ from validator _q_ (_q_ ≠ _p_) / 看见收到他人 Precommit 不是已经 Verify 不对 local process 发出的 Precommit 调用 bundled（353 Usage） interchangeable / 已经本地票也 Verify interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable，也不是已经 round 0 height h MAY add without calling Verify（352） interchangeable / 已经迟到扩展已经 Verify 过 interchangeable，也不是已经 VerifyVoteExtensionRequest.hash 不保证跑过 Process bundled（353 Usage） interchangeable / 已经对该块跑过 Process interchangeable。**  
   官方 When 前提写：When a node _p_ is in consensus round _r_, height _h_, and _p_ receives a Precommit message for round _r_, height _h_ from validator _q_ (_q_ ≠ _p_)。看见收到他人票，不是已经 Verify 不对本进程自己发出的 Precommit 调用（353 Usage） interchangeable——353 钉 Usage 侧本地票不调，本页钉 When step 2 收到侧 call 单句。看见 _q_ ≠ _p_，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉本地 ExtendVote 路径，本页钉收到他人 Precommit 后 call Verify。看见 round _r_ height _h_，不是已经 round 0 height h MAY add without calling Verify（352） interchangeable——352 钉迟到扩展 MAY 路径，本页钉正常 When step 2 call。
3. **看见 step 2 before The Application returns `ACCEPT` or `REJECT` via `VerifyVoteExtensionResponse.status` (step 3) / 看见 step 2 在应用回 status 之前 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经写进 last_commit interchangeable，也不是已经 VerifyVoteExtensionResponse.status bundled（433） interchangeable / 已经 REJECT 丢掉 Precommit interchangeable / 已经当成块非法 interchangeable，也不是已经 ACCEPT 留给 h+1 Prepare bundled（435 step 4） interchangeable / 已经 Verify 过迟到扩展 interchangeable，也不是已经 VerifyVoteExtension MUST be deterministic bundled（433 Usage） interchangeable / 已经 status 必须只依赖请求和上一份状态 interchangeable。**  
   官方 When 把 step 2 和 step 3 分开。看见 step 2 在 return 之前，不是已经 Verify When 正式流程（435） interchangeable——435 钉 bundled 四步，本页钉 step 2 call 单句。看见 CometBFT 会调，不是已经 Application returns ACCEPT/REJECT（435 step 3–4） interchangeable——435 钉 step 3–4 后效，本页钉 step 2 在 return 之前。看见 call 了，不是已经 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法（433） interchangeable——433 钉回包栏，本页钉 When step 2 call 单句。

怎样做填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo 是规范里的做法，本页不抄。Verify When 正式流程（435）、step 1 discard（514）、Verify 回包 status（433）、迟到扩展 MAY 不加 Verify（352）是另外那套，本页不抄。

## 官方为什么这样拆

- **calls VerifyVoteExtension ≠ Verify When 正式流程 bundled interchangeable：** 官方把 step 2 call 单句和 steps 1/3/4 bundled 分开。
- **received from q≠p ≠ 不对 local process 调用 bundled interchangeable：** 官方把 When step 2 收到侧 call 和 Usage 侧本地票不调分开。
- **step 2 before status return ≠ 已经验过扩展 interchangeable：** 官方把 step 2 call 和 step 3 ACCEPT/REJECT return 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| calls VerifyVoteExtension after step 1 else | 不是 Verify When bundled（435） | 不是 step 1 discard（514） |
| received Precommit from q≠p | 不是 local process also Verify | 不是 late extension MAY skip Verify（352） |
| step 2 before status return | 不是 already Accept | 不是 ACCEPT/REJECT bundled（435） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When call VerifyVoteExtension 正式三事，必须分开 calls VerifyVoteExtension 是不是 Verify When 正式流程 bundled interchangeable / 已经验过扩展 interchangeable、received from q≠p 是不是不对 local process 调用 bundled interchangeable / 已经本地票也 Verify interchangeable、step 2 before status return 是不是已经 Accept interchangeable / 已经写进 last_commit interchangeable。可以跳过「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable、已经 Accept interchangeable」。不要另写怎样填 VerifyVoteExtensionRequest。

## 本页不抄

- 怎样做填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- Verify When 正式流程 / ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit。那是不变量 435。
- step 1 discard invalid extension。那是不变量 514。
- VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法。那是不变量 433。
- 迟到扩展 MAY 不加 Verify 就已经 Verify 过。那是不变量 352。
