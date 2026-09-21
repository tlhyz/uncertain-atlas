# 例：看见 ProcessProposal 必须只依赖本次请求和上一份状态 / 看见必须确定 / 看见 Process 回了 is not already already like-prepare interchangeable / already same-as-nondet interchangeable / already settled interchangeable

**层次**：实现 / Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量）/ not 773 process-notlikeprepare interchangeable / not 340 processdet bundled interchangeable」，不是 ProcessProposal 确定性 bundled（340），也不是两边对任意块同一裁决不是已经只对诚实提案同一裁决（774 item 2 余量）或 Process 非确定 bug 没有现成解法不是已经丢了安全性（775 item 3 余量）。不要另写怎样写 ProcessProposal。

## 官方三件事

规范把 Requirements 里 `ProcessProposal` 必须只依赖本次请求和 *s_{h-1}*、必须确定 和「已经是必须确定就可以像 Prepare 那样依赖其它值 interchangeable / 已经是只依赖请求和上一份状态就已经和 Prepare 没有确定性要求同一句 interchangeable / 已经是 Process 回了就已经交差 interchangeable / 已经是 processdet bundled interchangeable」分开写成三件独立的实现事，不是「看见必须确定就可以像 Prepare 那样 interchangeable / 就已经和 Prepare nondet 同一句 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 ProcessProposal 必须只依赖本次请求和 *s_{h-1}* / 看见必须确定 / 看见是确定函数 is not already 已经可以像 Prepare 那样依赖其它值 interchangeable / 已经 like-prepare interchangeable / 已经可以依赖其它值交差 interchangeable / 340 processdet bundled interchangeable / 338 preparenondet interchangeable / processdet-sold-as-prepare interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 773 process-notlikeprepare interchangeable / 340 processdet item 1 interchangeable，也不是已经 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事 bundled（340 item 1 余量） interchangeable / 340 processdet item 1 interchangeable，也不是已经两边对任意块同一裁决不是已经只对诚实提案同一裁决（774） interchangeable / 775 process-notlostsafety interchangeable / 33 four gates interchangeable，也不是已经 Prepare 没有确定性要求（338） interchangeable。**  
   官方写：`ProcessProposal` 是当前状态和即将应用的那块的**确定**函数。正确进程 *p* 对任意块 *u* 叫 Process，Accept 或 Reject **只**依赖 *u* 和 *s_{p,h-1}*。看见必须确定，不是已经可以依赖其它值或操作。看见必须确定，不是已经 like-prepare interchangeable——340 钉 bundled 三事，本页从 item 1 侧钉 not already like-prepare 单句。看见是确定函数，不是已经 ProcessProposal 确定性 bundled（340） interchangeable——340 钉 bundled，本页钉 item 1 第一件事。看见必须确定，不是已经 Prepare 没有确定性要求（338） interchangeable——338 另钉。340 processdet vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见只依赖请求和上一份状态 / 看见只依赖 *u* 和 *s_{h-1}* / 看见不能另依赖其它值 is not already 已经和 Prepare 没有确定性要求同一句 interchangeable / 已经 same-as-nondet interchangeable / 已经和 Prepare / ExtendVote 同一把尺交差 interchangeable / 340 processdet bundled interchangeable / 338 preparenondet interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 773 process-notlikeprepare interchangeable / 340 processdet item 2 任意块 interchangeable / 340 processdet item 3 非确定 bug interchangeable，也不是已经 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事 bundled（340 item 1 余量） interchangeable / 340 processdet item 1 interchangeable，也不是已经可以像 Prepare 那样（本页第一件事） interchangeable。**  
   官方写：看见只依赖请求和上一份状态，不是已经和「Prepare 没有确定性要求」同一句。看见只依赖 *u* 和 *s_{h-1}*，不是已经 same-as-nondet interchangeable——本页钉 not already same-as-nondet 单句。看见不能另依赖其它值，不是已经可以像 Prepare 那样（本页第一件事） interchangeable——三件事分开钉。340 processdet vs prepare bundled unbundling 在本页 item 1 启动。

3. **看见 Process 回了 / 看见 ProcessProposal 回了 / 看见 Accept 或 Reject 回来了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差同一句 interchangeable / 340 processdet bundled interchangeable / 33 four gates interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 773 process-notlikeprepare interchangeable / 340 processdet item 2 / 340 processdet item 3，也不是已经 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事 bundled（340 item 1 余量） interchangeable / 340 processdet item 1 interchangeable，也不是已经可以像 Prepare 那样（本页第一件事） interchangeable / 已经和 Prepare nondet 同一句（本页第二件事） interchangeable。**  
   官方写：看见 Process 回了，不是已经交差。看见 ProcessProposal 回了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见 Accept 或 Reject 回来了，不是已经和 Prepare nondet 同一句（本页第二件事） interchangeable——三件事分开钉。340 processdet vs prepare bundled unbundling 在本页 item 1 启动。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。ProcessProposal 确定性 bundled（340）、两边对任意块同一裁决不是已经只对诚实提案同一裁决（340 item 2 余量 / 774）、Process 非确定 bug 没有现成解法不是已经丢了安全性（340 item 3 余量 / 775）、Prepare 没有确定性要求（338）、四门已经结算（33）、立刻整块执行已经离开关键路径（327）是另外那套，本页不抄。

## 官方为什么这样拆

- **必须确定 not already like-prepare ≠ 340 / 338 interchangeable：** 官方把 Process 必须确定和 Prepare 可以不确定分开。
- **只依赖请求和上一份状态 not already same-as-nondet ≠ 已经和 Prepare nondet 同一句 interchangeable：** 官方把只依赖请求 / 上一份状态和 Prepare 没有确定性要求分开。
- **Process 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Process 回了和已经交差分开；340 processdet vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须确定 | 不是 already like-prepare | 不是 Prepare 没有确定性要求 alone（338） |
| 只依赖请求和上一份状态 | 不是 already same-as-nondet | 不是四门已经结算 alone（33） |
| Process 回了 | 不是 already settled | 不是两边同判就已经只对诚实提案 alone（774） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量），必须分开必须确定 是不是 already like-prepare interchangeable / 340 processdet bundled interchangeable / processdet-sold-as-prepare interchangeable、只依赖请求和上一份状态 是不是 already same-as-nondet interchangeable、Process 回了 是不是 already settled interchangeable。可以跳过「看见必须确定就可以像 Prepare 那样 interchangeable / 就已经和 Prepare nondet 同一句 interchangeable / 就已经交差 interchangeable」。不要把 SHOULD Accept 当不确定已经拒坏块。不要另写怎样写 ProcessProposal。340 processdet vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-process-nothonestonly-vs-bundled.md`](worked-example-process-nothonestonly-vs-bundled.md)（不变量 774 item 2）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- ProcessProposal 确定性 bundled。那是不变量 340。
- 两边对任意块同一裁决不是已经只对诚实提案同一裁决。那是不变量 340 item 2 余量 / 774。
- Process 非确定 bug 没有现成解法不是已经丢了安全性。那是不变量 340 item 3 余量 / 775。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
- 立刻整块执行已经离开关键路径。那是不变量 327。
