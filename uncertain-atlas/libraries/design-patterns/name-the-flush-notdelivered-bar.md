# 模式：点名 Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事（374 余量）

**层次**：实现 / Flush。  
**分类**：建议（产品）。  
**对应例**：[worked-example-flush-notdelivered-vs-bundled.md](../../tracks/implementation/worked-example-flush-notdelivered-vs-bundled.md)。

Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事（374 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **冲队列 不是已经送到：** 看见叫了 Flush，不是已经 309 interchangeable / 803 flush-notdelivered interchangeable。
- **看见在冲 不是已经入队：** 看见叫了 Flush，不是已经入队 interchangeable。
- **看见排队了 不是已经断开：** 看见冲队列，不是已经断开 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush 冲队列 正式三事（374 余量），先数清问的是是不是已经送到 / 309、是不是已经入队、还是看见排队了是不是已经断开，再决定要不要同一次发布。374 flush vs sent bundled unbundling 在本页 item 1 启动。
