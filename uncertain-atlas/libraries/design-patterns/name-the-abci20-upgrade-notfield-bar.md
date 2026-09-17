# 模式：点名 必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事（346 余量）

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：建议（产品）。  
**对应例**：[worked-example-abci20-upgrade-notfield-vs-bundled.md](../../tracks/implementation/worked-example-abci20-upgrade-notfield-vs-bundled.md)。

必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事（346 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **协调升级 不是已经只改 VoteExtensionsEnableHeight：** 看见必须协调升级，不是已经只改 VoteExtensionsEnableHeight interchangeable / 875 abci20-upgrade-notfield interchangeable。
- **看见一个节点升了二进制 不是已经是单节点能切：** 看见一个节点升了二进制，不是已经是单节点能切 interchangeable。
- **看见能改启用高度 不是已经交差：** 看见能改启用高度，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须协调升级 正式三事（346 余量），先数清问的是是不是已经只改 VoteExtensionsEnableHeight、是不是已经是单节点能切、还是看见能改启用高度是不是已经交差，再决定要不要同一次发布。346 abci20 vs height bundled unbundling 在本页 item 1 启动。
