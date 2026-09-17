# 模式：点名 回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事（361 余量）

**层次**：实现 / ExtendVote 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-when-notsame-vs-bundled.md](../../tracks/implementation/worked-example-extend-when-notsame-vs-bundled.md)。

回包字节不被共识算法解释 not already same extension / not already packed CanonicalVoteExtension / not already settled 正式三事（361 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回了 不是已经是同一份扩展：** 看见回了，不是已经是同一份扩展 interchangeable / 844 extend-when-notsame interchangeable。
- **看见不解释 不是已经包进 CanonicalVoteExtension：** 看见回了，不是已经包进 CanonicalVoteExtension interchangeable / 358。
- **看见有字节 不是已经交差：** 看见回了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包字节不被共识算法解释 正式三事（361 余量），先数清问的是是不是已经是同一份扩展、是不是已经包进 CanonicalVoteExtension / 358、还是看见有字节是不是已经交差，再决定要不要同一次发布。361 extend-when vs locked bundled unbundling 在本页 item 3 完成。
