# 反模式：把 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量）说成已经从块里抽出 / 已经带了公钥 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Prepare 里有这份 not already from-block ≠ bundled（369）](../../tracks/implementation/worked-example-extvoteinfo-notfromblock-vs-bundled.md)。

## 卖法

把 Prepare 里有这份 / ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出 / Prepare 里有 `ExtendedCommitInfo` 写成已经从拟议块或已决块抽出 interchangeable / 已经 from-block interchangeable / 已经从块里抽出交差 interchangeable / 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable；把有 `ExtendedVoteInfo.validator` / 有 validator 字段 / 票里有 Validator 写成已经带了公钥 interchangeable / 已经 pubkey interchangeable / 已经带了公钥交差 interchangeable；把能抽 / 能从本进程抽出 / 抽得出来 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 369 extvoteinfo bundled / extvoteinfo-sold-as-local interchangeable / 854 extvoteinfo-notfromblock interchangeable。

## 为什么错

官方把 Prepare 里有这份、不是已经带了公钥、不是已经交差写成三件独立的实现事。把它们卖成 already from-block interchangeable / already pubkey interchangeable / already settled interchangeable，会把 not already from-block、not already pubkey、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled 正式三事（369 余量），必须分开 not already from-block、not already pubkey、not already settled 三件事，不要和 369 / 365 / 855 / 856 糊成一句。

## 和相邻反模式

- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 extvoteinfo bundled 全段，不是本页 Prepare 里有这份 item 1 单句边界。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是从拟议块或已决块抽出就已经带了公钥（365），不是本页 not already from-block 单句边界。
- [voteinfo-notpubkey-sold-as-bundled](voteinfo-notpubkey-sold-as-bundled.md) 是 VoteInfo 抽出 not already pubkey（365 余量 / 843），不是本页 not already pubkey 边界。
