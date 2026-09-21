# 例：看见 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值；看见两边对任意块同一裁决不是已经只对诚实提案同一裁决；看见 Process 非确定 bug 没有现成解法不是已经丢了安全性

**层次**：实现 / ProcessProposal 确定性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 / 两边对任意块同一裁决不是已经只对诚实提案同一裁决 / Process 非确定 bug 没有现成解法不是已经丢了安全性」，不是 Prepare 没有确定性要求，也不是四门已经结算。不要另写怎样写 ProcessProposal。 340 processdet vs prepare bundled unbundling 续（773 + 774）；精读 [`worked-example-process-notlikeprepare-vs-bundled.md`](worked-example-process-notlikeprepare-vs-bundled.md)；[`worked-example-process-nothonestonly-vs-bundled.md`](worked-example-process-nothonestonly-vs-bundled.md)（不变量 774 item 2）。

## 官方三件事

规范把 Process 的确定性写成三件独立的实现事，不是「看见必须确定就已经可以像 Prepare 那样、已经只对诚实提案、已经丢了安全性」一件事：

1. **看见 `ProcessProposal` 必须只依赖本次请求和 `s_{h-1}` / 看见必须确定 不是已经可以像 Prepare 那样依赖其它值，也不是已经和 Prepare / ExtendVote 同一把尺。**  
   官方写：`ProcessProposal` 是当前状态和即将应用的那块的**确定**函数。正确进程 *p* 对任意块 *u* 叫 Process，Accept 或 Reject **只**依赖 *u* 和 *s_{p,h-1}*。看见必须确定，不是已经可以依赖其它值或操作。看见只依赖请求和上一份状态，不是已经和「Prepare 没有确定性要求」同一句。看见 Process 回了，不是已经交差。
2. **看见两边对任意块同一裁决 / 看见提议者是拜占庭 不是已经只对诚实提案同一裁决，也不是已经是诚实 Prepare 必须被诚实 Process Accept。**  
   官方写：Requirement 4 和 5 保证所有正确进程对一份提案的反应相同，**即使提议者是拜占庭**。看见两边同判，不是已经只对诚实 *u_p* 同判。看见提议者坏了，不是已经可以各判各的。看见任意块，不是已经是 Req 3 那句诚实对诚实。
3. **看见 Process 里有非确定 bug / 看见没有现成解法 不是已经丢了安全性，也不是已经有协议层补丁。**  
   官方写：Process 若有 bug 让 Accept/Reject 不再确定，打中的进程就无法守 Req 4 或 5，严格说已经是 Byzantine。这时 CometBFT 的**活性不能保证**。多数验证者跑同一份软件时，很可能在同一点打中。目前**没有清楚的解法**，实现者必须非常小心。通则是 `ProcessProposal` SHOULD 一律 Accept。看见活性不能保证，不是已经丢了安全性。看见没有现成解法，不是已经有引擎补丁。看见 SHOULD Accept，不是已经必须拒坏块。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。Prepare 没有确定性要求是不变量 338，本页不抄。

## 官方为什么这样拆

- **Process 必须只依赖请求和上一份状态 ≠ 已经可以像 Prepare 那样依赖其它值：** 官方把 Process 必须确定和 Prepare 可以不确定分开。
- **两边对任意块同一裁决 ≠ 已经只对诚实提案同一裁决：** 官方把拜占庭提议者和诚实对诚实分开。
- **Process 非确定 bug 没有现成解法 ≠ 已经丢了安全性：** 官方把活性不能保证、没有清楚解法、SHOULD Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 必须只依赖请求和上一份状态 | 不是已经可以像 Prepare 那样依赖其它值 | 不是 Prepare 没有确定性要求（338） |
| 两边对任意块同一裁决 | 不是已经只对诚实提案同一裁决 | 不是四门已经结算（33） |
| Process 非确定 bug 没有现成解法 | 不是已经丢了安全性 | 不是立刻整块执行已经离开关键路径（327） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须确定就已经可以像 Prepare 那样、已经只对诚实提案、已经丢了安全性」，必须分开 Process 必须只依赖请求和上一份状态是不是已经可以像 Prepare 那样依赖其它值、两边对任意块同一裁决是不是已经只对诚实提案同一裁决、Process 非确定 bug 没有现成解法是不是已经丢了安全性。可以跳过「看见必须确定就已经可以像 Prepare 那样」。不要把 SHOULD Accept 当不确定已经拒坏块。不要另写怎样写 ProcessProposal。 340 processdet vs prepare bundled unbundling 续（773 + 774 item 2）；续 [`worked-example-process-notlostsafety-vs-bundled.md`](worked-example-process-notlostsafety-vs-bundled.md)（不变量 775 item 3）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
