# 例：看见建议再看 / 看见 Prepare 在用扩展 / 看见能改提案 is not already already engine-reverify interchangeable / already req6-done interchangeable / already settled interchangeable

**层次**：实现 / 建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量）/ not 810 lateext-notreverify interchangeable / not 352 lateext bundled interchangeable」，不是迟到扩展 bundled（352），也不是 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过（809 item 1 余量）或下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify（811 item 3 余量）。不要另写怎样再验迟到扩展。

## 官方三件事

规范把 Methods 里应用 MAY 用 commit info 里的扩展改提案、建议按 Verify 同款逻辑再看一遍 和「已经是建议再看就已经是引擎会再 Verify interchangeable / 已经是 Prepare 在用扩展就已经过了 Req 6 interchangeable / 已经是能改提案就已经交差 interchangeable / 已经是 lateext bundled interchangeable」分开写成三件独立的实现事，不是「看见建议再看就已经是引擎会再 Verify interchangeable / 就已经过了 Req 6 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见建议按 `VerifyVoteExtension` 同款逻辑再看一遍 / 看见建议再看 / 看见同款逻辑再看 is not already 已经是引擎会再 Verify interchangeable / 已经 engine-reverify interchangeable / 已经引擎再 Verify 交差 interchangeable / 352 lateext bundled interchangeable / 348 req6coherence interchangeable / lateext-sold-as-verified interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 810 lateext-notreverify interchangeable / 352 lateext item 2 interchangeable，也不是已经建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事 bundled（352 item 2 余量） interchangeable / 352 lateext item 2 interchangeable，也不是已经 Verify 过（809） interchangeable / 811 lateext-notrecall interchangeable / 34 vote-extension-block interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable。**  
   官方写：应用 MAY 用 commit info 里的扩展改提案；这时建议按 Verify 同款逻辑再看一遍。看见建议再看，不是引擎已经再叫了 Verify。看见建议再看，不是已经 engine-reverify interchangeable——352 钉 bundled 三事，本页从 item 2 侧钉 not already engine-reverify 单句。看见建议按 Verify 同款逻辑再看一遍，不是已经迟到扩展 bundled（352） interchangeable——352 钉 bundled，本页钉 item 2 第一件事。看见建议再看，不是已经 Verify 过（809） interchangeable——809 另钉 item 1。看见建议再看，不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable——348 另钉。352 lateext vs verified bundled unbundling 在本页 item 2 续。

2. **看见 Prepare 在用扩展 / 看见 Prepare 要用这些扩展改提案 / 看见用扩展改提案 is not already 已经过了 Req 6 interchangeable / 已经 req6-done interchangeable / 已经 Req 6 交差 interchangeable / 352 lateext bundled interchangeable / 348 req6coherence interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 810 lateext-notreverify interchangeable / 352 lateext item 1 写进 interchangeable / 352 lateext item 3 写进 interchangeable，也不是已经建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事 bundled（352 item 2 余量） interchangeable / 352 lateext item 2 interchangeable，也不是已经是引擎会再 Verify（本页第一件事） interchangeable。**  
   官方写：看见 Prepare 在用扩展，不是已经过了 Req 6。看见 Prepare 要用这些扩展改提案，不是已经 req6-done interchangeable——本页钉 not already req6-done 单句。看见用扩展改提案，不是已经是引擎会再 Verify（本页第一件事） interchangeable——三件事分开钉。352 lateext vs verified bundled unbundling 在本页 item 2 续。

3. **看见能改提案 / 看见 MAY 用扩展改提案 / 看见可以改提案 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 352 lateext bundled interchangeable / 330 veheight interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 810 lateext-notreverify interchangeable / 352 lateext item 1 / 352 lateext item 3，也不是已经建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事 bundled（352 item 2 余量） interchangeable / 352 lateext item 2 interchangeable，也不是已经是引擎会再 Verify（本页第一件事） interchangeable / 已经过了 Req 6（本页第二件事） interchangeable。**  
   官方写：看见能改提案，不是已经交差。看见 MAY 用扩展改提案，不是已经 settled interchangeable——本页钉 not already settled 单句。看见可以改提案，不是已经过了 Req 6（本页第二件事） interchangeable——三件事分开钉。352 lateext vs verified bundled unbundling 在本页 item 2 续。

怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。迟到扩展 bundled（352）、+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过（352 item 1 余量 / 809）、下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify（352 item 3 余量 / 811）、验签拒收整张预提交就已经是块非法（34）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、到了 H 已经 Prepare 带了扩展（330）是另外那套，本页不抄。

## 官方为什么这样拆

- **建议再看 not already engine-reverify ≠ 352 / 348 interchangeable：** 官方把建议再看和引擎会再叫 Verify 分开。
- **Prepare 在用扩展 not already req6-done ≠ 已经过了 Req 6 interchangeable：** 官方把 Prepare 在用扩展和已经过了 Req 6 分开。
- **能改提案 not already settled ≠ 已经交差 interchangeable：** 官方把能改提案和已经交差分开；352 lateext vs verified bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 建议再看 | 不是 already engine-reverify | 不是正确进程交出的扩展必须被正确接收者 Verify Accept alone（348） |
| Prepare 在用扩展 | 不是 already req6-done | 不是写进了 last_commit already verified alone（809） |
| 能改提案 | 不是 already settled | 不是写进 ExtendedCommitInfo already called-again alone（811） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量），必须分开建议再看 是不是 already engine-reverify interchangeable / 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable、Prepare 在用扩展 是不是 already req6-done interchangeable、能改提案 是不是 already settled interchangeable。可以跳过「看见建议再看就已经是引擎会再 Verify interchangeable / 就已经过了 Req 6 interchangeable / 就已经交差 interchangeable」。不要另写怎样再验迟到扩展。352 lateext vs verified bundled unbundling 在本页 item 2 续（809 + 810）；续 [`worked-example-lateext-notrecall-vs-bundled.md`](worked-example-lateext-notrecall-vs-bundled.md)（不变量 811 item 3）；完成见 811。

## 本页不抄

- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 迟到扩展 bundled。那是不变量 352。
- +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过。那是不变量 352 item 1 余量 / 809。
- 下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify。那是不变量 352 item 3 余量 / 811。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
