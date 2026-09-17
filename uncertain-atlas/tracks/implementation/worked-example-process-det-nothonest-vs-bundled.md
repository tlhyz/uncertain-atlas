# 例：看见两边对任意块同一裁决 is not already only honest same verdict interchangeable / not already Req 3 honest Accept interchangeable / not already settled interchangeable

**层次**：实现 / 两边对任意块同一裁决 not already only honest same verdict / not already Req 3 honest Accept / not already settled 正式三事（340 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5 [`ProcessProposal`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边对任意块同一裁决 not already only honest same verdict / not already Req 3 honest Accept / not already settled 正式三事（340 余量）/ not 894 process-det-nothonest interchangeable / not 340 process-det-vs-prepare bundled interchangeable」，不是 ProcessProposal 确定性 bundled（340），也不是四门已经结算（33），也不是 Req 3 诚实对诚实必须 Accept（347/872）。不要另写怎样写 ProcessProposal。

## 官方三件事

1. **看见两边对任意块同一裁决 / 看见提议者是拜占庭 这份同判 is not already 已经只对诚实提案同一裁决 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 894 process-det-nothonest interchangeable / 893 process-det-notprep interchangeable / 340 process-det item 1 必须确定 interchangeable，也不是已经两边对任意块同一裁决 not already only honest same verdict / not already Req 3 honest Accept / not already settled 正式三事 bundled（340 item 2 余量） interchangeable / 340 process-det item 2 interchangeable。**  
   官方写：Requirement 4 和 5 保证所有正确进程对一份提案的反应相同，即使提议者是拜占庭。看见两边同判，不是已经只对诚实 *u_p* 同判 interchangeable——本页从 340 item 2 侧钉 not already only honest same verdict 单句。340 process-det vs prepare bundled unbundling 在本页 item 2 续。

2. **看见提议者坏了 / 看见任意块 / 这份同判 is not already 已经是诚实 Prepare 必须被诚实 Process Accept interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 894 process-det-nothonest interchangeable / 340 process-det item 3 无解 interchangeable / 895 process-det-notfix interchangeable，也不是已经 Req 3 必须 Accept interchangeable / 347 / 872 req3-notany interchangeable。**  
   官方把任意块和已经是 Req 3 那句诚实对诚实分开——340 bundled 第二件事常与 347 混成「看见两边同判就已经只对诚实提案或已经是 Req 3 Accept interchangeable」，本页钉 not already Req 3 honest Accept 单句。

3. **看见任意块 / 看见两边同判 / 这份同判 is not already 已经交差 interchangeable，也不是已经 ProcessProposal 确定性 bundled（340） interchangeable / 894 process-det-nothonest interchangeable / 893 process-det-notprep interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把任意块和已经可以各判各的 / 已经交差分开。看见提议者坏了，不是已经可以各判各的 interchangeable。340 process-det vs prepare bundled unbundling 在本页 item 2 续。

怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **两边对任意块同一裁决 not already only honest same verdict ≠ 已经只对诚实提案同一裁决 interchangeable：** 官方把拜占庭提议者和诚实对诚实分开。
- **看见任意块 not already Req 3 honest Accept ≠ 已经是诚实 Prepare 必须被诚实 Process Accept interchangeable：** 官方把任意块同判和 Req 3 诚实对诚实分开。
- **看见两边同判 not already settled ≠ 已经交差 interchangeable：** 官方把两边同判和已经交差分开；340 process-det vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边对任意块同一裁决 | 不是已经只对诚实提案同一裁决 | 不是四门已经结算（33） |
| 看见任意块 | 不是已经是诚实 Prepare 必须被诚实 Process Accept | 不是 Req 3 必须 Accept（347/872） |
| 看见两边同判 | 不是已经交差 | 不是 Process 必须确定就已经可以像 Prepare 那样（893） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意块同一裁决 not already only honest same verdict / not already Req 3 honest Accept / not already settled 正式三事（340 余量），必须分开是不是已经只对诚实提案同一裁决、是不是已经是 Req 3 诚实对诚实、是不是已经交差。可以跳过「看见两边同判就已经只对诚实提案」。不要另写怎样写 ProcessProposal。340 process-det vs prepare bundled unbundling 在本页 item 2 续；续 [`worked-example-process-det-notfix-vs-bundled.md`](worked-example-process-det-notfix-vs-bundled.md)（不变量 895 item 3）。

## 本页不抄

- 怎样写 `ProcessProposal`、怎样测确定性、怎样写测试向量。
- ProcessProposal 确定性 bundled。那是不变量 340。
- Process 必须只依赖请求和上一份状态。那是不变量 340 item 1 余量 / 893。
- 四门已经结算。那是不变量 33。
- Req 3 必须 Accept。那是不变量 347 / 872。
