# 模式：把 Validator 类型三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**例**：[Validator 用 address 认人 ≠ 已经带了公钥](../../tracks/implementation/worked-example-validator-vs-update.md)。

## 三个名字

1. **Validator 用 address 认人不是已经带了公钥：** 看见只有 address 和 power 不是已经能验签。
2. **不带 PubKey 不是已经选型：** 看见省了字段不是已经没有后量子钥。
3. **ValidatorUpdate 用公钥认人不是已经改了集合：** 看见有 `pub_key_type` 不是已经是 VoteInfo 里那份 Validator。

## 为什么要分开叫

官方把 `Validator` 用 address 认人、不带 PubKey 以免在 ABCI 上传大后量子公钥、`ValidatorUpdate` 用公钥认人写成三件事。把它们叫成一个「看见 VoteInfo 里有验证者就已经带了公钥」，会把集合延迟、空名单和回包义务一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 VoteInfo 里有验证者就已经带了公钥」，先数清问的是 Validator 用 address 认人不是已经带了公钥、不带 PubKey 不是已经选型，还是 ValidatorUpdate 用公钥认人不是已经改了集合，再决定要不要同一次发布。
