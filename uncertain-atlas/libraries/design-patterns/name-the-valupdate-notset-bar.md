# 模式：把 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**例**：[有公钥字段 not already same-val ≠ bundled（364）](../../tracks/implementation/worked-example-valupdate-notset-vs-bundled.md)。

## 三个名字

1. **有公钥字段 不是 already same-val：** 看见有公钥字段 / ValidatorUpdate 用 `pub_key_type` 和 `pub_key_bytes` 认人 / 有公钥字段，不是已经是 VoteInfo / CommitInfo 里那份 Validator interchangeable / 已经 same-val interchangeable / 已经是那份 Validator 交差 interchangeable，不是 364 validator bundled interchangeable / validator-sold-as-update interchangeable。

2. **回了更新 不是 already changed-set：** 看见回了更新 / 用来告诉 CometBFT 更新验证者集合 / 回了 ValidatorUpdate，不是已经改了集合 interchangeable / 已经 changed-set interchangeable / 已经改了集合交差 interchangeable，不是 363 finresp interchangeable / 839 valaddr-notpubkey interchangeable。

3. **有 pub_key_type 不是 already algo：** 看见有 pub_key_type / 有 PubKeyType / 有类型字段，不是已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，不是 840 valnopub-notalgo interchangeable / 33 fourgates interchangeable。

官方把有公钥字段、不是已经改了集合、不是已经选型写成三个名字。把它们叫成一个「看见有公钥字段就已经是 VoteInfo 里那份 Validator interchangeable / 就已经改了集合 interchangeable / 就已经选型 interchangeable」，会把 not already same-val、not already changed-set、not already algo 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量），先数清问的是有公钥字段 是不是 already same-val / 364 / validator-sold-as-update，是不是回了更新 是不是 already changed-set，还是有 pub_key_type 是不是 already algo，再决定要不要同一次发布。364 validator-vs-update bundled unbundling 在本页 item 3 完成。
