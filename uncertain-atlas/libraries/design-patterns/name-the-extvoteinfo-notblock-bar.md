# 模式：点名 ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事（369 余量）

**层次**：实现 / ExtendedVoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extvoteinfo-notblock-vs-bundled.md](../../tracks/implementation/worked-example-extvoteinfo-notblock-vs-bundled.md)。

ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事（369 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **从本进程抽出 不是已经从块里抽出：** 看见 Prepare 里有这份，不是已经 365 interchangeable / 818 extvoteinfo-notblock interchangeable。
- **看见有 validator 不是已经带了公钥：** 看见 Prepare 里有这份，不是已经带了公钥 interchangeable。
- **看见能抽 不是已经交差：** 看见 Prepare 里有这份，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo 抽出 正式三事（369 余量），先数清问的是是不是已经从块里抽出 / 365、是不是已经带了公钥、还是看见能抽是不是已经交差，再决定要不要同一次发布。369 extvoteinfo vs local bundled unbundling 在本页 item 1 启动。
