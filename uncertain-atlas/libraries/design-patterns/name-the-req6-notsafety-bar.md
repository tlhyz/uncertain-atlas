# 模式：把会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**例**：[会面对和 Req 5 同一类活性问题 not already lost-safety ≠ bundled（348）](../../tracks/implementation/worked-example-req6-notsafety-vs-bundled.md)。

## 三个名字

1. **会面对和 Req 5 同一类活性问题 不是 already lost-safety：** 看见会面对和 Requirement 5 同一类活性问题 / 会伤活性 / 和 Process 确定性那条同一路，不是已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable，不是 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable。

2. **和 Req 5 同一路 不是 already req3-same：** 看见和 Req 5 同一路 / 和 Process 确定性那条同一路 / 同一类活性问题，不是已经是 347 那种提案一致性 interchangeable / 已经 req3-same interchangeable / 已经提案一致性交差 interchangeable，不是 347 req3coherence interchangeable / 340 processdet interchangeable。

3. **扩展这条 不是 already proposal-path：** 看见扩展这条 / Extend–Verify 这条活性 / Req 6 这条，不是已经是提案那条 interchangeable / 已经 proposal-path interchangeable / 已经提案路径交差 interchangeable，不是 797 req6-notany interchangeable / 798 req6-notliveness interchangeable。

官方把会面对和 Req 5 同一类活性问题、不是已经是提案一致性、不是已经是提案那条写成三个名字。把它们叫成一个「看见会伤活性就已经丢了安全性 interchangeable / 就已经是提案一致性 interchangeable / 就已经是提案那条 interchangeable」，会把 not already lost-safety、not already req3-same、not already proposal-path 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看会面对和 Req 5 同一类活性问题不是已经丢了安全性 not already lost-safety / not already req3-same / not already proposal-path 正式三事（348 余量），先数清问的是会面对和 Req 5 同一类活性问题 是不是 already lost-safety / 348 / req6coherence-sold-as-accept，是不是和 Req 5 同一路 是不是 already req3-same，还是扩展这条 是不是 already proposal-path，再决定要不要同一次发布。348 req6 vs accept bundled unbundling 在本页 item 3 完成。
