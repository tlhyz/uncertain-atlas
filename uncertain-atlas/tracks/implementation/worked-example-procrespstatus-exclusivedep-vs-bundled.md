# 例：看见 ProcessProposalResponse.status MUST exclusively depend on request and previous committed state / exclusive dependence is not Prepare can depend on other values / status exclusive dependence is not Process 340 Req 4-5 same ruling 不是已经 Process 回包栏 bundled interchangeable / 已经可以像 Prepare 那样依赖其它值 interchangeable / 已经和对任意块同一裁决 interchangeable

**层次**：实现 / ProcessProposal Response status must exclusively depend 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response status MUST exclusively depend 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「status MUST exclusively depend / not Prepare can depend on other values / not Process 340 Req 4-5 same ruling 不是 Process 回包栏 bundled interchangeable / 不是已经可以像 Prepare 那样依赖其它值 interchangeable / 不是已经和对任意块同一裁决 interchangeable」，不是 ProcessProposal Response bundled（430），也不是 Process 340 determinism Req 4-5 bundled，也不是 Prepare 没有确定性要求（338）。不要另写怎样写 Process 回包栏。

## 官方三件事

规范把 ProcessProposal Response 表上 status MUST exclusively depend on ProcessProposalRequest and previous committed state 写成三件独立的实现事，不是「看见 must exclusively depend 就已经可以像 Prepare 那样依赖其它值 interchangeable、已经和对任意块同一裁决 interchangeable、已经 honest proposal 必须 Accept interchangeable」一件事：

1. **看见 `ProcessProposalResponse.status` MUST exclusively depend on `ProcessProposalRequest` and previous committed state / 看见 status 必须只依赖请求和上一份已提交状态 不是已经 Process 回包栏 bundled（430） interchangeable / 已经可以像 Prepare 那样依赖其它值 interchangeable / 已经 MUST Accept interchangeable，也不是已经 Prepare 没有确定性要求 bundled（338） interchangeable / 已经 Prepare 可以依赖其它值 interchangeable，也不是已经 status valid/invalid bundled（430 第一件事 / 537 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 ExtendVote 没有确定性要求 bundled（338 余量） interchangeable / 已经 ExtendVote 可以依赖其它值 interchangeable。**  
   官方 ProcessProposal Response 写：`ProcessProposal` MUST be deterministic。`ProcessProposalResponse.status` MUST **exclusively** depend on `ProcessProposalRequest` parameters and previous committed Application state。看见 MUST exclusively depend，不是已经 Process 回包栏 bundled（430） interchangeable——430 钉 bundled 三事，本页钉 exclusive dependence 单句。看见 status 必须只依赖，不是已经 Prepare 没有确定性要求（338） interchangeable——338 钉 Prepare 可以不确定，本页钉 Process status exclusive dependence 单句。看见 exclusively depend，不是已经 status valid/invalid（537 余量） interchangeable——533 钉 valid/invalid 语义，本页钉 must exclusively depend 单句。
2. **看见 exclusive dependence is not Prepare can depend on other values / 看见必须只依赖不是已经可以像 Prepare 那样依赖其它值 不是已经 Process 回包栏 bundled（430） interchangeable / 已经可以像 Prepare 那样依赖其它值 interchangeable，也不是已经 Prepare 没有确定性要求 bundled（338） interchangeable / 已经 Prepare MAY be non-deterministic interchangeable / 已经 Prepare 可以改列表 interchangeable，也不是已经 Process 340 MUST deterministic bundled（340） interchangeable / 已经 Process 必须只依赖请求和上一份状态 interchangeable / 已经和对任意块同一裁决 interchangeable，也不是已经 status valid/invalid bundled（537 余量） interchangeable / 已经当成块非法 interchangeable。**  
   官方 ProcessProposal Response 把 status exclusive dependence 和 Prepare 可以依赖其它值分开——430 bundled 常被写成「must exclusively depend = 已经可以像 Prepare 那样」，本页钉 not Prepare can depend 单句。看见 not Prepare nondet，不是已经 Prepare 没有确定性要求（338） interchangeable——338 钉 Prepare 侧没有 MUST deterministic，本页钉 Process status 必须只依赖单句。看见 exclusive dependence，不是已经 Process 340 MUST deterministic（340） interchangeable——340 钉 Req 4-5 函数确定性，本页钉 Response status exclusive dependence 单句。
3. **看见 status exclusive dependence is not Process 340 Req 4-5 same ruling for any block / 看见 status 必须只依赖不是已经和对任意块同一裁决一回事 不是已经 Process 回包栏 bundled（430） interchangeable / 已经和对任意块同一裁决 interchangeable / 已经 honest proposal 必须 Accept interchangeable，也不是已经 Process 340 MUST deterministic bundled（340） interchangeable / 已经 Req 4-5 同一裁决 interchangeable / 已经拜占庭提议者也同一裁决 interchangeable，也不是已经 honest proposal must Accept at Req bundled（347） interchangeable / 已经 correct proposer must Accept interchangeable，也不是已经 status valid/invalid bundled（537 余量） interchangeable / 已经 SHOULD Accept bundled（530 余量） interchangeable。**  
   官方 ProcessProposal Response 把 status exclusive dependence 和 Process 340 Req 4-5 确定性通则分开——340 钉 Process 函数对任意块同一裁决，本页钉 status must exclusively depend 不是已经 340 通则 interchangeable 单句。看见 not same ruling general rule，不是已经 Process 340（340） interchangeable——340 钉 Req 4-5 / 非确定 bug 伤活性，本页钉 Response status exclusive dependence 单句。看见 not honest proposal must Accept，不是已经 honest proposal must Accept at Req（347） interchangeable——347 钉 Req 3 must Accept，本页钉 status exclusive dependence 边界。

怎样做写 Process 回包栏、怎样测确定性 是规范里的做法，本页不抄。Process 回包栏 bundled（430）、Process 340 determinism（340）、status valid/invalid（537 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **status MUST exclusively depend ≠ 已经可以像 Prepare 那样依赖其它值 interchangeable：** 官方把 Process status exclusive dependence 和 Prepare 可以不确定分开。
- **exclusive dependence not Prepare nondet ≠ Process 340 MUST deterministic interchangeable：** 官方把 Response status 依赖边界和 Req 4-5 函数确定性分开。
- **status exclusive dependence ≠ Process 340 same ruling for any block interchangeable：** 官方把 status must exclusively depend 和 340 通则、347 honest proposal must Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| status MUST exclusively depend | 不是 Prepare can depend on other values | 不是 Prepare 没有确定性要求（338） |
| exclusive dependence not Prepare nondet | 不是 Process 340 MUST deterministic | 不是 Process 340 Req 4-5 same ruling（340） |
| status exclusive dependence | 不是 same ruling general rule | 不是 honest proposal must Accept at Req（347） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Response status must exclusively depend 正式三事，必须分开 status MUST exclusively depend 是不是已经 Prepare can depend on other values interchangeable / 已经 MUST Accept interchangeable、exclusive dependence not Prepare nondet 是不是 Process 340 MUST deterministic interchangeable、status exclusive dependence 是不是 Process 340 same ruling interchangeable / 347 honest proposal must Accept interchangeable。可以跳过「看见 must exclusively depend 就已经可以像 Prepare 那样依赖其它值 interchangeable」。不要另写怎样写 Process 回包栏。

## 本页不抄

- 怎样做写 Process 回包栏、怎样测确定性。
- ProcessProposalResponse.status valid/invalid 语义。那是不变量 537（430 item 1 余量）。
- 应用 SHOULD always set ACCEPT。那是不变量 530（456 item 1 / 430 Usage 余量）。
- Process 340 determinism Req 4-5 正式三事 bundled。那是不变量 340。
