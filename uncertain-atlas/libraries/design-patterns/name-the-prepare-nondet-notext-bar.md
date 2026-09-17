# 模式：点名 ExtendVote 没有确定性要求 not already same extension / not already same ruler as Verify / not already settled 正式三事（338 余量）

**层次**：实现 / PrepareProposal 与 ExtendVote 的确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-nondet-notext-vs-bundled.md](../../tracks/implementation/worked-example-prepare-nondet-notext-vs-bundled.md)。

ExtendVote 没有确定性要求 not already same extension / not already same ruler as Verify / not already settled 正式三事（338 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **没有确定性要求 不是已经是同一份扩展：** 看见同一块，不是已经是同一份扩展 interchangeable / 898 prepare-nondet-notext interchangeable。
- **看见同一块 不是已经和 Verify 同一把尺：** 看见同一块，不是已经和 Verify 同一把尺 interchangeable。
- **看见能签扩展 不是已经交差：** 看见能签扩展，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 没有确定性要求 正式三事（338 余量），先数清问的是是不是已经是同一份扩展、是不是已经和 Verify 同一把尺、还是看见能签扩展是不是已经交差，再决定要不要同一次发布。338 prepare-nondet vs process bundled unbundling 在本页 item 3 完成。
