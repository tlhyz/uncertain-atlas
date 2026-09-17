# 模式：点名 定期 Flush not already four gates / not already received / not already settled 正式三事（374 余量）

**层次**：实现 / Flush。  
**分类**：建议（产品）。  
**对应例**：[worked-example-flush-notgates-vs-bundled.md](../../tracks/implementation/worked-example-flush-notgates-vs-bundled.md)。

定期 Flush not already four gates / not already received / not already settled 正式三事（374 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **定期 Flush 不是已经是四门：** 看见定期在冲，不是已经 307 interchangeable / 804 flush-notgates interchangeable。
- **看见发出去了 不是已经收到：** 看见定期在冲，不是已经收到 interchangeable。
- **看见异步 不是已经交差：** 看见定期 Flush，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看定期 Flush 正式三事（374 余量），先数清问的是是不是已经是四门 / 307、是不是已经收到、还是看见异步是不是已经交差，再决定要不要同一次发布。374 flush vs sent bundled unbundling 在本页 item 2 续。
