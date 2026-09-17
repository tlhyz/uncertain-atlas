# 例：看见 Verify 非确定会伤活性 is not already lost safety interchangeable / not already engine patch interchangeable / not already settled interchangeable

**层次**：实现 / Verify 非确定会伤活性 not already lost safety / not already engine patch / not already settled 正式三事（341 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Verify 非确定会伤活性 not already lost safety / not already engine patch / not already settled 正式三事（341 余量）/ not 892 verify-det-notsafety interchangeable / not 341 verify-det-vs-extend bundled interchangeable」，不是 VerifyVoteExtension 确定性 bundled（341），也不是 Process 非确定 bug 没有现成解法（340），也不是 Req 6 会面对同一类活性问题（348/871）。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

1. **看见 Verify 里有非确定 bug / 看见活性会被伤 这份活性 is not already 已经丢了安全性 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 892 verify-det-notsafety interchangeable / 890 verify-det-notext interchangeable / 341 verify-det item 1 必须确定 interchangeable，也不是已经 Verify 非确定会伤活性 not already lost safety / not already engine patch / not already settled 正式三事 bundled（341 item 3 余量） interchangeable / 341 verify-det item 3 interchangeable。**  
   官方写：Verify 若有 bug 让 Accept/Reject 不再确定，就会违反 Requirement 7 或 8。这时活性会被伤。实现 `ExtendVote` 和 `VerifyVoteExtension` 必须非常小心。通则是 `VerifyVoteExtension` SHOULD 一律 Accept。看见活性会被伤，不是已经丢了安全性 interchangeable——本页从 341 item 3 侧钉 not already lost safety 单句。341 verify-det vs extend bundled unbundling 在本页 item 3 完成。

2. **看见要小心两边 / 看见 SHOULD Accept / 这份活性 is not already 已经有协议层补丁 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 892 verify-det-notsafety interchangeable / 341 verify-det item 2 任意扩展 interchangeable / 891 verify-det-nothonest interchangeable，也不是已经 Process 非确定 bug 没有现成解法 interchangeable / 340 process-nondet interchangeable。**  
   官方把要小心两边和已经有引擎补丁分开——341 bundled 第三件事常与 340 / 348 混成「看见活性会被伤就已经丢了安全性或已经有补丁 interchangeable」，本页钉 not already engine patch 单句。

3. **看见 SHOULD Accept / 看见活性会被伤 / 这份活性 is not already 已经交差 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 892 verify-det-notsafety interchangeable / 890 verify-det-notext interchangeable，也不是已经必须拒坏扩展 interchangeable。**  
   官方把 SHOULD Accept 和已经必须拒坏扩展 / 已经交差分开。看见 SHOULD Accept，不是已经必须拒坏扩展 interchangeable。341 verify-det vs extend bundled unbundling 在本页 item 3 完成。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Verify 非确定会伤活性 not already lost safety ≠ 已经丢了安全性 interchangeable：** 官方把活性会被伤和已经丢了安全性分开。
- **看见要小心两边 not already engine patch ≠ 已经有协议层补丁 interchangeable：** 官方把要小心两边和已经有引擎补丁分开。
- **看见 SHOULD Accept not already settled ≠ 已经交差 interchangeable：** 官方把 SHOULD Accept 和已经交差分开；341 verify-det vs extend bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Verify 非确定会伤活性 | 不是已经丢了安全性 | 不是 Process 非确定 bug 没有现成解法（340） |
| 看见要小心两边 | 不是已经有协议层补丁 | 不是 Req 6 会面对同一类活性问题（348/871） |
| 看见 SHOULD Accept | 不是已经交差 | 不是 Verify 必须确定就已经可以像 ExtendVote 那样（890） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 非确定会伤活性 not already lost safety / not already engine patch / not already settled 正式三事（341 余量），必须分开是不是已经丢了安全性、是不是已经有协议层补丁、是不是已经交差。可以跳过「看见活性会被伤就已经丢了安全性」。不要把 SHOULD Accept 当不确定已经拒坏扩展。不要另写怎样写 VerifyVoteExtension。341 verify-det vs extend bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- VerifyVoteExtension 确定性 bundled。那是不变量 341。
- Verify 必须只依赖扩展、这块和上一份状态。那是不变量 341 item 1 余量 / 890。
- Process 非确定 bug 没有现成解法。那是不变量 340。
- Req 6 会面对同一类活性问题。那是不变量 348 / 871。
