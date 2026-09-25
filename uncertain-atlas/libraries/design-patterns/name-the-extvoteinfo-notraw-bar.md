# 模式：把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[有签 not already raw ≠ bundled（369）](../../tracks/implementation/worked-example-extvoteinfo-notraw-vs-bundled.md)。

## 三个名字

1. **有签 不是 already raw：** 看见有签 / `extension_signature` 已由引擎验过、交给应用再处理；扩展启用时两份签都在 / 有 extension_signature，不是已经按原样签 interchangeable / 已经 raw interchangeable / 已经按原样签交差 interchangeable，不是 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable。

2. **交给应用 不是 already protected：** 看见交给应用 / 把签交给应用再处理或再验 / 交给应用，不是已经有重放保护 interchangeable / 已经 protected interchangeable / 已经有重放保护交差 interchangeable，不是 358 nonrp interchangeable / 854 extvoteinfo-notfromblock interchangeable。

3. **签了空切片 不是 already must-fill：** 看见签了空切片 / 没给 `non_rp_vote_extension` 就签空切片 / 签空切片，不是已经必须填 interchangeable / 已经 must-fill interchangeable / 已经必须填交差 interchangeable，不是 856 extvoteinfo-notveheight interchangeable / 418 nonrp interchangeable。

官方把有签、不是已经有重放保护、不是已经必须填写成三个名字。把它们叫成一个「看见有签就已经按原样签 interchangeable / 就已经有重放保护 interchangeable / 就已经必须填 interchangeable」，会把 not already raw、not already protected、not already must-fill 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill 正式三事（369 余量），先数清问的是有签 是不是 already raw / 369 / extvoteinfo-sold-as-local，是不是交给应用 是不是 already protected，还是签了空切片 是不是 already must-fill，再决定要不要同一次发布。369 extvoteinfo-vs-local bundled unbundling 在本页 item 2 续。
