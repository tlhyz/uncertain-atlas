# 模式：点名 不带 PubKey not already selected / not already no PQ key / not already settled 正式三事（364 余量）

**层次**：实现 / Validator 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validator-notselected-vs-bundled.md](../../tracks/implementation/worked-example-validator-notselected-vs-bundled.md)。

不带 PubKey not already selected / not already no PQ key / not already settled 正式三事（364 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **省了字段 不是已经选型：** 看见省了字段，不是已经选型 interchangeable / 834 validator-notselected interchangeable。
- **看见提到后量子公钥 不是已经没有后量子钥：** 看见省了字段，不是已经没有后量子钥 interchangeable。
- **看见 ABCI 不传公钥 不是已经交差：** 看见省了字段，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不带 PubKey 正式三事（364 余量），先数清问的是是不是已经选型、是不是已经没有后量子钥、还是看见 ABCI 不传公钥是不是已经交差，再决定要不要同一次发布。364 validator vs update bundled unbundling 在本页 item 2 续。
