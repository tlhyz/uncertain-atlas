# 模式：点名 发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事（326 余量）

**层次**：实现 / Peer Filtering。  
**分类**：建议（产品）。  
**对应例**：[worked-example-peerfilter-notaccept-vs-bundled.md](../../tracks/implementation/worked-example-peerfilter-notaccept-vs-bundled.md)。

发了 addr 过滤查询 not already accepted / not already past-id / not already settled 正式三事（326 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **发了 addr 过滤查询 不是已经收下这个人：** 看见发了 addr，不是已经收下 interchangeable / 944 peerfilter-notaccept interchangeable。
- **看见 TCP 连上 不是已经过了 id 那一道：** 看见 TCP 连上，不是已经过了 Query interchangeable。
- **看见只问了地址 不是已经交差：** 看见只问了地址，不是已经问了 id interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看发了 addr 过滤查询 正式三事（326 余量），先数清问的是是不是已经收下这个人、是不是已经过了 id 那一道、还是看见只问了地址是不是已经交差，再决定要不要同一次发布。326 peerfilter vs query bundled unbundling 在本页 item 1 启动。
