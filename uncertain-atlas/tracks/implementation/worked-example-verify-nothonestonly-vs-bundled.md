# 例：看见两边对任意扩展同一裁决 / 看见扩展来自拜占庭 / 看见任意扩展 is not already already honest-only interchangeable / already may-diverge interchangeable / already req6-same interchangeable

**层次**：实现 / 两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量）/ not 777 verify-nothonestonly interchangeable / not 341 verifydet bundled interchangeable」，不是 VerifyVoteExtension 确定性 bundled（341），也不是 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值（776 item 1 余量）或 Verify 非确定会伤活性不是已经丢了安全性（778 item 3 余量）。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

规范把 Requirements 里两边对任意扩展同一裁决、扩展来自拜占庭 和「已经是两边同判就已经只对诚实扩展同判 interchangeable / 已经是扩展坏了就可以各判各的 interchangeable / 已经是任意扩展就已经是 Req 6 诚实对诚实 interchangeable / 已经是 verifydet bundled interchangeable」分开写成三件独立的实现事，不是「看见两边同判就已经只对诚实扩展 interchangeable / 就可以各判各的 interchangeable / 就已经是 Req 6 interchangeable」一件事：

1. **看见两边对任意扩展同一裁决 / 看见两边同判 / 看见所有正确进程对一份扩展反应相同 is not already 已经只对诚实扩展同一裁决 interchangeable / 已经 honest-only interchangeable / 已经只对诚实 *e_p* 同判交差 interchangeable / 341 verifydet bundled interchangeable / 348 req6-coherence interchangeable / verifydet-sold-as-extend interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 777 verify-nothonestonly interchangeable / 341 verifydet item 2 interchangeable，也不是已经两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事 bundled（341 item 2 余量） interchangeable / 341 verifydet item 2 interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值（776） interchangeable / 778 verify-notlostsafety interchangeable / 34 vote-extension interchangeable，也不是已经诚实扩展必须被诚实 Verify Accept（348） interchangeable。**  
   官方写：Requirement 7 和 8 保证所有正确进程对一份扩展的反应相同，用来挡住拜占庭进程送来的**任意**扩展数据，和 Requirement 4、5 挡住任意提案同一路。看见两边同判，不是已经只对诚实 *e_p* 同判。看见两边同判，不是已经 honest-only interchangeable——341 钉 bundled 三事，本页从 item 2 侧钉 not already honest-only 单句。看见所有正确进程对一份扩展反应相同，不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable——341 钉 bundled，本页钉 item 2 第一件事。看见两边同判，不是已经诚实扩展必须被诚实 Verify Accept（348） interchangeable——348 另钉。341 verifydet vs extend bundled unbundling 在本页 item 2 续。

2. **看见扩展来自拜占庭 / 看见扩展坏了 / 看见扩展可以不诚实 is not already 已经可以各判各的 interchangeable / 已经 may-diverge interchangeable / 已经各判各的交差 interchangeable / 341 verifydet bundled interchangeable / 34 vote-extension interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 777 verify-nothonestonly interchangeable / 341 verifydet item 1 像 ExtendVote interchangeable / 341 verifydet item 3 非确定 bug interchangeable，也不是已经两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事 bundled（341 item 2 余量） interchangeable / 341 verifydet item 2 interchangeable，也不是已经只对诚实扩展同判（本页第一件事） interchangeable。**  
   官方写：看见扩展坏了，不是已经可以各判各的。看见扩展来自拜占庭，不是已经 may-diverge interchangeable——本页钉 not already may-diverge 单句。看见扩展可以不诚实，不是已经只对诚实扩展同判（本页第一件事） interchangeable——三件事分开钉。341 verifydet vs extend bundled unbundling 在本页 item 2 续。

3. **看见任意扩展 / 看见对任意扩展 *e* / 看见不是只对诚实交出的扩展 is not already 已经是 Req 6 诚实对诚实 interchangeable / 已经 req6-same interchangeable / 已经诚实对诚实交差 interchangeable / 341 verifydet bundled interchangeable / 348 req6-coherence interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 777 verify-nothonestonly interchangeable / 341 verifydet item 1 / 341 verifydet item 3，也不是已经两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事 bundled（341 item 2 余量） interchangeable / 341 verifydet item 2 interchangeable，也不是已经只对诚实扩展同判（本页第一件事） interchangeable / 已经可以各判各的（本页第二件事） interchangeable。**  
   官方写：看见任意扩展，不是已经是 Req 6 那句诚实对诚实。看见对任意扩展 *e*，不是已经 req6-same interchangeable——本页钉 not already req6-same 单句。看见不是只对诚实交出的扩展，不是已经可以各判各的（本页第二件事） interchangeable——三件事分开钉。341 verifydet vs extend bundled unbundling 在本页 item 2 续。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。VerifyVoteExtension 确定性 bundled（341）、Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值（341 item 1 余量 / 776）、Verify 非确定会伤活性不是已经丢了安全性（341 item 3 余量 / 778）、ExtendVote 没有确定性要求（338）、验签拒收整张预提交（34）、诚实扩展必须被诚实 Verify Accept（348）是另外那套，本页不抄。

## 官方为什么这样拆

- **两边同判 not already honest-only ≠ 341 / 348 interchangeable：** 官方把拜占庭扩展数据下的同判和只对诚实扩展同判分开。
- **扩展坏了 not already may-diverge ≠ 已经可以各判各的 interchangeable：** 官方把扩展坏了和已经可以各判各的分开。
- **任意扩展 not already req6-same ≠ 已经是 Req 6 interchangeable：** 官方把任意扩展同判和 Req 6 诚实对诚实分开；341 verifydet vs extend bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边同判 | 不是 already honest-only | 不是诚实扩展必须被诚实 Verify Accept alone（348） |
| 扩展坏了 | 不是 already may-diverge | 不是必须确定就已经可以像 ExtendVote 那样 alone（776） |
| 任意扩展 | 不是 already req6-same | 不是非确定 bug 就已经丢了安全性 alone（778） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 not already honest-only / not already may-diverge / not already req6-same 正式三事（341 余量），必须分开两边同判 是不是 already honest-only interchangeable / 341 verifydet bundled interchangeable / verifydet-sold-as-extend interchangeable、扩展坏了 是不是 already may-diverge interchangeable、任意扩展 是不是 already req6-same interchangeable。可以跳过「看见两边同判就已经只对诚实扩展 interchangeable / 就可以各判各的 interchangeable / 就已经是 Req 6 interchangeable」。不要把 SHOULD Accept 当不确定已经拒坏扩展。不要另写怎样写 VerifyVoteExtension。341 verifydet vs extend bundled unbundling 在本页 item 2 续（776 + 777）；续 [`worked-example-verify-notlostsafety-vs-bundled.md`](worked-example-verify-notlostsafety-vs-bundled.md)（不变量 778 item 3）已写；完成见 778。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- VerifyVoteExtension 确定性 bundled。那是不变量 341。
- Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值。那是不变量 341 item 1 余量 / 776。
- Verify 非确定会伤活性不是已经丢了安全性。那是不变量 341 item 3 余量 / 778。
- ExtendVote 没有确定性要求。那是不变量 338。
- 验签拒收整张预提交。那是不变量 34。
- 诚实扩展必须被诚实 Verify Accept。那是不变量 348。
