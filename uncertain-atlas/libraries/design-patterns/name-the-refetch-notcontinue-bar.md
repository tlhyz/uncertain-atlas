# 模式：点名 reject_senders not already can continue / not already halted / not already complete 正式三事（378 余量）

**层次**：实现 / ApplySnapshotChunk 再拉。  
**分类**：建议（产品）。  
**对应例**：[worked-example-refetch-notcontinue-vs-bundled.md](../../tracks/implementation/worked-example-refetch-notcontinue-vs-bundled.md)。

reject_senders not already can continue / not already halted / not already complete 正式三事（378 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **reject_senders 不是已经能接着装：** 看见拒了人，不是已经 375 interchangeable / 796 refetch-notcontinue interchangeable。
- **看见丢掉排队 不是已经停：** 看见拒了人，不是已经停 interchangeable。
- **看见已装的还在 不是已经齐：** 看见 reject_senders，不是已经齐 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 reject_senders 正式三事（378 余量），先数清问的是是不是已经能接着装 / 375、是不是已经停、还是看见已装的还在是不是已经齐，再决定要不要同一次发布。378 refetch vs restored bundled unbundling 在本页 item 3 完成。
