# 模式：把从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**例**：[从块里抽出 not already pubkey ≠ bundled（365）](../../tracks/implementation/worked-example-voteinfo-notpubkey-vs-bundled.md)。

## 三个名字

1. **从块里抽出 不是 already pubkey：** 看见从块里抽出 / 这份信息通常从拟议块或已决块抽出 / 从块抽出，不是已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable，不是 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable。

2. **有 VoteInfo.validator 不是 already update：** 看见有 `VoteInfo.validator` / 有 validator 字段 / 票里有 Validator，不是已经是 ValidatorUpdate interchangeable / 已经 update interchangeable / 已经是 ValidatorUpdate 交差 interchangeable，不是 364 validator interchangeable / 842 voteinfo-notslashed interchangeable。

3. **块里有票 不是 already changed-set：** 看见块里有票 / 拟议块或已决块里有票 / 块里抽出了票，不是已经改了集合 interchangeable / 已经 changed-set interchangeable / 已经改了集合交差 interchangeable，不是 844 voteinfo-notinblock interchangeable / 33 fourgates interchangeable。

官方把从块里抽出、不是已经是 ValidatorUpdate、不是已经改了集合写成三个名字。把它们叫成一个「看见从块里抽出就已经带了公钥 interchangeable / 就已经是 ValidatorUpdate interchangeable / 就已经改了集合 interchangeable」，会把 not already pubkey、not already update、not already changed-set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量），先数清问的是从块里抽出 是不是 already pubkey / 365 / voteinfo-sold-as-rewarded，是不是有 VoteInfo.validator 是不是 already update，还是块里有票 是不是 already changed-set，再决定要不要同一次发布。365 voteinfo-vs-reward bundled unbundling 在本页 item 2 续。
