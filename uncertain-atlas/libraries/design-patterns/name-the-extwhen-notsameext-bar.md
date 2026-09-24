# 模式：把回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[回包不解释 not already same-ext ≠ bundled（361）](../../tracks/implementation/worked-example-extwhen-notsameext-vs-bundled.md)。

## 三个名字

1. **回了 不是 already same-ext：** 看见回了 / 应用回了一串字节 `ExtendVoteResponse.extension` / 回了 extension，不是已经是同一份扩展 interchangeable / 已经 same-ext interchangeable / 已经同一份扩展交差 interchangeable，不是 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable。

2. **不解释 不是 already canon-ve：** 看见不解释 / 共识算法不解释 / 引擎不读这些字节，不是已经包进 CanonicalVoteExtension interchangeable / 已经 canon-ve interchangeable / 已经包进 CanonicalVoteExtension 交差 interchangeable，不是 358 nonrp interchangeable / 833 extwhen-notwillcall interchangeable。

3. **有字节 不是 already settled：** 看见有字节 / 回包有 extension 字段 / 字节数组在，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 834 extwhen-notlaterrevise interchangeable / 33 fourgates interchangeable。

官方把回了、不是已经包进 CanonicalVoteExtension、不是已经交差写成三个名字。把它们叫成一个「看见回了就已经是同一份扩展 interchangeable / 就已经包进 CanonicalVoteExtension interchangeable / 就已经交差 interchangeable」，会把 not already same-ext、not already canon-ve、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量），先数清问的是回了 是不是 already same-ext / 361 / extendwhen-sold-as-locked，是不是不解释 是不是 already canon-ve，还是有字节 是不是 already settled，再决定要不要同一次发布。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。
