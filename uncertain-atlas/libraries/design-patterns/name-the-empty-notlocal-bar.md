# 模式：把不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**例**：[不对本进程自己发出的 Precommit 调用 not already self-verified ≠ bundled（353）](../../tracks/implementation/worked-example-empty-notlocal-vs-bundled.md)。

## 三个名字

1. **不调本地票 不是 already self-verified：** 看见 `VerifyVoteExtension` 不对本进程自己发出的 Precommit 调用 / 不调本地票 / 是本地票，不是已经自己验过 interchangeable / 已经 self-verified interchangeable / 已经自己验过交差 interchangeable，不是 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable。

2. **是自己签的 不是 already accept：** 看见是自己签的 / 本地签的 Precommit / 本进程发出的票，不是已经 Accept interchangeable / 已经 accept interchangeable / 已经 Accept 交差 interchangeable，不是 348 req6coherence interchangeable / 812 empty-notskip interchangeable。

3. **跳过本地 不是 already req6-done：** 看见跳过本地 / 不调本地 / 本地票被跳过，不是已经过了 Req 6 interchangeable / 已经 req6-done interchangeable / 已经 Req 6 交差 interchangeable，不是 814 hash-notprocess interchangeable / 351 processalso interchangeable。

官方把不调本地票、不是已经 Accept、不是已经过了 Req 6 写成三个名字。把它们叫成一个「看见不调本地票就已经自己验过 interchangeable / 就已经 Accept interchangeable / 就已经过了 Req 6 interchangeable」，会把 not already self-verified、not already accept、not already req6-done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不对本进程自己发出的 Precommit 调用不是已经自己验过 not already self-verified / not already accept / not already req6-done 正式三事（353 余量），先数清问的是不调本地票 是不是 already self-verified / 353 / verifywhen-sold-as-skipped，是不是是自己签的 是不是 already accept，还是跳过本地 是不是 already req6-done，再决定要不要同一次发布。353 verifywhen vs empty bundled unbundling 在本页 item 2 续。
