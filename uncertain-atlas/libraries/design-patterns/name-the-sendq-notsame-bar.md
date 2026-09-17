# 模式：点名 sendq-notsame 杠

**层次**：网络 / TrySend 回假 not already stopped / not already same-scale / not already delivered 正式三事（309 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md) p2p reactor API / send vs enqueued。  
**对应**：[`../tracks/network/worked-example-sendq-notsame-vs-bundled.md`](../tracks/network/worked-example-sendq-notsame-vs-bundled.md)。

- **TrySend 回假 不是已经停掉这个人：** 看见立刻失败，不是已经停掉这个人 interchangeable / 1012 sendq-notsame interchangeable。
- **看见回了假 不是已经和 Send 等过同一段时间：** 看见回了假，不是已经和 Send 等过同一段时间 interchangeable。
- **看见非阻塞 不是已经送到：** 看见非阻塞，不是已经送到 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 TrySend 回假 正式三事（309 余量），先数清问的是是不是已经停掉这个人、是不是已经和 Send 等过同一段时间、还是看见非阻塞是不是已经送到，再决定要不要同一次发布。309 send vs enqueued bundled unbundling 在本页 item 3 完成。
