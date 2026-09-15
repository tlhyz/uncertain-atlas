# 反模式：把 ExtendVote When call / synchronous 正式三事卖成 lock values bundled / ExtendVote 何时调用 bundled / ExtendVote When 正式流程

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[call / synchronous ≠ bundled](../../tracks/implementation/worked-example-extwhen-call-vs-bundled.md)。

## 卖法

- 「看见 calls ExtendVote with v in ExtendVoteRequest 就已经 lock values bundled interchangeable / 已经 step 1 before call interchangeable。」
- 「看见 The call is synchronous 就已经 ExtendVote 何时调用 bundled interchangeable / 已经能在返回之后再改扩展 interchangeable。」
- 「看见 step 2 before return extension 就已经 ExtendVote When 正式流程 interchangeable / 已经广播 Precommit interchangeable。」

## 为什么错

官方把 calls ExtendVote with v、synchronous call、step 2 before return extension 写成三件独立的实现事。把它们卖成 lock values bundled、ExtendVote 何时调用 bundled、ExtendVote When 正式流程，会把 call with v、sync、step 2 顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When call / synchronous 正式三事，必须分开 calls ExtendVote with v、synchronous ExtendVote call、step 2 before return extension 三个名字，不要把它们卖成 lock values bundled / ExtendVote 何时调用 bundled / ExtendVote When 正式流程。

## 和相邻反模式

- [extwhen-lock-sold-as-bundled](extwhen-lock-sold-as-bundled.md) 是 ExtendVote When lock values 三事，不是本页 calls ExtendVote with v 单句专用边界。
- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 ExtendVote 何时调用三事，不是本页 synchronous call 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 step 2 before return extension 单句专用边界。
