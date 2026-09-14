# 例：看见 VerifyVoteExtensionResponse.status MUST exclusively depend on request and previous committed state / exclusive dependence is not ExtendVote can depend on other values / status exclusive dependence is not Verify 341 Req 7-8 same ruling 不是已经 Verify 回包栏 bundled interchangeable / 已经可以像 ExtendVote 那样依赖其它值 interchangeable / 已经和对任意扩展同一裁决 interchangeable

**层次**：实现 / VerifyVoteExtension Response status must exclusively depend 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response status MUST exclusively depend 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「status MUST exclusively depend / not ExtendVote can depend on other values / not Verify 341 Req 7-8 same ruling 不是 Verify 回包栏 bundled interchangeable / 不是已经可以像 ExtendVote 那样依赖其它值 interchangeable / 不是已经和对任意扩展同一裁决 interchangeable」，不是 VerifyVoteExtension Response bundled（433），也不是 Verify 341 determinism Req 7-8 bundled，也不是 ExtendVote 没有确定性要求（338）。不要另写怎样写 Verify 回包栏。

## 官方三件事

规范把 VerifyVoteExtension Response 表上 status MUST exclusively depend on VerifyVoteExtensionRequest and previous committed state 写成三件独立的实现事，不是「看见 must exclusively depend 就已经可以像 ExtendVote 那样依赖其它值 interchangeable、已经和对任意扩展同一裁决 interchangeable、已经 correct process 交出的扩展必须 Accept interchangeable」一件事：

1. **看见 `VerifyVoteExtensionResponse.status` MUST exclusively depend on `VerifyVoteExtensionRequest` and previous committed state / 看见 status 必须只依赖请求和上一份已提交状态 不是已经 Verify 回包栏 bundled（433） interchangeable / 已经可以像 ExtendVote 那样依赖其它值 interchangeable / 已经 MUST Accept interchangeable，也不是已经 ExtendVote 没有确定性要求 bundled（338） interchangeable / 已经 ExtendVote 可以依赖其它值 interchangeable，也不是已经 status valid/invalid bundled（433 第一件事 / 535 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 Prepare 没有确定性要求 bundled（338 余量） interchangeable / 已经 Prepare 可以依赖其它值 interchangeable。**  
   官方 VerifyVoteExtension Response 写：`VerifyVoteExtension` MUST be deterministic。`VerifyVoteExtensionResponse.status` MUST **exclusively** depend on `VerifyVoteExtensionRequest` parameters and previous committed Application state。看见 MUST exclusively depend，不是已经 Verify 回包栏 bundled（433） interchangeable——433 钉 bundled 三事，本页钉 exclusive dependence 单句。看见 status 必须只依赖，不是已经 ExtendVote 没有确定性要求（338） interchangeable——338 钉 ExtendVote 可以不确定，本页钉 Verify status exclusive dependence 单句。看见 exclusively depend，不是已经 status valid/invalid（535 余量） interchangeable——535 钉 valid/invalid 语义，本页钉 must exclusively depend 单句。
2. **看见 exclusive dependence is not ExtendVote can depend on other values / 看见必须只依赖不是已经可以像 ExtendVote 那样依赖其它值 不是已经 Verify 回包栏 bundled（433） interchangeable / 已经可以像 ExtendVote 那样依赖其它值 interchangeable，也不是已经 ExtendVote 没有确定性要求 bundled（338） interchangeable / 已经 ExtendVote MAY be non-deterministic interchangeable / 已经 logic can vary interchangeable，也不是已经 Verify 341 MUST deterministic bundled（341） interchangeable / 已经 Verify 必须只依赖请求和上一份状态 interchangeable / 已经和对任意扩展同一裁决 interchangeable，也不是已经 status valid/invalid bundled（535 余量） interchangeable / 已经当成块非法 interchangeable。**  
   官方 VerifyVoteExtension Response 把 status exclusive dependence 和 ExtendVote 可以依赖其它值分开——433 bundled 常被写成「must exclusively depend = 已经可以像 ExtendVote 那样」，本页钉 not ExtendVote can depend 单句。看见 not ExtendVote nondet，不是已经 ExtendVote 没有确定性要求（338） interchangeable——338 钉 ExtendVote 侧没有 MUST deterministic，本页钉 Verify status 必须只依赖单句。看见 exclusive dependence，不是已经 Verify 341 MUST deterministic（341） interchangeable——341 钉 Req 7–8 函数确定性，本页钉 Response status exclusive dependence 单句。
3. **看见 status exclusive dependence is not Verify 341 Req 7-8 same ruling for any extension / 看见 status 必须只依赖不是已经和对任意扩展同一裁决一回事 不是已经 Verify 回包栏 bundled（433） interchangeable / 已经和对任意扩展同一裁决 interchangeable / 已经 correct process 交出的扩展必须 Accept interchangeable，也不是已经 Verify 341 MUST deterministic bundled（341） interchangeable / 已经 Req 7-8 同一裁决 interchangeable / 已经拜占庭扩展也同一裁决 interchangeable，也不是已经 Extend–Verify consistency bundled（348） interchangeable / 已经 correct process must Accept interchangeable，也不是已经 status valid/invalid bundled（535 余量） interchangeable / 已经 SHOULD Accept bundled（527 余量） interchangeable。**  
   官方 VerifyVoteExtension Response 把 status exclusive dependence 和 Verify 341 Req 7–8 确定性通则分开——341 钉 Verify 函数对任意扩展同一裁决，本页钉 status must exclusively depend 不是已经 341 通则 interchangeable 单句。看见 not same ruling general rule，不是已经 Verify 341（341） interchangeable——341 钉 Req 7–8 / 非确定 bug 伤活性，本页钉 Response status exclusive dependence 单句。看见 not correct process must Accept，不是已经 Extend–Verify consistency（348） interchangeable——348 钉 Req 6 must Accept，本页钉 status exclusive dependence 边界。

怎样做写 Verify 回包栏、怎样测确定性 是规范里的做法，本页不抄。Verify 回包栏 bundled（433）、Verify 341 determinism（341）、status valid/invalid（535 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **status MUST exclusively depend ≠ 已经可以像 ExtendVote 那样依赖其它值 interchangeable：** 官方把 Verify status exclusive dependence 和 ExtendVote 可以不确定分开。
- **exclusive dependence not ExtendVote nondet ≠ Verify 341 MUST deterministic interchangeable：** 官方把 Response status 依赖边界和 Req 7–8 函数确定性分开。
- **status exclusive dependence ≠ Verify 341 same ruling for any extension interchangeable：** 官方把 status must exclusively depend 和 341 通则、348 correct process must Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| status MUST exclusively depend | 不是 ExtendVote can depend on other values | 不是 ExtendVote 没有确定性要求（338） |
| exclusive dependence not ExtendVote nondet | 不是 Verify 341 MUST deterministic | 不是 Verify 341 Req 7-8 same ruling（341） |
| status exclusive dependence | 不是 same ruling general rule | 不是 Extend–Verify consistency must Accept（348） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Response status must exclusively depend 正式三事，必须分开 status MUST exclusively depend 是不是已经 ExtendVote can depend on other values interchangeable / 已经 MUST Accept interchangeable、exclusive dependence not ExtendVote nondet 是不是 Verify 341 MUST deterministic interchangeable、status exclusive dependence 是不是 Verify 341 same ruling interchangeable / 348 correct process must Accept interchangeable。可以跳过「看见 must exclusively depend 就已经可以像 ExtendVote 那样依赖其它值 interchangeable」。不要另写怎样写 Verify 回包栏。

## 本页不抄

- 怎样做写 Verify 回包栏、怎样测确定性。
- VerifyVoteExtensionResponse.status valid/invalid 语义。那是不变量 535（433 item 1 余量）。
- 应用 SHOULD always set ACCEPT。那是不变量 527（457 item 1 / 433 Usage 余量）。
- Verify 341 determinism Req 7-8 正式三事 bundled。那是不变量 341。
