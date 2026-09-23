# 模式：把 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**例**：[vote_extension 包进 CanonicalVoteExtension not already raw-signed ≠ bundled（358）](../../tracks/implementation/worked-example-nonrp-notraw-vs-bundled.md)。

## 三个名字

1. **绑了这些字段 不是 already raw-signed：** 看见绑了 Height Round ChainID / `vote_extension` 会包进 `CanonicalVoteExtension` / 绑了这些字段，不是已经按原样签 interchangeable / 已经 raw-signed interchangeable / 已经按原样签交差 interchangeable，不是 358 nonrp bundled interchangeable / nonrp-sold-as-protected interchangeable。

2. **有包装 不是 already canon-vote：** 看见有包装 / 进了 CanonicalVoteExtension / 绑了包装字段，不是已经是票上那份 CanonicalVote interchangeable / 已经 canon-vote interchangeable / 已经是 CanonicalVote 交差 interchangeable，不是 34 canonvote interchangeable / 828 nonrp-notprotected interchangeable。

3. **签了 不是 already settled：** 看见签了 / 填完字段后签名 / 签名挂上，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 829 nonrp-notsame interchangeable / 33 fourgates interchangeable。

官方把绑了这些字段、不是已经是 CanonicalVote、不是已经交差写成三个名字。把它们叫成一个「看见绑了这些字段就已经按原样签 interchangeable / 就已经是 CanonicalVote interchangeable / 就已经交差 interchangeable」，会把 not already raw-signed、not already canon-vote、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 not already raw-signed / not already canon-vote / not already settled 正式三事（358 余量），先数清问的是绑了这些字段 是不是 already raw-signed / 358 / nonrp-sold-as-protected，是不是有包装 是不是 already canon-vote，还是签了 是不是 already settled，再决定要不要同一次发布。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。
