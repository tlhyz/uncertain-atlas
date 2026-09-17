# 模式：点名 total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事（372 余量）

**层次**：实现 / Misbehavior 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-misbehavior-notreward-vs-bundled.md](../../tracks/implementation/worked-example-misbehavior-notreward-vs-bundled.md)。

total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事（372 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **总权 不是已经按到场定奖惩：** 看见有总权，不是已经 365 interchangeable / 811 misbehavior-notreward interchangeable。
- **看见填了权 不是已经改了集合：** 看见有总权，不是已经改了集合 interchangeable。
- **看见有集合 不是已经罚没：** 看见总权，不是已经罚没 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 total_voting_power 正式三事（372 余量），先数清问的是是不是已经按到场定奖惩 / 365、是不是已经改了集合、还是看见有集合是不是已经罚没，再决定要不要同一次发布。372 misbehavior vs enum bundled unbundling 在本页 item 3 完成。
