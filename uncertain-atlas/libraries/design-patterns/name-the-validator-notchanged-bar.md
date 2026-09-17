# 模式：点名 ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事（364 余量）

**层次**：实现 / Validator 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validator-notchanged-vs-bundled.md](../../tracks/implementation/worked-example-validator-notchanged-vs-bundled.md)。

ValidatorUpdate 用公钥认人 not already VoteInfo Validator / not already changed set / not already selected 正式三事（364 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **有公钥字段 不是已经是 VoteInfo 里那份：** 看见更新集合，不是已经是 VoteInfo 里那份 interchangeable / 835 validator-notchanged interchangeable。
- **看见回了更新 不是已经改了集合：** 看见更新集合，不是已经 363 interchangeable。
- **看见有 pub_key_type 不是已经选型：** 看见更新集合，不是已经选型 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValidatorUpdate 用公钥认人 正式三事（364 余量），先数清问的是是不是已经是 VoteInfo 里那份、是不是已经改了集合 / 363、还是看见有 pub_key_type 是不是已经选型，再决定要不要同一次发布。364 validator vs update bundled unbundling 在本页 item 3 完成。
