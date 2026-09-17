# 模式：点名 MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事（331 余量）

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-evidence-maxbytes-notunbond-vs-bundled.md](../../tracks/implementation/worked-example-evidence-maxbytes-notunbond-vs-bundled.md)。

MaxBytes > 0 not already covering unbonding / not already enough to punish / not already settled 正式三事（331 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **> 0 不是已经盖住解绑：** 看见大于 0，不是已经盖住解绑期 interchangeable / 921 evidence-maxbytes-notunbond interchangeable。
- **看见合法 不是已经够罚：** 看见合法，不是已经能罚到人走之前 interchangeable。
- **看见大于 0 不是已经交差：** 看见大于 0，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes > 0 正式三事（331 余量），先数清问的是是不是已经盖住解绑、是不是已经够罚、还是看见大于 0 是不是已经交差，再决定要不要同一次发布。331 evidence-maxbytes vs block bundled unbundling 在本页 item 2 续。
