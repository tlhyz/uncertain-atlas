# 模式：点名 +2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事（361 余量）

**层次**：实现 / ExtendVote 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extend-when-notcall-vs-bundled.md](../../tracks/implementation/worked-example-extend-when-notcall-vs-bundled.md)。

+2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事（361 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **到了 prevote 步 不是已经会调 ExtendVote：** 看见到了 prevote 步，不是已经会调 ExtendVote interchangeable / 842 extend-when-notcall interchangeable。
- **看见规范写了 When 不是已经是一轮一份扩展：** 看见到了 prevote 步，不是已经是一轮一份扩展 interchangeable / 350。
- **看见有提案 不是已经锁住：** 看见到了 prevote 步，不是已经锁住 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 prevote 才锁住再调 ExtendVote 正式三事（361 余量），先数清问的是是不是已经会调 ExtendVote、是不是已经是一轮一份扩展 / 350、还是看见有提案是不是已经锁住，再决定要不要同一次发布。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。
