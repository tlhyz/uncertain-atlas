# 例：看见 VerifyVoteExtension 必须只依赖扩展、这块和上一份状态 / 看见必须确定 / 看见 Verify 回了 is not already already like-extend interchangeable / already same-as-nondet interchangeable / already settled interchangeable

**层次**：实现 / Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量）/ not 776 verify-notlikeextend interchangeable / not 341 verifydet bundled interchangeable」，不是 VerifyVoteExtension 确定性 bundled（341），也不是两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决（777 item 2 余量）或 Verify 非确定会伤活性不是已经丢了安全性（778 item 3 余量）。不要另写怎样写 VerifyVoteExtension。

## 官方三件事

规范把 Requirements 里 `VerifyVoteExtension` 必须只依赖扩展、这块和 *s_{h-1}*、必须确定 和「已经是必须确定就可以像 ExtendVote 那样依赖其它值 interchangeable / 已经是只依赖扩展、这块和上一份状态就已经和 ExtendVote 没有确定性要求同一句 interchangeable / 已经是 Verify 回了就已经交差 interchangeable / 已经是 verifydet bundled interchangeable」分开写成三件独立的实现事，不是「看见必须确定就可以像 ExtendVote 那样 interchangeable / 就已经和 ExtendVote nondet 同一句 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 VerifyVoteExtension 必须只依赖扩展、这块和 *s_{h-1}* / 看见必须确定 / 看见是确定函数 is not already 已经可以像 ExtendVote 那样依赖其它值 interchangeable / 已经 like-extend interchangeable / 已经可以依赖其它值交差 interchangeable / 341 verifydet bundled interchangeable / 338 preparenondet interchangeable / verifydet-sold-as-extend interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 776 verify-notlikeextend interchangeable / 341 verifydet item 1 interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事 bundled（341 item 1 余量） interchangeable / 341 verifydet item 1 interchangeable，也不是已经两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决（777） interchangeable / 778 verify-notlostsafety interchangeable / 34 vote-extension interchangeable，也不是已经 ExtendVote 没有确定性要求（338） interchangeable。**  
   官方写：`VerifyVoteExtension` 是当前状态、收到的扩展、以及扩展所指那份提案的**确定**函数。正确进程 *p* 对任意扩展 *e* 和任意块 *w* 叫 Verify，Accept 或 Reject **只**依赖 *e*、*w* 和 *s_{p,h-1}*。看见必须确定，不是已经可以依赖其它值或操作。看见必须确定，不是已经 like-extend interchangeable——341 钉 bundled 三事，本页从 item 1 侧钉 not already like-extend 单句。看见是确定函数，不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable——341 钉 bundled，本页钉 item 1 第一件事。看见必须确定，不是已经 ExtendVote 没有确定性要求（338） interchangeable——338 另钉。341 verifydet vs extend bundled unbundling 在本页 item 1 启动。

2. **看见只依赖扩展、这块和上一份状态 / 看见只依赖 *e*、*w* 和 *s_{h-1}* / 看见不能另依赖其它值 is not already 已经和 ExtendVote 没有确定性要求同一句 interchangeable / 已经 same-as-nondet interchangeable / 已经和 ExtendVote 同一把尺交差 interchangeable / 341 verifydet bundled interchangeable / 338 preparenondet interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 776 verify-notlikeextend interchangeable / 341 verifydet item 2 任意扩展 interchangeable / 341 verifydet item 3 非确定 bug interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事 bundled（341 item 1 余量） interchangeable / 341 verifydet item 1 interchangeable，也不是已经可以像 ExtendVote 那样（本页第一件事） interchangeable。**  
   官方写：看见只依赖扩展、这块和上一份状态，不是已经和「ExtendVote 没有确定性要求」同一句。看见只依赖 *e*、*w* 和 *s_{h-1}*，不是已经 same-as-nondet interchangeable——本页钉 not already same-as-nondet 单句。看见不能另依赖其它值，不是已经可以像 ExtendVote 那样（本页第一件事） interchangeable——三件事分开钉。341 verifydet vs extend bundled unbundling 在本页 item 1 启动。

3. **看见 Verify 回了 / 看见 VerifyVoteExtension 回了 / 看见 Accept 或 Reject 回来了 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差同一句 interchangeable / 341 verifydet bundled interchangeable / 34 vote-extension interchangeable，也不是已经 VerifyVoteExtension 确定性 bundled（341） interchangeable / 776 verify-notlikeextend interchangeable / 341 verifydet item 2 / 341 verifydet item 3，也不是已经 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事 bundled（341 item 1 余量） interchangeable / 341 verifydet item 1 interchangeable，也不是已经可以像 ExtendVote 那样（本页第一件事） interchangeable / 已经和 ExtendVote nondet 同一句（本页第二件事） interchangeable。**  
   官方写：看见 Verify 回了，不是已经交差。看见 VerifyVoteExtension 回了，不是已经 settled interchangeable——本页钉 not already settled 单句。看见 Accept 或 Reject 回来了，不是已经和 ExtendVote nondet 同一句（本页第二件事） interchangeable——三件事分开钉。341 verifydet vs extend bundled unbundling 在本页 item 1 启动。

怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量是规范里的做法，本页不抄。VerifyVoteExtension 确定性 bundled（341）、两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决（341 item 2 余量 / 777）、Verify 非确定会伤活性不是已经丢了安全性（341 item 3 余量 / 778）、ExtendVote 没有确定性要求（338）、验签拒收整张预提交（34）、ProcessProposal 确定性（340）是另外那套，本页不抄。

## 官方为什么这样拆

- **必须确定 not already like-extend ≠ 341 / 338 interchangeable：** 官方把 Verify 必须确定和 ExtendVote 可以不确定分开。
- **只依赖扩展、这块和上一份状态 not already same-as-nondet ≠ 已经和 ExtendVote nondet 同一句 interchangeable：** 官方把只依赖扩展 / 这块 / 上一份状态和 ExtendVote 没有确定性要求分开。
- **Verify 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Verify 回了和已经交差分开；341 verifydet vs extend bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须确定 | 不是 already like-extend | 不是 ExtendVote 没有确定性要求 alone（338） |
| 只依赖扩展、这块和上一份状态 | 不是 already same-as-nondet | 不是验签拒收整张预提交 alone（34） |
| Verify 回了 | 不是 already settled | 不是两边同判就已经只对诚实扩展 alone（777） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量），必须分开必须确定 是不是 already like-extend interchangeable / 341 verifydet bundled interchangeable / verifydet-sold-as-extend interchangeable、只依赖扩展、这块和上一份状态 是不是 already same-as-nondet interchangeable、Verify 回了 是不是 already settled interchangeable。可以跳过「看见必须确定就可以像 ExtendVote 那样 interchangeable / 就已经和 ExtendVote nondet 同一句 interchangeable / 就已经交差 interchangeable」。不要把 SHOULD Accept 当不确定已经拒坏扩展。不要另写怎样写 VerifyVoteExtension。341 verifydet vs extend bundled unbundling 在本页 item 1 启动；续 [`worked-example-verify-nothonestonly-vs-bundled.md`](worked-example-verify-nothonestonly-vs-bundled.md)（不变量 777 item 2）。

## 本页不抄

- 怎样写 `VerifyVoteExtension`、怎样测确定性、怎样写测试向量。
- VerifyVoteExtension 确定性 bundled。那是不变量 341。
- 两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决。那是不变量 341 item 2 余量 / 777。
- Verify 非确定会伤活性不是已经丢了安全性。那是不变量 341 item 3 余量 / 778。
- ExtendVote 没有确定性要求。那是不变量 338。
- 验签拒收整张预提交。那是不变量 34。
- ProcessProposal 确定性。那是不变量 340。
