# 模式：点名 id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事（326 余量）

**层次**：实现 / Peer Filtering。  
**分类**：建议（产品）。  
**对应例**：[worked-example-peerfilter-notaddr-vs-bundled.md](../../tracks/implementation/worked-example-peerfilter-notaddr-vs-bundled.md)。

id 过滤查询绿了 not already past-addr / not already interactive / not already settled 正式三事（326 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **id 过滤查询绿了 不是已经过了 addr：** 看见 id 绿了，不是 addr 已经绿 interchangeable / 945 peerfilter-notaddr interchangeable。
- **看见公钥地址对上 不是已经能交互：** 看见公钥地址对上，不是已经能交互 interchangeable。
- **看见拒连 不是已经交差：** 看见拒连，不是已经写进持久封禁表 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 id 过滤查询绿了 正式三事（326 余量），先数清问的是是不是已经过了 addr、是不是已经能交互、还是看见拒连是不是已经交差，再决定要不要同一次发布。326 peerfilter vs query bundled unbundling 在本页 item 2 续。
