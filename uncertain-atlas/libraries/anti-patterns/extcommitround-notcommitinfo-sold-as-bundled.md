# 反模式：把 ExtendedCommitInfo.round not CommitInfo.round / not already ranked / not already settled 正式三事（394 余量） 说成已经是 CommitInfo.round / 已经按投票权排过 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ExtendedCommitInfo.round ≠ bundled（394）](../../tracks/implementation/worked-example-extcommitround-notcommitinfo-vs-bundled.md)。

## 卖法

把 ExtendedCommitInfo 轮这句写成已经已经是 CommitInfo.round / 已经按投票权排过 / 已经交差 interchangeable，或已经和 394 extcommitround-vs-commitinfo bundled / extcommitround-notcommitinfo-sold-as-bundled interchangeable。

## 为什么错

官方把 ExtendedCommitInfo.round / Finalize 请求 next_validators_hash / Echo 请求 Message 三条核心句写成三件独立的实现事。把它们卖成已经是 CommitInfo.round / 已经按投票权排过 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedCommitInfo.round 正式三事（394 余量），必须分开 not CommitInfo.round、not already ranked、not already settled 三件事，不要和 394 / 392 / 750 / 751 糊成一句。

## 和相邻反模式

- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 ExtendedCommitInfo 轮 bundled（394），不是本页 item 1 单句边界。
- [extcommitround-notsamefields-sold-as-bundled](extcommitround-notsamefields-sold-as-bundled.md) 是 next_validators_hash 单句边界（750 item 2），不是本页 round 边界。
