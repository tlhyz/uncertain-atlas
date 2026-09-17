# 例：看见 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值；看见两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决；看见 Verify 非确定会伤活性不是已经丢了安全性

**层次**：实现 / VerifyVoteExtension 确定性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 / 两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 / Verify 非确定会伤活性不是已经丢了安全性」，不是 ExtendVote 没有确定性要求，也不是验签拒收已经是块非法。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

规范把 Verify 的确定性写成三件独立的实现事，不是「看见必须确定就已经可以像 ExtendVote 那样、已经只对诚实扩展、已经丢了安全性」一件事：

1. **看见 `VerifyVoteExtension` 必须只依赖扩展、这块和上一份状态 / 看见必须确定 不是已经可以像 ExtendVote 那样依赖其它值，也不是已经和 ExtendVote 同一把尺。**  
   官方写：`VerifyVoteExtension` 是当前状态、收到的扩展、以及扩展所指那份提案的**确定**函数。正确进程 *p* 对任意扩展 *e* 和任意块 *w* 叫 Verify，Accept 或 Reject **只**依赖 *e*、*w* 和 *s_{p,h-1}*。看见必须确定，不是已经可以依赖其它值或操作。看见只依赖扩展、这块和上一份状态，不是已经和「ExtendVote 没有确定性要求」同一句。看见 Verify 回了，不是已经交差。
2. **看见两边对任意扩展同一裁决 / 看见扩展来自拜占庭 不是已经只对诚实扩展同一裁决，也不是已经是诚实扩展必须被诚实 Verify Accept。**  
   官方写：Requirement 7 和 8 保证所有正确进程对一份扩展的反应相同，用来挡住拜占庭进程送来的**任意**扩展数据，和 Requirement 4、5 挡住任意提案同一路。看见两边同判，不是已经只对诚实 *e_p* 同判。看见扩展坏了，不是已经可以各判各的。看见任意扩展，不是已经是 Req 6 那句诚实对诚实。
3. **看见 Verify 里有非确定 bug / 看见活性会被伤 不是已经丢了安全性，也不是已经有协议层补丁。**  
   官方写：Verify 若有 bug 让 Accept/Reject 不再确定，就会违反 Requirement 7 或 8。这时**活性会被伤**。实现 `ExtendVote` 和 `VerifyVoteExtension` 必须非常小心。通则是 `VerifyVoteExtension` SHOULD 一律 Accept。看见活性会被伤，不是已经丢了安全性。看见要小心两边，不是已经有引擎补丁。看见 SHOULD Accept，不是已经必须拒坏扩展。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。ExtendVote 没有确定性要求是不变量 338，本页不抄。

## 官方为什么这样拆

- **Verify 必须只依赖扩展、这块和上一份状态 ≠ 已经可以像 ExtendVote 那样依赖其它值：** 官方把 Verify 必须确定和 ExtendVote 可以不确定分开。
- **两边对任意扩展同一裁决 ≠ 已经只对诚实扩展同一裁决：** 官方把拜占庭扩展数据和诚实对诚实分开。
- **Verify 非确定会伤活性 ≠ 已经丢了安全性：** 官方把活性会被伤、两边都要小心、SHOULD Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Verify 必须只依赖扩展、这块和上一份状态 | 不是已经可以像 ExtendVote 那样依赖其它值 | 不是 ExtendVote 没有确定性要求（338） |
| 两边对任意扩展同一裁决 | 不是已经只对诚实扩展同一裁决 | 不是验签拒收已经是块非法（34） |
| Verify 非确定会伤活性 | 不是已经丢了安全性 | 不是 Process 非确定 bug 没有现成解法（340） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须确定就已经可以像 ExtendVote 那样、已经只对诚实扩展、已经丢了安全性」，必须分开 Verify 必须只依赖扩展、这块和上一份状态是不是已经可以像 ExtendVote 那样依赖其它值、两边对任意扩展同一裁决是不是已经只对诚实扩展同一裁决、Verify 非确定会伤活性是不是已经丢了安全性。可以跳过「看见必须确定就已经可以像 ExtendVote 那样」。不要把 SHOULD Accept 当不确定已经拒坏扩展。不要另写怎样写 VerifyVoteExtension。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- ExtendVote 没有确定性要求。那是不变量 338。
- 验签拒收已经是块非法。那是不变量 34。
- Process 非确定 bug 没有现成解法。那是不变量 340。
