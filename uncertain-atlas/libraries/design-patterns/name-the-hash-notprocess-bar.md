# 模式：把请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**例**：[请求里的 hash not already ran-process ≠ bundled（353）](../../tracks/implementation/worked-example-hash-notprocess-vs-bundled.md)。

## 三个名字

1. **有 hash 不是 already ran-process：** 看见请求里的 `hash` / 有 hash / 指向某块，不是已经对该块跑过 `ProcessProposal` interchangeable / 已经 ran-process interchangeable / 已经 Process 过交差 interchangeable，不是 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable。

2. **是同一块 不是 already this-process：** 看见是同一块 / hash 指向同一块 / 同一块身份，不是已经对上这次 Process interchangeable / 已经 this-process interchangeable / 已经对上这次 Process 交差 interchangeable，不是 351 processalso interchangeable / 813 empty-notlocal interchangeable。

3. **不保证 不是 already processalso：** 看见不保证 / 不保证已经暴露给应用 / 规范说不保证，不是已经是提议者那边也会叫 Process interchangeable / 已经 processalso interchangeable / 已经 processalso 交差 interchangeable，不是 812 empty-notskip interchangeable / 351 processalso interchangeable。

官方把有 hash、不是已经对上这次 Process、不是已经是提议者那边也会叫 Process 写成三个名字。把它们叫成一个「看见有 hash 就已经 Process 过 interchangeable / 就已经对上这次 Process interchangeable / 就已经是提议者那边也会叫 Process interchangeable」，会把 not already ran-process、not already this-process、not already processalso 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量），先数清问的是有 hash 是不是 already ran-process / 353 / verifywhen-sold-as-skipped，是不是是同一块 是不是 already this-process，还是不保证 是不是 already processalso，再决定要不要同一次发布。353 verifywhen vs empty bundled unbundling 在本页 item 3 完成。
