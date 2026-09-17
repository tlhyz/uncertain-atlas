# 模式：点名 Query 回了 not already replicated / not already consensus / not already settled 正式三事（329 余量）

**层次**：实现 / Query。  
**分类**：建议（产品）。  
**对应例**：[worked-example-query-notrepl-vs-bundled.md](../../tracks/implementation/worked-example-query-notrepl-vs-bundled.md)。

Query 回了 not already replicated / not already consensus / not already settled 正式三事（329 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **Query 回了 不是已经复制到各节点：** 看见回了，不是已经全网同一份 interchangeable / 938 query-notrepl interchangeable。
- **看见 RPC 绿了 不是已经过了共识：** 看见 RPC 绿了，不是已经过了共识 interchangeable。
- **看见 RPC 绿了 不是已经交差：** 看见 RPC 绿了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 正式三事（329 余量），先数清问的是是不是已经复制到各节点、是不是已经过了共识、还是看见 RPC 绿了是不是已经交差，再决定要不要同一次发布。329 query vs replicated bundled unbundling 在本页 item 1 启动。
