# 模式：点名 立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事（374 余量）

**层次**：实现 / Flush。  
**分类**：建议（产品）。  
**对应例**：[worked-example-flush-notproceed-vs-bundled.md](../../tracks/implementation/worked-example-flush-notproceed-vs-bundled.md)。

立刻 Flush not already can proceed / not already Commit / not already unlocked 正式三事（374 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **立刻 Flush 不是已经能往下走：** 看见立刻叫了，不是已经 310 interchangeable / 805 flush-notproceed interchangeable。
- **看见回包回来 不是已经 Commit：** 看见立刻叫了，不是已经 Commit interchangeable。
- **看见同步了 不是已经解锁：** 看见立刻 Flush，不是已经解锁 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻 Flush 正式三事（374 余量），先数清问的是是不是已经能往下走 / 310、是不是已经 Commit、还是看见同步了是不是已经解锁，再决定要不要同一次发布。374 flush vs sent bundled unbundling 在本页 item 3 完成。
