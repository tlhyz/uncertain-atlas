# 模式：点名 Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事（372 余量）

**层次**：实现 / Misbehavior 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-misbehavior-notslashed-vs-bundled.md](../../tracks/implementation/worked-example-misbehavior-notslashed-vs-bundled.md)。

Misbehavior.type not already slashed / not already rewarded / not already settled 正式三事（372 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **type 不是已经罚没：** 看见有类型，不是已经 21 interchangeable / 809 misbehavior-notslashed interchangeable。
- **看见写成双签 不是已经定了奖惩：** 看见有类型，不是已经定了奖惩 interchangeable。
- **看见枚举在 不是已经交差：** 看见 type，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Misbehavior.type 正式三事（372 余量），先数清问的是是不是已经罚没 / 21、是不是已经定了奖惩、还是看见枚举在是不是已经交差，再决定要不要同一次发布。372 misbehavior vs enum bundled unbundling 在本页 item 1 启动。
