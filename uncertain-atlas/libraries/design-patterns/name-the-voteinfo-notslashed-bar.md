# 模式：点名 VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事（365 余量）

**层次**：实现 / VoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-voteinfo-notslashed-vs-bundled.md](../../tracks/implementation/worked-example-voteinfo-notslashed-vs-bundled.md)。

VoteInfo 定奖惩 not already slashed / not already settled / not already decided_last_commit computed 正式三事（365 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **有 block_id_flag 不是已经罚没：** 看见有这列，不是已经 21 interchangeable / 830 voteinfo-notslashed interchangeable。
- **看见能定奖惩 不是已经交差：** 看见有这列，不是已经交差 interchangeable。
- **看见能定奖惩 不是已经用 decided_last_commit 算完：** 看见有这列，不是已经算完 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VoteInfo 定奖惩 正式三事（365 余量），先数清问的是是不是已经罚没 / 21、是不是已经交差、还是看见能定奖惩是不是已经用 decided_last_commit 算完，再决定要不要同一次发布。365 voteinfo vs reward bundled unbundling 在本页 item 1 启动。
