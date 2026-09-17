# 反模式：把 Finalize 请求 next_validators_hash not already same fields / not already swapped / not already settled 正式三事（394 余量） 说成已经是同一套字段 / 已经换了人 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Finalize ≠ bundled（394）](../../tracks/implementation/worked-example-extcommitround-notsamefields-vs-bundled.md)。

## 卖法

把 ExtendedCommitInfo 轮这句写成已经已经是同一套字段 / 已经换了人 / 已经交差 interchangeable，或已经和 394 extcommitround-vs-commitinfo bundled / extcommitround-notsamefields-sold-as-bundled interchangeable。

## 为什么错

官方把 ExtendedCommitInfo.round / Finalize 请求 next_validators_hash / Echo 请求 Message 三条核心句写成三件独立的实现事。把它们卖成已经是同一套字段 / 已经换了人 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求 next_validators_hash 正式三事（394 余量），必须分开 not already same fields、not already swapped、not already settled 三件事，不要和 394 / 359 / 749 / 751 糊成一句。

## 和相邻反模式

- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 ExtendedCommitInfo 轮 bundled（394），不是本页 item 2 单句边界。
- [extcommitround-notcommitinfo-sold-as-bundled](extcommitround-notcommitinfo-sold-as-bundled.md) 是 round 单句边界（749 item 1），不是本页 next_validators_hash 边界。
