# 反模式：把 Validator 用 address 认人 not already has pubkey / not already can verify sig / not already ValidatorUpdate 正式三事（364 余量） 卖成 已经带了公钥 / 已经能验签 / 已经是 ValidatorUpdate

**层次**：实现 / Validator 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validator-notpubkey-vs-bundled.md](../../tracks/implementation/worked-example-validator-notpubkey-vs-bundled.md)。

官方把 Validator 用 address 认人 / 不带 PubKey / ValidatorUpdate 用公钥认人三条核心句写成三件独立的实现事。把它们卖成已经带了公钥 / 已经能验签 / 已经是 ValidatorUpdate，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validator 用 address 认人 正式三事（364 余量），必须分开 not already has pubkey、not already can verify sig、not already ValidatorUpdate 三件事，不要和 364 / 365 / 831 / 35 / 385 / 774 / 834 / 835 糊成一句。

## 和相邻反模式

- [voteinfo-notpubkey-sold-as-bundled](voteinfo-notpubkey-sold-as-bundled.md) 是从块抽出就已经带了公钥（365/831），不是本页 address 认人边界。
- [paramsblock-notpubkey-sold-as-bundled](paramsblock-notpubkey-sold-as-bundled.md) 是 ConsensusParams.validator 就已经带了公钥（385/774），不是本页 address 认人边界。
