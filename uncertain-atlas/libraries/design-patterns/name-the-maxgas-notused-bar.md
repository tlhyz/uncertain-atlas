# 模式：点名 GasUsed not already consensus-checked / not already counted / not already settled 正式三事（315 余量）

**层次**：实现 / 气。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxgas-notused-vs-bundled.md](../../tracks/implementation/worked-example-maxgas-notused-vs-bundled.md)。

GasUsed not already consensus-checked / not already counted / not already settled 正式三事（315 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **GasUsed 不是已经按实用气验过：** 看见有 GasUsed，不是已经按实用气验过 interchangeable / 915 maxgas-notused interchangeable。
- **看见 GasWanted 过了池门 不是已经算进共识：** 看见 GasWanted 过了池门，不是已经算进共识 interchangeable。
- **看见有 GasUsed 不是已经交差：** 看见有 GasUsed，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 GasUsed 正式三事（315 余量），先数清问的是是不是已经按实用气验过、是不是已经算进共识、还是看见有 GasUsed 是不是已经交差，再决定要不要同一次发布。315 maxgas vs enforced bundled unbundling 在本页 item 2 续。
