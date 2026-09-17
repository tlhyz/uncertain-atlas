# 模式：把 Prepare 回包校验 crash not Process REJECT / not must Accept / not ProposalStatus REJECT 正式三事（357 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[crash ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notcrash-vs-bundled.md)。

## 三个名字

1. **crash 不是已经是 Process REJECT：** 看见崩了，不是已经 455 interchangeable / 717 prepvalid-notcrash interchangeable。
2. **看见回包坏了 不是 honest proposal 必须 Accept：** 看见引擎停了，不是已经 347 interchangeable。
3. **看见崩溃了 不是 ProposalStatus REJECT：** 看见 Prepare crash，不是已经 376 / 504 interchangeable。

官方把 Prepare 回包校验三条核心句拆成三个名字。把它们叫成一个「看见回了提案就已经验过重复」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 crash 正式三事（357 余量），先数清问的是崩溃是不是 Process REJECT / 455、是不是 Req 3 必须 Accept / 347、还是看见崩了是不是 376 / 504，再决定要不要同一次发布。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。
