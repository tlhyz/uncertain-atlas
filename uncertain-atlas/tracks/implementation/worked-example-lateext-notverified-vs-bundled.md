# 例：看见写进了 last_commit / 看见有扩展 / 看见凑齐了 +2/3 is not already already verified interchangeable / already accept interchangeable / already later-verified interchangeable

**层次**：实现 / +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量）/ not 809 lateext-notverified interchangeable / not 352 lateext bundled interchangeable」，不是迟到扩展 bundled（352），也不是建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify（810 item 2 余量）或下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify（811 item 3 余量）。不要另写怎样再验迟到扩展。

## 官方三件事

规范把 Methods 里 commit info 中过了最低 +2/3 之后才加进来的扩展**没有**被 Verify 和「已经是写进了 last_commit 就已经 Verify 过 interchangeable / 已经是有扩展就已经 Accept interchangeable / 已经是凑齐了 +2/3 就已经后来的也验过 interchangeable / 已经是 lateext bundled interchangeable」分开写成三件独立的实现事，不是「看见写进了 last_commit 就已经 Verify 过 interchangeable / 就已经 Accept interchangeable / 就已经后来的也验过 interchangeable」一件事：

1. **看见 +2/3 之后才进来的扩展写进了 commit info / 看见写进了 last_commit / 看见 last_commit 里有扩展 is not already 已经 Verify 过 interchangeable / 已经 verified interchangeable / 已经 Verify 交差 interchangeable / 352 lateext bundled interchangeable / 34 vote-extension-block interchangeable / lateext-sold-as-verified interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 809 lateext-notverified interchangeable / 352 lateext item 1 interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事 bundled（352 item 1 余量） interchangeable / 352 lateext item 1 interchangeable，也不是已经是引擎会再 Verify（810） interchangeable / 811 lateext-notrecall interchangeable / 348 req6coherence interchangeable，也不是已经验签拒收整张预提交就已经是块非法（34） interchangeable。**  
   官方写：commit info 里，过了最低 +2/3 之后才加进来的那些票上的扩展，**没有**被 Verify。看见写进了 last_commit，不是已经 Verify 过。看见写进了 last_commit，不是已经 verified interchangeable——352 钉 bundled 三事，本页从 item 1 侧钉 not already verified 单句。看见 +2/3 之后才进来的扩展写进了 commit info，不是已经迟到扩展 bundled（352） interchangeable——352 钉 bundled，本页钉 item 1 第一件事。看见写进了 last_commit，不是已经是引擎会再 Verify（810） interchangeable——810 另钉 item 2。看见写进了 last_commit，不是已经验签拒收整张预提交就已经是块非法（34） interchangeable——34 另钉。352 lateext vs verified bundled unbundling 在本页 item 1 启动。

2. **看见有扩展 / 看见票上带了扩展 / 看见扩展字节在 is not already 已经 Accept interchangeable / 已经 accept interchangeable / 已经 Accept 交差 interchangeable / 352 lateext bundled interchangeable / 348 req6coherence interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 809 lateext-notverified interchangeable / 352 lateext item 2 建议再看 interchangeable / 352 lateext item 3 写进 interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事 bundled（352 item 1 余量） interchangeable / 352 lateext item 1 interchangeable，也不是已经 Verify 过（本页第一件事） interchangeable。**  
   官方写：看见有扩展，不是已经 Accept。看见票上带了扩展，不是已经 accept interchangeable——本页钉 not already accept 单句。看见扩展字节在，不是已经 Verify 过（本页第一件事） interchangeable——三件事分开钉。352 lateext vs verified bundled unbundling 在本页 item 1 启动。

3. **看见凑齐了 +2/3 / 看见过了最低 +2/3 / 看见最低门槛到了 is not already 已经后来的也验过 interchangeable / 已经 later-verified interchangeable / 已经后来验过交差 interchangeable / 352 lateext bundled interchangeable / 330 veheight interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 809 lateext-notverified interchangeable / 352 lateext item 2 / 352 lateext item 3，也不是已经 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事 bundled（352 item 1 余量） interchangeable / 352 lateext item 1 interchangeable，也不是已经 Verify 过（本页第一件事） interchangeable / 已经 Accept（本页第二件事） interchangeable。**  
   官方写：看见凑齐了 +2/3，不是后来的也已经验过。看见过了最低 +2/3，不是已经 later-verified interchangeable——本页钉 not already later-verified 单句。看见最低门槛到了，不是已经 Accept（本页第二件事） interchangeable——三件事分开钉。352 lateext vs verified bundled unbundling 在本页 item 1 启动。

怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。迟到扩展 bundled（352）、建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify（352 item 2 余量 / 810）、下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify（352 item 3 余量 / 811）、验签拒收整张预提交就已经是块非法（34）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、到了 H 已经 Prepare 带了扩展（330）是另外那套，本页不抄。

## 官方为什么这样拆

- **写进了 last_commit not already verified ≠ 352 / 34 interchangeable：** 官方把写进 commit info 和已经 Verify 过分开。
- **有扩展 not already accept ≠ 已经 Accept interchangeable：** 官方把有扩展和已经 Accept 分开。
- **凑齐了 +2/3 not already later-verified ≠ 已经后来的也验过 interchangeable：** 官方把凑齐了 +2/3 和后来的也已经验过分开；352 lateext vs verified bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写进了 last_commit | 不是 already verified | 不是验签拒收整张预提交就已经是块非法 alone（34） |
| 有扩展 | 不是 already accept | 不是正确进程交出的扩展必须被正确接收者 Verify Accept alone（348） |
| 凑齐了 +2/3 | 不是 already later-verified | 不是建议再看 already engine-reverify alone（810） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量），必须分开写进了 last_commit 是不是 already verified interchangeable / 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable、有扩展 是不是 already accept interchangeable、凑齐了 +2/3 是不是 already later-verified interchangeable。可以跳过「看见写进了 last_commit 就已经 Verify 过 interchangeable / 就已经 Accept interchangeable / 就已经后来的也验过 interchangeable」。不要另写怎样再验迟到扩展。352 lateext vs verified bundled unbundling 在本页 item 1 启动；完成 [`worked-example-lateext-notreverify-vs-bundled.md`](worked-example-lateext-notreverify-vs-bundled.md)（不变量 810 item 2）；完成 [`worked-example-lateext-notrecall-vs-bundled.md`](worked-example-lateext-notrecall-vs-bundled.md)（不变量 811 item 3）。

## 本页不抄

- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 迟到扩展 bundled。那是不变量 352。
- 建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify。那是不变量 352 item 2 余量 / 810。
- 下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify。那是不变量 352 item 3 余量 / 811。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
