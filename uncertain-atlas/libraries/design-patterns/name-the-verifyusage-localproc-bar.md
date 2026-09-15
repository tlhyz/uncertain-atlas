# 模式：把 VerifyVoteExtension Usage not called for local process 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage 本地票句。  
**例**：[not called for local process ≠ bundled](../../tracks/implementation/worked-example-verifyusage-localproc-vs-bundled.md)。

## 三个名字

1. **not called for local process 不是 local process also Verify：** 看见 is not called for precommit votes sent by local process，不是 353 bundled interchangeable / 515 received from q≠p interchangeable / 438 ExtendVote When interchangeable。
2. **not called for local process 不是 already self-verified：** 看见不调本地票，不是 already Accept interchangeable / 348 Req 6 must Accept interchangeable / 509 return extension interchangeable。
3. **not called for local process 不是 When received from q≠p call：** 看见 Usage 侧 local process，不是 515 step 2 call interchangeable / 514 received from others interchangeable / 521 empty ext still calls interchangeable。

## 为什么要分开叫

官方把 not called for local process、not already self-verified、not When received from q≠p、Verify Usage bundled（353）、Verify When step 2 call（515）、ExtendVote When（438）写成三个名字。把它们叫成一个「看见是本地票就已经自己验过 interchangeable、已经 Accept interchangeable、已经本地票也 Verify interchangeable」，会把 Usage 侧本地票不调、不是已经自己验过、不是 When 收到侧 call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage not called for local process 正式三事，先数清问的是 not called for local process 是不是 local process also Verify、not already self-verified 是不是 Accept、not When received from q≠p 是不是 Verify Usage bundled，再决定要不要同一次发布。
