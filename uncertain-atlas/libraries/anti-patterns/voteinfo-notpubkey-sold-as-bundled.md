# 反模式：把 从块抽出 not already has pubkey / not already ValidatorUpdate / not already changed set 正式三事（365 余量） 卖成 已经带了公钥 / 已经是 ValidatorUpdate / 已经改了集合

**层次**：实现 / VoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-voteinfo-notpubkey-vs-bundled.md](../../tracks/implementation/worked-example-voteinfo-notpubkey-vs-bundled.md)。

官方把 VoteInfo 能按到场定奖惩 / 从拟议块或已决块抽出 / 按投票权降序排三条核心句写成三件独立的实现事。把它们卖成已经带了公钥 / 已经是 ValidatorUpdate / 已经改了集合，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看从块抽出 正式三事（365 余量），必须分开 not already has pubkey、not already ValidatorUpdate、not already changed set 三件事，不要和 365 / 364 / 369 / 818 / 363 / 830 / 832 糊成一句。

## 和相邻反模式

- [voteinfo-notslashed-sold-as-bundled](voteinfo-notslashed-sold-as-bundled.md) 是定奖惩单句边界（830 item 1），不是本页从块抽出边界。
- [extvoteinfo-notblock-sold-as-bundled](extvoteinfo-notblock-sold-as-bundled.md) 是 ExtendedVoteInfo 本进程抽出就已经从块抽出（369/818），不是本页从块抽出边界。
