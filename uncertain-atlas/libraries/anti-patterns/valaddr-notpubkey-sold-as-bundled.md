# 反模式：把 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量）说成已经带了公钥 / 已经能验签 / 已经是 ValidatorUpdate

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有结构 not already pubkey ≠ bundled（364）](../../tracks/implementation/worked-example-valaddr-notpubkey-vs-bundled.md)。

## 卖法

把有结构 / VoteInfo / CommitInfo / ExtendedCommitInfo 里有这份 Validator / 只有 address 和 power 写成已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable / 364 validator bundled interchangeable / validator-sold-as-update interchangeable；把有 address / 字段有 address / 用 address 认人 写成已经能验签 interchangeable / 已经 verify interchangeable / 已经能验签交差 interchangeable；把有 power / 字段有 power / 有投票权 写成已经是 ValidatorUpdate interchangeable / 已经 update interchangeable / 已经是 ValidatorUpdate 交差 interchangeable，或已经和 364 validator bundled / validator-sold-as-update interchangeable / 839 valaddr-notpubkey interchangeable。

## 为什么错

官方把有结构、不是已经能验签、不是已经是 ValidatorUpdate 写成三件独立的实现事。把它们卖成 already pubkey interchangeable / already verify interchangeable / already update interchangeable，会把 not already pubkey、not already verify、not already update 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validator 用 address 认人不是已经带了公钥 not already pubkey / not already verify / not already update 正式三事（364 余量），必须分开 not already pubkey、not already verify、not already update 三件事，不要和 364 / 35 / 363 / 840 / 841 糊成一句。

## 和相邻反模式

- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 类型 bundled 全段，不是本页有结构 item 1 单句边界。
- [validator-update-sold-as-immediate](validator-update-sold-as-immediate.md) 是 H 的更新已经在 H+1 计票（35），不是本页 not already pubkey 边界。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空名单就已经没有集合（318），不是本页 not already update 边界。
