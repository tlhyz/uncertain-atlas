# 模式：把 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**例**：[有结构 not already pubkey ≠ bundled（364）](../../tracks/implementation/worked-example-valaddr-notpubkey-vs-bundled.md)。

## 三个名字

1. **有结构 不是 already pubkey：** 看见有结构 / VoteInfo / CommitInfo / ExtendedCommitInfo 里有这份 Validator / 只有 address 和 power，不是已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable，不是 364 validator bundled interchangeable / validator-sold-as-update interchangeable。

2. **有 address 不是 already verify：** 看见有 address / 字段有 address / 用 address 认人，不是已经能验签 interchangeable / 已经 verify interchangeable / 已经能验签交差 interchangeable，不是 35 valupdate interchangeable / 840 valnopub-notalgo interchangeable。

3. **有 power 不是 already update：** 看见有 power / 字段有 power / 有投票权，不是已经是 ValidatorUpdate interchangeable / 已经 update interchangeable / 已经是 ValidatorUpdate 交差 interchangeable，不是 841 valupdate-notset interchangeable / 33 fourgates interchangeable。

官方把有结构、不是已经能验签、不是已经是 ValidatorUpdate 写成三个名字。把它们叫成一个「看见有结构就已经带了公钥 interchangeable / 就已经能验签 interchangeable / 就已经是 ValidatorUpdate interchangeable」，会把 not already pubkey、not already verify、not already update 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量），先数清问的是有结构 是不是 already pubkey / 364 / validator-sold-as-update，是不是有 address 是不是 already verify，还是有 power 是不是 already update，再决定要不要同一次发布。364 validator-vs-update bundled unbundling 在本页 item 1 启动。
