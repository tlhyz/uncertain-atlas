# 反模式：把回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量）说成已经是同一份扩展 / 已经包进 CanonicalVoteExtension / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回包不解释 not already same-ext ≠ bundled（361）](../../tracks/implementation/worked-example-extwhen-notsameext-vs-bundled.md)。

## 卖法

把回了 / 应用回了一串字节 `ExtendVoteResponse.extension` / 回了 extension 写成已经是同一份扩展 interchangeable / 已经 same-ext interchangeable / 已经同一份扩展交差 interchangeable / 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable；把不解释 / 共识算法不解释 写成已经包进 CanonicalVoteExtension interchangeable / 已经 canon-ve interchangeable / 已经包进 CanonicalVoteExtension 交差 interchangeable；把有字节 / 回包有 extension 字段 / 字节数组在 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 361 extendwhen bundled / extendwhen-sold-as-locked interchangeable / 835 extwhen-notsameext interchangeable。

## 为什么错

官方把回了、不是已经包进 CanonicalVoteExtension、不是已经交差写成三件独立的实现事。把它们卖成 already same-ext interchangeable / already canon-ve interchangeable / already settled interchangeable，会把 not already same-ext、not already canon-ve、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包字节不被共识算法解释不是已经是同一份扩展 not already same-ext / not already canon-ve / not already settled 正式三事（361 余量），必须分开 not already same-ext、not already canon-ve、not already settled 三件事，不要和 361 / 338 / 358 / 833 / 834 糊成一句。

## 和相邻反模式

- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 ExtendVote 何时调用 bundled 全段，不是本页回了 item 3 单句边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 ExtendVote 没有确定性要求就已经是同一份扩展（338），不是本页 not already same-ext 边界。
- [extwhen-notlaterrevise-sold-as-bundled](extwhen-notlaterrevise-sold-as-bundled.md) 是 ExtendVote 同步 not already later-revise（361 item 2），不是本页 not already settled 边界。
