# 反模式：把从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量）说成已经带了公钥 / 已经是 ValidatorUpdate / 已经改了集合

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[从块里抽出 not already pubkey ≠ bundled（365）](../../tracks/implementation/worked-example-voteinfo-notpubkey-vs-bundled.md)。

## 卖法

把从块里抽出 / 这份信息通常从拟议块或已决块抽出 / 从块抽出 写成已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable / 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable；把有 `VoteInfo.validator` / 有 validator 字段 / 票里有 Validator 写成已经是 ValidatorUpdate interchangeable / 已经 update interchangeable / 已经是 ValidatorUpdate 交差 interchangeable；把块里有票 / 拟议块或已决块里有票 / 块里抽出了票 写成已经改了集合 interchangeable / 已经 changed-set interchangeable / 已经改了集合交差 interchangeable，或已经和 365 voteinfo bundled / voteinfo-sold-as-rewarded interchangeable / 843 voteinfo-notpubkey interchangeable。

## 为什么错

官方把从块里抽出、不是已经是 ValidatorUpdate、不是已经改了集合写成三件独立的实现事。把它们卖成 already pubkey interchangeable / already update interchangeable / already changed-set interchangeable，会把 not already pubkey、not already update、not already changed-set 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从拟议块或已决块抽出不是已经带了公钥 not already pubkey / not already update / not already changed-set 正式三事（365 余量），必须分开 not already pubkey、not already update、not already changed-set 三件事，不要和 365 / 364 / 842 / 844 糊成一句。

## 和相邻反模式

- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo bundled 全段，不是本页从块里抽出 item 2 单句边界。
- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 用 address 认人就已经带了公钥（364），不是本页 not already pubkey 边界。
- [voteinfo-notslashed-sold-as-bundled](voteinfo-notslashed-sold-as-bundled.md) 是 VoteInfo 能按到场定奖惩 not already slashed（365 item 1），不是本页 not already update 边界。
