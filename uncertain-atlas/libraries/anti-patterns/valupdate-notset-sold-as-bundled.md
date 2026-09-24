# 反模式：把 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量）说成已经是那份 Validator / 已经改了集合 / 已经选型

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有公钥字段 not already same-val ≠ bundled（364）](../../tracks/implementation/worked-example-valupdate-notset-vs-bundled.md)。

## 卖法

把有公钥字段 / ValidatorUpdate 用 `pub_key_type` 和 `pub_key_bytes` 认人 / 有公钥字段 写成已经是 VoteInfo / CommitInfo 里那份 Validator interchangeable / 已经 same-val interchangeable / 已经是那份 Validator 交差 interchangeable / 364 validator bundled interchangeable / validator-sold-as-update interchangeable；把回了更新 / 用来告诉 CometBFT 更新验证者集合 / 回了 ValidatorUpdate 写成已经改了集合 interchangeable / 已经 changed-set interchangeable / 已经改了集合交差 interchangeable；把有 pub_key_type / 有 PubKeyType / 有类型字段 写成已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，或已经和 364 validator bundled / validator-sold-as-update interchangeable / 841 valupdate-notset interchangeable。

## 为什么错

官方把有公钥字段、不是已经改了集合、不是已经选型写成三件独立的实现事。把它们卖成 already same-val interchangeable / already changed-set interchangeable / already algo interchangeable，会把 not already same-val、not already changed-set、not already algo 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValidatorUpdate 用公钥认人不是已经改了集合 not already same-val / not already changed-set / not already algo 正式三事（364 余量），必须分开 not already same-val、not already changed-set、not already algo 三件事，不要和 364 / 363 / 839 / 840 糊成一句。

## 和相邻反模式

- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 类型 bundled 全段，不是本页有公钥字段 item 3 单句边界。
- [finalizeequiv-sold-as-gates](finalizeequiv-sold-as-gates.md) 是必须回四列就已经改了集合（363），不是本页 not already changed-set 边界。
- [valaddr-notpubkey-sold-as-bundled](valaddr-notpubkey-sold-as-bundled.md) 是 Validator 用 address 认人 not already pubkey（364 item 1），不是本页 not already same-val 边界。
- [valnopub-notalgo-sold-as-bundled](valnopub-notalgo-sold-as-bundled.md) 是不带 PubKey not already algo（364 item 2），不是本页 not already algo 边界。
