# 例：看见 FinalizeBlock 算出的状态必须只依赖上一份状态和决定块 / 看见必须确定 / 看见 Finalize 回了 is not already already like-prepare interchangeable / already same-as-nondet interchangeable / already settled interchangeable

**层次**：实现 / Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（342 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 11–12 [`FinalizeBlock`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（342 余量）/ not 779 finalize-notlikeprepare interchangeable / not 342 finalizedet bundled interchangeable」，不是 FinalizeBlock 确定性 bundled（342），也不是 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头（780 item 2 余量）或两边状态机复制不是已经是 Process 对任意块同一裁决（781 item 3 余量）。不要另写怎样写 FinalizeBlock。

## 官方三件事

规范把 Requirements 里 `FinalizeBlock` 算出的状态必须只依赖 *s_{h-1}* 和决定块 *v*、必须确定 和「已经是必须确定就可以像 Prepare 那样依赖其它值 interchangeable / 已经是只依赖上一份状态和决定块就已经和 Prepare 没有确定性要求同一句 interchangeable / 已经是 Finalize 回了就已经交差 interchangeable / 已经是 finalizedet bundled interchangeable」分开写成三件独立的实现事，不是「看见必须确定就可以像 Prepare 那样 interchangeable / 就已经和 Prepare nondet 同一句 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 FinalizeBlock 算出的状态必须只依赖 *s_{h-1}* 和 *v* / 看见必须确定 / 看见造出 *s_h* is not already 已经可以像 Prepare 那样依赖其它值 interchangeable / 已经 like-prepare interchangeable / 已经可以依赖其它值交差 interchangeable / 342 finalizedet bundled interchangeable / 338 preparenondet interchangeable / finalizedet-sold-as-prepare interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 779 finalize-notlikeprepare interchangeable / 342 finalizedet item 1 interchangeable，也不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事 bundled（342 item 1 余量） interchangeable / 342 finalizedet item 1 interchangeable，也不是已经 Finalize 算出的结果不是已经印进本头（780） interchangeable / 781 finalize-notprocesssame interchangeable / 340 processdet interchangeable，也不是已经 Prepare 没有确定性要求（338） interchangeable。**  
   官方写：正确进程 *p* 在高度 *h* 叫 `FinalizeBlock`，把决定块 *v_{p,h}* 交进去，**造出**状态 *s_{p,h}*。Requirement 11：*s_{p,h}* **只**依赖 *s_{p,h-1}* 和 *v_{p,h}*。看见必须确定，不是已经可以依赖其它值或操作。看见必须确定，不是已经 like-prepare interchangeable——342 钉 bundled 三事，本页从 item 1 侧钉 not already like-prepare 单句。看见造出 *s_h*，不是已经 FinalizeBlock 确定性 bundled（342） interchangeable——342 钉 bundled，本页钉 item 1 第一件事。看见必须确定，不是已经 Prepare 没有确定性要求（338） interchangeable——338 另钉。342 finalizedet vs prepare bundled unbundling 在本页 item 1 启动。

2. **看见只依赖上一份状态和决定块 / 看见只依赖 *s_{h-1}* 和 *v* / 看见不能另依赖其它值 is not already 已经和 Prepare 没有确定性要求同一句 interchangeable / 已经 same-as-nondet interchangeable / 已经和 Prepare / ExtendVote 同一把尺交差 interchangeable / 342 finalizedet bundled interchangeable / 338 preparenondet interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 779 finalize-notlikeprepare interchangeable / 342 finalizedet item 2 结果集合 interchangeable / 342 finalizedet item 3 状态机复制 interchangeable，也不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事 bundled（342 item 1 余量） interchangeable / 342 finalizedet item 1 interchangeable，也不是已经可以像 Prepare 那样（本页第一件事） interchangeable。**  
   官方写：看见只依赖上一份状态和决定块，不是已经和「Prepare 没有确定性要求」同一句。看见只依赖 *s_{h-1}* 和 *v*，不是已经 same-as-nondet interchangeable——本页钉 not already same-as-nondet 单句。看见不能另依赖其它值，不是已经可以像 Prepare 那样（本页第一件事） interchangeable——三件事分开钉。342 finalizedet vs prepare bundled unbundling 在本页 item 1 启动。

3. **看见 Finalize 回了 / 看见 FinalizeBlock 回了 / 看见造出了 *s_h* is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差同一句 interchangeable / 342 finalizedet bundled interchangeable / 335 finalizepersist interchangeable，也不是已经 FinalizeBlock 确定性 bundled（342） interchangeable / 779 finalize-notlikeprepare interchangeable / 342 finalizedet item 2 / 342 finalizedet item 3，也不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事 bundled（342 item 1 余量） interchangeable / 342 finalizedet item 1 interchangeable，也不是已经可以像 Prepare 那样（本页第一件事） interchangeable / 已经和 Prepare nondet 同一句（本页第二件事） interchangeable。**  
   官方写：看见 Finalize 回了，不是已经交差。看见 FinalizeBlock 回了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见造出了 *s_h*，不是已经和 Prepare nondet 同一句（本页第二件事） interchangeable——三件事分开钉。不要把造出 *s_h* 当已经落盘。342 finalizedet vs prepare bundled unbundling 在本页 item 1 启动。

怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。FinalizeBlock 确定性 bundled（342）、Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头（342 item 2 余量 / 780）、两边状态机复制不是已经是 Process 对任意块同一裁决（342 item 3 余量 / 781）、Prepare 没有确定性要求（338）、结果列表已经同一顺序（316）、ProcessProposal 确定性（340）是另外那套，本页不抄。

## 官方为什么这样拆

- **必须确定 not already like-prepare ≠ 342 / 338 interchangeable：** 官方把 Finalize 必须确定和 Prepare 可以不确定分开。
- **只依赖上一份状态和决定块 not already same-as-nondet ≠ 已经和 Prepare nondet 同一句 interchangeable：** 官方把只依赖上一份状态 / 决定块和 Prepare 没有确定性要求分开。
- **Finalize 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Finalize 回了和已经交差分开；342 finalizedet vs prepare bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须确定 | 不是 already like-prepare | 不是 Prepare 没有确定性要求 alone（338） |
| 只依赖上一份状态和决定块 | 不是 already same-as-nondet | 不是结果列表已经同一顺序 alone（316） |
| Finalize 回了 | 不是 already settled | 不是结果必须确定就已经印进本头 alone（780） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（342 余量），必须分开必须确定 是不是 already like-prepare interchangeable / 342 finalizedet bundled interchangeable / finalizedet-sold-as-prepare interchangeable、只依赖上一份状态和决定块 是不是 already same-as-nondet interchangeable、Finalize 回了 是不是 already settled interchangeable。可以跳过「看见必须确定就可以像 Prepare 那样 interchangeable / 就已经和 Prepare nondet 同一句 interchangeable / 就已经交差 interchangeable」。不要把造出 *s_h* 当已经落盘。不要另写怎样写 FinalizeBlock。342 finalizedet vs prepare bundled unbundling 在本页 item 1 启动；续 [`worked-example-finalize-notprinted-vs-bundled.md`](worked-example-finalize-notprinted-vs-bundled.md)（不变量 780 item 2）。

## 本页不抄

- 怎样写 `FinalizeBlock`、怎样测确定性、怎样写测试向量。
- FinalizeBlock 确定性 bundled。那是不变量 342。
- Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头。那是不变量 342 item 2 余量 / 780。
- 两边状态机复制不是已经是 Process 对任意块同一裁决。那是不变量 342 item 3 余量 / 781。
- Prepare 没有确定性要求。那是不变量 338。
- 结果列表已经同一顺序。那是不变量 316。
- ProcessProposal 确定性。那是不变量 340。
