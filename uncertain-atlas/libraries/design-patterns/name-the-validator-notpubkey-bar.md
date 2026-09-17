# 模式：点名 Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事（364 余量）

**层次**：实现 / Validator 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validator-notpubkey-vs-bundled.md](../../tracks/implementation/worked-example-validator-notpubkey-vs-bundled.md)。

Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事（364 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **只有 address 和 power 不是已经带了公钥：** 看见只有 address 和 power，不是已经带了公钥 interchangeable / 833 validator-notpubkey interchangeable。
- **看见有 address 不是已经能验签：** 看见只有 address 和 power，不是已经能验签 interchangeable。
- **看见有 power 不是已经是 ValidatorUpdate：** 看见只有 address 和 power，不是已经是 ValidatorUpdate interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validator 用 address 认人 正式三事（364 余量），先数清问的是是不是已经带了公钥、是不是已经能验签、还是看见有 power 是不是已经是 ValidatorUpdate，再决定要不要同一次发布。364 validator vs update bundled unbundling 在本页 item 1 启动。
