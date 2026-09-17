# 反模式：把 CommitInfo.round not already ranked / not already slashed / not already settled 正式三事（392 余量） 说成已经按投票权排过 / 已经罚没 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[CommitInfo.round ≠ bundled（392）](../../tracks/implementation/worked-example-initapphash-notranked-vs-bundled.md)。

## 卖法

把 InitChain 回包余栏这句写成已经已经按投票权排过 / 已经罚没 / 已经交差 interchangeable，或已经和 392 initapphash-vs-header bundled / initapphash-notranked-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain 回包 app_hash / Finalize 请求 hash / CommitInfo.round 三条核心句写成三件独立的实现事。把它们卖成已经按投票权排过 / 已经罚没 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CommitInfo.round 正式三事（392 余量），必须分开 not already ranked、not already slashed、not already settled 三件事，不要和 392 / 365 / 394 / 749 / 755 / 756 糊成一句。

## 和相邻反模式

- [initapphash-sold-as-header](initapphash-sold-as-header.md) 是 InitChain 回包余栏 bundled（392），不是本页 item 3 单句边界。
- [extcommitround-notcommitinfo-sold-as-bundled](extcommitround-notcommitinfo-sold-as-bundled.md) 是 ExtendedCommitInfo.round 就已经是 CommitInfo.round（394/749），不是本页 CommitInfo.round 边界。
