# 例：看见 extensions after minimum +2/3 in commit info are not verified / Application MAY use commit info extensions to modify proposal / suggested validate same manner as VerifyVoteExtension 不是已经迟到扩展 bundled interchangeable / 已经 Verify 过 interchangeable / 已经是引擎会再 Verify interchangeable

**层次**：实现 / PrepareProposal When +2/3 late extensions not verified 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「+2/3 late extensions not verified / MAY use commit info extensions / suggested validate like Verify 不是迟到扩展 bundled interchangeable / 不是已经 Verify 过 interchangeable / 不是已经是引擎会再 Verify interchangeable」，不是迟到扩展 bundled（352），也不是 Verify When 正式流程（435 / 514–517）。不要另写怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

规范把 PrepareProposal When step 3 里 +2/3 之后扩展未 Verify、MAY 用 commit info 扩展改提案、建议按 Verify 同款逻辑再看写成三件独立的实现事，不是「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经是引擎会再 Verify interchangeable、已经又叫了 Verify interchangeable」一件事：

1. **看见 extensions of votes included in the commit info after the minimum of +2/3 had been reached are not verified / 看见 +2/3 之后才进来的扩展写进了 commit info 没有被 Verify 不是已经迟到扩展 bundled（352） interchangeable / 已经 Verify 过 interchangeable / 已经 Accept interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经 step 2 call bundled（515） interchangeable / 已经 ACCEPT keep for h+1 Prepare bundled（517） interchangeable，也不是已经 MAY add without calling Verify bundled（518） interchangeable / 已经又叫了 Verify interchangeable，也不是已经 last_commit 里有扩展 interchangeable / 已经写进 last_commit interchangeable。**  
   官方 PrepareProposal When step 3 脚注写：extensions of votes included in the commit info after the minimum of +2/3 had been reached are not verified。看见 not verified，不是已经迟到扩展（352） interchangeable——352 钉 bundled 三事，本页钉 +2/3 commit info 未 Verify 单句。看见写进了 commit info，不是已经 Verify 过 interchangeable——352 第一件事 bundled 常被写成「写进了就已经 Verify 过」，本页钉未 Verify 单句。看见 +2/3 之后，不是已经 Verify When 正常 When steps（514–517） interchangeable——正常 When 会 call Verify，本页钉 +2/3 之后这批没 Verify。
2. **看见 the Application MAY use the vote extensions in the commit info to modify the proposal / 看见 MAY 用 commit info 里的扩展改提案 不是已经迟到扩展 bundled（352） interchangeable / 已经 Verify 过 interchangeable，也不是已经 ExtendedCommitInfo 就已经进了块 interchangeable / 已经交差 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 已经从内存池删掉 interchangeable，也不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable / 已经 Verify 过 interchangeable，也不是已经 local_last_commit 是上一高度预提交带扩展 bundled（359） interchangeable / 已经本高度刚签的扩展 interchangeable。**  
   官方 PrepareProposal When step 3 写：the Application MAY use the vote extensions in the commit info to modify the proposal。看见 MAY use extensions，不是已经迟到扩展（352） interchangeable——352 钉 bundled 三事，本页钉 MAY 用 commit info 扩展改提案单句。看见改提案，不是已经 Verify 过 interchangeable——本页钉未 Verify 前提下 MAY 使用。看见 commit info 里的扩展，不是已经 ExtendedCommitInfo 就已经进了块 interchangeable——359/441 钉 Notes/Usage 异路，本页钉 Prepare 侧 MAY 使用单句。
3. **看见 it is suggested that extensions be validated in the same manner as done in `VerifyVoteExtension` / 看见建议按 Verify 同款逻辑再看一遍 不是已经迟到扩展 bundled（352 第二件事） interchangeable / 已经是引擎会再 Verify interchangeable，也不是已经 Verify When 正式流程 step 2 call bundled（515） interchangeable / 已经 CometBFT 会叫 interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable / 已经 Req 6 已经测过 interchangeable，也不是已经建议再看 interchangeable / 已经 Accept interchangeable，也不是已经 MAY add without calling Verify bundled（518） interchangeable / 已经又叫了 Verify interchangeable。**  
   官方 PrepareProposal When step 3 续：it is suggested that extensions be validated in the same manner as done in VerifyVoteExtension。看见 suggested validate like Verify，不是已经迟到扩展（352 第二件事） interchangeable——352 钉「建议再看不是引擎会再 Verify」，本页钉 suggested validate 单句。看见建议再看，不是已经 Verify When step 2 call（515） interchangeable——515 钉引擎会 call Verify，本页钉 Prepare 侧应用建议自验。看见 same manner as VerifyVoteExtension，不是已经 Req 6 必须 Accept（348） interchangeable——348 钉必须 Accept，本页钉 suggested 不是 must。

怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。迟到扩展 bundled（352）、Verify When 正式流程（435 / 514–517）、MAY add without Verify（518）是另外那套，本页不抄。

## 官方为什么这样拆

- **+2/3 commit info extensions not verified ≠ 迟到扩展 bundled interchangeable：** 官方把 not verified 单句和 MAY add without Verify / 建议再看 bundled 分开。
- **MAY use commit info extensions to modify proposal ≠ 已经 Verify 过 interchangeable：** 官方把 MAY 使用和已经 Verify 分开。
- **suggested validate like VerifyVoteExtension ≠ 已经是引擎会再 Verify interchangeable：** 官方把应用建议自验和引擎会再 call Verify 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| +2/3 commit info extensions not verified | 不是 352 bundled | 不是 normal Verify When（514–517） |
| MAY use commit info extensions to modify proposal | 不是 already verified | 不是 already in block |
| suggested validate like VerifyVoteExtension | 不是 engine will re-Verify | 不是 Req 6 must Accept（348） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When +2/3 late extensions not verified 正式三事，必须分开 +2/3 commit info extensions not verified 是不是迟到扩展 bundled interchangeable / 已经 Verify 过 interchangeable、MAY use commit info extensions 是不是已经 Verify 过 interchangeable / 已经进了块 interchangeable、suggested validate like Verify 是不是已经是引擎会再 Verify interchangeable / 已经 Accept interchangeable。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable」。519 PrepareProposal When lateext-unverified bundled unbundling 完成（1319 item 1 / 1320 item 2 / 1321 item 3）；精读 [`worked-example-whenlate-notver-vs-bundled.md`](worked-example-whenlate-notver-vs-bundled.md)（不变量 1319 item 1）、[`worked-example-whenlate-notuse-vs-bundled.md`](worked-example-whenlate-notuse-vs-bundled.md)（不变量 1320 item 2）、[`worked-example-whenlate-notsug-vs-bundled.md`](worked-example-whenlate-notsug-vs-bundled.md)（不变量 1321 item 3）。不要另写怎样再验迟到扩展。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 下一高度 round 0 MAY add without Verify / 建议再看不是引擎会再 Verify bundled。那是不变量 352 / 518。
- Verify When 正式流程 / step 2 call / ACCEPT keep。那是不变量 435 / 515 / 517。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
