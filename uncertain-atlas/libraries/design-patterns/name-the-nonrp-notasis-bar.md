# 模式：点名 vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事（358 余量）

**层次**：实现 / 两份扩展两份签。  
**分类**：建议（产品）。  
**对应例**：[worked-example-nonrp-notasis-vs-bundled.md](../../tracks/implementation/worked-example-nonrp-notasis-vs-bundled.md)。

vote_extension 会包进 CanonicalVoteExtension not already signed as-is / not already CanonicalVote / not already settled 正式三事（358 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **绑了 Height Round ChainID 不是已经按原样签：** 看见绑了这些字段，不是已经按原样签 interchangeable / 848 nonrp-notasis interchangeable。
- **看见有包装 不是已经是 CanonicalVote：** 看见绑了这些字段，不是已经是 CanonicalVote interchangeable / 34。
- **看见签了 不是已经交差：** 看见绑了这些字段，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 会包进 CanonicalVoteExtension 正式三事（358 余量），先数清问的是是不是已经按原样签、是不是已经是 CanonicalVote / 34、还是看见签了是不是已经交差，再决定要不要同一次发布。358 nonrp vs wrapped bundled unbundling 在本页 item 1 启动。
