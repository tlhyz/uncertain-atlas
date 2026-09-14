# 模式：把 VerifyVoteExtension Usage empty extension still calls Verify 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage 空扩展句。  
**例**：[empty extension still calls Verify ≠ bundled](../../tracks/implementation/worked-example-verifyusage-emptyext-vs-bundled.md)。

## 三个名字

1. **even for 0-length still calls Verify 不是 skip Verify：** 看见 will call even for 0-length，不是 353 bundled interchangeable / 514 no valid sig discard interchangeable / 437 0 长 ExtendVote interchangeable。
2. **empty extension means sender chose not to extend 不是 0 长就不叫 Verify：** 看见 chose not to extend，不是 skip Verify interchangeable / 0 长就不合法 interchangeable / 437 must fill content interchangeable。
3. **still calls Verify 不是 Verify Usage bundled：** 看见 still calls，不是 353 bundled interchangeable / 522 local process interchangeable / 523 hash Process interchangeable。

## 为什么要分开叫

官方把 even for 0-length、sender chose not to extend、still calls Verify、Verify Usage bundled（353）、Verify When step 1 discard（514）写成三个名字。把它们叫成一个「看见空扩展就已经跳过 Verify interchangeable、已经 0 长就不叫 Verify interchangeable」，会把 0 长仍会 call、选择不扩语义、仍会调 Verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage empty extension still calls Verify 正式三事，先数清问的是 even for 0-length 是不是 skip Verify、empty extension 是不是 0 长就不叫 Verify、still calls 是不是 Verify Usage bundled，再决定要不要同一次发布。
