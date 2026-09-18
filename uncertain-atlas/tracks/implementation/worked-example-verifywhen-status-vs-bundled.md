# 例：看见 Application returns ACCEPT or REJECT via VerifyVoteExtensionResponse.status / step 3 after call VerifyVoteExtension / step 3 before ACCEPT keep or REJECT discard 不是已经 Verify When 正式流程 interchangeable / 已经验过扩展 interchangeable / 已经写进 last_commit interchangeable

**层次**：实现 / VerifyVoteExtension When return status 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Application returns ACCEPT/REJECT / step 3 after call / step 3 before keep or discard 不是 Verify When 正式流程 interchangeable / 不是已经验过扩展 interchangeable / 不是已经写进 last_commit interchangeable」，不是 Verify When 正式流程（435），也不是 step 2 call（515），也不是 Verify 回包栏（433）。不要另写怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

规范把 VerifyVoteExtension When step 3 里应用回 status、接在 step 2 call 之后、在 step 4 keep/discard 之前写成三件独立的实现事，不是「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable、已经 REJECT 丢掉 Precommit interchangeable、已经写进 last_commit interchangeable」一件事：

1. **看见 The Application returns `ACCEPT` or `REJECT` via `VerifyVoteExtensionResponse.status` / 看见应用回 status 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经验过扩展 interchangeable / 已经 Accept interchangeable，也不是已经 step 2 call bundled（515） interchangeable / 已经 CometBFT 会叫 interchangeable，也不是已经 VerifyVoteExtensionResponse.status bundled（433） interchangeable / 已经当成块非法 interchangeable / 已经 MUST 只依赖请求和上一份状态 interchangeable，也不是已经 Precommit 没有带有效签的扩展就会当非法丢掉 bundled（435 第一件事） interchangeable / 已经跳过 Verify interchangeable。**  
   官方 When step 3 写：The Application returns `ACCEPT` or `REJECT` via `VerifyVoteExtensionResponse.status`。看见 returns status，不是已经 Verify When 正式流程（435） interchangeable——435 钉 steps 1–4 bundled，本页钉 step 3 return 单句。看见回了 ACCEPT/REJECT，不是已经验过扩展 interchangeable——515 钉 step 2 call 在 return 之前，本页钉 step 3 return 单句。看见 Application returns，不是已经 Verify 回包栏（433） interchangeable——433 钉 Response 表上 status 语义 / MUST 只依赖 / SHOULD Accept，本页钉 When step 3 return 单句。
2. **看见 step 3 after _p_'s CometBFT calls `VerifyVoteExtension` (step 2) / 看见 step 3 在 call VerifyVoteExtension 之后 不是已经 step 2 call bundled（515） interchangeable / 已经 CometBFT 会叫 interchangeable，也不是已经 step 1 discard bundled（514） interchangeable / 已经跳过 Verify interchangeable，也不是已经空扩展仍会调 Verify bundled（353） interchangeable / 已经 0 长就不叫 Verify interchangeable，也不是已经 round 0 height h MAY add without calling Verify（352） interchangeable / 已经迟到扩展已经 Verify 过 interchangeable。**  
   官方 When 把 step 3 接在 step 2 之后。看见 step 3 在 call 之后，不是已经 step 2 call（515） interchangeable——515 钉 step 2 call 单句，本页钉 step 3 在 call 之后。看见 Application returns，不是已经 step 1 discard（514） interchangeable——514 钉 step 1 无有效签先丢掉，本页钉 step 3 在 call 之后 return。看见回了 status，不是已经迟到扩展 MAY 不加 Verify（352） interchangeable——352 钉迟到扩展 MAY 路径，本页钉正常 When step 3 return。
3. **看见 step 3 before If the Application returns ACCEPT keep vote / REJECT discard Precommit (step 4) / 看见 step 3 在 keep 或 discard 之前 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经写进 last_commit interchangeable，也不是已经 ACCEPT 留给 h+1 Prepare bundled（435 step 4） interchangeable / 已经 REJECT 丢掉 Precommit interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info（352） interchangeable / 已经 Verify 过 interchangeable，也不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法 bundled（433） interchangeable / 已经 Process REJECT prevote nil interchangeable。**  
   官方 When 把 step 3 和 step 4 分开。看见 step 3 在 keep/discard 之前，不是已经 Verify When 正式流程（435） interchangeable——435 钉 bundled 四步，本页钉 step 3 return 单句。看见回了 status，不是已经 ACCEPT 留给 h+1 Prepare（435 step 4） interchangeable——435 钉 step 4 后效，本页钉 step 3 在 keep/discard 之前。看见 Application returns，不是已经 REJECT 丢掉 Precommit（435 step 4 bundled） interchangeable——435 钉 step 4 discard，本页钉 step 3 return 单句。

怎样做写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo 是规范里的做法，本页不抄。Verify When 正式流程（435）、step 2 call（515）、Verify 回包栏（433）、迟到扩展 MAY 不加 Verify（352）是另外那套，本页不抄。

## 官方为什么这样拆

- **Application returns ACCEPT/REJECT ≠ Verify When 正式流程 bundled interchangeable：** 官方把 step 3 return 单句和 steps 1/2/4 bundled 分开。
- **step 3 after call VerifyVoteExtension ≠ step 2 call bundled interchangeable：** 官方把 step 3 return 和 step 2 call 分开。
- **step 3 before keep/discard ≠ 已经写进 last_commit interchangeable：** 官方把 step 3 return 和 step 4 ACCEPT/REJECT 后效分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Application returns ACCEPT/REJECT via status | 不是 Verify When bundled（435） | 不是 Verify 回包栏 bundled（433） |
| step 3 after call VerifyVoteExtension | 不是 step 2 call（515） | 不是 step 1 discard（514） |
| step 3 before keep/discard | 不是 already last_commit | 不是 ACCEPT/REJECT post-effects bundled（435） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When return status 正式三事，必须分开 Application returns ACCEPT/REJECT 是不是 Verify When 正式流程 bundled interchangeable / 已经 Accept interchangeable、step 3 after call 是不是 step 2 call bundled interchangeable、step 3 before keep/discard 是不是已经写进 last_commit interchangeable / 已经 REJECT 丢掉 Precommit interchangeable。可以跳过「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable、已经 REJECT 丢掉 Precommit interchangeable」。516 VerifyVoteExtension When status bundled unbundling 完成（1331 item 1 / 1332 item 2 / 1333 item 3）；精读 [`worked-example-vwstat-notret-vs-bundled.md`](worked-example-vwstat-notret-vs-bundled.md)（不变量 1331 item 1）、[`worked-example-vwstat-notafter-vs-bundled.md`](worked-example-vwstat-notafter-vs-bundled.md)（不变量 1332 item 2）、[`worked-example-vwstat-notkeep-vs-bundled.md`](worked-example-vwstat-notkeep-vs-bundled.md)（不变量 1333 item 3）。不要另写怎样写 Verify 回包栏。

## 本页不抄

- 怎样做写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- Verify When 正式流程 / ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit。那是不变量 435。
- step 2 call VerifyVoteExtension。那是不变量 515。
- VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 / MUST 只依赖 / SHOULD Accept。那是不变量 433。
- 迟到扩展 MAY 不加 Verify 就已经 Verify 过。那是不变量 352。
