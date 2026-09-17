# 模式：点名 可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事（363 余量）

**层次**：实现 / Finalize 回包义务。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-equiv-notslashed-vs-bundled.md](../../tracks/implementation/worked-example-finalize-equiv-notslashed-vs-bundled.md)。

可以用 decided_last_commit 和 misbehavior 定奖惩 not already slashed / not already LastCommit +2/3 / not already settled 正式三事（363 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **有这两列 不是已经罚没：** 看见有这两列，不是已经罚没 interchangeable / 837 finalize-equiv-notslashed interchangeable。
- **看见有上一份 commit 不是已经是本头 LastCommit：** 看见有这两列，不是已经是本头 LastCommit 就已经是本高 +2/3 interchangeable。
- **看见能定奖惩 不是已经交差：** 看见有这两列，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看可以用 decided_last_commit 和 misbehavior 定奖惩 正式三事（363 余量），先数清问的是是不是已经罚没、是不是已经是本头 LastCommit 就已经是本高 +2/3、还是看见能定奖惩是不是已经交差，再决定要不要同一次发布。363 finalize-equiv vs gates bundled unbundling 在本页 item 2 续。
