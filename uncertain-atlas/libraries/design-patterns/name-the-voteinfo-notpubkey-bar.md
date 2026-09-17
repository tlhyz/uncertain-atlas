# 模式：点名 从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事（365 余量）

**层次**：实现 / VoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-voteinfo-notpubkey-vs-bundled.md](../../tracks/implementation/worked-example-voteinfo-notpubkey-vs-bundled.md)。

从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事（365 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **从块里抽出 不是已经带了公钥：** 看见块里有票，不是已经 364 interchangeable / 831 voteinfo-notpubkey interchangeable。
- **看见有 validator 不是已经是 ValidatorUpdate：** 看见块里有票，不是已经是 ValidatorUpdate interchangeable。
- **看见从块里抽出 不是已经改了集合：** 看见块里有票，不是已经改了集合 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从块抽出 正式三事（365 余量），先数清问的是是不是已经带了公钥 / 364、是不是已经是 ValidatorUpdate、还是看见从块里抽出是不是已经改了集合，再决定要不要同一次发布。365 voteinfo vs reward bundled unbundling 在本页 item 2 续。
