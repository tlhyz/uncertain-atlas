# 模式：把 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**例**：[non_rp_extension 按原样签 not already replay-protected ≠ bundled（358）](../../tracks/implementation/worked-example-nonrp-notprotected-vs-bundled.md)。

## 三个名字

1. **按原样签了 不是 already replay-protected：** 看见按原样签了 / `non_rp_extension` 按应用给的字节原样签 / 没有再套一层重放保护，不是已经有重放保护 interchangeable / 已经 replay-protected interchangeable / 已经有 Height Round ChainID 交差 interchangeable，不是 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable。

2. **字段在 不是 already must-fill：** 看见字段在 / non_rp_extension 字段存在 / 挂上 Precommit，不是已经必须填 interchangeable / 已经 must-fill interchangeable / 已经必须填交差 interchangeable，不是 353 emptyverify interchangeable / 827 nonrp-notraw interchangeable。

3. **没有包装 不是 already settled：** 看见没有包装 / 不套一层重放保护 / 和 vote_extension 不同，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 829 nonrp-notsame interchangeable / 33 fourgates interchangeable。

官方把按原样签了、不是已经必须填、不是已经交差写成三个名字。把它们叫成一个「看见按原样签了就已经有重放保护 interchangeable / 就已经必须填 interchangeable / 就已经交差 interchangeable」，会把 not already replay-protected、not already must-fill、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 按原样签不是已经有重放保护 not already replay-protected / not already must-fill / not already settled 正式三事（358 余量），先数清问的是按原样签了 是不是 already replay-protected / 358 / nonrp-sold-as-protected，是不是字段在 是不是 already must-fill，还是没有包装 是不是 already settled，再决定要不要同一次发布。358 nonrp vs wrapped bundled unbundling 在本页 item 2 续。
