# 例：看见两边对任意块同一裁决 / 看见提议者是拜占庭 / 看见任意块 is not already already honest-only interchangeable / already may-diverge interchangeable / already req3-same interchangeable

**层次**：实现 / 两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量）/ not 774 process-nothonestonly interchangeable / not 340 processdet bundled interchangeable」，不是 ProcessProposal 确定性 bundled（340），也不是 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值（773 item 1 余量）或 Process 非确定 bug 没有现成解法不是已经丢了安全性（775 item 3 余量）。不要另写怎样写 ProcessProposal。

## 官方三件事

规范把 Requirements 里两边对任意块同一裁决、提议者是拜占庭 和「已经是两边同判就已经只对诚实提案同判 interchangeable / 已经是提议者坏了就可以各判各的 interchangeable / 已经是任意块就已经是 Req 3 诚实对诚实 interchangeable / 已经是 processdet bundled interchangeable」分开写成三件独立的实现事，不是「看见两边同判就已经只对诚实提案 interchangeable / 就可以各判各的 interchangeable / 就已经是 Req 3 interchangeable」一件事：

1. **看见两边对任意块同一裁决 / 看见两边同判 / 看见所有正确进程对一份提案反应相同 is not already 已经只对诚实提案同一裁决 interchangeable / 已经 honest-only interchangeable / 已经只对诚实 *u_p* 同判交差 interchangeable / 340 processdet bundled interchangeable / 347 req3-coherence interchangeable / processdet-sold-as-prepare interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 774 process-nothonestonly interchangeable / 340 processdet item 2 interchangeable，也不是已经两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事 bundled（340 item 2 余量） interchangeable / 340 processdet item 2 interchangeable，也不是已经 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值（773） interchangeable / 775 process-notlostsafety interchangeable / 33 four gates interchangeable，也不是已经诚实 Prepare 必须被诚实 Process Accept（347） interchangeable。**  
   官方写：Requirement 4 和 5 保证所有正确进程对一份提案的反应相同，**即使提议者是拜占庭**。看见两边同判，不是已经只对诚实 *u_p* 同判。看见两边同判，不是已经 honest-only interchangeable——340 钉 bundled 三事，本页从 item 2 侧钉 not already honest-only 单句。看见所有正确进程对一份提案反应相同，不是已经 ProcessProposal 确定性 bundled（340） interchangeable——340 钉 bundled，本页钉 item 2 第一件事。看见两边同判，不是已经诚实 Prepare 必须被诚实 Process Accept（347） interchangeable——347 另钉。340 processdet vs prepare bundled unbundling 在本页 item 2 续。

2. **看见提议者是拜占庭 / 看见提议者坏了 / 看见提议者可以不诚实 is not already 已经可以各判各的 interchangeable / 已经 may-diverge interchangeable / 已经各判各的交差 interchangeable / 340 processdet bundled interchangeable / 33 four gates interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 774 process-nothonestonly interchangeable / 340 processdet item 1 像 Prepare interchangeable / 340 processdet item 3 非确定 bug interchangeable，也不是已经两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事 bundled（340 item 2 余量） interchangeable / 340 processdet item 2 interchangeable，也不是已经只对诚实提案同判（本页第一件事） interchangeable。**  
   官方写：看见提议者坏了，不是已经可以各判各的。看见提议者是拜占庭，不是已经 may-diverge interchangeable——本页钉 not already may-diverge 单句。看见提议者可以不诚实，不是已经只对诚实提案同判（本页第一件事） interchangeable——三件事分开钉。340 processdet vs prepare bundled unbundling 在本页 item 2 续。

3. **看见任意块 / 看见对任意块 *u* / 看见不是只对诚实准备好的提案 is not already 已经是 Req 3 诚实对诚实 interchangeable / 已经 req3-same interchangeable / 已经诚实对诚实交差 interchangeable / 340 processdet bundled interchangeable / 347 req3-coherence interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 774 process-nothonestonly interchangeable / 340 processdet item 1 / 340 processdet item 3，也不是已经两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事 bundled（340 item 2 余量） interchangeable / 340 processdet item 2 interchangeable，也不是已经只对诚实提案同判（本页第一件事） interchangeable / 已经可以各判各的（本页第二件事） interchangeable。**  
   官方写：看见任意块，不是已经是 Req 3 那句诚实对诚实。看见对任意块 *u*，不是已经 req3-same interchangeable——本页钉 not already req3-same 单句。看见不是只对诚实准备好的提案，不是已经可以各判各的（本页第二件事） interchangeable——三件事分开钉。340 processdet vs prepare bundled unbundling 在本页 item 2 续。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。ProcessProposal 确定性 bundled（340）、Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值（340 item 1 余量 / 773）、Process 非确定 bug 没有现成解法不是已经丢了安全性（340 item 3 余量 / 775）、Prepare 没有确定性要求（338）、四门已经结算（33）、诚实 Prepare 必须被诚实 Process Accept（347）是另外那套，本页不抄。

## 官方为什么这样拆

- **两边同判 not already honest-only ≠ 340 / 347 interchangeable：** 官方把拜占庭提议者下的同判和只对诚实提案同判分开。
- **提议者坏了 not already may-diverge ≠ 已经可以各判各的 interchangeable：** 官方把提议者坏了和已经可以各判各的分开。
- **任意块 not already req3-same ≠ 已经是 Req 3 interchangeable：** 官方把任意块同判和 Req 3 诚实对诚实分开；340 processdet vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边同判 | 不是 already honest-only | 不是诚实 Prepare 必须被诚实 Process Accept alone（347） |
| 提议者坏了 | 不是 already may-diverge | 不是必须确定就已经可以像 Prepare 那样 alone（773） |
| 任意块 | 不是 already req3-same | 不是非确定 bug 就已经丢了安全性 alone（775） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意块同一裁决不是已经只对诚实提案同一裁决 not already honest-only / not already may-diverge / not already req3-same 正式三事（340 余量），必须分开两边同判 是不是 already honest-only interchangeable / 340 processdet bundled interchangeable / processdet-sold-as-prepare interchangeable、提议者坏了 是不是 already may-diverge interchangeable、任意块 是不是 already req3-same interchangeable。可以跳过「看见两边同判就已经只对诚实提案 interchangeable / 就可以各判各的 interchangeable / 就已经是 Req 3 interchangeable」。不要把 SHOULD Accept 当不确定已经拒坏块。不要另写怎样写 ProcessProposal。340 processdet vs prepare bundled unbundling 在本页 item 2 续（773 + 774）；续 [`worked-example-process-notlostsafety-vs-bundled.md`](worked-example-process-notlostsafety-vs-bundled.md)（不变量 775 item 3）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- ProcessProposal 确定性 bundled。那是不变量 340。
- Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值。那是不变量 340 item 1 余量 / 773。
- Process 非确定 bug 没有现成解法不是已经丢了安全性。那是不变量 340 item 3 余量 / 775。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
- 诚实 Prepare 必须被诚实 Process Accept。那是不变量 347。
