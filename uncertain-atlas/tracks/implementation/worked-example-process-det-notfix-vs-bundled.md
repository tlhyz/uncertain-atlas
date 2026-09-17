# 例：看见 Process 非确定 bug 没有现成解法 is not already lost safety interchangeable / not already engine patch interchangeable / not already settled interchangeable

**层次**：实现 / Process 非确定 bug 没有现成解法 not already lost safety / not already engine patch / not already settled 正式三事（340 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 非确定 bug 没有现成解法 not already lost safety / not already engine patch / not already settled 正式三事（340 余量）/ not 895 process-det-notfix interchangeable / not 340 process-det-vs-prepare bundled interchangeable」，不是 ProcessProposal 确定性 bundled（340），也不是立刻整块执行已经离开关键路径（327），也不是 Verify 非确定会伤活性（341/892）。不要另写怎样写 ProcessProposal。

## 官方三件事

1. **看见 Process 里有非确定 bug / 看见没有现成解法 这份无解 is not already 已经丢了安全性 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 895 process-det-notfix interchangeable / 893 process-det-notprep interchangeable / 340 process-det item 1 必须确定 interchangeable，也不是已经 Process 非确定 bug 没有现成解法 not already lost safety / not already engine patch / not already settled 正式三事 bundled（340 item 3 余量） interchangeable / 340 process-det item 3 interchangeable。**  
   官方写：Process 若有 bug 让 Accept/Reject 不再确定，打中的进程就无法守 Req 4 或 5，严格说已经是 Byzantine。这时 CometBFT 的活性不能保证。多数验证者跑同一份软件时，很可能在同一点打中。目前没有清楚的解法，实现者必须非常小心。通则是 `ProcessProposal` SHOULD 一律 Accept。看见活性不能保证，不是已经丢了安全性 interchangeable——本页从 340 item 3 侧钉 not already lost safety 单句。340 process-det vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见没有现成解法 / 看见 SHOULD Accept / 这份无解 is not already 已经有协议层补丁 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 895 process-det-notfix interchangeable / 340 process-det item 2 任意块 interchangeable / 894 process-det-nothonest interchangeable，也不是已经立刻整块执行已经离开关键路径 interchangeable / 327 leave-path interchangeable。**  
   官方把没有现成解法和已经有引擎补丁分开——340 bundled 第三件事常与 327 / 341 混成「看见活性不能保证就已经丢了安全性或已经有补丁 interchangeable」，本页钉 not already engine patch 单句。

3. **看见 SHOULD Accept / 看见活性不能保证 / 这份无解 is not already 已经交差 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 895 process-det-notfix interchangeable / 893 process-det-notprep interchangeable，也不是已经必须拒坏块 interchangeable。**  
   官方把 SHOULD Accept 和已经必须拒坏块 / 已经交差分开。看见 SHOULD Accept，不是已经必须拒坏块 interchangeable。340 process-det vs prepare bundled unbundling 在本页 item 3 完成。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Process 非确定 bug 没有现成解法 not already lost safety ≠ 已经丢了安全性 interchangeable：** 官方把活性不能保证和已经丢了安全性分开。
- **看见没有现成解法 not already engine patch ≠ 已经有协议层补丁 interchangeable：** 官方把没有清楚解法和已经有引擎补丁分开。
- **看见 SHOULD Accept not already settled ≠ 已经交差 interchangeable：** 官方把 SHOULD Accept 和已经交差分开；340 process-det vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Process 非确定 bug 没有现成解法 | 不是已经丢了安全性 | 不是立刻整块执行已经离开关键路径（327） |
| 看见没有现成解法 | 不是已经有协议层补丁 | 不是 Verify 非确定会伤活性（341/892） |
| 看见 SHOULD Accept | 不是已经交差 | 不是 Process 必须确定就已经可以像 Prepare 那样（893） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 非确定 bug 没有现成解法 not already lost safety / not already engine patch / not already settled 正式三事（340 余量），必须分开是不是已经丢了安全性、是不是已经有协议层补丁、是不是已经交差。可以跳过「看见活性不能保证就已经丢了安全性」。不要把 SHOULD Accept 当不确定已经拒坏块。不要另写怎样写 ProcessProposal。340 process-det vs prepare bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- ProcessProposal 确定性 bundled。那是不变量 340。
- Process 必须只依赖请求和上一份状态。那是不变量 340 item 1 余量 / 893。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- Verify 非确定会伤活性。那是不变量 341 / 892。
