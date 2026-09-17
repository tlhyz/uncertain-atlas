# 模式：点名 height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事（359 余量）

**层次**：实现 / Prepare 请求字段。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-fields-nothash-vs-bundled.md](../../tracks/implementation/worked-example-prepare-fields-nothash-vs-bundled.md)。

height / time / proposer_address 对上拟议头 not already header hash / not already ExecuteTxState / not already settled 正式三事（359 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **对得上 不是已经知道本头哈希：** 看见对得上，不是已经知道本头哈希 interchangeable / 847 prepare-fields-nothash interchangeable。
- **看见头上有这些 不是已经是 ExecuteTxState：** 看见对得上，不是已经是 ExecuteTxState interchangeable / 311。
- **看见拟议头 不是已经交差：** 看见对得上，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height / time / proposer_address 对上拟议头 正式三事（359 余量），先数清问的是是不是已经知道本头哈希、是不是已经是 ExecuteTxState / 311、还是看见拟议头是不是已经交差，再决定要不要同一次发布。359 prepare-fields vs same bundled unbundling 在本页 item 3 完成。
