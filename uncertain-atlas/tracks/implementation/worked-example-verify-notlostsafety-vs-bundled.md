# 例：看见活性会被伤 / 看见没有现成解法 / 看见 SHOULD Accept is not already already lost-safety interchangeable / already has-patch interchangeable / already must-reject interchangeable

**层次**：实现 / Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量）/ not 778 verify-notlostsafety interchangeable / not 341 verifydet bundled interchangeable」，不是 VerifyVoteExtension 确定性 bundled（341），也不是 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值（776 item 1 余量）或两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决（777 item 2 余量）。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

规范把 Requirements 里 Verify 非确定 bug、活性会被伤、两边都要小心 和「已经是活性会被伤就已经丢了安全性 interchangeable / 已经是要小心就已经有引擎补丁 interchangeable / 已经是 SHOULD Accept 就必须拒坏扩展 interchangeable / 已经是 verifydet bundled interchangeable」分开写成三件独立的实现事，不是「看见活性会被伤就已经丢了安全性 interchangeable / 就已经有补丁 interchangeable / 就必须拒坏扩展 interchangeable」一件事：

1. **看见活性会被伤 / 看见 Verify 里有非确定 bug / 看见打中的进程无法守 Req 7 或 8 is not already 已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable / 341 verifydet bundled interchangeable / 340 processdet interchangeable / verifydet-sold-as-extend interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 778 verify-notlostsafety interchangeable / 341 verifydet item 3 interchangeable，也不是已经 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事 bundled（341 item 3 余量） interchangeable / 341 verifydet item 3 interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值（776） interchangeable / 777 verify-nothonestonly interchangeable / 34 vote-extension interchangeable，也不是已经 Process 非确定 bug 没有现成解法（340） interchangeable。**  
   官方写：Verify 若有 bug 让 Accept/Reject 不再确定，就会违反 Requirement 7 或 8。这时**活性会被伤**。看见活性会被伤，不是已经丢了安全性。看见活性会被伤，不是已经 lost-safety interchangeable——341 钉 bundled 三事，本页从 item 3 侧钉 not already lost-safety 单句。看见 Verify 里有非确定 bug，不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable——341 钉 bundled，本页钉 item 3 第一件事。看见活性会被伤，不是已经 Process 非确定 bug 没有现成解法（340） interchangeable——340 另钉。341 verifydet vs extend bundled unbundling 在本页 item 3 完成。

2. **看见没有现成解法 / 看见实现 ExtendVote 和 VerifyVoteExtension 必须非常小心 / 看见没有协议层补丁 is not already 已经有引擎补丁 interchangeable / 已经 has-patch interchangeable / 已经有补丁交差 interchangeable / 341 verifydet bundled interchangeable / 34 vote-extension interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 778 verify-notlostsafety interchangeable / 341 verifydet item 1 像 ExtendVote interchangeable / 341 verifydet item 2 任意扩展 interchangeable，也不是已经 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事 bundled（341 item 3 余量） interchangeable / 341 verifydet item 3 interchangeable，也不是已经丢了安全性（本页第一件事） interchangeable。**  
   官方写：实现 `ExtendVote` 和 `VerifyVoteExtension` 必须非常小心。看见必须非常小心，不是已经有引擎补丁。看见没有协议层补丁，不是已经 has-patch interchangeable——本页钉 not already has-patch 单句。看见两边都要小心，不是已经丢了安全性（本页第一件事） interchangeable——三件事分开钉。341 verifydet vs extend bundled unbundling 在本页 item 3 完成。

3. **看见 SHOULD Accept / 看见通则是一律 Accept / 看见建议一律 Accept is not already 已经必须拒坏扩展 interchangeable / 已经 must-reject interchangeable / 已经必须拒交差 interchangeable / 341 verifydet bundled interchangeable / 348 req6-coherence interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 778 verify-notlostsafety interchangeable / 341 verifydet item 1 / 341 verifydet item 2，也不是已经 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事 bundled（341 item 3 余量） interchangeable / 341 verifydet item 3 interchangeable，也不是已经丢了安全性（本页第一件事） interchangeable / 已经有补丁（本页第二件事） interchangeable。**  
   官方写：通则是 `VerifyVoteExtension` SHOULD 一律 Accept。看见 SHOULD Accept，不是已经必须拒坏扩展。看见通则是一律 Accept，不是已经 must-reject interchangeable——本页钉 not already must-reject 单句。看见建议一律 Accept，不是已经有补丁（本页第二件事） interchangeable——三件事分开钉。341 verifydet vs extend bundled unbundling 在本页 item 3 完成。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。VerifyVoteExtension 确定性 bundled（341）、Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值（341 item 1 余量 / 776）、两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决（341 item 2 余量 / 777）、ExtendVote 没有确定性要求（338）、验签拒收整张预提交（34）、Process 非确定 bug 没有现成解法（340）是另外那套，本页不抄。

## 官方为什么这样拆

- **活性会被伤 not already lost-safety ≠ 341 / 340 interchangeable：** 官方把活性会被伤和已经丢了安全性分开。
- **必须非常小心 not already has-patch ≠ 已经有引擎补丁 interchangeable：** 官方把两边都要小心和已经有引擎补丁分开。
- **SHOULD Accept not already must-reject ≠ 已经必须拒坏扩展 interchangeable：** 官方把 SHOULD Accept 和已经必须拒坏扩展分开；341 verifydet vs extend bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 活性会被伤 | 不是 already lost-safety | 不是 Process 非确定 bug 没有现成解法 alone（340） |
| 必须非常小心 | 不是 already has-patch | 不是必须确定就已经可以像 ExtendVote 那样 alone（776） |
| SHOULD Accept | 不是 already must-reject | 不是两边同判就已经只对诚实扩展 alone（777） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量），必须分开活性会被伤 是不是 already lost-safety interchangeable / 341 verifydet bundled interchangeable / verifydet-sold-as-extend interchangeable、必须非常小心 是不是 already has-patch interchangeable、SHOULD Accept 是不是 already must-reject interchangeable。可以跳过「看见活性会被伤就已经丢了安全性 interchangeable / 就已经有补丁 interchangeable / 就必须拒坏扩展 interchangeable」。不要把 SHOULD Accept 当不确定已经拒坏扩展。不要另写怎样写 VerifyVoteExtension。341 verifydet vs extend bundled unbundling 在本页 item 3 完成（776 + 777 + 778）。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- VerifyVoteExtension 确定性 bundled。那是不变量 341。
- Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值。那是不变量 341 item 1 余量 / 776。
- 两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决。那是不变量 341 item 2 余量 / 777。
- ExtendVote 没有确定性要求。那是不变量 338。
- 验签拒收整张预提交。那是不变量 34。
- Process 非确定 bug 没有现成解法。那是不变量 340。
