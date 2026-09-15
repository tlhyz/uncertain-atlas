# 反模式：把 VerifyVoteExtension Response status must exclusively depend 正式三事卖成 Verify 回包栏 bundled / 已经可以像 ExtendVote 那样依赖其它值 / 已经和对任意扩展同一裁决 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[status must exclusively depend ≠ bundled](../../tracks/implementation/worked-example-verifyrespstatus-exclusivedep-vs-bundled.md)。

## 卖法

- 「看见 VerifyVoteExtensionResponse.status 必须只依赖请求和上一份已提交状态 就已经 Verify 回包栏 bundled interchangeable / 已经可以像 ExtendVote 那样依赖其它值 interchangeable。」
- 「看见 MUST exclusively depend 就已经 ExtendVote 没有确定性要求 interchangeable / 已经 ExtendVote logic can vary interchangeable。」
- 「看见 status 必须只依赖 就已经 Verify 341 Req 7-8 同一裁决 interchangeable / 已经 correct process 交出的扩展必须 Accept interchangeable。」

## 为什么错

官方把 status MUST exclusively depend、exclusive dependence not ExtendVote nondet、status exclusive dependence not Verify 341 same ruling 写成三件独立的实现事。把它们卖成 Verify 回包栏 bundled、已经可以像 ExtendVote 那样依赖其它值、已经和对任意扩展同一裁决 interchangeable，会把 exclusive dependence、ExtendVote 边界、341 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Response status must exclusively depend 正式三事，必须分开 status MUST exclusively depend、exclusive dependence not ExtendVote nondet、status exclusive dependence not Verify 341 same ruling 三个名字，不要把它们卖成 Verify 回包栏 bundled / 已经可以像 ExtendVote 那样依赖其它值 / 已经和对任意扩展同一裁决 interchangeable。

## 和相邻反模式

- [verifyrespstatus-sold-as-verifystatus](verifyrespstatus-sold-as-verifystatus.md) 是 433 bundled 三事专用；本页是 status must exclusively depend 单句边界。
- [verifyrespstatus-validinvalid-sold-as-bundled](verifyrespstatus-validinvalid-sold-as-bundled.md) 是 status valid/invalid 专用，不是本页 exclusive dependence 边界。
- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 Verify 341 determinism 通则，不是本页 Response status exclusive dependence 边界。
