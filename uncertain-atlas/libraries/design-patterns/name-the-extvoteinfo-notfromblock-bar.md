# 模式：把 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[Prepare 里有这份 not already from-block ≠ bundled（369）](../../tracks/implementation/worked-example-extvoteinfo-notfromblock-vs-bundled.md)。

## 三个名字

1. **Prepare 里有这份 不是 already from-block：** 看见 Prepare 里有这份 / ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出 / Prepare 里有 `ExtendedCommitInfo`，不是已经从拟议块或已决块抽出 interchangeable / 已经 from-block interchangeable / 已经从块里抽出交差 interchangeable，不是 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable。

2. **有 ExtendedVoteInfo.validator 不是 already pubkey：** 看见有 `ExtendedVoteInfo.validator` / 有 validator 字段 / 票里有 Validator，不是已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable，不是 365 voteinfo interchangeable / 855 extvoteinfo-notraw interchangeable。

3. **能抽 不是 already settled：** 看见能抽 / 能从本进程抽出 / 抽得出来，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 856 extvoteinfo-notveheight interchangeable / 33 fourgates interchangeable。

官方把 Prepare 里有这份、不是已经带了公钥、不是已经交差写成三个名字。把它们叫成一个「看见 Prepare 里有这份就已经从块里抽出 interchangeable / 就已经带了公钥 interchangeable / 就已经交差 interchangeable」，会把 not already from-block、not already pubkey、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量），先数清问的是 Prepare 里有这份 是不是 already from-block / 369 / extvoteinfo-sold-as-local，是不是有 ExtendedVoteInfo.validator 是不是 already pubkey，还是能抽 是不是 already settled，再决定要不要同一次发布。369 extvoteinfo-vs-local bundled unbundling 在本页 item 1 启动。
