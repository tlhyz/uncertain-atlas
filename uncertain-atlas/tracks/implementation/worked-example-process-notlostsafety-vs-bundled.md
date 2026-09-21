# 例：看见活性不能保证 / 看见没有现成解法 / 看见 SHOULD Accept is not already already lost-safety interchangeable / already has-patch interchangeable / already must-reject interchangeable

**层次**：实现 / Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量）/ not 775 process-notlostsafety interchangeable / not 340 processdet bundled interchangeable」，不是 ProcessProposal 确定性 bundled（340），也不是 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值（773 item 1 余量）或两边对任意块同一裁决不是已经只对诚实提案同一裁决（774 item 2 余量）。不要另写怎样写 ProcessProposal。

## 官方三件事

规范把 Requirements 里 Process 非确定 bug、活性不能保证、没有现成解法 和「已经是活性不能保证就已经丢了安全性 interchangeable / 已经是没有现成解法就已经有引擎补丁 interchangeable / 已经是 SHOULD Accept 就必须拒坏块 interchangeable / 已经是 processdet bundled interchangeable」分开写成三件独立的实现事，不是「看见活性不能保证就已经丢了安全性 interchangeable / 就已经有补丁 interchangeable / 就必须拒坏块 interchangeable」一件事：

1. **看见活性不能保证 / 看见 Process 里有非确定 bug / 看见打中的进程无法守 Req 4 或 5 is not already 已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable / 340 processdet bundled interchangeable / 327 preparetimeout interchangeable / processdet-sold-as-prepare interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 775 process-notlostsafety interchangeable / 340 processdet item 3 interchangeable，也不是已经 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事 bundled（340 item 3 余量） interchangeable / 340 processdet item 3 interchangeable，也不是已经 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值（773） interchangeable / 774 process-nothonestonly interchangeable / 33 four gates interchangeable，也不是已经立刻整块执行已经离开关键路径（327） interchangeable。**  
   官方写：Process 若有 bug 让 Accept/Reject 不再确定，打中的进程就无法守 Req 4 或 5，严格说已经是 Byzantine。这时 CometBFT 的**活性不能保证**。看见活性不能保证，不是已经丢了安全性。看见活性不能保证，不是已经 lost-safety interchangeable——340 钉 bundled 三事，本页从 item 3 侧钉 not already lost-safety 单句。看见 Process 里有非确定 bug，不是已经 ProcessProposal 确定性 bundled（340） interchangeable——340 钉 bundled，本页钉 item 3 第一件事。看见活性不能保证，不是已经立刻整块执行已经离开关键路径（327） interchangeable——327 另钉。340 processdet vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见没有现成解法 / 看见目前没有清楚的解法 / 看见没有协议层补丁 is not already 已经有引擎补丁 interchangeable / 已经 has-patch interchangeable / 已经有补丁交差 interchangeable / 340 processdet bundled interchangeable / 33 four gates interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 775 process-notlostsafety interchangeable / 340 processdet item 1 像 Prepare interchangeable / 340 processdet item 2 任意块 interchangeable，也不是已经 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事 bundled（340 item 3 余量） interchangeable / 340 processdet item 3 interchangeable，也不是已经丢了安全性（本页第一件事） interchangeable。**  
   官方写：目前**没有清楚的解法**，实现者必须非常小心。看见没有现成解法，不是已经有引擎补丁。看见目前没有清楚的解法，不是已经 has-patch interchangeable——本页钉 not already has-patch 单句。看见没有协议层补丁，不是已经丢了安全性（本页第一件事） interchangeable——三件事分开钉。340 processdet vs prepare bundled unbundling 在本页 item 3 完成。

3. **看见 SHOULD Accept / 看见通则是一律 Accept / 看见建议一律 Accept is not already 已经必须拒坏块 interchangeable / 已经 must-reject interchangeable / 已经必须拒交差 interchangeable / 340 processdet bundled interchangeable / 347 req3-coherence interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 775 process-notlostsafety interchangeable / 340 processdet item 1 / 340 processdet item 2，也不是已经 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事 bundled（340 item 3 余量） interchangeable / 340 processdet item 3 interchangeable，也不是已经丢了安全性（本页第一件事） interchangeable / 已经有补丁（本页第二件事） interchangeable。**  
   官方写：通则是 `ProcessProposal` SHOULD 一律 Accept。看见 SHOULD Accept，不是已经必须拒坏块。看见通则是一律 Accept，不是已经 must-reject interchangeable——本页钉 not already must-reject 单句。看见建议一律 Accept，不是已经有补丁（本页第二件事） interchangeable——三件事分开钉。340 processdet vs prepare bundled unbundling 在本页 item 3 完成。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。ProcessProposal 确定性 bundled（340）、Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值（340 item 1 余量 / 773）、两边对任意块同一裁决不是已经只对诚实提案同一裁决（340 item 2 余量 / 774）、Prepare 没有确定性要求（338）、四门已经结算（33）、立刻整块执行已经离开关键路径（327）是另外那套，本页不抄。

## 官方为什么这样拆

- **活性不能保证 not already lost-safety ≠ 340 / 327 interchangeable：** 官方把活性不能保证和已经丢了安全性分开。
- **没有现成解法 not already has-patch ≠ 已经有引擎补丁 interchangeable：** 官方把没有清楚解法和已经有引擎补丁分开。
- **SHOULD Accept not already must-reject ≠ 已经必须拒坏块 interchangeable：** 官方把 SHOULD Accept 和已经必须拒坏块分开；340 processdet vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 活性不能保证 | 不是 already lost-safety | 不是立刻整块执行已经离开关键路径 alone（327） |
| 没有现成解法 | 不是 already has-patch | 不是必须确定就已经可以像 Prepare 那样 alone（773） |
| SHOULD Accept | 不是 already must-reject | 不是两边同判就已经只对诚实提案 alone（774） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量），必须分开活性不能保证 是不是 already lost-safety interchangeable / 340 processdet bundled interchangeable / processdet-sold-as-prepare interchangeable、没有现成解法 是不是 already has-patch interchangeable、SHOULD Accept 是不是 already must-reject interchangeable。可以跳过「看见活性不能保证就已经丢了安全性 interchangeable / 就已经有补丁 interchangeable / 就必须拒坏块 interchangeable」。不要把 SHOULD Accept 当不确定已经拒坏块。不要另写怎样写 ProcessProposal。340 processdet vs prepare bundled unbundling 在本页 item 3 完成（773 + 774 + 775）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- ProcessProposal 确定性 bundled。那是不变量 340。
- Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值。那是不变量 340 item 1 余量 / 773。
- 两边对任意块同一裁决不是已经只对诚实提案同一裁决。那是不变量 340 item 2 余量 / 774。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
