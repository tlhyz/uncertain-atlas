# 模式：把 PrepareProposal When +2/3 late extensions not verified 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**例**：[+2/3 late extensions not verified ≠ bundled](../../tracks/implementation/worked-example-preparewhen-lateext-unverified-vs-bundled.md)。

## 三个名字

1. **+2/3 commit info extensions not verified 不是迟到扩展 bundled：** 看见 after minimum +2/3 not verified，不是 352 bundled interchangeable / 已经 Verify 过 interchangeable / 518 MAY add interchangeable。
2. **MAY use commit info extensions to modify proposal 不是已经 Verify 过：** 看见 MAY use extensions，不是 435 Verify When interchangeable / 330 H already Prepare interchangeable / 359 local_last_commit interchangeable。
3. **suggested validate like VerifyVoteExtension 不是引擎会再 Verify：** 看见 suggested validate，不是 352 第二件事 bundled interchangeable / 515 step 2 call interchangeable / 348 Req 6 must Accept interchangeable。

## 为什么要分开叫

官方把 not verified、MAY use extensions、suggested validate like Verify、迟到扩展 bundled（352）、Verify When steps（514–517）、MAY add without Verify（518）写成三个名字。把它们叫成一个「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经是引擎会再 Verify interchangeable」，会把未 Verify、MAY 使用、建议自验三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When +2/3 late extensions not verified 正式三事，先数清问的是 +2/3 commit info extensions not verified 是不是迟到扩展 bundled interchangeable、suggested validate like Verify 是不是已经是引擎会再 Verify interchangeable，再决定要不要同一次发布。
