# 例：看见 VerifyVoteExtensionResponse.status exclusive dependence is not already extend-nondet interchangeable / not already same-ruling interchangeable / not already same-ruler interchangeable

**层次**：实现 / VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量）/ not 1077 vresp-notext interchangeable / not 433 verifyresp-vs-status bundled interchangeable」，不是 Verify 回包栏 bundled（433），也不是 ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样（338），也不是 Verify 必须只依赖扩展、这块和上一份状态那种对任意扩展同一裁决。不要另写怎样写 Verify 回包栏。

## 官方三件事

1. **看见 VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态 / 看见回了 status 这份栏 is not already 已经可以像 ExtendVote 那样依赖其它值 interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1077 vresp-notext interchangeable / 1076 vresp-notinvalid interchangeable / 433 verifyresp item 1 status interchangeable，也不是已经 VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事 bundled（433 item 2 余量） interchangeable / 433 verifyresp item 2 interchangeable。**  
   官方写：VerifyVoteExtension 的实现 MUST 确定。VerifyVoteExtensionResponse.status MUST exclusively depend on VerifyVoteExtensionRequest 里的参数，以及上一份已提交的 Application state。看见回了 status，不是已经可以像 ExtendVote 那样依赖其它值 interchangeable——本页从 433 item 2 侧钉 not already extend-nondet 单句。433 verifyresp vs status bundled unbundling 在本页 item 2 续。

2. **看见必须只依赖请求和上一份状态 / 看见回了 status / 这份栏 is not already 已经和对任意扩展同一裁决一回事 interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1077 vresp-notext interchangeable / 433 verifyresp item 3 should-accept interchangeable / 1078 vresp-nothonest interchangeable，也不是已经 ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样 interchangeable / 338 prepare-nondet interchangeable。**  
   官方把必须只依赖请求和上一份状态和已经和对任意扩展同一裁决一回事分开。看见必须只依赖，不是已经和对任意扩展同一裁决一回事 interchangeable。本页钉 not already same-ruling 单句。

3. **看见有确定要求 / 看见回了 status / 这份栏 is not already 已经和 ExtendVote 同一把尺 interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1077 vresp-notext interchangeable / 1076 vresp-notinvalid interchangeable，也不是已经 Verify 必须只依赖扩展、这块和上一份状态那种对任意扩展同一裁决 interchangeable。**  
   官方把有确定要求和已经和 ExtendVote 同一把尺分开。看见有确定要求，不是已经和 ExtendVote 同一把尺 interchangeable。433 verifyresp vs status bundled unbundling 在本页 item 2 续。

怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet ≠ 已经可以像 ExtendVote 那样依赖其它值 interchangeable：** 官方把 status 的 exclusive dependence 和 ExtendVote 没有确定性要求分开。
- **看见必须只依赖请求和上一份状态 not already same-ruling ≠ 已经和对任意扩展同一裁决一回事 interchangeable：** 官方把 exclusive dependence 和已经和对任意扩展同一裁决一回事分开。
- **看见有确定要求 not already same-ruler ≠ 已经和 ExtendVote 同一把尺 interchangeable：** 官方把有确定要求和已经和 ExtendVote 同一把尺分开；433 verifyresp vs status bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionResponse.status 必须只依赖 VerifyVoteExtensionRequest 和上一份已提交状态 | 不是已经可以像 ExtendVote 那样依赖其它值 | 不是 ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样（338） |
| 看见必须只依赖请求和上一份状态 | 不是已经和对任意扩展同一裁决一回事 | 不是 Verify 必须只依赖扩展、这块和上一份状态那种对任意扩展同一裁决 |
| 看见有确定要求 | 不是已经和 ExtendVote 同一把尺 | 不是 SHOULD Accept 就已经正确进程交出的扩展必须 Accept（1078） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量），必须分开是不是已经可以像 ExtendVote 那样依赖其它值、是不是已经和对任意扩展同一裁决一回事、是不是已经和 ExtendVote 同一把尺。可以跳过「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法」。不要另写怎样写 Verify 回包栏。433 verifyresp vs status bundled unbundling 在本页 item 2 续；续 [`worked-example-vresp-nothonest-vs-bundled.md`](worked-example-vresp-nothonest-vs-bundled.md)（不变量 1078 item 3）。

## 本页不抄

- 怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit。
- Verify 回包栏 bundled。那是不变量 433。
- ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样。那是不变量 338。
- Verify 必须只依赖扩展、这块和上一份状态那种对任意扩展同一裁决。那是相邻 Verify 确定页，不是本页。
