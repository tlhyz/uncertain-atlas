# 模式：点名 H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事（333 余量）

**层次**：实现 / ConsensusParams 生效延迟。  
**分类**：建议（产品）。  
**对应例**：[worked-example-params-delay-notvalset-vs-bundled.md](../../tracks/implementation/worked-example-params-delay-notvalset-vs-bundled.md)。

H+1 立刻用了新参数 not already validator H+2 / not already last_commit H+3 / not already settled 正式三事（333 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **H+1 立刻用了新参数 不是已经是验证人集合那种 H+2 才计票：** 看见参数已经在 H+1 用上，不是新人已经在 H+1 计票 interchangeable / 912 params-delay-notvalset interchangeable。
- **看见「立刻」 不是已经是 H+3 才带 last_commit：** 看见「立刻」，不是已经和 last_commit 同一张表 interchangeable。
- **看见参数延迟 不是已经交差：** 看见参数延迟，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 立刻用了新参数 正式三事（333 余量），先数清问的是是不是已经是验证人集合那种 H+2 才计票、是不是已经是 H+3 才带 last_commit、还是看见参数延迟是不是已经交差，再决定要不要同一次发布。333 params-delay vs set bundled unbundling 在本页 item 2 续。
