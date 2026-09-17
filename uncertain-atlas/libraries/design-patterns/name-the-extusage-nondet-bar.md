# 模式：把 ExtendVote Usage extension creation logic can be non-deterministic 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage non-deterministic 句。  
**例**：[logic can be non-deterministic ≠ bundled](../../tracks/implementation/worked-example-extusage-nondet-vs-bundled.md)。

## 三个名字

1. **logic can be non-deterministic 不是 must same extension：** 看见造扩展逻辑可以非确定，不是 437 bundled interchangeable / 430 Verify MUST deterministic interchangeable / 509 must return same bytes interchangeable。
2. **logic can vary / same block ≠ same extension 不是 ExtendVote Usage bundled：** 看见逻辑可以变，不是 437 bundled interchangeable / 509 not interpreted interchangeable / 338 ExtendVote no det req at Req interchangeable。
3. **no MUST deterministic for ExtendVote 不是 Verify MUST deterministic：** 看见 ExtendVote 没有这道 MUST，不是 430 Verify MUST interchangeable / 340 Process MUST interchangeable / 437 bundled interchangeable。

## 为什么要分开叫

官方把 logic can be non-deterministic、logic can vary / same block does not imply same extension、no MUST deterministic for ExtendVote unlike Verify、ExtendVote Usage bundled（437）、VerifyVoteExtension MUST be deterministic（430）、ExtendVote 没有确定性要求 at Req（338）写成三个名字。把它们叫成一个「看见可以非确定 就已经必须同一份扩展 interchangeable、已经 Verify 必须确定 interchangeable」，会把 creation logic 非确定、logic can vary、ExtendVote 没有 MUST deterministic 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage extension creation logic can be non-deterministic 正式三事，先数清问的是 logic can be non-deterministic 是不是 must same extension、logic can vary 是不是 same block implies same extension、no MUST for ExtendVote 是不是 Verify MUST deterministic，再决定要不要同一次发布。
