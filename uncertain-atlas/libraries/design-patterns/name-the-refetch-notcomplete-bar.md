# 模式：点名 refetch_chunks not already complete / not already settled / not already same snapshot 正式三事（378 余量）

**层次**：实现 / ApplySnapshotChunk 再拉。  
**分类**：建议（产品）。  
**对应例**：[worked-example-refetch-notcomplete-vs-bundled.md](../../tracks/implementation/worked-example-refetch-notcomplete-vs-bundled.md)。

refetch_chunks not already complete / not already settled / not already same snapshot 正式三事（378 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **refetch_chunks 不是已经齐：** 看见列了块号，不是已经 332 interchangeable / 795 refetch-notcomplete interchangeable。
- **看见再装 不是已经交差：** 看见列了块号，不是已经交差 interchangeable。
- **看见按顺序 不是已经是同一份：** 看见 refetch_chunks，不是已经是同一份 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 refetch_chunks 正式三事（378 余量），先数清问的是是不是已经齐 / 332、是不是已经交差、还是看见按顺序是不是已经是同一份，再决定要不要同一次发布。378 refetch vs restored bundled unbundling 在本页 item 2 续。
