# 模式：点名 Finalize 没回 not already cleared / not already changed / not already settled 正式三事（319 余量）

**层次**：实现 / ConsensusParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-consensusparams-notcleared-vs-bundled.md](../../tracks/implementation/worked-example-consensusparams-notcleared-vs-bundled.md)。

Finalize 没回 not already cleared / not already changed / not already settled 正式三事（319 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **Finalize 没回 不是已经清掉：** 看见没回，不是已经清成默认 interchangeable / 909 consensusparams-notcleared interchangeable。
- **看见空着 不是已经改了：** 看见空着，不是已经改过 interchangeable。
- **看见能更新 不是已经交差：** 看见能更新，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 没回 正式三事（319 余量），先数清问的是是不是已经清掉、是不是已经改了、还是看见能更新是不是已经交差，再决定要不要同一次发布。319 consensusparams vs update bundled unbundling 在本页 item 2 续。
