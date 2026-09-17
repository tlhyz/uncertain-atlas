# 模式：点名 ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事（350 余量）

**层次**：实现 / 一轮一份扩展。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-once-notnil-vs-bundled.md](../../tracks/implementation/worked-example-extend-once-notnil-vs-bundled.md)。

ExtendVote 只在即将广播非 nil Precommit 时才叫 not already signed nil / not already every vote calls / not already settled 正式三事（350 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **叫了 ExtendVote 不是已经签了 nil 票：** 看见叫了 ExtendVote，不是已经签了 nil 票 interchangeable / 864 extend-once-notnil interchangeable。
- **看见启用了扩展 不是已经每张票都会叫：** 看见启用了扩展，不是已经每张票都会叫 interchangeable。
- **看见有一张票 不是已经交差：** 看见有一张票，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 只在即将广播非 nil Precommit 时才叫 正式三事（350 余量），先数清问的是是不是已经签了 nil 票、是不是已经每张票都会叫、还是看见有一张票是不是已经交差，再决定要不要同一次发布。350 extend-once vs round bundled unbundling 在本页 item 2 续。
