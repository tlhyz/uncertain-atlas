# 例：看见两边对任意扩展同一裁决 is not already only honest same verdict interchangeable / not already Req 6 honest Accept interchangeable / not already settled interchangeable

**层次**：实现 / 两边对任意扩展同一裁决 not already only honest same verdict / not already Req 6 honest Accept / not already settled 正式三事（341 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边对任意扩展同一裁决 not already only honest same verdict / not already Req 6 honest Accept / not already settled 正式三事（341 余量）/ not 891 verify-det-nothonest interchangeable / not 341 verify-det-vs-extend bundled interchangeable」，不是 VerifyVoteExtension 确定性 bundled（341），也不是验签拒收已经是块非法（34），也不是 Req 6 诚实对诚实必须 Accept（348/869）。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

1. **看见两边对任意扩展同一裁决 / 看见扩展来自拜占庭 这份同判 is not already 已经只对诚实扩展同一裁决 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 891 verify-det-nothonest interchangeable / 890 verify-det-notext interchangeable / 341 verify-det item 1 必须确定 interchangeable，也不是已经两边对任意扩展同一裁决 not already only honest same verdict / not already Req 6 honest Accept / not already settled 正式三事 bundled（341 item 2 余量） interchangeable / 341 verify-det item 2 interchangeable。**  
   官方写：Requirement 7 和 8 保证所有正确进程对一份扩展的反应相同，用来挡住拜占庭进程送来的任意扩展数据，和 Requirement 4、5 挡住任意提案同一路。看见两边同判，不是已经只对诚实 *e_p* 同判 interchangeable——本页从 341 item 2 侧钉 not already only honest same verdict 单句。341 verify-det vs extend bundled unbundling 在本页 item 2 续。

2. **看见扩展坏了 / 看见任意扩展 / 这份同判 is not already 已经是诚实扩展必须被诚实 Verify Accept interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 891 verify-det-nothonest interchangeable / 341 verify-det item 3 活性 interchangeable / 892 verify-det-notsafety interchangeable，也不是已经 Req 6 必须 Accept interchangeable / 348 / 869 req6-notany interchangeable。**  
   官方把任意扩展和已经是 Req 6 那句诚实对诚实分开——341 bundled 第二件事常与 348 混成「看见两边同判就已经只对诚实扩展或已经是 Req 6 Accept interchangeable」，本页钉 not already Req 6 honest Accept 单句。

3. **看见任意扩展 / 看见两边同判 / 这份同判 is not already 已经交差 interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 891 verify-det-nothonest interchangeable / 890 verify-det-notext interchangeable，也不是已经验签拒收已经是块非法 interchangeable / 34 sig-reject interchangeable。**  
   官方把任意扩展和已经可以各判各的 / 已经交差分开。看见扩展坏了，不是已经可以各判各的 interchangeable。341 verify-det vs extend bundled unbundling 在本页 item 2 续。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **两边对任意扩展同一裁决 not already only honest same verdict ≠ 已经只对诚实扩展同一裁决 interchangeable：** 官方把拜占庭扩展数据和诚实对诚实分开。
- **看见任意扩展 not already Req 6 honest Accept ≠ 已经是诚实扩展必须被诚实 Verify Accept interchangeable：** 官方把任意扩展同判和 Req 6 诚实对诚实分开。
- **看见两边同判 not already settled ≠ 已经交差 interchangeable：** 官方把两边同判和已经交差分开；341 verify-det vs extend bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边对任意扩展同一裁决 | 不是已经只对诚实扩展同一裁决 | 不是验签拒收已经是块非法（34） |
| 看见任意扩展 | 不是已经是诚实扩展必须被诚实 Verify Accept | 不是 Req 6 必须 Accept（348/869） |
| 看见两边同判 | 不是已经交差 | 不是 Verify 必须确定就已经可以像 ExtendVote 那样（890） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意扩展同一裁决 not already only honest same verdict / not already Req 6 honest Accept / not already settled 正式三事（341 余量），必须分开是不是已经只对诚实扩展同一裁决、是不是已经是 Req 6 诚实对诚实、是不是已经交差。可以跳过「看见两边同判就已经只对诚实扩展」。不要另写怎样写 VerifyVoteExtension。341 verify-det vs extend bundled unbundling 在本页 item 2 续；续 [`worked-example-verify-det-notsafety-vs-bundled.md`](worked-example-verify-det-notsafety-vs-bundled.md)（不变量 892 item 3）。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- VerifyVoteExtension 确定性 bundled。那是不变量 341。
- Verify 必须只依赖扩展、这块和上一份状态。那是不变量 341 item 1 余量 / 890。
- 验签拒收已经是块非法。那是不变量 34。
- Req 6 必须 Accept。那是不变量 348 / 869。
