# 反模式：把 ExtendedVoteInfo 抽出 not already from block / not already has pubkey / not already settled 正式三事（369 余量） 卖成 已经从块里抽出 / 已经带了公钥 / 已经交差

**层次**：实现 / ExtendedVoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extvoteinfo-notblock-vs-bundled.md](../../tracks/implementation/worked-example-extvoteinfo-notblock-vs-bundled.md)。

官方把 ExtendedVoteInfo 从本进程抽出 / 把验过的签交给应用 / 扩展关掉则字段全空三条核心句写成三件独立的实现事。把它们卖成已经从块里抽出 / 已经带了公钥 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo 抽出 正式三事（369 余量），必须分开 not already from block、not already has pubkey、not already settled 三件事，不要和 369 / 365 / 421 / 394 / 749 / 819 / 820 糊成一句。

## 和相邻反模式

- VoteInfo 从拟议块或已决块抽出就已经带了公钥是不变量 365，不是本页本进程抽出边界。
- ExtendedVoteInfo 余栏就已经从本进程抽出是不变量 421，不是本页本进程抽出边界。
