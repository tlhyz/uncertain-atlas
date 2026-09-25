# 模式：把扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[空着 not already ve-height ≠ bundled（369）](../../tracks/implementation/worked-example-extvoteinfo-notveheight-vs-bundled.md)。

## 三个名字

1. **空着 不是 already ve-height：** 看见空着 / 扩展关掉则 `vote_extension` / `non_rp_vote_extension` 和对应的签都空 / 扩展字段空，不是已经到了启用高度 interchangeable / 已经 ve-height interchangeable / 已经到了启用高度交差 interchangeable，不是 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable。

2. **关掉了 不是 already settled：** 看见关掉了 / 投票扩展关掉 / 扩展关，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 330 veheight interchangeable / 854 extvoteinfo-notfromblock interchangeable。

3. **字段在 不是 already from-block：** 看见字段在 / 扩展字段仍在报文里 / 字段还在，不是已经从块里抽出 interchangeable / 已经 from-block interchangeable / 已经从块里抽出交差 interchangeable，不是 855 extvoteinfo-notraw interchangeable / 365 voteinfo interchangeable。

官方把空着、不是已经交差、不是已经从块里抽出写成三个名字。把它们叫成一个「看见空着就已经到了启用高度 interchangeable / 就已经交差 interchangeable / 就已经从块里抽出 interchangeable」，会把 not already ve-height、not already settled、not already from-block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量），先数清问的是空着 是不是 already ve-height / 369 / extvoteinfo-sold-as-local，是不是关掉了 是不是 already settled，还是字段在 是不是 already from-block，再决定要不要同一次发布。369 extvoteinfo-vs-local bundled unbundling 在本页 item 3 完成。
