# 反模式：看见 Validator 用 address 认人就当成已经带了公钥 / 看见不带 PubKey 就当成已经选型 / 看见 ValidatorUpdate 用公钥认人就当成已经改了集合

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator / ValidatorUpdate。  
**例**：[Validator 用 address 认人 ≠ 已经带了公钥](../../tracks/implementation/worked-example-validator-vs-update.md)。

## 塌法

1. 看见 Validator 用 address 认人 / 看见只有 address 和 power，就当成已经带了公钥，或当成已经能验签。
2. 看见不带 PubKey 是为了不在 ABCI 上传大后量子公钥 / 看见省了字段，就当成已经选型，或当成已经没有后量子钥。
3. 看见 ValidatorUpdate 用 `pub_key_type` 和 `pub_key_bytes` 认人 / 看见更新集合，就当成已经是 VoteInfo 里那份 Validator，或当成已经改了集合。

## 为什么会出事

官方写：`Validator` 用 address 认人，字段只有 `address` 和 `power`。不带 PubKey，是为了避免在 ABCI 上传送可能很大的后量子公钥。`ValidatorUpdate` 用 PubKeyType 和 PubKeyBytes 认人，用来告诉 CometBFT 更新验证者集合。

## 和相邻反模式

- [valaddr-notpubkey-sold-as-bundled](valaddr-notpubkey-sold-as-bundled.md) 是 Validator 用 address 认人 not already pubkey / not already verify / not already update 正式三事（364 item 1），不是本页 bundled 全段 alone。
- [validator-update-sold-as-immediate](validator-update-sold-as-immediate.md) 是 H 的更新已经在 H+1 计票，不是本页这种 Validator 用 address 认人不是已经带了公钥。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空名单就已经没有集合，不是本页这种不带 PubKey 不是已经选型。
- [finalizeequiv-sold-as-gates](finalizeequiv-sold-as-gates.md) 是必须回四列就已经改了集合，不是本页这种 ValidatorUpdate 用公钥认人不是已经改了集合。
