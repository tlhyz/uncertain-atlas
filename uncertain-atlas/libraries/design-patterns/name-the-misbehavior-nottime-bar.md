# 模式：点名 height/time not already verified time / not already settled / not already +2/3 正式三事（372 余量）

**层次**：实现 / Misbehavior 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-misbehavior-nottime-vs-bundled.md](../../tracks/implementation/worked-example-misbehavior-nottime-vs-bundled.md)。

height/time not already verified time / not already settled / not already +2/3 正式三事（372 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **height/time 不是已经验过这个时间：** 看见有时间，不是已经 304 interchangeable / 810 misbehavior-nottime interchangeable。
- **看见有高度 不是已经交差：** 看见有时间，不是已经交差 interchangeable。
- **看见对上了高度 不是已经是本高 +2/3：** 看见 height/time，不是已经是本高 +2/3 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height/time 正式三事（372 余量），先数清问的是是不是已经验过这个时间 / 304、是不是已经交差、还是看见对上了高度是不是已经是本高 +2/3，再决定要不要同一次发布。372 misbehavior vs enum bundled unbundling 在本页 item 2 续。
