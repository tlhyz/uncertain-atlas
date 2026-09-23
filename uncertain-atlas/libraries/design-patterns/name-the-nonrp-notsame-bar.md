# 模式：把要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**例**：[要签原样数据可以用 non_rp not already same-as-ve ≠ bundled（358）](../../tracks/implementation/worked-example-nonrp-notsame-vs-bundled.md)。

## 三个名字

1. **有第二份 不是 already same-as-ve：** 看见有第二份 / 应用要签原样数据可以用 `non_rp` / 有第二份字段，不是已经和 vote_extension 同一份 interchangeable / 已经 same-as-ve interchangeable / 已经和第一份同一对象交差 interchangeable，不是 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable。

2. **能空 不是 already empty-verify：** 看见能空 / `non_rp_vote_extension` 可选也可以空 / 能空着，不是已经是空扩展仍验签 interchangeable / 已经 empty-verify interchangeable / 已经是 34 那种空扩展仍验签交差 interchangeable，不是 353 emptyverify interchangeable / 827 nonrp-notraw interchangeable。

3. **能用 不是 already settled：** 看见能用 / 可以用这份字段 / 不要包装也能签，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 828 nonrp-notprotected interchangeable / 33 fourgates interchangeable。

官方把有第二份、不是已经是空扩展仍验签、不是已经交差写成三个名字。把它们叫成一个「看见有第二份就已经和 vote_extension 同一份 interchangeable / 就已经是空扩展仍验签 interchangeable / 就已经交差 interchangeable」，会把 not already same-as-ve、not already empty-verify、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份 not already same-as-ve / not already empty-verify / not already settled 正式三事（358 余量），先数清问的是有第二份 是不是 already same-as-ve / 358 / nonrp-sold-as-protected，是不是能空 是不是 already empty-verify，还是能用 是不是 already settled，再决定要不要同一次发布。358 nonrp vs wrapped bundled unbundling 在本页 item 3 完成。
