# 模式：点名 同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事（318 余量）

**层次**：实现 / ValidatorUpdate。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validatorupdate-notdup-vs-bundled.md](../../tracks/implementation/worked-example-validatorupdate-notdup-vs-bundled.md)。

同一批重复公钥 not already last wins / not already recoverable / not already settled 正式三事（318 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **同一批重复公钥 不是已经按后一条改权：** 看见重复，不是已经按后一条算 interchangeable / 906 validatorupdate-notdup interchangeable。
- **看见失败 不是已经能恢复：** 看见失败，不是已经能重放修好 interchangeable。
- **看见同一把钥 不是已经交差：** 看见同一把钥，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同一批重复公钥 正式三事（318 余量），先数清问的是是不是已经按后一条改权、是不是已经能恢复、还是看见同一把钥是不是已经交差，再决定要不要同一次发布。318 validatorupdate vs set bundled unbundling 在本页 item 2 续。
